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
  --additional-properties=packageName=perimeter81sdk,disallowAdditionalPropertiesIfNotPresent=false \
  --skip-validate-spec

go mod tidy
go build ./...

# -unreachable=false: the stock Go model_oneof.mustache (openapi-generator 7.24.0)
# has a template bug — its "no match" branch lives inside the {{#oneOf}} loop
# instead of outside it, so for any oneOf schema with N>=2 variants it emits N
# copies of the same if/err-else block, and vet flags copies 2..N as dead code
# (e.g. model_get_application_by_id_200_response.go, whose 5-variant oneOf is
# the A4 discriminator target). The duplicated code is inert, not a defect in
# our spec or overlay, and the fix lives in openapi-generator's own template —
# not something to patch by hand-editing generated output, and not something to
# fix via a local model_oneof.mustache override here: that template is the exact
# mechanism the A4 discriminator finding depends on, so it must be regenerated
# stock and inspected as-is, not modified for an unrelated cosmetic vet warning.
go vet -unreachable=false ./...
echo "SDK regenerated successfully"
