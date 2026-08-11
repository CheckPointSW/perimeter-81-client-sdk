# \EnhancedPrivateDNSAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetEnhancedNetworkPrivateDNS**](EnhancedPrivateDNSAPI.md#GetEnhancedNetworkPrivateDNS) | **Get** /v3/networks/enhanced/{networkId}/privateDNS | Get network-level private DNS settings
[**GetEnhancedRegionPrivateDNS**](EnhancedPrivateDNSAPI.md#GetEnhancedRegionPrivateDNS) | **Get** /v3/networks/enhanced/{networkId}/regions/{regionId}/privateDNS | Get region-level private DNS settings
[**UpdateEnhancedNetworkPrivateDNS**](EnhancedPrivateDNSAPI.md#UpdateEnhancedNetworkPrivateDNS) | **Put** /v3/networks/enhanced/{networkId}/privateDNS | Update network-level private DNS settings
[**UpdateEnhancedRegionPrivateDNS**](EnhancedPrivateDNSAPI.md#UpdateEnhancedRegionPrivateDNS) | **Put** /v3/networks/enhanced/{networkId}/regions/{regionId}/privateDNS | Update region-level private DNS settings



## GetEnhancedNetworkPrivateDNS

> CustomDns GetEnhancedNetworkPrivateDNS(ctx, networkId).Execute()

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
	resp, r, err := apiClient.EnhancedPrivateDNSAPI.GetEnhancedNetworkPrivateDNS(context.Background(), networkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedPrivateDNSAPI.GetEnhancedNetworkPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEnhancedNetworkPrivateDNS`: CustomDns
	fmt.Fprintf(os.Stdout, "Response from `EnhancedPrivateDNSAPI.GetEnhancedNetworkPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEnhancedNetworkPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CustomDns**](CustomDns.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEnhancedRegionPrivateDNS

> CustomDns GetEnhancedRegionPrivateDNS(ctx, networkId, regionId).Execute()

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
	resp, r, err := apiClient.EnhancedPrivateDNSAPI.GetEnhancedRegionPrivateDNS(context.Background(), networkId, regionId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedPrivateDNSAPI.GetEnhancedRegionPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEnhancedRegionPrivateDNS`: CustomDns
	fmt.Fprintf(os.Stdout, "Response from `EnhancedPrivateDNSAPI.GetEnhancedRegionPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**regionId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEnhancedRegionPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CustomDns**](CustomDns.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateEnhancedNetworkPrivateDNS

> AsyncOperationResponse UpdateEnhancedNetworkPrivateDNS(ctx, networkId).CustomDnsUpdate(customDnsUpdate).Execute()

Update network-level private DNS settings



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
	customDnsUpdate := *openapiclient.NewCustomDnsUpdate(false, *openapiclient.NewCustomDnsUpdateAttributes([]openapiclient.CustomDnsServer{*openapiclient.NewCustomDnsServer("Address_example", false)}, []string{"SearchDomains_example"})) // CustomDnsUpdate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedPrivateDNSAPI.UpdateEnhancedNetworkPrivateDNS(context.Background(), networkId).CustomDnsUpdate(customDnsUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedPrivateDNSAPI.UpdateEnhancedNetworkPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateEnhancedNetworkPrivateDNS`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedPrivateDNSAPI.UpdateEnhancedNetworkPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateEnhancedNetworkPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **customDnsUpdate** | [**CustomDnsUpdate**](CustomDnsUpdate.md) |  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateEnhancedRegionPrivateDNS

> AsyncOperationResponse UpdateEnhancedRegionPrivateDNS(ctx, networkId, regionId).CustomDnsUpdate(customDnsUpdate).Execute()

Update region-level private DNS settings



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
	customDnsUpdate := *openapiclient.NewCustomDnsUpdate(false, *openapiclient.NewCustomDnsUpdateAttributes([]openapiclient.CustomDnsServer{*openapiclient.NewCustomDnsServer("Address_example", false)}, []string{"SearchDomains_example"})) // CustomDnsUpdate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedPrivateDNSAPI.UpdateEnhancedRegionPrivateDNS(context.Background(), networkId, regionId).CustomDnsUpdate(customDnsUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedPrivateDNSAPI.UpdateEnhancedRegionPrivateDNS``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateEnhancedRegionPrivateDNS`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedPrivateDNSAPI.UpdateEnhancedRegionPrivateDNS`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**regionId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateEnhancedRegionPrivateDNSRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **customDnsUpdate** | [**CustomDnsUpdate**](CustomDnsUpdate.md) |  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

