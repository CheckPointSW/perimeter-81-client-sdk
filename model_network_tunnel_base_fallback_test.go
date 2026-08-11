package perimeter81sdk

import (
	"encoding/json"
	"testing"
	"time"
)

// TestNetworkTunnel_UnrecognizedTypeWithCreatedAt_FallsBackToBase covers
// overlay entry A15-network-tunnel-anyof-add-base-fallback: GET
// /v3/networks/standard/{id} returns tunnel objects whose `type` is not one
// of the four concrete NetworkTunnel variants the spec enumerates (openvpn,
// wireguard, ipsec single, ipsec redundant) — `connector` is the documented
// example. Before A15, the anyOf decoder had nowhere for such a payload to
// land and every read of a network containing one failed outright. This
// case includes createdAt, so NetworkTunnelBase's own required-field check
// (inherited from BaseDates.required=[createdAt]) is satisfied and the
// fallback decodes cleanly — see the sibling test below for the realistic
// case where createdAt is absent, which currently does NOT decode cleanly.
func TestNetworkTunnel_UnrecognizedTypeWithCreatedAt_FallsBackToBase(t *testing.T) {
	payload := []byte(`{"id":"abc123","network":"n1","region":"r1","instance":"i1","interfaceName":"conn01","type":"connector","isHA":false,"tenantId":"t1","createdAt":"2026-01-01T00:00:00Z"}`)

	var got NetworkTunnel
	err := json.Unmarshal(payload, &got)
	if err != nil {
		t.Fatalf("Unmarshal() returned error for a connector-shaped payload: %v", err)
	}
	if got.NetworkTunnelBase == nil {
		t.Fatal("expected NetworkTunnelBase to be populated, got nil")
	}
	if got.NetworkTunnelBase.Id != "abc123" {
		t.Errorf("NetworkTunnelBase.Id = %q, want %q", got.NetworkTunnelBase.Id, "abc123")
	}
	if got.NetworkTunnelBase.Type != "connector" {
		t.Errorf("NetworkTunnelBase.Type = %q, want %q", got.NetworkTunnelBase.Type, "connector")
	}
	if got.NetworkTunnelOpenvpn != nil || got.NetworkTunnelWireguard != nil ||
		got.NetworkTunnelIpsecSingle != nil || got.NetworkTunnelIpsecRedundant != nil {
		t.Error("expected only NetworkTunnelBase to be populated, but a concrete variant was also set")
	}
}

// TestNetworkTunnel_UnrecognizedTypeWithoutCreatedAt_StillErrors documents a
// gap this task's dispatch explicitly flagged as a decision point rather
// than something to improvise a fix for: the task brief's own example
// connector payload omits createdAt (noting that omission is realistic —
// it is the exact wire shape v2.3's hand-patch was written against), on the
// assumption that CreatedAt (a non-pointer time.Time) would decode to its
// zero value once "strict decoding" is off.
//
// That assumption does not hold. NetworkTunnelBase.UnmarshalJSON (generated
// by model_simple.mustache's {{#hasRequired}} block, gated only on whether
// the schema has required fields at all — NOT on the
// disallowAdditionalPropertiesIfNotPresent flag generate.sh sets) explicitly
// checks that every required property, including createdAt, exists as a key
// in the raw JSON object before attempting to populate the struct. createdAt
// is required on NetworkTunnelBase (inherited from BaseDates.required via
// its allOf composition), so a payload that omits it fails this presence
// check before CreatedAt ever gets a chance to zero-value-decode, and
// NetworkTunnelBase (like every other anyOf member) fails to match — with
// no other member matching a `type: connector` payload either, the whole
// anyOf decode still returns "data failed to match schemas in
// anyOf(NetworkTunnel)", i.e. the original bug, for exactly the realistic
// wire shape A15 was meant to fix.
// Resolving this would require loosening NetworkTunnelBase.required (e.g. an
// overlay entry dropping createdAt, mirroring A10's treatment of
// EnhancedHealthCheckMeta) — a schema-level behavior change intentionally
// left for a human decision, not made here.
func TestNetworkTunnel_UnrecognizedTypeWithoutCreatedAt_StillErrors(t *testing.T) {
	payload := []byte(`{"id":"abc123","network":"n1","region":"r1","instance":"i1","interfaceName":"conn01","type":"connector","isHA":false,"tenantId":"t1"}`)

	var got NetworkTunnel
	err := json.Unmarshal(payload, &got)
	if err == nil {
		t.Fatal("Unmarshal() unexpectedly succeeded for a connector payload missing createdAt — " +
			"if NetworkTunnelBase.required has since been loosened to drop createdAt, update this " +
			"test (and its sibling) to assert the new, fixed behavior instead of documenting the gap.")
	}
	if got.NetworkTunnelBase != nil {
		t.Errorf("expected NetworkTunnelBase to remain nil on decode failure, got %+v", got.NetworkTunnelBase)
	}
}

// TestNetworkTunnel_ConcreteVariantDoesNotFallBackToBase guards the ordering
// requirement in A15: NetworkTunnelBase's fields are a strict subset of
// every concrete variant's, so a genuine wireguard (or openvpn/ipsec)
// payload also satisfies NetworkTunnelBase's required-field check. If the
// generated anyOf decoder tried NetworkTunnelBase before the concrete
// variants, it would swallow this payload and the wireguard-specific fields
// (LeftAllowedIP, LeftEndpoint, Vault, RequestConfigToken) would be lost.
// This is the regression the "NetworkTunnelBase must be last" requirement
// protects against.
func TestNetworkTunnel_ConcreteVariantDoesNotFallBackToBase(t *testing.T) {
	payload := []byte(`{
		"id": "wg1",
		"network": "n1",
		"region": "r1",
		"instance": "i1",
		"interfaceName": "wg01",
		"type": "wireguard",
		"isHA": false,
		"tenantId": "t1",
		"createdAt": "2026-01-01T00:00:00Z",
		"leftAllowedIP": ["10.0.0.0/24"],
		"leftEndpoint": "10.0.0.1:51820",
		"vault": "vault-1",
		"requestConfigToken": "token-1"
	}`)

	var got NetworkTunnel
	err := json.Unmarshal(payload, &got)
	if err != nil {
		t.Fatalf("Unmarshal() returned error for a valid wireguard payload: %v", err)
	}
	if got.NetworkTunnelBase != nil {
		t.Fatalf("expected a wireguard payload to land in NetworkTunnelWireguard, but NetworkTunnelBase was populated instead: %+v", got.NetworkTunnelBase)
	}
	if got.NetworkTunnelWireguard == nil {
		t.Fatal("expected NetworkTunnelWireguard to be populated, got nil")
	}
	if got.NetworkTunnelWireguard.Id != "wg1" {
		t.Errorf("NetworkTunnelWireguard.Id = %q, want %q", got.NetworkTunnelWireguard.Id, "wg1")
	}
	if got.NetworkTunnelWireguard.LeftEndpoint != "10.0.0.1:51820" {
		t.Errorf("NetworkTunnelWireguard.LeftEndpoint = %q, want %q", got.NetworkTunnelWireguard.LeftEndpoint, "10.0.0.1:51820")
	}
	wantCreatedAt := time.Date(2026, 1, 1, 0, 0, 0, 0, time.UTC)
	if !got.NetworkTunnelWireguard.CreatedAt.Equal(wantCreatedAt) {
		t.Errorf("NetworkTunnelWireguard.CreatedAt = %v, want %v", got.NetworkTunnelWireguard.CreatedAt, wantCreatedAt)
	}
}
