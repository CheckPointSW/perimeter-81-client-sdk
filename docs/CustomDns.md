# CustomDns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** | Indicates whether private DNS is enabled | 
**Attributes** | Pointer to [**CustomDnsAttributes**](CustomDnsAttributes.md) |  | [optional] 

## Methods

### NewCustomDns

`func NewCustomDns(enabled bool, ) *CustomDns`

NewCustomDns instantiates a new CustomDns object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsWithDefaults

`func NewCustomDnsWithDefaults() *CustomDns`

NewCustomDnsWithDefaults instantiates a new CustomDns object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *CustomDns) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *CustomDns) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *CustomDns) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetAttributes

`func (o *CustomDns) GetAttributes() CustomDnsAttributes`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *CustomDns) GetAttributesOk() (*CustomDnsAttributes, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *CustomDns) SetAttributes(v CustomDnsAttributes)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *CustomDns) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


