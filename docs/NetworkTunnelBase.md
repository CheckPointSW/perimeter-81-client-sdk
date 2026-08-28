# NetworkTunnelBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique ID. | 
**Network** | Pointer to **string** | ID of the network. | [optional] 
**Region** | Pointer to **string** | ID of the network region. | [optional] 
**Instance** | Pointer to **string** | ID of the network instance. | [optional] 
**InterfaceName** | Pointer to **string** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 
**IsHA** | Pointer to **bool** | Indicates if it&#39;s a redundant tunnel. | [optional] 
**TenantId** | Pointer to **string** | ID of the tenant. | [optional] 
**CreatedAt** | Pointer to **time.Time** | The date when this record was created. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | The date of last update of the record. | [optional] 

## Methods

### NewNetworkTunnelBase

`func NewNetworkTunnelBase(id string, ) *NetworkTunnelBase`

NewNetworkTunnelBase instantiates a new NetworkTunnelBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNetworkTunnelBaseWithDefaults

`func NewNetworkTunnelBaseWithDefaults() *NetworkTunnelBase`

NewNetworkTunnelBaseWithDefaults instantiates a new NetworkTunnelBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *NetworkTunnelBase) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *NetworkTunnelBase) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *NetworkTunnelBase) SetId(v string)`

SetId sets Id field to given value.


### GetNetwork

`func (o *NetworkTunnelBase) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *NetworkTunnelBase) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *NetworkTunnelBase) SetNetwork(v string)`

SetNetwork sets Network field to given value.

### HasNetwork

`func (o *NetworkTunnelBase) HasNetwork() bool`

HasNetwork returns a boolean if a field has been set.

### GetRegion

`func (o *NetworkTunnelBase) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *NetworkTunnelBase) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *NetworkTunnelBase) SetRegion(v string)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *NetworkTunnelBase) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### GetInstance

`func (o *NetworkTunnelBase) GetInstance() string`

GetInstance returns the Instance field if non-nil, zero value otherwise.

### GetInstanceOk

`func (o *NetworkTunnelBase) GetInstanceOk() (*string, bool)`

GetInstanceOk returns a tuple with the Instance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstance

`func (o *NetworkTunnelBase) SetInstance(v string)`

SetInstance sets Instance field to given value.

### HasInstance

`func (o *NetworkTunnelBase) HasInstance() bool`

HasInstance returns a boolean if a field has been set.

### GetInterfaceName

`func (o *NetworkTunnelBase) GetInterfaceName() string`

GetInterfaceName returns the InterfaceName field if non-nil, zero value otherwise.

### GetInterfaceNameOk

`func (o *NetworkTunnelBase) GetInterfaceNameOk() (*string, bool)`

GetInterfaceNameOk returns a tuple with the InterfaceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInterfaceName

`func (o *NetworkTunnelBase) SetInterfaceName(v string)`

SetInterfaceName sets InterfaceName field to given value.

### HasInterfaceName

`func (o *NetworkTunnelBase) HasInterfaceName() bool`

HasInterfaceName returns a boolean if a field has been set.

### GetType

`func (o *NetworkTunnelBase) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *NetworkTunnelBase) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *NetworkTunnelBase) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *NetworkTunnelBase) HasType() bool`

HasType returns a boolean if a field has been set.

### GetIsHA

`func (o *NetworkTunnelBase) GetIsHA() bool`

GetIsHA returns the IsHA field if non-nil, zero value otherwise.

### GetIsHAOk

`func (o *NetworkTunnelBase) GetIsHAOk() (*bool, bool)`

GetIsHAOk returns a tuple with the IsHA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsHA

`func (o *NetworkTunnelBase) SetIsHA(v bool)`

SetIsHA sets IsHA field to given value.

### HasIsHA

`func (o *NetworkTunnelBase) HasIsHA() bool`

HasIsHA returns a boolean if a field has been set.

### GetTenantId

`func (o *NetworkTunnelBase) GetTenantId() string`

GetTenantId returns the TenantId field if non-nil, zero value otherwise.

### GetTenantIdOk

`func (o *NetworkTunnelBase) GetTenantIdOk() (*string, bool)`

GetTenantIdOk returns a tuple with the TenantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenantId

`func (o *NetworkTunnelBase) SetTenantId(v string)`

SetTenantId sets TenantId field to given value.

### HasTenantId

`func (o *NetworkTunnelBase) HasTenantId() bool`

HasTenantId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *NetworkTunnelBase) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *NetworkTunnelBase) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *NetworkTunnelBase) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *NetworkTunnelBase) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *NetworkTunnelBase) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *NetworkTunnelBase) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *NetworkTunnelBase) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *NetworkTunnelBase) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


