package perimeter81sdk

import (
	"net/url"
	"testing"
)

// TestDeepObjectMapParamUsesBracketNotation is the third regression pin on
// parameterAddToHeaderOrQuery, after the query-parameter fix (9b20b40) and the
// header-parameter fix (eb4b8ce). All three have the same cause: this file is a
// hand-carried v2.3-era client.go, and it predates the generator's handling of
// the case in question.
//
// GET /v3/users declares sort as `style: deepObject, explode: true` over an
// object of enum strings, documented as "sort[email]=asc". The generated
// api_team.go passes a *map[string]string with style "deepObject". Before the
// fix, the url.Values branch here handled only reflect.Slice and a scalar
// default, and ignored `style` entirely, so a map went to the wire as Go's own
// map formatting -- `?sort=map[email:asc]` -- which the server cannot parse.
//
// sort is the ONLY deepObject parameter in the whole SDK
// (grep -c '"deepObject"' api_*.go is 1, at api_team.go:787), so this test also
// documents the full blast radius of the fix.
func TestDeepObjectMapParamUsesBracketNotation(t *testing.T) {
	sort := map[string]string{"email": "asc"}
	params := url.Values{}
	parameterAddToHeaderOrQuery(params, "sort", &sort, "deepObject", "")

	if got := params.Get("sort[email]"); got != "asc" {
		t.Errorf("sort[email] = %q, want %q; encoded query was %q",
			got, "asc", params.Encode())
	}
	if params.Get("sort") != "" {
		t.Errorf("a bare `sort` key is present (%q): the map was formatted as a "+
			"single value instead of being expanded", params.Get("sort"))
	}
}

// TestDeepObjectMapParamExpandsEveryKey pins that expansion is per-key rather
// than only handling a single-entry map.
func TestDeepObjectMapParamExpandsEveryKey(t *testing.T) {
	sort := map[string]string{"email": "asc", "firstName": "desc"}
	params := url.Values{}
	parameterAddToHeaderOrQuery(params, "sort", &sort, "deepObject", "")

	if got := params.Get("sort[email]"); got != "asc" {
		t.Errorf("sort[email] = %q, want asc", got)
	}
	if got := params.Get("sort[firstName]"); got != "desc" {
		t.Errorf("sort[firstName] = %q, want desc", got)
	}
}

// TestScalarAndSliceQueryParamsAreUnchanged is the guard on the other direction:
// the map case must not disturb the two shapes that already worked, one of which
// (the explicitly-set scalar pointer) was itself a fix.
func TestScalarAndSliceQueryParamsAreUnchanged(t *testing.T) {
	params := url.Values{}
	page := int32(1)
	parameterAddToHeaderOrQuery(params, "page", &page, "form", "")
	if got := params.Get("page"); got != "1" {
		t.Errorf("page = %q, want 1", got)
	}

	ids := []string{"a", "b"}
	parameterAddToHeaderOrQuery(params, "ids", ids, "form", "csv")
	if got := params.Get("ids"); got != "a,b" {
		t.Errorf("ids = %q, want a,b", got)
	}
}
