package perimeter81sdk

import (
	"encoding/json"
	"testing"
)

func TestNetworkTunnel_ConnectorWithoutCreatedAt_UnmarshalsAsWireGuard(t *testing.T) {
	payload := []byte(`{
		"id": "wg1",
		"network": "n1",
		"region": "r1",
		"instance": "i1",
		"interfaceName": "conn01",
		"type": "connector",
		"isHA": false,
		"tenantId": "t1",
		"leftAllowedIP": ["10.0.0.0/24"],
		"leftEndpoint": "10.0.0.1",
		"vault": "vault-1",
		"requestConfigToken": "token-1"
	}`)

	var got NetworkTunnel
	if err := json.Unmarshal(payload, &got); err != nil {
		t.Fatalf("Unmarshal() failed for connector payload without createdAt: %v", err)
	}
	if got.NetworkTunnelWireGuard == nil {
		t.Fatal("expected NetworkTunnelWireGuard to be populated, got nil")
	}
	if got.NetworkTunnelOpenvpn != nil || got.NetworkTunnelIpsecSingle != nil {
		t.Error("expected only NetworkTunnelWireGuard to be populated")
	}
	if got.NetworkTunnelWireGuard.Id != "wg1" || got.NetworkTunnelWireGuard.Type != "connector" {
		t.Errorf("unexpected id/type: %q / %q", got.NetworkTunnelWireGuard.Id, got.NetworkTunnelWireGuard.Type)
	}
	if got.NetworkTunnelWireGuard.HasCreatedAt() {
		t.Errorf("expected CreatedAt to be unset, got %v", got.NetworkTunnelWireGuard.GetCreatedAt())
	}
	if got.NetworkTunnelWireGuard.LeftEndpoint != "10.0.0.1" {
		t.Errorf("LeftEndpoint = %q, want %q", got.NetworkTunnelWireGuard.LeftEndpoint, "10.0.0.1")
	}
}

func TestNetworkTunnel_ConnectorMissingWireGuardFields_ReturnsError(t *testing.T) {
	payload := []byte(`{
		"id": "conn1",
		"network": "n1",
		"region": "r1",
		"instance": "i1",
		"interfaceName": "conn01",
		"type": "connector",
		"isHA": false,
		"tenantId": "t1"
	}`)

	var got NetworkTunnel
	if err := json.Unmarshal(payload, &got); err == nil {
		t.Fatal("expected error for connector payload missing required WireGuard fields, got nil")
	}
	if got.NetworkTunnelWireGuard != nil {
		t.Errorf("expected NetworkTunnelWireGuard to remain nil on error, got %+v", got.NetworkTunnelWireGuard)
	}
}

func TestNetworkTunnel_OpenvpnWithoutCreatedAt_Unmarshals(t *testing.T) {
	payload := []byte(`{
		"id": "ovpn1",
		"network": "n1",
		"region": "r1",
		"instance": "i1",
		"interfaceName": "tun0",
		"type": "openvpn",
		"isHA": false,
		"tenantId": "t1",
		"passphrase": "secretPass123",
		"username": "vpnuser"
	}`)

	var got NetworkTunnel
	if err := json.Unmarshal(payload, &got); err != nil {
		t.Fatalf("Unmarshal() failed for openvpn payload without createdAt: %v", err)
	}
	if got.NetworkTunnelOpenvpn == nil {
		t.Fatal("expected NetworkTunnelOpenvpn to be populated, got nil")
	}
	if got.NetworkTunnelWireGuard != nil || got.NetworkTunnelIpsecSingle != nil {
		t.Error("expected only NetworkTunnelOpenvpn to be populated")
	}
	if got.NetworkTunnelOpenvpn.HasCreatedAt() {
		t.Errorf("expected CreatedAt to be unset, got %v", got.NetworkTunnelOpenvpn.GetCreatedAt())
	}
	if got.NetworkTunnelOpenvpn.Username != "vpnuser" {
		t.Errorf("Username = %q, want %q", got.NetworkTunnelOpenvpn.Username, "vpnuser")
	}
}

func TestNetworkTunnel_IpsecWithoutCreatedAt_UnmarshalsSingleAndHA(t *testing.T) {
	payload := []byte(`{
		"id": "ipsec1",
		"network": "n1",
		"region": "r1",
		"instance": "i1",
		"interfaceName": "ipsec0",
		"type": "ipsec",
		"isHA": true,
		"tenantId": "t1",
		"keyExchange": "ikev2",
		"ikeLifeTime": "8h",
		"lifetime": "1h",
		"dpdDelay": "10s",
		"dpdTimeout": "30s",
		"phase1": {"auth": ["sha256"], "encryption": ["aes256"], "dh": [14]},
		"phase2": {"auth": ["sha256"], "encryption": ["aes256"], "dh": [14]},
		"right": "203.0.113.10",
		"rightID": "203.0.113.10",
		"passphrase": "secretPass123",
		"dpdAction": "restart",
		"leftSubnets": ["10.255.0.0/16"],
		"rightSubnets": ["192.168.0.0/24"]
	}`)

	var got NetworkTunnel
	if err := json.Unmarshal(payload, &got); err != nil {
		t.Fatalf("Unmarshal() failed for ipsec payload without createdAt: %v", err)
	}
	if got.NetworkTunnelIpsecSingle == nil {
		t.Fatal("expected NetworkTunnelIpsecSingle to be populated, got nil")
	}
	if got.NetworkTunnelOpenvpn != nil || got.NetworkTunnelWireGuard != nil {
		t.Error("expected only NetworkTunnelIpsecSingle to be populated")
	}
	if !got.NetworkTunnelIpsecSingle.IsHA {
		t.Error("expected IsHA = true")
	}
	if got.NetworkTunnelIpsecSingle.HasCreatedAt() {
		t.Errorf("expected CreatedAt to be unset, got %v", got.NetworkTunnelIpsecSingle.GetCreatedAt())
	}
}

func TestNetworkTunnel_UnrecognizedType_LeavesActualInstanceNil(t *testing.T) {
	payload := []byte(`{"id": "x1", "type": "unknown"}`)

	var got NetworkTunnel
	if err := json.Unmarshal(payload, &got); err != nil {
		t.Fatalf("expected stock discriminator decoder to return nil error on unrecognized type, got: %v", err)
	}
	if got.GetActualInstance() != nil {
		t.Errorf("expected GetActualInstance() == nil for unrecognized type, got %#v", got.GetActualInstance())
	}
}
