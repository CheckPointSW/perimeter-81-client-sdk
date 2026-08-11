# \AuthenticationAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeToken**](AuthenticationAPI.md#AuthorizeToken) | **Post** /v3/auth/authorize | Get Access Token



## AuthorizeToken

> AuthorizeResponse AuthorizeToken(ctx).AuthorizeRequest(authorizeRequest).Execute()

Get Access Token



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {
	authorizeRequest := *openapiclient.NewAuthorizeRequest("GrantType_example", "ApiKey_example") // AuthorizeRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationAPI.AuthorizeToken(context.Background()).AuthorizeRequest(authorizeRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationAPI.AuthorizeToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AuthorizeToken`: AuthorizeResponse
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationAPI.AuthorizeToken`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAuthorizeTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorizeRequest** | [**AuthorizeRequest**](AuthorizeRequest.md) |  | 

### Return type

[**AuthorizeResponse**](AuthorizeResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

