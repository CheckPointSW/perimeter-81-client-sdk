# \FirewallPolicyAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetGranularFirewallPolicy**](FirewallPolicyAPI.md#GetGranularFirewallPolicy) | **Get** /v3/networks/{networkId}/firewall-policy | Get firewall policy by network ID
[**UpdateGranularFirewallPolicy**](FirewallPolicyAPI.md#UpdateGranularFirewallPolicy) | **Put** /v3/networks/{networkId}/firewall-policy | Update firewall policy by network ID



## GetGranularFirewallPolicy

> GranularFirewallPolicy GetGranularFirewallPolicy(ctx, networkId).Execute()

Get firewall policy by network ID



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
	resp, r, err := apiClient.FirewallPolicyAPI.GetGranularFirewallPolicy(context.Background(), networkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FirewallPolicyAPI.GetGranularFirewallPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetGranularFirewallPolicy`: GranularFirewallPolicy
	fmt.Fprintf(os.Stdout, "Response from `FirewallPolicyAPI.GetGranularFirewallPolicy`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetGranularFirewallPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GranularFirewallPolicy**](GranularFirewallPolicy.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateGranularFirewallPolicy

> AsyncOperationResponse UpdateGranularFirewallPolicy(ctx, networkId).GranularFirewallPolicy(granularFirewallPolicy).Execute()

Update firewall policy by network ID



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
	granularFirewallPolicy := *openapiclient.NewGranularFirewallPolicy(false, false, "ZwAeo5wqiF", false, []openapiclient.GranularFirewallPolicyRule{*openapiclient.NewGranularFirewallPolicyRule("Name_example", false, false, openapiclient.SourcesAndDestinations{Addresses: openapiclient.NewAddresses([]string{"Addresses_example"})}, openapiclient.SourcesAndDestinations{Addresses: openapiclient.NewAddresses([]string{"Addresses_example"})}, false)}) // GranularFirewallPolicy | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FirewallPolicyAPI.UpdateGranularFirewallPolicy(context.Background(), networkId).GranularFirewallPolicy(granularFirewallPolicy).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FirewallPolicyAPI.UpdateGranularFirewallPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateGranularFirewallPolicy`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `FirewallPolicyAPI.UpdateGranularFirewallPolicy`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateGranularFirewallPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **granularFirewallPolicy** | [**GranularFirewallPolicy**](GranularFirewallPolicy.md) |  | 

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

