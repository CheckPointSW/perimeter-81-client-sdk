#!/usr/bin/env python3
"""Check each v2.3-era hand-patch against the v3 upstream spec.

Prints CONFIRMED (defect still present, needs an overlay entry) or
ALREADY-FIXED (upstream corrected it, no entry needed) per candidate.
"""
import pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
doc = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))
schemas = doc["components"]["schemas"]
paths = doc["paths"]
results = []


def record(cid, desc, defect_present, detail):
    results.append((cid, desc, "CONFIRMED" if defect_present else "ALREADY-FIXED", detail))


# A4 — Application GET oneOf missing a discriminator
op = paths.get("/v3/applications/{applicationId}", {}).get("get", {})
sch = op.get("responses", {}).get("200", {}).get("content", {}).get("application/json", {}).get("schema", {})
ref = sch.get("$ref", "")
target = schemas.get(ref.rsplit("/", 1)[-1], {}) if ref else sch
has_oneof = "oneOf" in target
has_disc = "discriminator" in target
record("A4", "Application GET oneOf discriminator", has_oneof and not has_disc,
       f"oneOf={has_oneof} discriminator={has_disc}")

# A5 — ApplicationAuth.authEnabled wrongly required
auth = schemas.get("ApplicationAuth", {})
record("A5", "ApplicationAuth.authEnabled required", "authEnabled" in (auth.get("required") or []),
       f"required={auth.get('required')}")

# A6 — over-declared required lists
for name, field in (("IPSecSharedSettingsCreate", "p81ASN"),
                    ("IPSecRedundantTunnel", None),
                    ("NetworkTunnelIpsecRedundant", None)):
    s = schemas.get(name, {})
    req = s.get("required") or []
    if field:
        record(f"A6:{name}", f"{name}.{field} required", field in req, f"required={req}")
    else:
        record(f"A6:{name}", f"{name} required list", bool(req), f"required={req}")

# A8 — peakBandwidth vs peakBandwidthMbps
hits = [n for n, s in schemas.items()
        if isinstance(s, dict) and "peakBandwidth" in (s.get("properties") or {})]
record("A8", "peakBandwidth (not ...Mbps) property name", bool(hits), f"schemas={hits}")

# A9 — ASN integer width
for name in ("ASN", "RemoteASN"):
    s = schemas.get(name, {})
    record(f"A9:{name}", f"{name} type/format", s.get("type") != "integer",
           f"type={s.get('type')} format={s.get('format')}")

# A10 — EnhancedHealthCheckMeta over-required
s = schemas.get("EnhancedHealthCheckMeta", {})
record("A10", "EnhancedHealthCheckMeta required list", bool(s.get("required")),
       f"required={s.get('required')}")

# A11 — ObjectsServicesResponseObj missing id
s = schemas.get("ObjectsServicesResponseObj", {})
record("A11", "ObjectsServicesResponseObj.id present",
       "id" not in (s.get("properties") or {}),
       f"properties={sorted((s.get('properties') or {}).keys())}")

width = max(len(r[1]) for r in results)
for cid, desc, verdict, detail in results:
    print(f"{cid:<28} {desc:<{width}}  {verdict:<13} {detail}")
print(f"\nCONFIRMED: {sum(1 for r in results if r[2]=='CONFIRMED')} / {len(results)}")
