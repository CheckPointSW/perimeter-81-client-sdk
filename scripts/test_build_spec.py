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

def test_carried_forward_patches_are_applied():
    """One assertion per CONFIRMED row in api/AUDIT-2026-08-10.md.
    Delete an assertion only when its overlay entry is deleted.

    A6's other two schemas (IPSecRedundantTunnel, NetworkTunnelIpsecRedundant),
    A8 (peakBandwidth), and A9 (ASN/RemoteASN) came back ALREADY-FIXED in the
    audit, so they have no overlay entry and no assertion here."""
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
    # A6
    assert "p81ASN" not in (s["IPSecSharedSettingsCreate"].get("required") or [])
    # A10
    assert s["EnhancedHealthCheckMeta"].get("required") == []
    # A11
    assert "id" in s["ObjectsServicesResponseObj"]["properties"]
