# \EnhancedTunnelsAPI

All URIs are relative to *https://public-apigw.us.sase.checkpoint.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDynamicTunnel**](EnhancedTunnelsAPI.md#CreateDynamicTunnel) | **Post** /v3/networks/enhanced/{networkId}/tunnels/ipsec/dynamic | Create dynamic IPSec tunnel group
[**CreateStaticTunnel**](EnhancedTunnelsAPI.md#CreateStaticTunnel) | **Post** /v3/networks/enhanced/{networkId}/tunnels/ipsec/static | Create static IPSec tunnel
[**DeleteDynamicTunnel**](EnhancedTunnelsAPI.md#DeleteDynamicTunnel) | **Delete** /v3/networks/enhanced/{networkId}/tunnels/ipsec/dynamic/{dynamicTunnelId} | Delete dynamic IPSec tunnel group
[**DeleteStaticTunnel**](EnhancedTunnelsAPI.md#DeleteStaticTunnel) | **Delete** /v3/networks/enhanced/{networkId}/tunnels/ipsec/static/{tunnelId} | Delete static IPSec tunnel
[**GetDynamicTunnel**](EnhancedTunnelsAPI.md#GetDynamicTunnel) | **Get** /v3/networks/enhanced/{networkId}/tunnels/ipsec/dynamic/{dynamicTunnelId} | Get dynamic IPSec tunnel group
[**GetEnhancedRegionTunnelsPerNetwork**](EnhancedTunnelsAPI.md#GetEnhancedRegionTunnelsPerNetwork) | **Get** /v3/networks/enhanced/{networkId}/tunnels | Get tunnels for a network
[**GetEnhancedRegionTunnelsPerRegion**](EnhancedTunnelsAPI.md#GetEnhancedRegionTunnelsPerRegion) | **Get** /v3/networks/enhanced/{networkId}/regions/{regionId}/tunnels | Get tunnels for a region
[**GetStaticTunnel**](EnhancedTunnelsAPI.md#GetStaticTunnel) | **Get** /v3/networks/enhanced/{networkId}/tunnels/ipsec/static/{tunnelId} | Get static IPSec tunnel
[**UpdateDynamicTunnel**](EnhancedTunnelsAPI.md#UpdateDynamicTunnel) | **Put** /v3/networks/enhanced/{networkId}/tunnels/ipsec/dynamic/{dynamicTunnelId} | Update dynamic IPSec tunnel group
[**UpdateStaticTunnel**](EnhancedTunnelsAPI.md#UpdateStaticTunnel) | **Put** /v3/networks/enhanced/{networkId}/tunnels/ipsec/static/{tunnelId} | Update static IPSec tunnel



## CreateDynamicTunnel

> AsyncOperationResponse CreateDynamicTunnel(ctx, networkId).DynamicTunnelCreate(dynamicTunnelCreate).Execute()

Create dynamic IPSec tunnel group



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
	dynamicTunnelCreate := *openapiclient.NewDynamicTunnelCreate("londonlink", []openapiclient.DynamicTunnelDetails{*openapiclient.NewDynamicTunnelDetails("psk", "sXUeWwM8DM", "169.254.10.1", "169.254.10.2", "203.0.113.10", int32(65001), "remotegw01")}, *openapiclient.NewEnhancedIPSecSharedSettingsCreate([]string{"10.255.0.0/16"}, []string{"192.168.10.0/24"}, *openapiclient.NewNetworkFeaturesCreate(*openapiclient.NewNetworkFeaturesCloudSecurity(false), *openapiclient.NewNetworkFeaturesCloudSecurity(false), *openapiclient.NewNetworkFeaturesDNSServices(*openapiclient.NewNetworkFeaturesDNSServicesRedirectToResolver(false))), int32(64512)), *openapiclient.NewIPSecAdvancedSettingsV23("IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfigV23([]string{"Auth_example"}, []string{"Encryption_example"}, []string{"KeyExchangeMethod_example"}), *openapiclient.NewIPSecPhaseConfigV23([]string{"Auth_example"}, []string{"Encryption_example"}, []string{"KeyExchangeMethod_example"}), "KeyExchange_example")) // DynamicTunnelCreate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.CreateDynamicTunnel(context.Background(), networkId).DynamicTunnelCreate(dynamicTunnelCreate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.CreateDynamicTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDynamicTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.CreateDynamicTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateDynamicTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **dynamicTunnelCreate** | [**DynamicTunnelCreate**](DynamicTunnelCreate.md) |  | 

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


## CreateStaticTunnel

> AsyncOperationResponse CreateStaticTunnel(ctx, networkId).StaticTunnelCreate(staticTunnelCreate).Execute()

Create static IPSec tunnel



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
	staticTunnelCreate := *openapiclient.NewStaticTunnelCreate("psk", "sXUeWwM8DM", "londonlink01", []string{"10.255.0.0/16"}, []string{"192.168.10.0/24"}, "ikev2", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfigV23([]string{"Auth_example"}, []string{"Encryption_example"}, []string{"KeyExchangeMethod_example"}), *openapiclient.NewIPSecPhaseConfigV23([]string{"Auth_example"}, []string{"Encryption_example"}, []string{"KeyExchangeMethod_example"}), "203.0.113.10", *openapiclient.NewNetworkFeaturesCreate(*openapiclient.NewNetworkFeaturesCloudSecurity(false), *openapiclient.NewNetworkFeaturesCloudSecurity(false), *openapiclient.NewNetworkFeaturesDNSServices(*openapiclient.NewNetworkFeaturesDNSServicesRedirectToResolver(false)))) // StaticTunnelCreate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.CreateStaticTunnel(context.Background(), networkId).StaticTunnelCreate(staticTunnelCreate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.CreateStaticTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateStaticTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.CreateStaticTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateStaticTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **staticTunnelCreate** | [**StaticTunnelCreate**](StaticTunnelCreate.md) |  | 

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


## DeleteDynamicTunnel

> AsyncOperationResponse DeleteDynamicTunnel(ctx, networkId, dynamicTunnelId).Execute()

Delete dynamic IPSec tunnel group



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
	dynamicTunnelId := "dWkVMVLteY" // string | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the `haTunnelID` field of any tunnel in the group. 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.DeleteDynamicTunnel(context.Background(), networkId, dynamicTunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.DeleteDynamicTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteDynamicTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.DeleteDynamicTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**dynamicTunnelId** | **string** | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the &#x60;haTunnelID&#x60; field of any tunnel in the group.  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDynamicTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteStaticTunnel

> AsyncOperationResponse DeleteStaticTunnel(ctx, networkId, tunnelId).Execute()

Delete static IPSec tunnel



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
	tunnelId := "tunnelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.DeleteStaticTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.DeleteStaticTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteStaticTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.DeleteStaticTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteStaticTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDynamicTunnel

> []EnhancedTunnel GetDynamicTunnel(ctx, networkId, dynamicTunnelId).Execute()

Get dynamic IPSec tunnel group



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
	dynamicTunnelId := "dWkVMVLteY" // string | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the `haTunnelID` field of any tunnel in the group. 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.GetDynamicTunnel(context.Background(), networkId, dynamicTunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.GetDynamicTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDynamicTunnel`: []EnhancedTunnel
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.GetDynamicTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**dynamicTunnelId** | **string** | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the &#x60;haTunnelID&#x60; field of any tunnel in the group.  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDynamicTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**[]EnhancedTunnel**](EnhancedTunnel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEnhancedRegionTunnelsPerNetwork

> GetEnhancedRegionTunnelsPerNetwork200Response GetEnhancedRegionTunnelsPerNetwork(ctx, networkId).Page(page).Limit(limit).Execute()

Get tunnels for a network



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
	page := int32(56) // int32 | Specifies the current page of the paginated result set (optional)
	limit := int32(56) // int32 | Defines the number of results per page (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerNetwork(context.Background(), networkId).Page(page).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerNetwork``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEnhancedRegionTunnelsPerNetwork`: GetEnhancedRegionTunnelsPerNetwork200Response
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerNetwork`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEnhancedRegionTunnelsPerNetworkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **page** | **int32** | Specifies the current page of the paginated result set | 
 **limit** | **int32** | Defines the number of results per page | 

### Return type

[**GetEnhancedRegionTunnelsPerNetwork200Response**](GetEnhancedRegionTunnelsPerNetwork200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEnhancedRegionTunnelsPerRegion

> GetEnhancedRegionTunnelsPerNetwork200Response GetEnhancedRegionTunnelsPerRegion(ctx, networkId, regionId).Page(page).Limit(limit).Execute()

Get tunnels for a region



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
	page := int32(56) // int32 | Specifies the current page of the paginated result set (optional)
	limit := int32(56) // int32 | Defines the number of results per page (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerRegion(context.Background(), networkId, regionId).Page(page).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerRegion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEnhancedRegionTunnelsPerRegion`: GetEnhancedRegionTunnelsPerNetwork200Response
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.GetEnhancedRegionTunnelsPerRegion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**regionId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEnhancedRegionTunnelsPerRegionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **page** | **int32** | Specifies the current page of the paginated result set | 
 **limit** | **int32** | Defines the number of results per page | 

### Return type

[**GetEnhancedRegionTunnelsPerNetwork200Response**](GetEnhancedRegionTunnelsPerNetwork200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetStaticTunnel

> EnhancedTunnel GetStaticTunnel(ctx, networkId, tunnelId).Execute()

Get static IPSec tunnel



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
	tunnelId := "tunnelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.GetStaticTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.GetStaticTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetStaticTunnel`: EnhancedTunnel
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.GetStaticTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetStaticTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**EnhancedTunnel**](EnhancedTunnel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateDynamicTunnel

> AsyncOperationResponse UpdateDynamicTunnel(ctx, networkId, dynamicTunnelId).DynamicTunnelUpdate(dynamicTunnelUpdate).Execute()

Update dynamic IPSec tunnel group



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
	dynamicTunnelId := "dWkVMVLteY" // string | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the `haTunnelID` field of any tunnel in the group. 
	dynamicTunnelUpdate := *openapiclient.NewDynamicTunnelUpdate("londonlink") // DynamicTunnelUpdate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.UpdateDynamicTunnel(context.Background(), networkId, dynamicTunnelId).DynamicTunnelUpdate(dynamicTunnelUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.UpdateDynamicTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateDynamicTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.UpdateDynamicTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**dynamicTunnelId** | **string** | ID of a dynamic tunnel group, which is a set of member tunnels configured and managed together. Operations on this ID apply to every member of the group. Take the value from the &#x60;haTunnelID&#x60; field of any tunnel in the group.  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDynamicTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **dynamicTunnelUpdate** | [**DynamicTunnelUpdate**](DynamicTunnelUpdate.md) |  | 

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


## UpdateStaticTunnel

> AsyncOperationResponse UpdateStaticTunnel(ctx, networkId, tunnelId).StaticTunnelUpdate(staticTunnelUpdate).Execute()

Update static IPSec tunnel



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
	tunnelId := "tunnelId_example" // string | 
	staticTunnelUpdate := *openapiclient.NewStaticTunnelUpdate() // StaticTunnelUpdate | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EnhancedTunnelsAPI.UpdateStaticTunnel(context.Background(), networkId, tunnelId).StaticTunnelUpdate(staticTunnelUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EnhancedTunnelsAPI.UpdateStaticTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateStaticTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `EnhancedTunnelsAPI.UpdateStaticTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateStaticTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **staticTunnelUpdate** | [**StaticTunnelUpdate**](StaticTunnelUpdate.md) |  | 

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

