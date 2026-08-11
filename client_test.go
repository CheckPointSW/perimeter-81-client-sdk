package perimeter81sdk

import (
	"strings"
	"testing"
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
