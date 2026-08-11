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

def test_a12_harmony_sase_regions_list_items_have_no_sibling_additional_properties():
    """A12 removes a redundant `additionalProperties: true` sibling from
    HarmonySaseRegionsList.items that openapi-generator 7.24.0's Go codegen
    mis-resolves into invalid Go (`[]HarmonySaseRegion[string]interface{}`,
    a syntax error — see api/overlay.yaml's A12 entry for the full story).

    This asserts the spec-level precondition, not the generated .go file
    directly: doing so keeps this test fast (no openapi-generator subprocess)
    and precisely localizes a regression to the overlay/spec layer. The
    Go-level guarantee — that this precondition actually produces
    `[]HarmonySaseRegion` rather than the malformed form — is enforced
    end-to-end by `go build ./...` in scripts/generate.sh, which fails loudly
    (a compile error, not a silent behaviour change) if this regresses.

    The precondition proven (empirically, before this entry existed) to
    yield the correct `[]HarmonySaseRegion` type is: items has no
    additionalProperties key of its own, and its allOf has exactly one
    substantive branch — a single $ref — with any other branch being
    property-less (e.g. just a description)."""
    d = build()
    items = d["components"]["schemas"]["HarmonySaseRegionsList"]["items"]
    assert "additionalProperties" not in items, items
    refs = [b for b in items["allOf"] if "$ref" in b]
    non_ref_branches_with_properties = [
        b for b in items["allOf"] if "$ref" not in b and "properties" in b
    ]
    assert len(refs) == 1, items
    assert refs[0]["$ref"] == "#/components/schemas/HarmonySaseRegion"
    assert non_ref_branches_with_properties == [], items

    # The upstream shape this entry corrects is not unique to
    # HarmonySaseRegionsList — DynamicTunnelUpdate.updateTunnels.items has
    # the same allOf-plus-sibling-additionalProperties shape but is left
    # alone, because its non-$ref branch is a substantive inline object
    # (forcing model materialization, which sidesteps the bug). Confirm the
    # overlay didn't touch it and that it still has real content in that
    # branch, i.e. this test's "property-less other branch" precondition is
    # what actually distinguishes the two, not some property of
    # HarmonySaseRegionsList alone.
    other_items = d["components"]["schemas"]["DynamicTunnelUpdate"]["properties"][
        "updateTunnels"]["items"]
    assert "additionalProperties" in other_items
    other_non_ref_with_properties = [
        b for b in other_items["allOf"] if "$ref" not in b and "properties" in b
    ]
    assert other_non_ref_with_properties != []
