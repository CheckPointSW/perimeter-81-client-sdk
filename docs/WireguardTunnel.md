# WireGuardTunnel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RemoteEndpoint** | **string** |  | 
**RemoteSubnets** | **[]string** |  | 
**RegionID** | **string** | Region ID | 
**GatewayID** | **string** | Gateway ID | 
**TunnelName** | **string** | The name of the tunnel | 
**CreatedAt** | **time.Time** | The date when this record was created. | 
**UpdatedAt** | Pointer to **time.Time** | The date of last update of the record. | [optional] 
**TunnelID** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] [default to "wireguard"]

## Methods

### NewWireGuardTunnel

`func NewWireGuardTunnel(remoteEndpoint string, remoteSubnets []string, regionID string, gatewayID string, tunnelName string, createdAt time.Time, ) *WireGuardTunnel`

NewWireGuardTunnel instantiates a new WireGuardTunnel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWireGuardTunnelWithDefaults

`func NewWireGuardTunnelWithDefaults() *WireGuardTunnel`

NewWireGuardTunnelWithDefaults instantiates a new WireGuardTunnel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRemoteEndpoint

`func (o *WireGuardTunnel) GetRemoteEndpoint() string`

GetRemoteEndpoint returns the RemoteEndpoint field if non-nil, zero value otherwise.

### GetRemoteEndpointOk

`func (o *WireGuardTunnel) GetRemoteEndpointOk() (*string, bool)`

GetRemoteEndpointOk returns a tuple with the RemoteEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteEndpoint

`func (o *WireGuardTunnel) SetRemoteEndpoint(v string)`

SetRemoteEndpoint sets RemoteEndpoint field to given value.


### GetRemoteSubnets

`func (o *WireGuardTunnel) GetRemoteSubnets() []string`

GetRemoteSubnets returns the RemoteSubnets field if non-nil, zero value otherwise.

### GetRemoteSubnetsOk

`func (o *WireGuardTunnel) GetRemoteSubnetsOk() (*[]string, bool)`

GetRemoteSubnetsOk returns a tuple with the RemoteSubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteSubnets

`func (o *WireGuardTunnel) SetRemoteSubnets(v []string)`

SetRemoteSubnets sets RemoteSubnets field to given value.


### GetRegionID

`func (o *WireGuardTunnel) GetRegionID() string`

GetRegionID returns the RegionID field if non-nil, zero value otherwise.

### GetRegionIDOk

`func (o *WireGuardTunnel) GetRegionIDOk() (*string, bool)`

GetRegionIDOk returns a tuple with the RegionID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionID

`func (o *WireGuardTunnel) SetRegionID(v string)`

SetRegionID sets RegionID field to given value.


### GetGatewayID

`func (o *WireGuardTunnel) GetGatewayID() string`

GetGatewayID returns the GatewayID field if non-nil, zero value otherwise.

### GetGatewayIDOk

`func (o *WireGuardTunnel) GetGatewayIDOk() (*string, bool)`

GetGatewayIDOk returns a tuple with the GatewayID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGatewayID

`func (o *WireGuardTunnel) SetGatewayID(v string)`

SetGatewayID sets GatewayID field to given value.


### GetTunnelName

`func (o *WireGuardTunnel) GetTunnelName() string`

GetTunnelName returns the TunnelName field if non-nil, zero value otherwise.

### GetTunnelNameOk

`func (o *WireGuardTunnel) GetTunnelNameOk() (*string, bool)`

GetTunnelNameOk returns a tuple with the TunnelName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTunnelName

`func (o *WireGuardTunnel) SetTunnelName(v string)`

SetTunnelName sets TunnelName field to given value.


### GetCreatedAt

`func (o *WireGuardTunnel) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WireGuardTunnel) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WireGuardTunnel) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *WireGuardTunnel) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *WireGuardTunnel) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *WireGuardTunnel) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *WireGuardTunnel) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetTunnelID

`func (o *WireGuardTunnel) GetTunnelID() string`

GetTunnelID returns the TunnelID field if non-nil, zero value otherwise.

### GetTunnelIDOk

`func (o *WireGuardTunnel) GetTunnelIDOk() (*string, bool)`

GetTunnelIDOk returns a tuple with the TunnelID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTunnelID

`func (o *WireGuardTunnel) SetTunnelID(v string)`

SetTunnelID sets TunnelID field to given value.

### HasTunnelID

`func (o *WireGuardTunnel) HasTunnelID() bool`

HasTunnelID returns a boolean if a field has been set.

### GetType

`func (o *WireGuardTunnel) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *WireGuardTunnel) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *WireGuardTunnel) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *WireGuardTunnel) HasType() bool`

HasType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


