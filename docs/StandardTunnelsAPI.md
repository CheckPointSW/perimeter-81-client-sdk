# \StandardTunnelsAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StandardCreateIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardCreateIPSecRedundantTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant | Create a new IPSec redundant tunnel
[**StandardCreateIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardCreateIPSecSingleTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/ipsec/single | Create a new IPSec Single tunnel
[**StandardCreateOpenVPNTunnel**](StandardTunnelsAPI.md#StandardCreateOpenVPNTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/openvpn | Create a new OpenVPN tunnel
[**StandardCreateWireguardTunnel**](StandardTunnelsAPI.md#StandardCreateWireguardTunnel) | **Post** /v3/networks/standard/{networkId}/tunnels/wireguard | Create a new Wireguard tunnel
[**StandardDeleteIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardDeleteIPSecRedundantTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Delete IPSec redundant tunnel
[**StandardDeleteIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardDeleteIPSecSingleTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Delete IPSec single tunnel
[**StandardDeleteOpenVPNTunnel**](StandardTunnelsAPI.md#StandardDeleteOpenVPNTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Delete OpenVPN tunnel
[**StandardDeleteWireguardTunnel**](StandardTunnelsAPI.md#StandardDeleteWireguardTunnel) | **Delete** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Delete Wireguard tunnel
[**StandardGetIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardGetIPSecRedundantTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Get IPSec redundant tunnel by ID
[**StandardGetIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardGetIPSecSingleTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Get IPSec single tunnel by ID
[**StandardGetOpenVPNTunnel**](StandardTunnelsAPI.md#StandardGetOpenVPNTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Get one OpenVPN tunnel
[**StandardGetWireguardConfigUrl**](StandardTunnelsAPI.md#StandardGetWireguardConfigUrl) | **Get** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId}/config-token | Get Wireguard config download URL
[**StandardGetWireguardTunnel**](StandardTunnelsAPI.md#StandardGetWireguardTunnel) | **Get** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Get a Wireguard tunnel
[**StandardUpdateIPSecRedundantTunnel**](StandardTunnelsAPI.md#StandardUpdateIPSecRedundantTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/ipsec/redundant/{haTunnelId} | Update a new IPSec redundant tunnel
[**StandardUpdateIPSecSingleTunnel**](StandardTunnelsAPI.md#StandardUpdateIPSecSingleTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/ipsec/single/{tunnelId} | Update IPSec single tunnel
[**StandardUpdateOpenVPNTunnel**](StandardTunnelsAPI.md#StandardUpdateOpenVPNTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/openvpn/{tunnelId} | Update OpenVPN tunnel
[**StandardUpdateWireguardTunnel**](StandardTunnelsAPI.md#StandardUpdateWireguardTunnel) | **Put** /v3/networks/standard/{networkId}/tunnels/wireguard/{tunnelId} | Update a Wireguard tunnel



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
	createIPSecRedundantPayload := *openapiclient.NewCreateIPSecRedundantPayload("TunnelName_example", "RegionID_example", *openapiclient.NewIPSecRedundantTunnelPayload("Passphrase_example", "P81GWInternalIP_example", "RemoteGWInternalIP_example", "RemotePublicIP_example", int32(123), openapiclient.remoteID{String: new(string)}, "GatewayID_example"), *openapiclient.NewIPSecRedundantTunnelPayload("Passphrase_example", "P81GWInternalIP_example", "RemoteGWInternalIP_example", "RemotePublicIP_example", int32(123), openapiclient.remoteID{String: new(string)}, "GatewayID_example"), *openapiclient.NewIPSecSharedSettingsCreate([]string{"P81GatewaySubnets_example"}, []string{"RemoteGatewaySubnets_example"}), *openapiclient.NewIPSecAdvancedSettings("KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}))) // CreateIPSecRedundantPayload | 

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
	createIPSecSinglePayload := *openapiclient.NewCreateIPSecSinglePayload("RegionID_example", "GatewayID_example", "TunnelName_example", []string{"P81GatewaySubnets_example"}, []string{"RemoteGatewaySubnets_example"}, "KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), "Passphrase_example", "RemotePublicIP_example") // CreateIPSecSinglePayload | 

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
	baseTunnelValues := *openapiclient.NewBaseTunnelValues("RegionID_example", "GatewayID_example", "TunnelName_example") // BaseTunnelValues | 

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


## StandardCreateWireguardTunnel

> AsyncOperationResponse StandardCreateWireguardTunnel(ctx, networkId).CreateWireguardTunnelPayload(createWireguardTunnelPayload).Execute()

Create a new Wireguard tunnel



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
	createWireguardTunnelPayload := *openapiclient.NewCreateWireguardTunnelPayload("RemoteEndpoint_example", []string{"RemoteSubnets_example"}, "RegionID_example", "GatewayID_example", "TunnelName_example") // CreateWireguardTunnelPayload | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardCreateWireguardTunnel(context.Background(), networkId).CreateWireguardTunnelPayload(createWireguardTunnelPayload).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardCreateWireguardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardCreateWireguardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardCreateWireguardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardCreateWireguardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createWireguardTunnelPayload** | [**CreateWireguardTunnelPayload**](CreateWireguardTunnelPayload.md) |  | 

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


## StandardDeleteWireguardTunnel

> AsyncOperationResponse StandardDeleteWireguardTunnel(ctx, networkId, tunnelId).Execute()

Delete Wireguard tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardDeleteWireguardTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardDeleteWireguardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardDeleteWireguardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardDeleteWireguardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardDeleteWireguardTunnelRequest struct via the builder pattern


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


## StandardGetWireguardConfigUrl

> WireguardConfigUrl StandardGetWireguardConfigUrl(ctx, networkId, tunnelId).Execute()

Get Wireguard config download URL



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetWireguardConfigUrl(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetWireguardConfigUrl``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetWireguardConfigUrl`: WireguardConfigUrl
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetWireguardConfigUrl`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetWireguardConfigUrlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WireguardConfigUrl**](WireguardConfigUrl.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## StandardGetWireguardTunnel

> WireguardTunnel StandardGetWireguardTunnel(ctx, networkId, tunnelId).Execute()

Get a Wireguard tunnel



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
	resp, r, err := apiClient.StandardTunnelsAPI.StandardGetWireguardTunnel(context.Background(), networkId, tunnelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardGetWireguardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardGetWireguardTunnel`: WireguardTunnel
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardGetWireguardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardGetWireguardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**WireguardTunnel**](WireguardTunnel.md)

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
	updateIPSecRedundantPayload := *openapiclient.NewUpdateIPSecRedundantPayload(*openapiclient.NewIPSecSharedSettings([]string{"P81GatewaySubnets_example"}, []string{"RemoteGatewaySubnets_example"}), *openapiclient.NewIPSecAdvancedSettings("KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}))) // UpdateIPSecRedundantPayload | 

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
	iPSecSingleDetails := *openapiclient.NewIPSecSingleDetails("KeyExchange_example", "IkeLifeTime_example", "Lifetime_example", "DpdDelay_example", "DpdTimeout_example", *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), *openapiclient.NewIPSecPhaseConfig([]string{"Auth_example"}, []string{"Encryption_example"}, []int32{int32(123)}), []string{"P81GatewaySubnets_example"}, []string{"RemoteGatewaySubnets_example"}) // IPSecSingleDetails | 

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


## StandardUpdateWireguardTunnel

> AsyncOperationResponse StandardUpdateWireguardTunnel(ctx, networkId, tunnelId).WireGuradDetails(wireGuradDetails).Execute()

Update a Wireguard tunnel



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
	wireGuradDetails := *openapiclient.NewWireGuradDetails("RemoteEndpoint_example", []string{"RemoteSubnets_example"}) // WireGuradDetails | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.StandardTunnelsAPI.StandardUpdateWireguardTunnel(context.Background(), networkId, tunnelId).WireGuradDetails(wireGuradDetails).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `StandardTunnelsAPI.StandardUpdateWireguardTunnel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StandardUpdateWireguardTunnel`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `StandardTunnelsAPI.StandardUpdateWireguardTunnel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**networkId** | **string** |  | 
**tunnelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiStandardUpdateWireguardTunnelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **wireGuradDetails** | [**WireGuradDetails**](WireGuradDetails.md) |  | 

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

