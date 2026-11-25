package perimeter81sdk

import (
	"encoding/json"
	"testing"
)

func TestNetworkInstance_IdleField(t *testing.T) {
	base := func(idleField string) []byte {
		return []byte(`{
			"id": "inst1",
			"tenantId": "t1",
			"network": "n1",
			"region": "r1",
			"instanceType": "gw",
			"imageType": "standard",
			"imageVersion": "1.0",
			"dns": "gw.example.com",
			"ip": "203.0.113.1",
			"tunnels": [],
			"createdAt": "2026-01-01T00:00:00Z"` + idleField + `
		}`)
	}

	t.Run("idle true", func(t *testing.T) {
		var got NetworkInstance
		if err := json.Unmarshal(base(`,"idle":true`), &got); err != nil {
			t.Fatalf("Unmarshal() error: %v", err)
		}
		if !got.HasIdle() || !got.GetIdle() {
			t.Errorf("expected idle=true, got has=%v val=%v", got.HasIdle(), got.GetIdle())
		}
	})

	t.Run("idle false", func(t *testing.T) {
		var got NetworkInstance
		if err := json.Unmarshal(base(`,"idle":false`), &got); err != nil {
			t.Fatalf("Unmarshal() error: %v", err)
		}
		if !got.HasIdle() || got.GetIdle() {
			t.Errorf("expected idle=false, got has=%v val=%v", got.HasIdle(), got.GetIdle())
		}
	})

	t.Run("idle omitted", func(t *testing.T) {
		var got NetworkInstance
		if err := json.Unmarshal(base(``), &got); err != nil {
			t.Fatalf("Unmarshal() error: %v", err)
		}
		if got.HasIdle() {
			t.Errorf("expected idle to be unset when omitted, got %v", got.GetIdle())
		}
	})
}

func TestAsyncOperationResponse_MissingStatusUrlAndSamplingTime(t *testing.T) {
	var empty AsyncOperationResponse
	if err := json.Unmarshal([]byte(`{}`), &empty); err != nil {
		t.Fatalf("Unmarshal({}) failed: %v", err)
	}
	if empty.HasStatusUrl() || empty.HasSamplingTime() {
		t.Errorf("expected StatusUrl and SamplingTime to be unset, got %+v", empty)
	}

	var populated AsyncOperationResponse
	if err := json.Unmarshal([]byte(`{"statusUrl":"https://api.example.com/ops/1","samplingTime":5}`), &populated); err != nil {
		t.Fatalf("Unmarshal(populated) failed: %v", err)
	}
	if populated.GetStatusUrl() != "https://api.example.com/ops/1" || populated.GetSamplingTime() != 5 {
		t.Errorf("unexpected decoded values: statusUrl=%q samplingTime=%d", populated.GetStatusUrl(), populated.GetSamplingTime())
	}
}

func TestCustomUrlWriteRequest_RetainsNameDescriptionAndEntries(t *testing.T) {
	req := NewCustomUrlWriteRequest("blocked-sites")
	req.SetDescription("Test custom URLs")
	req.SetUrls([]string{"example.com", "*.corp.example.com"})

	raw, err := json.Marshal(req)
	if err != nil {
		t.Fatalf("Marshal() error: %v", err)
	}

	var decoded CustomUrlWriteRequest
	if err := json.Unmarshal(raw, &decoded); err != nil {
		t.Fatalf("Unmarshal() error: %v", err)
	}
	if decoded.Name != "blocked-sites" {
		t.Errorf("Name = %q, want %q", decoded.Name, "blocked-sites")
	}
	if decoded.GetDescription() != "Test custom URLs" {
		t.Errorf("Description = %q, want %q", decoded.GetDescription(), "Test custom URLs")
	}
	if decoded.GetEntryType() != "url" {
		t.Errorf("EntryType = %q, want %q", decoded.GetEntryType(), "url")
	}
	if len(decoded.Urls) != 2 || decoded.Urls[0] != "example.com" {
		t.Errorf("Urls = %v, want [example.com *.corp.example.com]", decoded.Urls)
	}

	var missingName CustomUrlWriteRequest
	if err := json.Unmarshal([]byte(`{"entryType":"url","urls":["example.com"]}`), &missingName); err == nil {
		t.Fatal("expected error when required `name` field is missing, got nil")
	}
}

func TestUpdateNotificationPagesRequest_TypedFieldsRoundTrip(t *testing.T) {
	req := NewUpdateNotificationPagesRequest()
	req.SetBlockPageMessage("Access denied")
	req.SetBlockPageIncludeUrl(true)

	raw, err := json.Marshal(req)
	if err != nil {
		t.Fatalf("Marshal() error: %v", err)
	}

	var decoded UpdateNotificationPagesRequest
	if err := json.Unmarshal(raw, &decoded); err != nil {
		t.Fatalf("Unmarshal() error: %v", err)
	}
	if decoded.GetBlockPageMessage() != "Access denied" {
		t.Errorf("BlockPageMessage = %q, want %q", decoded.GetBlockPageMessage(), "Access denied")
	}
	if !decoded.GetBlockPageIncludeUrl() {
		t.Error("expected BlockPageIncludeUrl = true")
	}
	if decoded.HasLogoFile() {
		t.Error("expected LogoFile to remain unset")
	}
}
