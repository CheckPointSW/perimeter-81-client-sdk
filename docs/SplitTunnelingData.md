# SplitTunnelingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cidr** | Pointer to **[]string** | List of CIDR blocks for split tunneling configuration | [optional] [default to {}]
**AddressObjectIds** | Pointer to **[]string** | List of address object IDs from shared objects | [optional] [default to {}]
**UpdatableObjectIds** | Pointer to **[]string** | List of updatable object IDs (UUIDs) | [optional] [default to {}]
**Exceptions** | Pointer to [**[]SplitTunnelingException**](SplitTunnelingException.md) | Subnet exceptions within included ranges that bypass the tunnel.  **Important:** Exceptions are only supported in &#39;out_of_tunnel&#39; mode. If provided when defaultTunnelingMode is &#39;via_tunnel&#39;,  the request will be rejected with a 400 Bad Request error.  Behavior in &#39;out_of_tunnel&#39; mode: - New exceptions are validated against allowed ranges (from included destinations) - Saved exceptions are filtered according to actual allowed ranges - Results are merged and deduplicated - Empty array will be merged with existing exceptions and will not remove saved exceptions by itself - If included destinations are removed from the payload and there are saved exceptions related to those subnets,    these exceptions will also be removed from the saved data - If omitted, exceptions value remains unchanged  | [optional] 

## Methods

### NewSplitTunnelingData

`func NewSplitTunnelingData() *SplitTunnelingData`

NewSplitTunnelingData instantiates a new SplitTunnelingData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSplitTunnelingDataWithDefaults

`func NewSplitTunnelingDataWithDefaults() *SplitTunnelingData`

NewSplitTunnelingDataWithDefaults instantiates a new SplitTunnelingData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCidr

`func (o *SplitTunnelingData) GetCidr() []string`

GetCidr returns the Cidr field if non-nil, zero value otherwise.

### GetCidrOk

`func (o *SplitTunnelingData) GetCidrOk() (*[]string, bool)`

GetCidrOk returns a tuple with the Cidr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCidr

`func (o *SplitTunnelingData) SetCidr(v []string)`

SetCidr sets Cidr field to given value.

### HasCidr

`func (o *SplitTunnelingData) HasCidr() bool`

HasCidr returns a boolean if a field has been set.

### GetAddressObjectIds

`func (o *SplitTunnelingData) GetAddressObjectIds() []string`

GetAddressObjectIds returns the AddressObjectIds field if non-nil, zero value otherwise.

### GetAddressObjectIdsOk

`func (o *SplitTunnelingData) GetAddressObjectIdsOk() (*[]string, bool)`

GetAddressObjectIdsOk returns a tuple with the AddressObjectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddressObjectIds

`func (o *SplitTunnelingData) SetAddressObjectIds(v []string)`

SetAddressObjectIds sets AddressObjectIds field to given value.

### HasAddressObjectIds

`func (o *SplitTunnelingData) HasAddressObjectIds() bool`

HasAddressObjectIds returns a boolean if a field has been set.

### GetUpdatableObjectIds

`func (o *SplitTunnelingData) GetUpdatableObjectIds() []string`

GetUpdatableObjectIds returns the UpdatableObjectIds field if non-nil, zero value otherwise.

### GetUpdatableObjectIdsOk

`func (o *SplitTunnelingData) GetUpdatableObjectIdsOk() (*[]string, bool)`

GetUpdatableObjectIdsOk returns a tuple with the UpdatableObjectIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatableObjectIds

`func (o *SplitTunnelingData) SetUpdatableObjectIds(v []string)`

SetUpdatableObjectIds sets UpdatableObjectIds field to given value.

### HasUpdatableObjectIds

`func (o *SplitTunnelingData) HasUpdatableObjectIds() bool`

HasUpdatableObjectIds returns a boolean if a field has been set.

### GetExceptions

`func (o *SplitTunnelingData) GetExceptions() []SplitTunnelingException`

GetExceptions returns the Exceptions field if non-nil, zero value otherwise.

### GetExceptionsOk

`func (o *SplitTunnelingData) GetExceptionsOk() (*[]SplitTunnelingException, bool)`

GetExceptionsOk returns a tuple with the Exceptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExceptions

`func (o *SplitTunnelingData) SetExceptions(v []SplitTunnelingException)`

SetExceptions sets Exceptions field to given value.

### HasExceptions

`func (o *SplitTunnelingData) HasExceptions() bool`

HasExceptions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


