# \StandardTunnelsAPI

All URIs are relative to *https://public-apigw.us.sase.checkpoint.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StandardCreateIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardCreateIPSecRedundantTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant | Create a new IPSec redundant tunnel
[**StandardCreateIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardCreateIPSecSingleTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/ipsec/single | Create a new IPSec Single tunnel
[**StandardCreateOpenVPNTunnel**](StandardTunnelsAPI.md#StandardCreateOpenVPNTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/openvpn | Create a new OpenVPN tunnel
[**StandardCreateWireGuardTunnel**](StandardTunnelsAPI.md#StandardCreateWireGuardTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/wireguard | Create a new WireGuard tunnel
[**StandardDeleteIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardDeleteIPSecRedundantTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Delete IPSec redundant tunnel
[**StandardDeleteIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardDeleteIPSecSingleTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Delete IPSec single tunnel
[**StandardDeleteOpenVPNTunnel**](StandardTunnelsAPI.md#StandardDeleteOpenVPNTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Delete OpenVPN tunnel
[**StandardDeleteWireGuardTunnel**](StandardTunnelsAPI.md#StandardDeleteWireGuardTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Delete WireGuard tunnel
[**StandardGetIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardGetIPSecRedundantTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Get IPSec redundant tunnel by ID
[**StandardGetIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardGetIPSecSingleTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Get IPSec single tunnel by ID
[**StandardGetOpenVPNTunnel**](StandardTunnelsAPI.md#StandardGetOpenVPNTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Get one OpenVPN tunnel
[**StandardGetWireGuardConfigUrl**](StandardTunnelsAPI.md#StandardGetWireGuardConfigUrl) | **Get** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId}/config-token | Get WireGuard config download URL
[**StandardGetWireGuardTunnel**](StandardTunnelsAPI.md#StandardGetWireGuardTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Get a WireGuard tunnel
[**StandardUpdateIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardUpdateIPSecRedundantTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Update a new IPSec redundant tunnel
[**StandardUpdateIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardUpdateIPSecSingleTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Update IPSec single tunnel
[**StandardUpdateOpenVPNTunnel**](StandardTunnelsAPI.md#StandardUpdateOpenVPNTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Update OpenVPN tunnel
[**StandardUpdateWireGuardTunnel**](StandardTunnelsAPI.md#StandardUpdateWireGuardTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Update a WireGuard tunnel



## StandardCreateIPSecRedundantTunnel

> AsyncOperationResponse StandardCreateIPSecRedundantTunnel(ctx, networkId).CreateIPSecRedundantPayload(createIPSecRedundantPayload).Execute()

Create a new IPSec redundant tunnel



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
	createIPSecRedundantPayload := *openapiclient.NewCreateIPSecRedundantPayload("londonlink01", "RegionID_example", *openapiclient.NewIPSecRedundantTunnelPayload("Str0ng.Shared_Key01", "P81GWInternalIP_example", "RemoteGWInternalIP_example", "RemotePublicIP_example", int32(65001), "remotegw01", "GatewayID_example"), *openapiclient.NewIPSecRedundantTunnelPayload("Str0ng.Shared_Key01", "P81GWInternalIP_example", "RemoteGWInternalIP_example", "RemotePublicIP_example", int32(65001), "remotegw01", "GatewayID_example"), *openapiclient.NewIPSecSharedSettingsCreate([]string{"10.255.0.0/16"}, []string{"192.168.10.0/24"}), *openapiclient.NewIPSecAdvancedSettings("KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}))) // CreateIPSecRedundantPayload | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardCreateIPSecRedundantTunnel(context.Background(), networkId).CreateIPSecRedundantPayload(createIPSecRedundantPayload).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardCreateIPSecRedundantTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardCreateIPSecRedundantTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardCreateIPSecRedundantTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardCreateIPSecRedundantTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createIPSecRedundantPayload** | [**CreateIPSecRedundantPayload**](CreateIPSecRedundantPayload.md) |  | 

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


## StandardCreateIPSecSingleTunnel

> AsyncOperationResponse StandardCreateIPSecSingleTunnel(ctx, networkId).CreateIPSecSinglePayload(createIPSecSinglePayload).Execute()

Create a new IPSec Single tunnel



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
	createIPSecSinglePayload := *openapiclient.NewCreateIPSecSinglePayload("RegionID_example", "GatewayID_example", "londonlink01", []string{"10.255.0.0/16"}, []string{"192.168.10.0/24"}, "KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), "Str0ng.Shared_Key01", "RemotePublicIP_example") // CreateIPSecSinglePayload | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardCreateIPSecSingleTunnel(context.Background(), networkId).CreateIPSecSinglePayload(createIPSecSinglePayload).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardCreateIPSecSingleTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardCreateIPSecSingleTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardCreateIPSecSingleTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardCreateIPSecSingleTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createIPSecSinglePayload** | [**CreateIPSecSinglePayload**](CreateIPSecSinglePayload.md) |  | 

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


## StandardCreateOpenVPNTunnel

> OpenVPNAsyncOperationResponse StandardCreateOpenVPNTunnel(ctx, networkId).BaseTunnelValues(baseTunnelValues).Execute()

Create a new OpenVPN tunnel



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
	baseTunnelValues := *openapiclient.NewBaseTunnelValues("RegionID_example", "GatewayID_example", "londonlink01") // BaseTunnelValues | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardCreateOpenVPNTunnel(context.Background(), networkId).BaseTunnelValues(baseTunnelValues).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardCreateOpenVPNTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardCreateOpenVPNTunnel`: OpenVPNAsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardCreateOpenVPNTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardCreateOpenVPNTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **baseTunnelValues** | [**BaseTunnelValues**](BaseTunnelValues.md) |  | 

### Return type

[**OpenVPNAsyncOperationResponse**](OpenVPNAsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardCreateWireGuardTunnel

> AsyncOperationResponse StandardCreateWireGuardTunnel(ctx, networkId).CreateWireGuardTunnelPayload(createWireGuardTunnelPayload).Execute()

Create a new WireGuard tunnel



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
	createWireGuardTunnelPayload := *openapiclient.NewCreateWireGuardTunnelPayload("RemoteEndpoint_example", []string{"RemoteSubnets_example"}, "RegionID_example", "GatewayID_example", "londonlink01") // CreateWireGuardTunnelPayload | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardCreateWireGuardTunnel(context.Background(), networkId).CreateWireGuardTunnelPayload(createWireGuardTunnelPayload).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardCreateWireGuardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardCreateWireGuardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardCreateWireGuardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardCreateWireGuardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createWireGuardTunnelPayload** | [**CreateWireGuardTunnelPayload**](CreateWireGuardTunnelPayload.md) |  | 

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


## StandardDeleteIPSecRedundantTunnel

> AsyncOperationResponse StandardDeleteIPSecRedundantTunnel(ctx, networkId, haTunnelId).Execute()

Delete IPSec redundant tunnel



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
	haTunnelId := "haTunnelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardDeleteIPSecRedundantTunnel(context.Background(), networkId, haTunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardDeleteIPSecRedundantTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardDeleteIPSecRedundantTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardDeleteIPSecRedundantTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**haTunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardDeleteIPSecRedundantTunnelRequest struct via the builder pattern


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


## StandardDeleteIPSecSingleTunnel

> AsyncOperationResponse StandardDeleteIPSecSingleTunnel(ctx, networkId, tunnelId).Execute()

Delete IPSec single tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardDeleteIPSecSingleTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardDeleteIPSecSingleTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardDeleteIPSecSingleTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardDeleteIPSecSingleTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardDeleteIPSecSingleTunnelRequest struct via the builder pattern


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


## StandardDeleteOpenVPNTunnel

> AsyncOperationResponse StandardDeleteOpenVPNTunnel(ctx, networkId, tunnelId).Execute()

Delete OpenVPN tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardDeleteOpenVPNTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardDeleteOpenVPNTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardDeleteOpenVPNTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardDeleteOpenVPNTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardDeleteOpenVPNTunnelRequest struct via the builder pattern


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


## StandardDeleteWireGuardTunnel

> AsyncOperationResponse StandardDeleteWireGuardTunnel(ctx, networkId, tunnelId).Execute()

Delete WireGuard tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardDeleteWireGuardTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardDeleteWireGuardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardDeleteWireGuardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardDeleteWireGuardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardDeleteWireGuardTunnelRequest struct via the builder pattern


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


## StandardGetIPSecRedundantTunnel

> IPSecRedundantTunnels StandardGetIPSecRedundantTunnel(ctx, networkId, haTunnelId).Execute()

Get IPSec redundant tunnel by ID



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
	haTunnelId := "haTunnelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetIPSecRedundantTunnel(context.Background(), networkId, haTunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetIPSecRedundantTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetIPSecRedundantTunnel`: IPSecRedundantTunnels
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetIPSecRedundantTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**haTunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetIPSecRedundantTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**IPSecRedundantTunnels**](IPSecRedundantTunnels.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardGetIPSecSingleTunnel

> IPSecSingleTunnel StandardGetIPSecSingleTunnel(ctx, networkId, tunnelId).Execute()

Get IPSec single tunnel by ID



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetIPSecSingleTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetIPSecSingleTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetIPSecSingleTunnel`: IPSecSingleTunnel
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetIPSecSingleTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetIPSecSingleTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**IPSecSingleTunnel**](IPSecSingleTunnel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardGetOpenVPNTunnel

> OpenVPNTunnel StandardGetOpenVPNTunnel(ctx, networkId, tunnelId).Execute()

Get one OpenVPN tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetOpenVPNTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetOpenVPNTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetOpenVPNTunnel`: OpenVPNTunnel
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetOpenVPNTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetOpenVPNTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**OpenVPNTunnel**](OpenVPNTunnel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardGetWireGuardConfigUrl

> WireGuardConfigUrl StandardGetWireGuardConfigUrl(ctx, networkId, tunnelId).Execute()

Get WireGuard config download URL



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetWireGuardConfigUrl(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetWireGuardConfigUrl``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetWireGuardConfigUrl`: WireGuardConfigUrl
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetWireGuardConfigUrl`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetWireGuardConfigUrlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WireGuardConfigUrl**](WireGuardConfigUrl.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardGetWireGuardTunnel

> WireGuardTunnel StandardGetWireGuardTunnel(ctx, networkId, tunnelId).Execute()

Get a WireGuard tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetWireGuardTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetWireGuardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetWireGuardTunnel`: WireGuardTunnel
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetWireGuardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetWireGuardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WireGuardTunnel**](WireGuardTunnel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardUpdateIPSecRedundantTunnel

> AsyncOperationResponse StandardUpdateIPSecRedundantTunnel(ctx, networkId, haTunnelId).UpdateIPSecRedundantPayload(updateIPSecRedundantPayload).Execute()

Update a new IPSec redundant tunnel



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
	haTunnelId := "haTunnelId_example" // string | 
	updateIPSecRedundantPayload := *openapiclient.NewUpdateIPSecRedundantPayload() // UpdateIPSecRedundantPayload | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardUpdateIPSecRedundantTunnel(context.Background(), networkId, haTunnelId).UpdateIPSecRedundantPayload(updateIPSecRedundantPayload).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardUpdateIPSecRedundantTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardUpdateIPSecRedundantTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardUpdateIPSecRedundantTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**haTunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardUpdateIPSecRedundantTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **updateIPSecRedundantPayload** | [**UpdateIPSecRedundantPayload**](UpdateIPSecRedundantPayload.md) |  | 

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


## StandardUpdateIPSecSingleTunnel

> AsyncOperationResponse StandardUpdateIPSecSingleTunnel(ctx, networkId, tunnelId).IPSecSingleDetails(iPSecSingleDetails).Execute()

Update IPSec single tunnel



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
	iPSecSingleDetails := *openapiclient.NewIPSecSingleDetails("KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), []string{"10.255.0.0/16"}, []string{"192.168.10.0/24"}) // IPSecSingleDetails | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardUpdateIPSecSingleTunnel(context.Background(), networkId, tunnelId).IPSecSingleDetails(iPSecSingleDetails).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardUpdateIPSecSingleTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardUpdateIPSecSingleTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardUpdateIPSecSingleTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardUpdateIPSecSingleTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **iPSecSingleDetails** | [**IPSecSingleDetails**](IPSecSingleDetails.md) |  | 

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


## StandardUpdateOpenVPNTunnel

> OpenVPNAsyncOperationResponse StandardUpdateOpenVPNTunnel(ctx, networkId, tunnelId).Execute()

Update OpenVPN tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardUpdateOpenVPNTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardUpdateOpenVPNTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardUpdateOpenVPNTunnel`: OpenVPNAsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardUpdateOpenVPNTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardUpdateOpenVPNTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**OpenVPNAsyncOperationResponse**](OpenVPNAsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardUpdateWireGuardTunnel

> AsyncOperationResponse StandardUpdateWireGuardTunnel(ctx, networkId, tunnelId).WireGuardDetails(wireGuardDetails).Execute()

Update a WireGuard tunnel



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
	wireGuardDetails := *openapiclient.NewWireGuardDetails("RemoteEndpoint_example", []string{"RemoteSubnets_example"}) // WireGuardDetails | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardUpdateWireGuardTunnel(context.Background(), networkId, tunnelId).WireGuardDetails(wireGuardDetails).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardUpdateWireGuardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardUpdateWireGuardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardUpdateWireGuardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardUpdateWireGuardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **wireGuardDetails** | [**WireGuardDetails**](WireGuardDetails.md) |  | 

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

