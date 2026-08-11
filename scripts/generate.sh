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
# The cost: this flag is generator-wide, so for the SDK's other 13 oneOf
# models (which have no discriminator) it also drops strict field decoding
# (newStrictDecoder) plus the gopkg.in/validator.v2 validation step from the
# per-branch match check, in favour of a plain json.Unmarshal + non-empty
# check. Ambiguity detection is NOT lost: those 13 decoders still count
# matches and still return an error on match > 1 or match == 0 — see
# model_sources_and_destinations.go for the shape. What changes is only what
# counts as a candidate match, which is looser than before.
# Measured, that cost is small: most of the 13 are type-disjoint primitive
# unions (e.g. ApplicationPort.value, FixedHost.value, RemoteID,
# RdpAttributes.maxConnections, NetworkIpsecBase.rightID, both `port`
# variants, `host`) where a JSON scalar is either a string or a number,
# never both — the loosened match check could never produce more than one
# candidate anyway, so nothing is lost. The remaining object unions
# (CommonCreateApplication, CreateApplicationRequest,
# ObjectServiceProtocolTCPUDP, SourcesAndDestinations) move from strict
# matching to the looser json.Unmarshal-based matching described above.
# ObjectServiceProtocolTCPUDP is one of the 21 files v2.3 had to hand-patch
# specifically because strict oneOf matching failed on it, so the looser
# matching is closer to already-shipped, already-validated production
# behaviour than the strict alternative. CommonCreateApplication/
# CreateApplicationRequest are request-only shapes serialized outbound, so
# their UnmarshalJSON is essentially never exercised against a real payload.
# SourcesAndDestinations is the one residual case with real (if small)
# mis-selection potential: it's a genuine object union that appears in
# firewall-policy response shapes, not just requests, so dropping strict
# decoding there makes a structurally-similar-but-wrong candidate more likely
# to also produce non-empty output — raising, not lowering, the odds of
# hitting match > 1 (or, less likely, match == 0) on some payload shape that
# used to cleanly resolve to one candidate under strict decoding. Phase 4's
# firewall/SWG work should test SourcesAndDestinations decoding against real
# payloads rather than assume the loosened match check still resolves
# cleanly.
# Also accepted: for the one schema this flag exists to fix
# (GetApplicationById200Response, via A4's discriminator), an unrecognised or
# absent `type` value falls through the generated decoder's if-chain to a
# bare `return nil` — the union decodes to all-nil fields with a nil error,
# silently, instead of the flag-off path's "data failed to match schemas in
# oneOf(...)" error. This is stock model_oneof.mustache behaviour, not
# something local to this SDK, and is not being patched here (that would
# require a model_oneof.mustache override, which this SDK deliberately does
# not carry — see the go vet comment below for why). Phase 4 should treat an
# application with an unrecognised `type` as an explicit test case: confirm
# callers check GetActualInstance()/IsNil() rather than assuming a non-nil
# decode implies a recognised type.
# enumClassPrefix=true prefixes every generated enum constant with its schema
# name (e.g. `ROUTINGTYPE_ROUTE` instead of bare `ROUTE`). This exists to
# prevent enum constant collisions at package scope: the Go enum template
# names constants purely from the enum value text with no per-schema scoping,
# so any two schemas that share an enum value (RoutingType/RoutingTypeUpdate
# both have 'route'/'policy'; StandardHealthCheckType/EnhancedHealthCheckType
# both have 'tunnel') collide as duplicate top-level `const` declarations and
# `go build` fails. An earlier version of this fix used per-schema
# x-enum-varnames overlay entries (A13/A14, now deleted) instead of this
# flag; that approach is why this flag also matters for compatibility, not
# just idempotency: it happens to preserve the prefixed names
# (`ROUTINGTYPE_ROUTE`) the v2.3 SDK always shipped and the terraform
# provider already depends on, whereas the deleted A13 renamed the *other*
# side of the collision (`RoutingTypeUpdate` -> `ROUTE_UPDATE`) and left the
# base schema's constants unprefixed and bare (`ROUTE`) — silently breaking
# that provider reference. This flag is also collision-proof against any
# future enum value shared across schemas, unlike a per-collision overlay
# entry.
# --git-user-id/--git-repo-id: without these the Go generator falls back to the
# literal placeholders GIT_USER_ID/GIT_REPO_ID for the module path baked into
# git_push.sh and README.md's import example. go.mod itself is unaffected (it
# is protected by .openapi-generator-ignore). These are still needed even
# though test/ is no longer generated (see apiTests=false below): git_push.sh
# hard-codes git_user_id/git_repo_id defaults from these flags, and README.md's
# example import line uses them too. gitRepoId carries the /v3 suffix so the
# emitted import path matches go.mod's module line exactly.
#
# apiTests=false: stops generating test/*_test.go. The Go generator's "Test
# files never overwrite an existing file of the same name" behaviour makes
# test/ write-once: once committed, a second `openapi-generator generate` run
# silently skips every test/*_test.go and drops those 19 entries from
# .openapi-generator/FILES, even though nothing else changed — breaking
# Task 8's `git diff --exit-code` CI gate on its very first run (verified: two
# consecutive runs are now byte-identical). The generated tests were also
# ~2000 lines of dead scaffolding: every one is unconditionally t.Skip'd (see
# the removed templates/api_test.mustache override, no longer needed), so none
# of it was ever an exercised regression test.
# apiDocs/modelDocs are deliberately left at their default (true), i.e. docs/
# keeps regenerating every run: doc files (*.md) do not have the "never
# overwrite" behaviour that breaks test/ — verified with two consecutive runs
# into an already-populated tree, docs/'s 279 FILES entries and file contents
# came back byte-identical both times — so turning them off would only freeze
# docs/ out of sync with the API surface for no idempotency benefit.
# There is no modelTests flag to set here: the Go generator has no model-test
# template, so it was already a no-op (no model_*_test.go has ever existed).
openapi-generator generate \
  -i api/swagger.yaml \
  -g go \
  -o . \
  -t templates \
  --git-user-id=CheckPointSW \
  --git-repo-id=perimeter-81-client-sdk/v3 \
  --global-property=apiTests=false \
  --additional-properties=packageName=perimeter81sdk,disallowAdditionalPropertiesIfNotPresent=false,useOneOfDiscriminatorLookup=true,enumClassPrefix=true \
  --skip-validate-spec

go mod tidy
go build ./...

# -unreachable=false: the stock Go model_oneof.mustache (openapi-generator 7.24.0)
# has a template bug — its "no match" branch lives inside the {{#oneOf}} loop
# instead of outside it, so for any oneOf schema with N>=2 variants it emits N
# copies of the same if/err-else block, and vet flags copies 2..N as dead code
# (e.g. model_sources_and_destinations.go, a 2-variant oneOf with no
# discriminator — still affected even with useOneOfDiscriminatorLookup=true,
# since that flag only changes the match check for non-discriminated oneOf
# models, not this duplicated-branch template shape; the discriminated
# GetApplicationById200Response, by contrast, no longer hits this bug at all,
# since the discriminator branch above is a single linear if-chain with no
# {{#oneOf}}-loop duplication). This dead code is generator-emitted, not
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
