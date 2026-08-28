# EnhancedIPSecSharedSettingsUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**P81GatewaySubnets** | **[]string** |  | 
**RemoteGatewaySubnets** | **[]string** |  | 
**P81ASN** | Pointer to **int32** |  | [optional] 
**Features** | Pointer to [**NetworkFeaturesCreate**](NetworkFeaturesCreate.md) |  | [optional] 

## Methods

### NewEnhancedIPSecSharedSettingsUpdate

`func NewEnhancedIPSecSharedSettingsUpdate(p81GatewaySubnets []string, remoteGatewaySubnets []string, ) *EnhancedIPSecSharedSettingsUpdate`

NewEnhancedIPSecSharedSettingsUpdate instantiates a new EnhancedIPSecSharedSettingsUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEnhancedIPSecSharedSettingsUpdateWithDefaults

`func NewEnhancedIPSecSharedSettingsUpdateWithDefaults() *EnhancedIPSecSharedSettingsUpdate`

NewEnhancedIPSecSharedSettingsUpdateWithDefaults instantiates a new EnhancedIPSecSharedSettingsUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81GatewaySubnets() []string`

GetP81GatewaySubnets returns the P81GatewaySubnets field if non-nil, zero value otherwise.

### GetP81GatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81GatewaySubnetsOk() (*[]string, bool)`

GetP81GatewaySubnetsOk returns a tuple with the P81GatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) SetP81GatewaySubnets(v []string)`

SetP81GatewaySubnets sets P81GatewaySubnets field to given value.


### GetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) GetRemoteGatewaySubnets() []string`

GetRemoteGatewaySubnets returns the RemoteGatewaySubnets field if non-nil, zero value otherwise.

### GetRemoteGatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetRemoteGatewaySubnetsOk() (*[]string, bool)`

GetRemoteGatewaySubnetsOk returns a tuple with the RemoteGatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) SetRemoteGatewaySubnets(v []string)`

SetRemoteGatewaySubnets sets RemoteGatewaySubnets field to given value.


### GetP81ASN

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81ASN() int32`

GetP81ASN returns the P81ASN field if non-nil, zero value otherwise.

### GetP81ASNOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81ASNOk() (*int32, bool)`

GetP81ASNOk returns a tuple with the P81ASN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81ASN

`func (o *EnhancedIPSecSharedSettingsUpdate) SetP81ASN(v int32)`

SetP81ASN sets P81ASN field to given value.

### HasP81ASN

`func (o *EnhancedIPSecSharedSettingsUpdate) HasP81ASN() bool`

HasP81ASN returns a boolean if a field has been set.

### GetFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) GetFeatures() NetworkFeaturesCreate`

GetFeatures returns the Features field if non-nil, zero value otherwise.

### GetFeaturesOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetFeaturesOk() (*NetworkFeaturesCreate, bool)`

GetFeaturesOk returns a tuple with the Features field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) SetFeatures(v NetworkFeaturesCreate)`

SetFeatures sets Features field to given value.

### HasFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) HasFeatures() bool`

HasFeatures returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


