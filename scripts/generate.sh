#!/usr/bin/env bash
# Regenerate the SDK from api/swagger.yaml.
#
# api/swagger.yaml is itself a build product (scripts/build_spec.py).
# Local template overrides live in templates/ and take precedence over the
# generator's embedded templates; anything not overridden falls back to stock.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

REQUIRED_GENERATOR_VERSION="7.24.0"
actual="$(openapi-generator version)"
if [[ "$actual" != "$REQUIRED_GENERATOR_VERSION" ]]; then
  echo "ERROR: openapi-generator $REQUIRED_GENERATOR_VERSION required, found $actual" >&2
  echo "Generated output differs between versions and CI compares byte-for-byte." >&2
  exit 1
fi

python3 scripts/build_spec.py

# disallowAdditionalPropertiesIfNotPresent=false makes an absent `additionalProperties`
# mean "unconstrained" (the spec-compliant reading). That suppresses the per-model strict
# decoder in model_simple.mustache for every schema that does not explicitly set
# `additionalProperties: false`, so the API's undocumented fields no longer cause
# deserialisation failures on response models — and avoids overriding a 573-line template.
#
# Two deliberate gaps, both benign:
#   * The oneOf decode path is not covered by this flag; templates/utils.mustache handles it.
#   * SupportOptionsRequest sets `additionalProperties: false` explicitly, so the flag leaves
#     it strictly decoded. It is a request-only schema (PUT body; responses use
#     SupportOptionsResponse), so its decoder is never exercised against an API payload.
#     Overriding an explicit spec statement here would contradict intent for no benefit.
#
# useOneOfDiscriminatorLookup=true is what makes overlay A4 (application GET
# discriminator) effective. Without it, model_oneof.mustache always emits the
# try-every-variant decoder regardless of whether the schema declares a
# discriminator, so the Application GET 200 decoder stays exactly the
# try-each-and-count-matches shape that caused OPEN-04 in v2.3 ("data matches
# more than one schema in oneOf") — A4 would be a no-op corrections entry. With
# the flag on, that decoder switches on `type` as intended.
# The cost: this flag is generator-wide, so it also swaps "exactly one match"
# validation for first-match-wins across the SDK's other 13 oneOf models.
# Measured, that cost is small: most of the 13 are type-disjoint primitive
# unions (e.g. ApplicationPort.value, FixedHost.value, RemoteID,
# RdpAttributes.maxConnections, NetworkIpsecBase.rightID, both `port`
# variants, `host`) where a JSON scalar is either a string or a number,
# never both — "more than one match" could never fire, so nothing is lost.
# The remaining object unions (CommonCreateApplication, CreateApplicationRequest,
# ObjectServiceProtocolTCPUDP, SourcesAndDestinations) move from strict
# matching to first-match-wins. ObjectServiceProtocolTCPUDP is one of the 21
# files v2.3 had to hand-patch specifically because strict oneOf matching
# failed on it, so first-match-wins is closer to already-shipped, already-
# validated production behaviour than the strict alternative. CommonCreateApplication/
# CreateApplicationRequest are request-only shapes serialized outbound, so
# their UnmarshalJSON is essentially never exercised against a real payload.
# SourcesAndDestinations is the one residual case with real (if small)
# mis-selection potential: it's a genuine object union that appears in
# firewall-policy response shapes, not just requests — Phase 4's
# firewall/SWG work should test it rather than assume first-match-wins picks
# the right variant.
# --git-user-id/--git-repo-id: without these the Go generator falls back to the
# literal placeholders GIT_USER_ID/GIT_REPO_ID for the module path baked into
# test/*_test.go and README.md. go.mod itself is unaffected (it is protected by
# .openapi-generator-ignore), but `go mod tidy`/`go build ./...`/`go vet ./...`
# below try to resolve those test-file imports and fail against a module that
# does not exist. gitRepoId carries the /v3 suffix so the emitted import path
# matches go.mod's module line exactly.
openapi-generator generate \
  -i api/swagger.yaml \
  -g go \
  -o . \
  -t templates \
  --git-user-id=CheckPointSW \
  --git-repo-id=perimeter-81-client-sdk/v3 \
  --additional-properties=packageName=perimeter81sdk,disallowAdditionalPropertiesIfNotPresent=false,useOneOfDiscriminatorLookup=true \
  --skip-validate-spec

go mod tidy
go build ./...

# -unreachable=false: the stock Go model_oneof.mustache (openapi-generator 7.24.0)
# has a template bug — its "no match" branch lives inside the {{#oneOf}} loop
# instead of outside it, so for any oneOf schema with N>=2 variants it emits N
# copies of the same if/err-else block, and vet flags copies 2..N as dead code
# (e.g. model_get_application_by_id_200_response.go, whose 5-variant oneOf is
# the A4 discriminator target). This dead code is generator-emitted, not
# hand-written, so `go vet`'s unreachable check has little value here — it
# would only ever flag output from this one upstream template bug, never a
# mistake a contributor made. It is not fixed by hand-editing the generated
# .go output (regeneration would wipe the edit) and deliberately not fixed by
# adding a local model_oneof.mustache override here either: that template is
# the exact mechanism the A4 discriminator finding depends on
# (useOneOfDiscriminatorLookup=true above), so it must be regenerated stock
# and inspected as-is, not modified for an unrelated cosmetic vet warning.
# Remove this flag once openapi-generator ships a fixed model_oneof.mustache
# (moves the "no match" branch outside the {{#oneOf}} loop) — check on upgrade.
go vet -unreachable=false ./...
echo "SDK regenerated successfully"
