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

# A8 — peakBandwidth vs peakBandwidthMbps (composition-aware)
hits = [n for n, s in schemas.items()
        if isinstance(s, dict) and declares_property(s, "peakBandwidth", schemas)]
record("A8", "peakBandwidth (not ...Mbps) property name", bool(hits), f"schemas={hits}")

# A9 — ASN integer width (top-level type/format; not a composition blind
# spot — ASN/RemoteASN declare `type` directly, so this check is left as-is)
for name in ("ASN", "RemoteASN"):
    s = schemas.get(name, {})
    record(f"A9:{name}", f"{name} type/format", s.get("type") != "integer",
           f"type={s.get('type')} format={s.get('format')}")

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
