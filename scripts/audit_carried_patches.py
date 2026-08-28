#!/usr/bin/env python3
"""Check each v2.3-era hand-patch against the v3 upstream spec.

Prints CONFIRMED (defect still present, needs an overlay entry) or
ALREADY-FIXED (upstream corrected it, no entry needed) per candidate.

Fix round 1: the original version of this script checked only each
schema's top-level `properties`/`required`. v3 composes heavily with
`allOf`/`oneOf`/`anyOf`, so that missed inherited/composed fields and
produced a false ALREADY-FIXED for A8 (peakBandwidth lives inside an allOf
branch of EnhancedTunnelBase / StaticTunnelCreate, not at top level) and
made the A6 required-list checks for IPSecRedundantTunnel and
NetworkTunnelIpsecRedundant unreliable (their required fields are nested
inside allOf branches / referenced sub-schemas too). declares_property()
and required_fields() below walk the full composition tree so every
property/required check in this script is composition-aware.

Fix round 2 (rebuilt from `.swagger-codegen-ignore` and the v2.3 hand-patched
files themselves, not from LEFTOVERS.md/DEVELOPER-GUIDE.md prose — see
api/AUDIT-2026-08-10.md): round 1 had two further defects, neither caused by
the composition blind spot above.

- A7 (object-service protocol anyOf shape, BUG-17) was listed as a
  carried-forward candidate in the design spec but had **no check at all**
  in round 1 of this script — not a wrong verdict, an absent one.
- A9 (ASN/RemoteASN, BUG-24) checked `schema.get("type") != "integer"`, which
  is a *proxy* for the defect, not the defect itself. v3's ASN/RemoteASN do
  declare `type: integer` at top level (so the proxy check passed and this
  script reported ALREADY-FIXED both rounds) but each ALSO carries a sibling
  `oneOf` of narrower integer ranges that drives openapi-generator 7.24.0 to
  emit an empty-struct wrapper regardless of the sibling `type: integer` —
  the exact symptom BUG-24 exists to fix. The check now tests the oneOf
  sibling directly.
"""
import pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
doc = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))
schemas = doc["components"]["schemas"]
paths = doc["paths"]
results = []


def record(cid, desc, defect_present, detail):
    results.append((cid, desc, "CONFIRMED" if defect_present else "ALREADY-FIXED", detail))


def declares_property(schema, name, schemas, depth=0):
    """True if `schema` declares property `name` at ANY composition depth.

    v3 composes heavily with allOf, so a top-level `properties` check misses
    inherited fields. That miss produced a false ALREADY-FIXED for A8.
    """
    if depth > 8 or not isinstance(schema, dict):
        return False
    if name in (schema.get("properties") or {}):
        return True
    ref = schema.get("$ref")
    if ref and declares_property(schemas.get(ref.rsplit("/", 1)[-1]), name, schemas, depth + 1):
        return True
    for key in ("allOf", "oneOf", "anyOf"):
        for branch in schema.get(key) or []:
            if declares_property(branch, name, schemas, depth + 1):
                return True
    return False


def required_fields(schema, schemas, depth=0):
    """Union of `required` entries across every composition branch."""
    out = set()
    if depth > 8 or not isinstance(schema, dict):
        return out
    out.update(schema.get("required") or [])
    ref = schema.get("$ref")
    if ref:
        out |= required_fields(schemas.get(ref.rsplit("/", 1)[-1]), schemas, depth + 1)
    for key in ("allOf", "oneOf", "anyOf"):
        for branch in schema.get(key) or []:
            out |= required_fields(branch, schemas, depth + 1)
    return out


# A4 — Application GET oneOf missing a discriminator
op = paths.get("/v3/applications/{applicationId}", {}).get("get", {})
sch = op.get("responses", {}).get("200", {}).get("content", {}).get("application/json", {}).get("schema", {})
ref = sch.get("$ref", "")
target = schemas.get(ref.rsplit("/", 1)[-1], {}) if ref else sch
has_oneof = "oneOf" in target
has_disc = "discriminator" in target
record("A4", "Application GET oneOf discriminator", has_oneof and not has_disc,
       f"oneOf={has_oneof} discriminator={has_disc}")

# A5 — ApplicationAuth.authEnabled wrongly required (composition-aware)
auth = schemas.get("ApplicationAuth", {})
auth_required = required_fields(auth, schemas)
record("A5", "ApplicationAuth.authEnabled required", "authEnabled" in auth_required,
       f"required={sorted(auth_required)}")

# A6 — over-declared required lists (composition-aware)
for name, field in (("IPSecSharedSettingsCreate", "p81ASN"),
                    ("IPSecRedundantTunnel", None),
                    ("NetworkTunnelIpsecRedundant", None)):
    s = schemas.get(name, {})
    req = required_fields(s, schemas)
    if field:
        record(f"A6:{name}", f"{name}.{field} required", field in req, f"required={sorted(req)}")
    else:
        record(f"A6:{name}", f"{name} required list", bool(req), f"required={sorted(req)}")

# A7 — object-service protocol shape (anyOf strict-match failure, BUG-17).
# Fix round 2: this candidate was named in the design spec's carried-forward
# table but round 1 of this script never checked it at all — there was no
# A7 record anywhere in the original version of this file. The defect is an
# anyOf wrapper directly at the schema's own top level (no composition to
# resolve), so a plain `"anyOf" in s` check is sufficient.
for name in ("ObjectsServicesProtocolRequestObj", "ObjectsServicesProtocolResponseObj"):
    s = schemas.get(name, {})
    has_anyof = "anyOf" in s
    record(f"A7:{name}", f"{name} anyOf wrapper (BUG-17)", has_anyof,
           f"anyOf={has_anyof}")

# A8 — peakBandwidth vs peakBandwidthMbps (composition-aware)
hits = [n for n, s in schemas.items()
        if isinstance(s, dict) and declares_property(s, "peakBandwidth", schemas)]
record("A8", "peakBandwidth (not ...Mbps) property name", bool(hits), f"schemas={hits}")

# A9 — ASN / RemoteASN empty-struct-via-oneOf (BUG-24). Fix round 2: round 1
# checked only `schema.get("type") != "integer"` and reported ALREADY-FIXED
# because v3's ASN/RemoteASN do declare `type: integer` at top level — true,
# but a proxy for the actual defect. Both schemas ALSO carry a sibling
# `oneOf` of narrower integer ranges, and openapi-generator 7.24.0's Go
# codegen follows that oneOf into a wrapper model instead of the sibling
# `type: integer`, regenerating the exact `type ASN struct {}` empty struct
# BUG-24 exists to work around (confirmed by generating this SDK from
# v3.upstream.yaml with no overlay entry: model_asn.go is `type ASN struct
# {}`). This check tests the oneOf sibling directly instead of using `type`
# as a stand-in for it.
for name in ("ASN", "RemoteASN"):
    s = schemas.get(name, {})
    has_redundant_oneof = s.get("type") == "integer" and "oneOf" in s
    record(f"A9:{name}", f"{name} type=integer + redundant oneOf (BUG-24)",
           has_redundant_oneof,
           f"type={s.get('type')} oneOf={'oneOf' in s}")

# A10 — EnhancedHealthCheckMeta over-required (composition-aware)
s = schemas.get("EnhancedHealthCheckMeta", {})
req = required_fields(s, schemas)
record("A10", "EnhancedHealthCheckMeta required list", bool(req), f"required={sorted(req)}")

# A11 — ObjectsServicesResponseObj missing id (composition-aware)
s = schemas.get("ObjectsServicesResponseObj", {})
record("A11", "ObjectsServicesResponseObj.id present",
       not declares_property(s, "id", schemas),
       f"properties={sorted((s.get('properties') or {}).keys())}")

width = max(len(r[1]) for r in results)
for cid, desc, verdict, detail in results:
    print(f"{cid:<28} {desc:<{width}}  {verdict:<13} {detail}")
print(f"\nCONFIRMED: {sum(1 for r in results if r[2]=='CONFIRMED')} / {len(results)}")
