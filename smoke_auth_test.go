package perimeter81sdk

import (
	"context"
	"os"
	"testing"
)

// TestSmokeAuthorizeAgainstLiveAPI is skipped unless CHECKPOINT_SASE_API_KEY is
// set, so it never runs in the offline tier. It proves /v3/auth/authorize
// exists and accepts our API key before any resource work depends on it.
//
// The base URL's path prefix is environment-dependent: the production
// region constants (BaseURLUS and friends, see configuration.go) end in
// /api/rest, and that suffix belongs on the wire path for those hosts. But
// it is not universal — the solo.safersoftware.net gateway used for live
// verification serves /v3/... at the root and returns 403 for
// /api/rest/v3/.... Do not assume /api/rest is always required; it depends
// on which host BASE_URL points at.
//
// Verified working invocation against that gateway (key supplied via the
// environment only, never written to a file):
//
//	cd perimeter-81-client-sdk
//	read -rs CHECKPOINT_SASE_API_KEY && export CHECKPOINT_SASE_API_KEY
//	export BASE_URL="https://public-apigw.solo.safersoftware.net"
//	go test -run TestSmokeAuth -v ./...
//	unset CHECKPOINT_SASE_API_KEY
func TestSmokeAuthorizeAgainstLiveAPI(t *testing.T) {
	apiKey := os.Getenv("CHECKPOINT_SASE_API_KEY")
	if apiKey == "" {
		t.Skip("CHECKPOINT_SASE_API_KEY not set; skipping live auth smoke test")
	}
	baseURL := os.Getenv("BASE_URL")
	if baseURL == "" {
		baseURL = BaseURLUS
	}

	client := NewAPIClient(NewConfiguration(apiKey, baseURL))
	token, err := client.GetBearerTokenFromApiKey(apiKey, baseURL)
	if err != nil {
		t.Fatalf("token exchange against %s failed: %v", authorizeURL(baseURL), err)
	}
	if token == nil || token.AccessToken == "" {
		t.Fatal("token exchange returned an empty access token")
	}
	// Never log the token itself.
	t.Logf("token exchange OK against %s (token length %d)", authorizeURL(baseURL), len(token.AccessToken))

	if _, _, err := client.NetworksAPI.GetStatus(context.Background()).Execute(); err != nil {
		t.Fatalf("authenticated GET /v3/status failed, so the token was not accepted: %v", err)
	}
}
