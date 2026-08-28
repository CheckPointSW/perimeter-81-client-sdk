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
// land and every read of a network containing one failed outright.
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
	if got.NetworkTunnelBase.GetType() != "connector" {
		t.Errorf("NetworkTunnelBase.GetType() = %q, want %q", got.NetworkTunnelBase.GetType(), "connector")
	}
	wantCreatedAt := time.Date(2026, 1, 1, 0, 0, 0, 0, time.UTC)
	if !got.NetworkTunnelBase.GetCreatedAt().Equal(wantCreatedAt) {
		t.Errorf("NetworkTunnelBase.GetCreatedAt() = %v, want %v", got.NetworkTunnelBase.GetCreatedAt(), wantCreatedAt)
	}
	if got.NetworkTunnelOpenvpn != nil || got.NetworkTunnelWireguard != nil ||
		got.NetworkTunnelIpsecSingle != nil || got.NetworkTunnelIpsecRedundant != nil {
		t.Error("expected only NetworkTunnelBase to be populated, but a concrete variant was also set")
	}
}

// TestNetworkTunnel_UnrecognizedTypeWithoutCreatedAt_FallsBackToBase is the
// realistic case and the whole point of A15/A16: the live API's undocumented
// tunnel types (connector is the documented example) are observed to omit
// createdAt on the wire — the same shape the v2.3 hand-patch's guard was
// written against (`raw.Id != ""`, nothing else). Before A16 trimmed
// NetworkTunnelBase's composed required set down to [id] (it had
// transitively required createdAt via allOf -> BaseDates), this exact
// payload failed with "data failed to match schemas in anyOf(NetworkTunnel)"
// — seeing this test go from failing to passing is the actual fix, not just
// the anyOf-membership plumbing A15 added on its own.
func TestNetworkTunnel_UnrecognizedTypeWithoutCreatedAt_FallsBackToBase(t *testing.T) {
	payload := []byte(`{"id":"abc123","network":"n1","region":"r1","instance":"i1","interfaceName":"conn01","type":"connector","isHA":false,"tenantId":"t1"}`)

	var got NetworkTunnel
	err := json.Unmarshal(payload, &got)
	if err != nil {
		t.Fatalf("Unmarshal() returned error for a connector-shaped payload missing createdAt: %v", err)
	}
	if got.NetworkTunnelBase == nil {
		t.Fatal("expected NetworkTunnelBase to be populated, got nil")
	}
	if got.NetworkTunnelBase.Id != "abc123" {
		t.Errorf("NetworkTunnelBase.Id = %q, want %q", got.NetworkTunnelBase.Id, "abc123")
	}
	if got.NetworkTunnelBase.GetType() != "connector" {
		t.Errorf("NetworkTunnelBase.GetType() = %q, want %q", got.NetworkTunnelBase.GetType(), "connector")
	}
	if got.NetworkTunnelBase.HasCreatedAt() {
		t.Errorf("expected CreatedAt to be unset (absent from the payload), got %v", got.NetworkTunnelBase.GetCreatedAt())
	}
	if got.NetworkTunnelOpenvpn != nil || got.NetworkTunnelWireguard != nil ||
		got.NetworkTunnelIpsecSingle != nil || got.NetworkTunnelIpsecRedundant != nil {
		t.Error("expected only NetworkTunnelBase to be populated, but a concrete variant was also set")
	}
}

// TestNetworkTunnel_EmptyPayloadStillFailsToMatch guards the other side of
// A16's trim: NetworkTunnelBase.required = [id] is permissive enough to
// catch any unrecognised tunnel type, but must still be strict enough that
// garbage or empty input does not silently produce a populated-but-meaningless
// fallback. This mirrors the exact guard the v2.3 hand-patch used
// (`raw.Id != ""`) — an object with no id at all must still fail every anyOf
// member, this one included.
func TestNetworkTunnel_EmptyPayloadStillFailsToMatch(t *testing.T) {
	payload := []byte(`{}`)

	var got NetworkTunnel
	err := json.Unmarshal(payload, &got)
	if err == nil {
		t.Fatal("Unmarshal() unexpectedly succeeded for an empty object — " +
			"the anyOf(NetworkTunnel) decoder's empty-struct check should have rejected it, " +
			"same as it does for the four concrete variants")
	}
	if got.NetworkTunnelBase != nil {
		t.Errorf("expected NetworkTunnelBase to remain nil for an empty payload, got %+v", got.NetworkTunnelBase)
	}
}

// TestNetworkTunnel_ConcreteVariantDoesNotFallBackToBase guards the ordering
// requirement in A15/model_anyof.mustache: NetworkTunnelBase's required set
// is now just [id] (A16), a strict subset of every concrete variant's, so a
// genuine wireguard (or openvpn/ipsec) payload also satisfies
// NetworkTunnelBase's required-field check trivially. If the generated
// anyOf decoder tried NetworkTunnelBase before the concrete variants, it
// would swallow this payload and the wireguard-specific fields
// (LeftAllowedIP, LeftEndpoint, Vault, RequestConfigToken) would be lost.
// This regression guard matters more now than it did before A16, since the
// base fallback accepts almost any payload with a non-empty id.
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
