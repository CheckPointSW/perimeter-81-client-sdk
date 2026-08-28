# SupportPhoneNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Description** | **string** | Label or description for the phone number (e.g., \&quot;US Support\&quot;, \&quot;Emergency\&quot;) | 
**PhoneNumber** | **string** | Phone number in international or local format | 

## Methods

### NewSupportPhoneNumber

`func NewSupportPhoneNumber(description string, phoneNumber string, ) *SupportPhoneNumber`

NewSupportPhoneNumber instantiates a new SupportPhoneNumber object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSupportPhoneNumberWithDefaults

`func NewSupportPhoneNumberWithDefaults() *SupportPhoneNumber`

NewSupportPhoneNumberWithDefaults instantiates a new SupportPhoneNumber object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDescription

`func (o *SupportPhoneNumber) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SupportPhoneNumber) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SupportPhoneNumber) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetPhoneNumber

`func (o *SupportPhoneNumber) GetPhoneNumber() string`

GetPhoneNumber returns the PhoneNumber field if non-nil, zero value otherwise.

### GetPhoneNumberOk

`func (o *SupportPhoneNumber) GetPhoneNumberOk() (*string, bool)`

GetPhoneNumberOk returns a tuple with the PhoneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneNumber

`func (o *SupportPhoneNumber) SetPhoneNumber(v string)`

SetPhoneNumber sets PhoneNumber field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


