# NetworkTunnelWireGuard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique ID. | 
**Network** | **string** | ID of the network. | 
**Region** | **string** | ID of the network region. | 
**Instance** | **string** | ID of the network instance. | 
**InterfaceName** | **string** |  | 
**Type** | **string** |  | 
**IsHA** | **bool** | Indicates if it&#39;s a redundant tunnel. | 
**TenantId** | **string** | ID of the tenant. | 
**CreatedAt** | Pointer to **time.Time** | The date when this record was created. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | The date of last update of the record. | [optional] 
**LeftAllowedIP** | **[]string** |  | 
**LeftEndpoint** | **string** |  | 
**Vault** | **string** | vault. | 
**RequestConfigToken** | **string** | requestConfigToken. | 

## Methods

### NewNetworkTunnelWireGuard

`func NewNetworkTunnelWireGuard(id string, network string, region string, instance string, interfaceName string, type_ string, isHA bool, tenantId string, leftAllowedIP []string, leftEndpoint string, vault string, requestConfigToken string, ) *NetworkTunnelWireGuard`

NewNetworkTunnelWireGuard instantiates a new NetworkTunnelWireGuard object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNetworkTunnelWireGuardWithDefaults

`func NewNetworkTunnelWireGuardWithDefaults() *NetworkTunnelWireGuard`

NewNetworkTunnelWireGuardWithDefaults instantiates a new NetworkTunnelWireGuard object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *NetworkTunnelWireGuard) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NetworkTunnelWireGuard) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NetworkTunnelWireGuard) SetId(v string)`

SetId sets Id field to given value.


### GetNetwork

`func (o *NetworkTunnelWireGuard) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *NetworkTunnelWireGuard) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *NetworkTunnelWireGuard) SetNetwork(v string)`

SetNetwork sets Network field to given value.


### GetRegion

`func (o *NetworkTunnelWireGuard) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *NetworkTunnelWireGuard) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *NetworkTunnelWireGuard) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetInstance

`func (o *NetworkTunnelWireGuard) GetInstance() string`

GetInstance returns the Instance field if non-nil, zero value otherwise.

### GetInstanceOk

`func (o *NetworkTunnelWireGuard) GetInstanceOk() (*string, bool)`

GetInstanceOk returns a tuple with the Instance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstance

`func (o *NetworkTunnelWireGuard) SetInstance(v string)`

SetInstance sets Instance field to given value.


### GetInterfaceName

`func (o *NetworkTunnelWireGuard) GetInterfaceName() string`

GetInterfaceName returns the InterfaceName field if non-nil, zero value otherwise.

### GetInterfaceNameOk

`func (o *NetworkTunnelWireGuard) GetInterfaceNameOk() (*string, bool)`

GetInterfaceNameOk returns a tuple with the InterfaceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInterfaceName

`func (o *NetworkTunnelWireGuard) SetInterfaceName(v string)`

SetInterfaceName sets InterfaceName field to given value.


### GetType

`func (o *NetworkTunnelWireGuard) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *NetworkTunnelWireGuard) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *NetworkTunnelWireGuard) SetType(v string)`

SetType sets Type field to given value.


### GetIsHA

`func (o *NetworkTunnelWireGuard) GetIsHA() bool`

GetIsHA returns the IsHA field if non-nil, zero value otherwise.

### GetIsHAOk

`func (o *NetworkTunnelWireGuard) GetIsHAOk() (*bool, bool)`

GetIsHAOk returns a tuple with the IsHA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsHA

`func (o *NetworkTunnelWireGuard) SetIsHA(v bool)`

SetIsHA sets IsHA field to given value.


### GetTenantId

`func (o *NetworkTunnelWireGuard) GetTenantId() string`

GetTenantId returns the TenantId field if non-nil, zero value otherwise.

### GetTenantIdOk

`func (o *NetworkTunnelWireGuard) GetTenantIdOk() (*string, bool)`

GetTenantIdOk returns a tuple with the TenantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenantId

`func (o *NetworkTunnelWireGuard) SetTenantId(v string)`

SetTenantId sets TenantId field to given value.


### GetCreatedAt

`func (o *NetworkTunnelWireGuard) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *NetworkTunnelWireGuard) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *NetworkTunnelWireGuard) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *NetworkTunnelWireGuard) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *NetworkTunnelWireGuard) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *NetworkTunnelWireGuard) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *NetworkTunnelWireGuard) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *NetworkTunnelWireGuard) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetLeftAllowedIP

`func (o *NetworkTunnelWireGuard) GetLeftAllowedIP() []string`

GetLeftAllowedIP returns the LeftAllowedIP field if non-nil, zero value otherwise.

### GetLeftAllowedIPOk

`func (o *NetworkTunnelWireGuard) GetLeftAllowedIPOk() (*[]string, bool)`

GetLeftAllowedIPOk returns a tuple with the LeftAllowedIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftAllowedIP

`func (o *NetworkTunnelWireGuard) SetLeftAllowedIP(v []string)`

SetLeftAllowedIP sets LeftAllowedIP field to given value.


### GetLeftEndpoint

`func (o *NetworkTunnelWireGuard) GetLeftEndpoint() string`

GetLeftEndpoint returns the LeftEndpoint field if non-nil, zero value otherwise.

### GetLeftEndpointOk

`func (o *NetworkTunnelWireGuard) GetLeftEndpointOk() (*string, bool)`

GetLeftEndpointOk returns a tuple with the LeftEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftEndpoint

`func (o *NetworkTunnelWireGuard) SetLeftEndpoint(v string)`

SetLeftEndpoint sets LeftEndpoint field to given value.


### GetVault

`func (o *NetworkTunnelWireGuard) GetVault() string`

GetVault returns the Vault field if non-nil, zero value otherwise.

### GetVaultOk

`func (o *NetworkTunnelWireGuard) GetVaultOk() (*string, bool)`

GetVaultOk returns a tuple with the Vault field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVault

`func (o *NetworkTunnelWireGuard) SetVault(v string)`

SetVault sets Vault field to given value.


### GetRequestConfigToken

`func (o *NetworkTunnelWireGuard) GetRequestConfigToken() string`

GetRequestConfigToken returns the RequestConfigToken field if non-nil, zero value otherwise.

### GetRequestConfigTokenOk

`func (o *NetworkTunnelWireGuard) GetRequestConfigTokenOk() (*string, bool)`

GetRequestConfigTokenOk returns a tuple with the RequestConfigToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestConfigToken

`func (o *NetworkTunnelWireGuard) SetRequestConfigToken(v string)`

SetRequestConfigToken sets RequestConfigToken field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


