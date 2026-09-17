package perimeter81sdk

import (
	"strings"
	"testing"
)

func TestAllFiveRegionBaseURLs(t *testing.T) {
	for name, got := range map[string]string{
		"US": BaseURLUS, "EU": BaseURLEU, "AU": BaseURLAU,
		"IN": BaseURLIN, "CA": BaseURLCA,
	} {
		if !strings.HasPrefix(got, "https://") {
			t.Errorf("%s base URL %q must use TLS", name, got)
		}
	}
}

func TestUserAgentReportsV3(t *testing.T) {
	cfg := NewConfiguration("dummy-key", BaseURLUS)
	if !strings.Contains(cfg.UserAgent, "3.0.0") {
		t.Errorf("UserAgent %q should report 3.0.0", cfg.UserAgent)
	}
}

func TestAuthorizeURLUsesV3AndKeepsRestSegment(t *testing.T) {
	got := authorizeURL(BaseURLUS)
	want := "https://public-apigw.us.sase.checkpoint.com/v3/auth/authorize"
	if got != want {
		t.Errorf("authorizeURL() = %q, want %q", got, want)
	}
}
