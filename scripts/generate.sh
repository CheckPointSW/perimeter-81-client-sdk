#!/usr/bin/env bash
# Regenerate the SDK from api/swagger.yaml.
#
# api/swagger.yaml is itself a build product (scripts/build_spec.py).
# Local template overrides live in templates/ and take precedence over the
# generator's embedded templates; anything not overridden falls back to stock.
set -euo pipefail

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
# decoder in model_simple.mustache, so the API's undocumented fields no longer cause
# deserialisation failures — and avoids overriding a 573-line template to achieve it.
# The oneOf decode path is NOT covered by this flag; templates/utils.mustache handles it.
openapi-generator generate \
  -i api/swagger.yaml \
  -g go \
  -o . \
  -t templates \
  --additional-properties=packageName=perimeter81sdk,disallowAdditionalPropertiesIfNotPresent=false \
  --skip-validate-spec

go mod tidy
go build ./...
go vet ./...
echo "SDK regenerated successfully"
