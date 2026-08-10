import subprocess, sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

def build():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_spec.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return yaml.safe_load(open(ROOT / "api" / "swagger.yaml"))

def test_bearer_security_scheme_restored():
    d = build()
    assert d["components"]["securitySchemes"]["bearer"] == {
        "type": "http", "scheme": "bearer", "bearerFormat": "JWT",
    }
    assert d["security"] == [{"bearer": []}]

def test_no_operation_declares_the_auth_param():
    d = build()
    offenders = []
    for path, item in d["paths"].items():
        for method, op in item.items():
            if method not in ("get", "post", "put", "delete", "patch"):
                continue
            for prm in op.get("parameters") or []:
                if "authParam" in str(prm.get("$ref", "")):
                    offenders.append(f"{method.upper()} {path}")
    assert offenders == [], offenders

def test_upstream_lacks_the_security_scheme_the_overlay_adds():
    """The upstream spec declares no securitySchemes at all — the key is ABSENT,
    not present-but-empty — and no top-level security. That is the defect A1
    corrects, so asserting it here also proves build_spec.py never mutates the
    upstream file."""
    d = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))
    assert "securitySchemes" not in d.get("components", {})
    assert "security" not in d

GUM_EXPECTED = {
    ("/v3/gum/custom-roles", "get"): "listCustomRoles",
    ("/v3/gum/custom-roles", "post"): "createCustomRole",
    ("/v3/gum/custom-roles/categories", "get"): "getCustomRoleCategories",
    ("/v3/gum/custom-roles/{roleId}", "get"): "getCustomRole",
    ("/v3/gum/custom-roles/{roleId}", "put"): "updateCustomRole",
    ("/v3/gum/custom-roles/{roleId}", "delete"): "deleteCustomRole",
}

def test_gum_operations_have_tags_and_operation_ids():
    d = build()
    for (path, method), op_id in GUM_EXPECTED.items():
        op = d["paths"][path][method]
        assert op.get("operationId") == op_id, (path, method, op.get("operationId"))
        assert op.get("tags") == ["Custom Roles"], (path, method, op.get("tags"))

def test_no_operation_is_left_untagged():
    d = build()
    untagged = [
        f"{m.upper()} {p}"
        for p, item in d["paths"].items()
        for m, op in item.items()
        if m in ("get", "post", "put", "delete", "patch") and not op.get("tags")
    ]
    assert untagged == [], untagged

def _declares_property_anywhere(schema, name, schemas, depth=0):
    """Composition-aware property check, mirroring
    scripts/audit_carried_patches.py's declares_property(). Used here so the
    A8 assertion can't be fooled by a property nested inside an allOf branch
    the way the first (buggy) audit pass was."""
    if depth > 8 or not isinstance(schema, dict):
        return False
    if name in (schema.get("properties") or {}):
        return True
    ref = schema.get("$ref")
    if ref and _declares_property_anywhere(schemas.get(ref.rsplit("/", 1)[-1]), name, schemas, depth + 1):
        return True
    for key in ("allOf", "oneOf", "anyOf"):
        for branch in schema.get(key) or []:
            if _declares_property_anywhere(branch, name, schemas, depth + 1):
                return True
    return False

def test_carried_forward_patches_are_applied():
    """One assertion per CONFIRMED row in api/AUDIT-2026-08-10.md.
    Delete an assertion only when its overlay entry is deleted.

    Fix round 1: A8 (peakBandwidth) and A6's other two schemas
    (IPSecRedundantTunnel, NetworkTunnelIpsecRedundant) were first recorded
    ALREADY-FIXED by a buggy top-level-only audit check, then corrected to
    CONFIRMED once the audit became composition-aware (see
    api/AUDIT-2026-08-10.md). A9 (ASN/RemoteASN) is the one candidate that
    stayed ALREADY-FIXED in both passes, so it still has no assertion here."""
    d = build()
    s = d["components"]["schemas"]
    # A4
    disc = d["paths"]["/v3/applications/{applicationId}"]["get"]["responses"]["200"][
        "content"]["application/json"]["schema"].get("discriminator")
    assert disc == {
        "propertyName": "type",
        "mapping": {
            "http": "#/components/schemas/HttpApplication",
            "https": "#/components/schemas/HttpsApplication",
            "rdp": "#/components/schemas/RdpApplication",
            "ssh": "#/components/schemas/SshApplication",
            "vnc": "#/components/schemas/VncApplication",
        },
    }
    # A5
    assert "authEnabled" not in (s["ApplicationAuth"].get("required") or [])
    # A6:IPSecSharedSettingsCreate
    assert "p81ASN" not in (s["IPSecSharedSettingsCreate"].get("required") or [])
    # A6:IPSecRedundantTunnel — passphrase/remoteID no longer required, but
    # still present as optional properties; the shared create-side ancestor
    # schemas must be untouched (passphrase genuinely required on create).
    redundant = s["IPSecRedundantTunnel"]
    assert "passphrase" not in (redundant.get("required") or [])
    assert "remoteID" not in (redundant.get("required") or [])
    assert "passphrase" in redundant["properties"]
    assert set(redundant["required"]) == {
        "p81GWInternalIP", "remoteGWInternalIP", "remotePublicIP", "remoteASN", "gatewayID",
    }
    assert "passphrase" in (s["IPSecRedundantTunnelDetails"].get("required") or []), (
        "the shared create-path ancestor must still require passphrase"
    )
    # A6:NetworkTunnelIpsecRedundant — rightASN/rightPrivateIP/leftPrivateIP
    # no longer required, haTunnelID still is, inline branch otherwise intact.
    branches = [b for b in s["NetworkTunnelIpsecRedundant"]["allOf"] if "$ref" not in b]
    assert len(branches) == 1
    assert branches[0]["required"] == ["haTunnelID"]
    assert "rightASN" in branches[0]["properties"]
    # A8 — composition-aware: no schema declares peakBandwidth at any depth,
    # and the two schemas that used to (EnhancedTunnelBase, StaticTunnelCreate)
    # now declare peakBandwidthMbps instead.
    for name, schema in s.items():
        assert not _declares_property_anywhere(schema, "peakBandwidth", s), name
    assert "peakBandwidthMbps" in s["EnhancedTunnelBase"]["allOf"][1]["properties"]
    assert "peakBandwidthMbps" in s["StaticTunnelCreate"]["allOf"][1]["properties"]
    # A10
    assert s["EnhancedHealthCheckMeta"].get("required") == []
    # A11
    assert "id" in s["ObjectsServicesResponseObj"]["properties"]
