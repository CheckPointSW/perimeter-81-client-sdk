# CustomDnsUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** | Whether private DNS is enabled. | 
**Attributes** | [**CustomDnsUpdateAttributes**](CustomDnsUpdateAttributes.md) |  | 

## Methods

### NewCustomDnsUpdate

`func NewCustomDnsUpdate(enabled bool, attributes CustomDnsUpdateAttributes, ) *CustomDnsUpdate`

NewCustomDnsUpdate instantiates a new CustomDnsUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsUpdateWithDefaults

`func NewCustomDnsUpdateWithDefaults() *CustomDnsUpdate`

NewCustomDnsUpdateWithDefaults instantiates a new CustomDnsUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *CustomDnsUpdate) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *CustomDnsUpdate) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *CustomDnsUpdate) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetAttributes

`func (o *CustomDnsUpdate) GetAttributes() CustomDnsUpdateAttributes`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *CustomDnsUpdate) GetAttributesOk() (*CustomDnsUpdateAttributes, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *CustomDnsUpdate) SetAttributes(v CustomDnsUpdateAttributes)`

SetAttributes sets Attributes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


