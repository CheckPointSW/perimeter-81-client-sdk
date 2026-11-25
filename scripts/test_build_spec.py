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

def test_upstream_now_declares_the_security_scheme_itself():
    """The 2026-11 refresh is the point upstream started declaring bearer auth
    centrally, which is why overlay entries A1a/A1b were deleted. Asserting the
    upstream file directly also proves build_spec.py never mutates it."""
    d = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))
    assert d["components"]["securitySchemes"]["bearer"] == {
        "type": "http", "scheme": "bearer", "bearerFormat": "JWT",
    }
    assert d["security"] == [{"bearer": []}]

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
    """One assertion per CONFIRMED row in api/AUDIT-2026-08-10.md that still
    has a live overlay entry. Delete an assertion only when its overlay entry
    is deleted.

    Fix round 1: A6's other two schemas (IPSecRedundantTunnel,
    NetworkTunnelIpsecRedundant) and A8 (peakBandwidth) were first recorded
    ALREADY-FIXED by a buggy top-level-only audit check, then corrected to
    CONFIRMED once the audit became composition-aware (see
    api/AUDIT-2026-08-10.md). A9 (ASN/RemoteASN) is the one candidate that
    stayed ALREADY-FIXED in both passes, so it still has no assertion here.

    2026-11 spec refresh: the A4, A8 and A6:NetworkTunnelIpsecRedundant
    assertions were deleted along with their entries — upstream now ships the
    application-GET discriminator itself (on a named ApplicationResponse
    schema rather than inline), renamed peakBandwidth to peakBandwidthMbps,
    and collapsed NetworkTunnelIpsecRedundant into NetworkTunnelIpsecSingle.
    The upstream side of those three is asserted by
    test_upstream_adopted_the_corrections_the_refresh_deleted below, so the
    deletions stay honest: if upstream ever regresses, that test fails rather
    than the defect passing unnoticed."""
    d = build()
    s = d["components"]["schemas"]
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
    # A10
    assert s["EnhancedHealthCheckMeta"].get("required") == []
    # A11
    assert "id" in s["ObjectsServicesResponseObj"]["properties"]


def test_upstream_adopted_the_corrections_the_refresh_deleted():
    """The 2026-11 refresh deleted A1a/A1b, A4, A8 and the two
    NetworkTunnelIpsecRedundant entries because upstream fixed each defect at
    source. Assert that against the pristine upstream file, so a future
    upstream regression reopens as a test failure instead of silently
    reintroducing a defect no overlay entry covers any more."""
    s = yaml.safe_load(open(ROOT / "api" / "v3.upstream.yaml"))["components"]["schemas"]
    # A4: the application-GET oneOf is now a named schema carrying its own
    # discriminator, rather than an inline oneOf with none.
    assert s["ApplicationResponse"]["discriminator"] == {
        "propertyName": "type",
        "mapping": {
            "http": "#/components/schemas/HttpApplication",
            "https": "#/components/schemas/HttpsApplication",
            "rdp": "#/components/schemas/RdpApplication",
            "ssh": "#/components/schemas/SshApplication",
            "vnc": "#/components/schemas/VncApplication",
        },
    }
    # A8: no schema declares peakBandwidth at any depth any more, and the two
    # schemas that used to now declare peakBandwidthMbps instead. Checked
    # composition-aware rather than at a fixed allOf index: the refresh also
    # reshaped EnhancedTunnelBase's branches (IPSecAdvancedSettingsV2_3
    # became IPSecAdvancedFieldsV2_3), so an index-based assertion would be
    # testing branch layout rather than the rename this entry is about.
    for name, schema in s.items():
        assert not _declares_property_anywhere(schema, "peakBandwidth", s), name
    for name in ("EnhancedTunnelBase", "StaticTunnelCreate"):
        assert _declares_property_anywhere(s[name], "peakBandwidthMbps", s), name
    # A6/A17d: the redundant-tunnel read variant is gone; a redundant tunnel is
    # reported as NetworkTunnelIpsecSingle with NetworkTunnelBase.isHA true.
    assert "NetworkTunnelIpsecRedundant" not in s
    assert [b["$ref"].rsplit("/", 1)[-1] for b in s["NetworkTunnel"]["oneOf"]] == [
        "NetworkTunnelOpenvpn", "NetworkTunnelWireGuard", "NetworkTunnelIpsecSingle",
    ]

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


def test_a25_tunnel_variants_drop_only_created_at_from_required():
    """A25a-A25c (2026-11 spec refresh) replace the A15/A16/A17a-d family.

    Upstream now models NetworkTunnel as a discriminated `oneOf` on `type`
    with `connector` enumerated, so A15's catch-all NetworkTunnelBase member
    (and A16's trim that made it usable, and A17a-d's re-pins that contained
    the trim) are all moot — see api/overlay.yaml's replacement note.

    What survives is the wire observation underneath them: these read
    payloads are observed without createdAt, and with no catch-all member
    left, a correctly-discriminated payload missing a required field now
    fails the whole standard-network read. A25a-C flatten each variant and
    restore its full composed required set MINUS createdAt. This asserts
    both halves: createdAt is gone from required, every other field is still
    required (so the rest of the model does not silently become pointers),
    and createdAt survives as an optional property."""
    d = build()
    s = d["components"]["schemas"]
    expected = {
        "NetworkTunnelOpenvpn": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "passphrase", "username",
        },
        "NetworkTunnelWireGuard": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "leftAllowedIP", "leftEndpoint",
            "vault", "requestConfigToken",
        },
        "NetworkTunnelIpsecSingle": {
            "id", "network", "region", "instance", "interfaceName", "type",
            "isHA", "tenantId", "keyExchange", "ikeLifeTime",
            "lifetime", "dpdDelay", "dpdTimeout", "phase1", "phase2",
            "right", "rightID", "passphrase", "dpdAction", "leftSubnets",
            "rightSubnets",
        },
    }
    for name, want in expected.items():
        schema = s[name]
        assert "allOf" not in schema, (name, schema)
        assert set(schema["required"]) == want, (name, set(schema["required"]) ^ want)
        assert "createdAt" in schema["properties"], name


def test_a26_fixed_host_value_oneof_branch_has_no_additional_properties():
    """A26 (2026-11 spec refresh): the refresh added
    `additionalProperties: true` to a FixedHost.value oneOf branch that
    resolves to a plain string via allOf -> $ref FQDN. openapi-generator
    concatenates the two into the literal Go type
    `*string[string]interface{}`, which does not compile, so generation
    aborts outright rather than degrading quietly. Asserting the built spec
    keeps the branch otherwise intact — the allOf is what carries the type."""
    d = build()
    branch = d["components"]["schemas"]["FixedHost"]["properties"]["value"]["oneOf"][0]
    assert "additionalProperties" not in branch, branch
    assert branch["allOf"][0]["$ref"] == "#/components/schemas/FQDN", branch


def test_a21_a22_user_and_group_declare_id():
    """A21a/A22a: BaseModel is @ApiExcludeClass() upstream, so both schemas lose
    `id` in the export while still sending it. Without these entries the
    generated models have no Id field and neither resource can address itself."""
    doc = build()
    for name in ("User", "Group"):
        schema = doc["components"]["schemas"][name]
        props = schema["properties"]
        assert "id" in props, f"{name} must declare id"
        assert props["id"]["type"] == "string"
        assert "id" not in schema.get("required", []), (
            f"{name}.id must stay optional: making it required would put it in the "
            "generated requiredProperties list and turn an omission into a whole-page "
            "decode failure"
        )


def test_a21b_a22b_required_lists_are_gone_entirely():
    """The two read models whose `required` lists over-promised. A strict
    UnmarshalJSON turns one absent key into a failure for the ENTIRE list
    response, so any field left in these lists is a way for one bad record to
    fail a whole page.

    The list goes completely rather than down to one field. An earlier version
    of A21b kept `email`, on the grounds that CreateUserDto marks it required --
    but IdP-synced accounts never pass through that DTO and Active Directory's
    `mail` attribute is optional, so a mail-less user is a real shape and
    keeping `email` would have left the defect fully live, one field over.

    The key is REMOVED, not set to []: OpenAPI 3.0 inherits JSON-Schema
    draft-4's "required MUST have at least one element", so `required: []`
    would be an invalid document.

    PermissionCategory has the same defect and is deliberately NOT corrected:
    nothing in this phase reads it, and a required trim with no consumer is
    churn. See LEFTOVERS L18."""
    doc = build()
    for name in ("User", "Group"):
        schema = doc["components"]["schemas"][name]
        assert "required" not in schema, (
            f"{name} must declare no `required` list at all, got "
            f"{schema.get('required')!r}"
        )


def test_a21b_a22b_removal_did_not_disturb_the_properties():
    """op_remove deletes a key from a container it reaches by walking a path, so
    a wrong path could delete the wrong thing and still leave a valid document.
    Pin that both schemas kept their full property sets, so the only thing the
    two remove entries changed is strictness."""
    doc = build()
    schemas = doc["components"]["schemas"]
    # The upstream property set, plus `id` from A21a/A22a.
    assert set(schemas["User"]["properties"]) == {
        "email", "emailVerified", "firstName", "idProviderGroups", "idProviders",
        "initials", "initialsColor", "invitationAttempts", "invitationToken",
        "inviteMessage", "lastName", "role", "roleName", "roles", "terminated",
        "username", "id",
    }
    assert set(schemas["Group"]["properties"]) == {
        "applications", "isDefault", "name", "networks", "users", "vpnLocations",
        "id",
    }


def test_a24_profile_name_patterns_allow_uppercase():
    """The upstream regex is /^[a-z '-]+$/i; the export dropped the i flag. A
    ValidateFunc built from the exported pattern would reject "John".

    A24/A24b use `op: set` on a whole property node, so each entry OWNS every
    key in that node -- if upstream later raises maxLength or changes the type,
    the entry silently reverts it. Every key the entry carries is therefore
    asserted here, not just the one it exists to fix."""
    doc = build()
    props = doc["components"]["schemas"]["UserProfileDto"]["properties"]
    for field in ("firstName", "lastName"):
        assert props[field]["pattern"] == "^[a-zA-Z '-]+$", (
            f"{field} pattern must accept uppercase"
        )
        assert props[field]["maxLength"] == 30, (
            f"{field} must keep upstream's 30-character cap: op_set replaced the "
            "whole property node, so a changed cap upstream would be silently "
            "reverted by this entry"
        )
        assert props[field]["type"] == "string", f"{field} must stay a string"
        assert set(props[field]) == {"type", "maxLength", "pattern"}, (
            f"{field} has keys {sorted(props[field])}: op_set replaced the whole "
            "node, so an added upstream key (a description, a format) would be "
            "dropped here without any other test noticing"
        )


def test_upstream_still_has_the_defects_a21_a22_a24_correct():
    """Guards against the entries outliving their reason: if upstream fixes any
    of these, this test fails and the corresponding entry should be deleted
    rather than silently kept forever.

    One assertion per entry. A21b/A22b additionally have a self-firing trigger
    -- build_spec.py's op_remove raises once its target is absent -- but these
    asserts name the entry, so they fail with a clearer message than a KeyError
    out of the build."""
    with open(ROOT / "api" / "v3.upstream.yaml") as fh:
        up = yaml.safe_load(fh)["components"]["schemas"]

    assert "id" not in up["User"]["properties"], "A21a is obsolete; delete it"
    assert "id" not in up["Group"]["properties"], "A22a is obsolete; delete it"

    # A21b / A22b: upstream must still declare an over-promising `required`.
    assert up["User"].get("required") == [
        "email", "emailVerified", "initials", "roleName", "lastName",
        "firstName", "username", "terminated",
    ], "A21b is obsolete or upstream's required list changed; re-measure and delete or narrow it"
    assert up["Group"].get("required") == [
        "name", "isDefault", "applications", "networks", "vpnLocations", "users",
    ], "A22b is obsolete or upstream's required list changed; re-measure and delete or narrow it"

    # A24 / A24b: one assert each, so fixing only one upstream still fires.
    assert up["UserProfileDto"]["properties"]["firstName"]["pattern"] == "^[a-z '-]+$", (
        "A24 is obsolete; delete it"
    )
    assert up["UserProfileDto"]["properties"]["lastName"]["pattern"] == "^[a-z '-]+$", (
        "A24b is obsolete; delete it"
    )
