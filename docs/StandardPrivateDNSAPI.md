# \StandardPrivateDNSAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetStandardNetworkPrivateDNS**](StandardPrivateDNSAPI.md#GetStandardNetworkPrivateDNS) | **Get** /v3/networks/standard/{networkId}/privateDNS | Get network-level private DNS settings
[**GetStandardRegionPrivateDNS**](StandardPrivateDNSAPI.md#GetStandardRegionPrivateDNS) | **Get** /v3/networks/standard/{networkId}/regions/{regionId}/privateDNS | Get region-level private DNS settings



## GetStandardNetworkPrivateDNS

> CustomDnsResponse GetStandardNetworkPrivateDNS(ctx, networkId).Execute()

Get network-level private DNS settings



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
	networkId := "networkId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardPrivateDNSAPI.GetStandardNetworkPrivateDNS(context.Background(), networkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardPrivateDNSAPI.GetStandardNetworkPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStandardNetworkPrivateDNS`: CustomDnsResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardPrivateDNSAPI.GetStandardNetworkPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetStandardNetworkPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CustomDnsResponse**](CustomDnsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStandardRegionPrivateDNS

> CustomDnsResponse GetStandardRegionPrivateDNS(ctx, networkId, regionId).Execute()

Get region-level private DNS settings



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
	networkId := "networkId_example" // string | 
	regionId := "regionId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardPrivateDNSAPI.GetStandardRegionPrivateDNS(context.Background(), networkId, regionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardPrivateDNSAPI.GetStandardRegionPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStandardRegionPrivateDNS`: CustomDnsResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardPrivateDNSAPI.GetStandardRegionPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**regionId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetStandardRegionPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CustomDnsResponse**](CustomDnsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

