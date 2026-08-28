# \SettingsAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSupportOptions**](SettingsAPI.md#GetSupportOptions) | **Get** /v3/account/customize/support-options | Get end users support information settings
[**UpdateSupportOptions**](SettingsAPI.md#UpdateSupportOptions) | **Put** /v3/account/customize/support-options | Update end users support information settings



## GetSupportOptions

> SupportOptionsResponse GetSupportOptions(ctx).XAuthLambdaAuthorization(xAuthLambdaAuthorization).Execute()

Get end users support information settings



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
	xAuthLambdaAuthorization := "xAuthLambdaAuthorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SettingsAPI.GetSupportOptions(context.Background()).XAuthLambdaAuthorization(xAuthLambdaAuthorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SettingsAPI.GetSupportOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSupportOptions`: SupportOptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `SettingsAPI.GetSupportOptions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetSupportOptionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAuthLambdaAuthorization** | **string** |  | 

### Return type

[**SupportOptionsResponse**](SupportOptionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSupportOptions

> SupportOptionsResponse UpdateSupportOptions(ctx).SupportOptionsRequest(supportOptionsRequest).XAuthLambdaAuthorization(xAuthLambdaAuthorization).Execute()

Update end users support information settings



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
	supportOptionsRequest := *openapiclient.NewSupportOptionsRequest("PhoneSupportType_example", false, "LiveChatType_example") // SupportOptionsRequest | 
	xAuthLambdaAuthorization := "xAuthLambdaAuthorization_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SettingsAPI.UpdateSupportOptions(context.Background()).SupportOptionsRequest(supportOptionsRequest).XAuthLambdaAuthorization(xAuthLambdaAuthorization).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SettingsAPI.UpdateSupportOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSupportOptions`: SupportOptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `SettingsAPI.UpdateSupportOptions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSupportOptionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportOptionsRequest** | [**SupportOptionsRequest**](SupportOptionsRequest.md) |  | 
 **xAuthLambdaAuthorization** | **string** |  | 

### Return type

[**SupportOptionsResponse**](SupportOptionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

