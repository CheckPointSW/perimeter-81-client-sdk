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
    # no longer required, haTunnelID still is, rightASN still present as an
    # optional property. NetworkTunnelIpsecRedundant no longer has an allOf
    # of its own to inspect a branch of: A17d (fix round 1 of 5, 2026-08-11)
    # fully flattened it into a standalone flat object (decoupling it from
    # NetworkTunnelBase's required-ness so A16's trim of NetworkTunnelBase
    # doesn't cascade into it) — see that entry for why. A6's own
    # required-trim still runs first and still matters: it's what makes
    # haTunnelID (not rightASN/rightPrivateIP/leftPrivateIP) the one
    # NetworkTunnelIpsecRedundant-specific field baked into A17d's explicit
    # required list below.
    assert "allOf" not in s["NetworkTunnelIpsecRedundant"]
    assert "haTunnelID" in s["NetworkTunnelIpsecRedundant"]["required"]
    assert "rightASN" not in s["NetworkTunnelIpsecRedundant"]["required"]
    assert "rightPrivateIP" not in s["NetworkTunnelIpsecRedundant"]["required"]
    assert "leftPrivateIP" not in s["NetworkTunnelIpsecRedundant"]["required"]
    assert "rightASN" in s["NetworkTunnelIpsecRedundant"]["properties"]
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

def test_a9_asn_and_remote_asn_have_no_redundant_oneof():
    """Fix round 2 (2026-08-11): A9 was mis-checked in both prior audit passes
    as "ASN/RemoteASN type/format" and reported ALREADY-FIXED because v3's
    ASN/RemoteASN declare `type: integer` at top level — true, but a proxy
    for the actual defect. Each schema ALSO carries a sibling `oneOf` of
    narrower integer ranges, and openapi-generator 7.24.0's Go codegen
    follows that oneOf into an empty-struct wrapper (`type ASN struct {}`)
    regardless of the sibling `type: integer` — confirmed by generating this
    SDK from api/v3.upstream.yaml with no A9 overlay entry. This asserts the
    real derived postcondition (type integer stands alone, oneOf gone), not
    merely that the entry exists in the overlay file.

    Note what this test does NOT cover: `go build`/`go vet` in
    scripts/generate.sh do not fail either way here — both the old
    `struct{}` and the fixed shape compile fine standalone, since nothing in
    this SDK module itself converts a bare int to ASN/RemoteASN. The actual
    Go-level effect (confirmed manually, see api/AUDIT-2026-08-10.md) is
    that openapi-generator 7.24.0 has no mechanism to alias a bare scalar
    schema to a named Go type — with the oneOf gone, ASN/RemoteASN generate
    no model file at all, and every field that used to reference them
    (DynamicTunnelDetails.RemoteASN, EnhancedIPSecSharedSettingsCreate.LeftASN,
    IPSecRedundantTunnel.RemoteASN, etc.) becomes a plain int32/*int32 field
    that correctly carries real values end-to-end — a strict improvement
    over the unusable empty struct, but not a distinct `ASN`/`RemoteASN` Go
    type. `ASN(int32(x))`-style conversions do not compile against this
    result; they fail with "undefined: ASN", not a struct-conversion error.
    """
    d = build()
    s = d["components"]["schemas"]
    for name in ("ASN", "RemoteASN"):
        schema = s[name]
        assert schema.get("type") == "integer", (name, schema)
        assert "oneOf" not in schema, (name, schema)


def test_a7_objects_services_protocol_objects_are_flat():
    """A7 (BUG-17) had no check at all in either prior audit pass — absent,
    not wrong. v3 still declares
    ObjectsServicesProtocolRequestObj/ResponseObj as a two-member anyOf
    (ObjectServiceProtocolTCPUDP, ObjectServiceProtocolICMPRequest/Response),
    which openapi-generator 7.24.0 still turns into a pointer-pair wrapper
    with a try-each UnmarshalJSON that cannot round-trip the real flat wire
    payload (`{protocol, valueType, value}` for tcp/udp,
    `{protocol, protocolOptions}` for icmp) — the same failure the v2.3
    hand-patch (model_objects_services_protocol_request_obj.go /
    model_objects_services_protocol_response_obj.go) worked around. This
    asserts the flattened postcondition directly: no anyOf, protocol alone
    required, and the request/response variants keep their own distinct
    protocolOptions $ref (ICMPrequest vs ICMPresponse) rather than
    collapsing to one shared type."""
    d = build()
    s = d["components"]["schemas"]
    for name, options_ref in (
        ("ObjectsServicesProtocolRequestObj", "ObjectServiceProtocolOptionsICMPrequest"),
        ("ObjectsServicesProtocolResponseObj", "ObjectServiceProtocolOptionsICMPresponse"),
    ):
        schema = s[name]
        assert "anyOf" not in schema, (name, schema)
        assert schema.get("type") == "object", (name, schema)
        assert schema.get("required") == ["protocol"], (name, schema)
        props = schema["properties"]
        assert set(props) == {"protocol", "valueType", "value", "protocolOptions"}, (name, props)
        assert props["value"]["items"]["$ref"] == "#/components/schemas/PortNumber"
        assert props["protocolOptions"]["$ref"] == f"#/components/schemas/{options_ref}"


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


def test_a15_network_tunnel_anyof_has_base_fallback_last():
    """A15 appends NetworkTunnelBase to NetworkTunnel's anyOf so tunnel types
    the spec doesn't enumerate (e.g. `connector`) have somewhere to land
    instead of failing every branch of the generated decoder (see
    api/overlay.yaml's A15 entry for the full story).

    NetworkTunnelBase must be LAST: openapi-generator 7.24.0's Go codegen
    collapses anyOf into a java.util.TreeSet<String> (alphabetical by Go type
    name, confirmed via javap on CodegenModel.class), ignoring the order of
    this list entirely — so this assertion on the spec-level list order does
    NOT by itself guarantee try-order in the generated decoder. The actual
    try-order guarantee comes from templates/model_anyof.mustache's
    dash-first split (documented there), which depends on NetworkTunnelBase
    sorting alphabetically first among these five names. This test still
    asserts list order because op: set's whole-array replacement is the
    overlay-level mechanism the entry uses, and a regression here (wrong
    order or a missing member) is still worth catching early, even though
    the Go-level ordering guarantee is enforced separately by
    model_network_tunnel_base_fallback_test.go's
    TestNetworkTunnel_ConcreteVariantDoesNotFallBackToBase."""
    d = build()
    any_of = d["components"]["schemas"]["NetworkTunnel"]["anyOf"]
    refs = [b["$ref"] for b in any_of]
    assert len(refs) == 5, refs
    assert refs[-1] == "#/components/schemas/NetworkTunnelBase", refs
    assert refs[:-1] == [
        "#/components/schemas/NetworkTunnelOpenvpn",
        "#/components/schemas/NetworkTunnelWireguard",
        "#/components/schemas/NetworkTunnelIpsecSingle",
        "#/components/schemas/NetworkTunnelIpsecRedundant",
    ], refs


def test_a16_network_tunnel_base_required_is_id_only():
    """A16 (fix round 1 of 5, 2026-08-11): NetworkTunnelBase's
    composition-resolved required set was 9 fields (its own 8-field inline
    branch, plus createdAt inherited via allOf -> BaseDates) — too strict
    for its post-A15 role as NetworkTunnel's anyOf fallback member, since the
    live API's undocumented tunnel types are observed to omit createdAt on
    the wire (see api/overlay.yaml's A16 entry). This asserts the
    flattened postcondition: no allOf left, required trimmed to exactly
    [id], and every field BaseDates/its own inline branch used to require
    (network, region, instance, interfaceName, type, isHA, tenantId,
    createdAt, updatedAt) is still present as an (now-optional) property —
    nothing was dropped, only required-ness."""
    d = build()
    base = d["components"]["schemas"]["NetworkTunnelBase"]
    assert "allOf" not in base, base
    assert base["required"] == ["id"], base["required"]
    for prop in (
        "id", "network", "region", "instance", "interfaceName", "type",
        "isHA", "tenantId", "createdAt", "updatedAt",
    ):
        assert prop in base["properties"], prop


def test_a17_concrete_tunnel_variants_required_sets_are_unchanged():
    """A17a-A17d (fix round 1 of 5, 2026-08-11): A16 trims NetworkTunnelBase's
    own required list to [id]. Because openapi-generator unions required
    fields across all of a schema's allOf branches at generation time, and
    NetworkTunnelOpenvpn/Wireguard/IpsecSingle/IpsecRedundant each compose
    NetworkTunnelBase via allOf, A16 would otherwise silently cascade into
    all four of their composed required sets too — the exact "no other
    schema's required set changed" hazard flagged when this fix round was
    reviewed. A17a-A17d flatten each of the four into a standalone object
    with their exact pre-A16 composed required set restored explicitly,
    decoupling them from NetworkTunnelBase's required-ness entirely. This
    asserts each schema's flattened required set still matches ground truth
    captured from the generated Go files before A16/A17a-A17d existed."""
    d = build()
    s = d["components"]["schemas"]
    expected = {
        "NetworkTunnelOpenvpn": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "createdAt", "passphrase", "username",
        },
        "NetworkTunnelWireguard": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "createdAt", "leftAllowedIP", "leftEndpoint",
            "vault", "requestConfigToken",
        },
        "NetworkTunnelIpsecSingle": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "createdAt", "keyExchange", "ikeLifeTime",
            "lifetime", "dpdDelay", "dpdTimeout", "phase1", "phase2",
            "right", "rightID", "passphrase", "dpdAction", "leftSubnets",
            "rightSubnets",
        },
        "NetworkTunnelIpsecRedundant": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "createdAt", "keyExchange", "ikeLifeTime",
            "lifetime", "dpdDelay", "dpdTimeout", "phase1", "phase2",
            "right", "rightID", "passphrase", "dpdAction", "leftSubnets",
            "rightSubnets", "haTunnelID",
        },
    }
    for name, want in expected.items():
        schema = s[name]
        assert "allOf" not in schema, (name, schema)
        assert set(schema["required"]) == want, (name, set(schema["required"]) ^ want)
