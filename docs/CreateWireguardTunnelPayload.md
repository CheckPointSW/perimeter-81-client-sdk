# CreateWireGuardTunnelPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RemoteEndpoint** | **string** |  | 
**RemoteSubnets** | **[]string** |  | 
**RegionID** | **string** | Region ID | 
**GatewayID** | **string** | Gateway ID | 
**TunnelName** | **string** | The name of the tunnel | 

## Methods

### NewCreateWireGuardTunnelPayload

`func NewCreateWireGuardTunnelPayload(remoteEndpoint string, remoteSubnets []string, regionID string, gatewayID string, tunnelName string, ) *CreateWireGuardTunnelPayload`

NewCreateWireGuardTunnelPayload instantiates a new CreateWireGuardTunnelPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWireGuardTunnelPayloadWithDefaults

`func NewCreateWireGuardTunnelPayloadWithDefaults() *CreateWireGuardTunnelPayload`

NewCreateWireGuardTunnelPayloadWithDefaults instantiates a new CreateWireGuardTunnelPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRemoteEndpoint

`func (o *CreateWireGuardTunnelPayload) GetRemoteEndpoint() string`

GetRemoteEndpoint returns the RemoteEndpoint field if non-nil, zero value otherwise.

### GetRemoteEndpointOk

`func (o *CreateWireGuardTunnelPayload) GetRemoteEndpointOk() (*string, bool)`

GetRemoteEndpointOk returns a tuple with the RemoteEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteEndpoint

`func (o *CreateWireGuardTunnelPayload) SetRemoteEndpoint(v string)`

SetRemoteEndpoint sets RemoteEndpoint field to given value.


### GetRemoteSubnets

`func (o *CreateWireGuardTunnelPayload) GetRemoteSubnets() []string`

GetRemoteSubnets returns the RemoteSubnets field if non-nil, zero value otherwise.

### GetRemoteSubnetsOk

`func (o *CreateWireGuardTunnelPayload) GetRemoteSubnetsOk() (*[]string, bool)`

GetRemoteSubnetsOk returns a tuple with the RemoteSubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteSubnets

`func (o *CreateWireGuardTunnelPayload) SetRemoteSubnets(v []string)`

SetRemoteSubnets sets RemoteSubnets field to given value.


### GetRegionID

`func (o *CreateWireGuardTunnelPayload) GetRegionID() string`

GetRegionID returns the RegionID field if non-nil, zero value otherwise.

### GetRegionIDOk

`func (o *CreateWireGuardTunnelPayload) GetRegionIDOk() (*string, bool)`

GetRegionIDOk returns a tuple with the RegionID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionID

`func (o *CreateWireGuardTunnelPayload) SetRegionID(v string)`

SetRegionID sets RegionID field to given value.


### GetGatewayID

`func (o *CreateWireGuardTunnelPayload) GetGatewayID() string`

GetGatewayID returns the GatewayID field if non-nil, zero value otherwise.

### GetGatewayIDOk

`func (o *CreateWireGuardTunnelPayload) GetGatewayIDOk() (*string, bool)`

GetGatewayIDOk returns a tuple with the GatewayID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGatewayID

`func (o *CreateWireGuardTunnelPayload) SetGatewayID(v string)`

SetGatewayID sets GatewayID field to given value.


### GetTunnelName

`func (o *CreateWireGuardTunnelPayload) GetTunnelName() string`

GetTunnelName returns the TunnelName field if non-nil, zero value otherwise.

### GetTunnelNameOk

`func (o *CreateWireGuardTunnelPayload) GetTunnelNameOk() (*string, bool)`

GetTunnelNameOk returns a tuple with the TunnelName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTunnelName

`func (o *CreateWireGuardTunnelPayload) SetTunnelName(v string)`

SetTunnelName sets TunnelName field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


