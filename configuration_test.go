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
		if !strings.HasSuffix(got, "/api/rest") {
			t.Errorf("%s base URL %q must end in /api/rest", name, got)
		}
		if !strings.HasPrefix(got, "https://") {
			t.Errorf("%s base URL %q must use TLS", name, got)
		}
	}
	if BaseURLCA != "https://api.ca.sase.checkpoint.com/api/rest" {
		t.Errorf("unexpected CA base URL: %q", BaseURLCA)
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
	want := "https://api.perimeter81.com/api/rest/v3/auth/authorize"
	if got != want {
		t.Errorf("authorizeURL() = %q, want %q", got, want)
	}
}
