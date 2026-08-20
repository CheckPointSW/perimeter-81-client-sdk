package perimeter81sdk

import (
	"context"
	"net/http"
	"net/http/httptest"
	"net/url"
	"strings"
	"testing"
	"time"
)

// TestDecodeTextPlainIntoString covers the defect found by the live smoke
// test: GET /v3/status returns HTTP 200 with content-type text/plain and
// body "Ok". The generator types that operation's first return as a plain
// string, but the stock decode() only recognized application/xml and
// application/json, so every text/plain endpoint failed with "undefined
// response type" despite a successful response. decode() now has a
// text/plain branch (see client.go); this locks in that fix.
func TestDecodeTextPlainIntoString(t *testing.T) {
	c := &APIClient{}
	var got string
	if err := c.decode(&got, []byte("Ok"), "text/plain"); err != nil {
		t.Fatalf("decode() returned error for text/plain: %v", err)
	}
	if got != "Ok" {
		t.Errorf("decode() = %q, want %q", got, "Ok")
	}
}

// TestDecodeTextPlainWithCharsetIntoString mirrors the real header sent by
// the live API: "text/plain; charset=utf-8", not the bare "text/plain".
func TestDecodeTextPlainWithCharsetIntoString(t *testing.T) {
	c := &APIClient{}
	var got string
	if err := c.decode(&got, []byte("Ok"), "text/plain; charset=utf-8"); err != nil {
		t.Fatalf("decode() returned error for text/plain; charset=utf-8: %v", err)
	}
	if got != "Ok" {
		t.Errorf("decode() = %q, want %q", got, "Ok")
	}
}

// TestDecodeTextPlainIntoNonStringReturnsError ensures a text/plain body
// decoded into anything other than *string fails with a clear error
// instead of panicking or silently doing nothing.
func TestDecodeTextPlainIntoNonStringReturnsError(t *testing.T) {
	c := &APIClient{}
	target := struct{ Foo string }{}
	err := c.decode(&target, []byte("Ok"), "text/plain")
	if err == nil {
		t.Fatal("decode() into a non-string target should return an error, got nil")
	}
	if !strings.Contains(err.Error(), "text/plain") {
		t.Errorf("decode() error %q should mention text/plain", err.Error())
	}
}

// TestDecodeApplicationJSONIntoStruct guards against regressing the
// pre-existing json branch while adding the text/plain one.
func TestDecodeApplicationJSONIntoStruct(t *testing.T) {
	c := &APIClient{}
	var got struct {
		Foo string `json:"foo"`
	}
	if err := c.decode(&got, []byte(`{"foo":"bar"}`), "application/json"); err != nil {
		t.Fatalf("decode() returned error for application/json: %v", err)
	}
	if got.Foo != "bar" {
		t.Errorf("decode() Foo = %q, want %q", got.Foo, "bar")
	}
}

// TestDecodeUnknownContentTypeReturnsError guards the fallback error path
// for content types decode() does not understand.
func TestDecodeUnknownContentTypeReturnsError(t *testing.T) {
	c := &APIClient{}
	var got string
	err := c.decode(&got, []byte("whatever"), "application/octet-stream")
	if err == nil {
		t.Fatal("decode() with an unknown content type should return an error, got nil")
	}
	if err.Error() != "undefined response type" {
		t.Errorf("decode() error = %q, want %q", err.Error(), "undefined response type")
	}
}

// TestParameterAddToHeaderOrQueryFormatsPointerScalars locks in the fix for the
// defect that blocked the objects-catalog acceptance test:
// parameterAddToHeaderOrQuery dereferenced a pointer argument into `v` and then
// formatted the ORIGINAL `obj`, so an explicitly-set scalar query parameter
// reached the server as a pointer address (`?page=0x14000112028`) instead of its
// value (`?page=1`). The generated request methods pass a POINTER exactly when
// the caller has set the value and a plain VALUE on the schema-default branch,
// so omitting a parameter worked while setting it did not -- no caller had ever
// successfully set an explicit scalar query parameter anywhere in this SDK. See
// the comment on the fixed line in client.go.
func TestParameterAddToHeaderOrQueryFormatsPointerScalars(t *testing.T) {
	tests := []struct {
		name string
		obj  interface{}
		want string
	}{
		{"pointer int32 page", PtrInt32(1), "1"},
		{"pointer int32 limit", PtrInt32(1000), "1000"},
		{"pointer int64", PtrInt64(9007199254740993), "9007199254740993"},
		{"pointer float64", PtrFloat64(1.5), "1.5"},
		{"pointer bool", PtrBool(true), "true"},
		{"pointer string", PtrString("updatable"), "updatable"},
		// The non-pointer rows are the generated code's schema-default branch,
		// which always worked; they are here so the fix cannot regress it.
		{"plain int32", int32(1), "1"},
		{"plain string", "updatable", "updatable"},
		{"plain bool", false, "false"},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			q := url.Values{}
			parameterAddToHeaderOrQuery(q, "page", tc.obj, "form", "")
			got := q.Get("page")
			if got != tc.want {
				t.Errorf("query value = %q, want %q", got, tc.want)
			}
			if strings.Contains(got, "0x") {
				t.Errorf("query value %q is a pointer address, not a value", got)
			}
		})
	}
}

// TestParameterAddToHeaderOrQueryKeepsSliceHandling guards the collection branch
// while changing the scalar one: it already formatted the dereferenced value and
// must keep joining elements with the collection-format delimiter.
func TestParameterAddToHeaderOrQueryKeepsSliceHandling(t *testing.T) {
	q := url.Values{}
	parameterAddToHeaderOrQuery(q, "cpId", &[]string{"a", "b"}, "form", "csv")
	if got := q.Get("cpId"); got != "a,b" {
		t.Errorf("query value = %q, want %q", got, "a,b")
	}
}

// TestParameterAddToHeaderOrQueryTypedNilDoesNotPanic pins the one behavioural
// edge the fix touches. A typed nil pointer inside an interface is not == nil, so
// it passes the function's nil guard and Elem() yields the zero reflect.Value.
// Formatting that with %v is safe (fmt prints a placeholder); v.Interface() would
// panic, which is why the fix formats `v` and not `v.Interface()`. No generated
// call site can reach this -- every one guards with `if r.<param> != nil` -- so
// the assertion is only "does not panic".
func TestParameterAddToHeaderOrQueryTypedNilDoesNotPanic(t *testing.T) {
	q := url.Values{}
	var typedNil *int32
	parameterAddToHeaderOrQuery(q, "page", typedNil, "form", "")
	// No assertion on the emitted value: it is a diagnostic placeholder either
	// way. Reaching this line without a panic is the whole point.
}

// TestGetUpdatableObjectsSendsExplicitPageAndLimitAsNumbers is the end-to-end
// form of the same defect, exercised through the real generated request builder
// rather than the helper. Before the fix this produced
// `?limit=0x...&page=0x...`, which the live API rejected with 422
// "limit must be >= 1, page must be >= 1".
func TestGetUpdatableObjectsSendsExplicitPageAndLimitAsNumbers(t *testing.T) {
	var gotQuery url.Values
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		gotQuery = r.URL.Query()
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte(`{"data":[]}`))
	}))
	defer srv.Close()

	cfg := NewConfiguration("unused-api-key", srv.URL)
	// Pre-seeded so prepareRequest does not try to exchange the API key for a
	// bearer token over the network; this test must stay offline.
	cfg.BearerTokenData = &TokenData{
		TokenType:         "Bearer",
		AccessToken:       "test-token",
		AccessTokenExpire: time.Now().Add(time.Hour).Unix(),
	}
	client := NewAPIClient(cfg)

	_, _, err := client.ObjectsAPI.GetUpdatableObjects(context.Background()).
		Page(1).Limit(1000).Execute()
	if err != nil {
		t.Fatalf("Execute() returned error: %v", err)
	}

	if got := gotQuery.Get("page"); got != "1" {
		t.Errorf("page query parameter = %q, want %q", got, "1")
	}
	if got := gotQuery.Get("limit"); got != "1000" {
		t.Errorf("limit query parameter = %q, want %q", got, "1000")
	}
}
