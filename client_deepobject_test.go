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

// TestListUsersSendsSortAsBracketedQueryParam is the end-to-end form of the
// three helper tests above, driven through the REAL generated request builder
// against an httptest server. It follows the pattern
// TestGetUpdatableObjectsSendsExplicitPageAndLimitAsNumbers established for the
// previous fix in this same function.
//
// WHY THE HELPER TESTS ARE NOT ENOUGH: all three of them hand-build a
// url.Values and call parameterAddToHeaderOrQuery directly, so none of them
// observes api_team.go at all. A regeneration that changed ListUsers to pass
// r.sort by value, or dropped the "deepObject" style argument, or renamed the
// parameter, would leave every one of them green while the wire silently
// reverted to something the server cannot parse. This test is the only thing
// that pins the SDK's actual outbound query string.
func TestListUsersSendsSortAsBracketedQueryParam(t *testing.T) {
	var gotRawQuery string
	var gotQuery url.Values
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		gotRawQuery = r.URL.RawQuery
		gotQuery = r.URL.Query()
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		// UserList requires all four of these keys, so a bare {"data":[]}
		// would fail to decode and mask the query assertion behind an error.
		_, _ = w.Write([]byte(`{"data":[],"page":1,"totalPage":1,"itemsTotal":0}`))
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

	_, _, err := client.TeamAPI.ListUsers(context.Background()).
		Sort(map[string]string{"email": "asc"}).Execute()
	if err != nil {
		t.Fatalf("Execute() returned error: %v", err)
	}

	// The semantic requirement: the server must see a parameter NAMED
	// `sort[email]`. url.Values.Get does the percent-decoding, so this is the
	// assertion that matches how a server-side query parser reads the request.
	if got := gotQuery.Get("sort[email]"); got != "asc" {
		t.Errorf("sort[email] = %q, want %q; raw query was %q", got, "asc", gotRawQuery)
	}
	if gotQuery.Get("sort") != "" {
		t.Errorf("a bare `sort` key reached the wire (%q): the map was not expanded; raw query was %q",
			gotQuery.Get("sort"), gotRawQuery)
	}

	// And the exact bytes. Go's url.Values.Encode percent-encodes the brackets,
	// so the wire form is sort%5Bemail%5D=asc rather than the literal
	// sort[email]=asc the API docs print. That is RFC 3986-equivalent -- a
	// server decodes the key before parsing it, which is why the decoded
	// assertion above is the one that speaks to correctness -- but pinning the
	// raw form too means a future change to the encoding shows up here as a
	// deliberate decision rather than passing unnoticed.
	if !strings.Contains(gotRawQuery, "sort%5Bemail%5D=asc") {
		t.Errorf("raw query %q does not contain sort%%5Bemail%%5D=asc", gotRawQuery)
	}
}

// TestDeepObjectMapOfSlicesUsesTheLocalCommaJoinedForm pins the one place where
// this fix deliberately diverges from stock openapi-generator 7.24.0, so the
// divergence is a recorded fact rather than something a future reader discovers
// by surprise. The reflect.Map case recurses into the local reflect.Slice case,
// which always comma-joins; stock's Slice case indexes elements when
// style == "deepObject" and would emit sort[tags][0]=a&sort[tags][1]=b.
//
// Nothing in this SDK passes a map of slices -- ListUsers' sort is the only map
// parameter and it is map[string]string -- so this is a documentation test, not
// a requirement. If a map-of-slices parameter ever appears, THIS TEST IS THE
// ONE TO REVISIT: matching stock would then mean teaching the Slice case above
// to index under deepObject.
func TestDeepObjectMapOfSlicesUsesTheLocalCommaJoinedForm(t *testing.T) {
	sort := map[string][]string{"tags": {"a", "b"}}
	params := url.Values{}
	parameterAddToHeaderOrQuery(params, "sort", &sort, "deepObject", "")

	if got := params.Get("sort[tags]"); got != "a,b" {
		t.Errorf("sort[tags] = %q, want %q (the local comma-joined form)", got, "a,b")
	}
	if got := params.Get("sort[tags][0]"); got != "" {
		t.Errorf("sort[tags][0] = %q: the local Slice case does not index, so "+
			"finding an indexed key here means the Slice case changed and this "+
			"test plus the client.go comment above it both need updating", got)
	}
}

// TestDeepObjectMapOfPointersDereferences pins the other shape the client.go
// comment claims recursion buys for free: a map whose values are pointers is
// handled by the reflect.Ptr dereference at the top of the function, with no
// second implementation in the map case.
func TestDeepObjectMapOfPointersDereferences(t *testing.T) {
	asc := "asc"
	sort := map[string]*string{"email": &asc}
	params := url.Values{}
	parameterAddToHeaderOrQuery(params, "sort", &sort, "deepObject", "")

	if got := params.Get("sort[email]"); got != "asc" {
		t.Errorf("sort[email] = %q, want asc", got)
	}
}

// TestDeepObjectNilMapEmitsNothing pins that a nil map omits the parameter
// rather than emitting a placeholder. MapRange over a nil map yields zero
// iterations, so this falls out of the implementation -- but it is the shape a
// caller hits most easily, and "silently omitted" versus "sent as empty" is a
// difference the server can see.
func TestDeepObjectNilMapEmitsNothing(t *testing.T) {
	var sort map[string]string // nil
	params := url.Values{}
	parameterAddToHeaderOrQuery(params, "sort", &sort, "deepObject", "")

	if len(params) != 0 {
		t.Errorf("a nil map produced query parameters %q, want none", params.Encode())
	}
}
