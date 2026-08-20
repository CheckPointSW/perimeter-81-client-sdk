package perimeter81sdk

import (
	"net/http"
	"strings"
	"testing"
)

// TestHeaderParamPointerSerialisesAsValue is the header-parameter twin of the
// query-parameter regression test. api_settings.go passes the *string
// x-auth-lambda-authorization through parameterAddToHeaderOrQuery at two call
// sites, so before the fix an explicitly-set value travelled as a pointer
// address in an HTTP auth header -- a credential the server cannot possibly
// accept, failing as "unauthorized" rather than as a serialisation bug.
func TestHeaderParamPointerSerialisesAsValue(t *testing.T) {
	token := "Bearer abc123"
	headers := map[string]string{}
	parameterAddToHeaderOrQuery(headers, "x-auth-lambda-authorization", &token, "simple", "")

	got := headers["x-auth-lambda-authorization"]
	if got != token {
		t.Errorf("header = %q, want %q", got, token)
	}
	if strings.HasPrefix(got, "0x") {
		t.Errorf("header carries a pointer address (%q), not the value", got)
	}
	// A non-pointer must keep working too.
	parameterAddToHeaderOrQuery(headers, "plain", "literal", "simple", "")
	if headers["plain"] != "literal" {
		t.Errorf("non-pointer header = %q, want %q", headers["plain"], "literal")
	}
	var _ http.Header // header params are copied into an http.Header downstream
}
