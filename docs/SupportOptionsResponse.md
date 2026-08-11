# SupportOptionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PhoneSupportType** | **string** | Type of phone support configured: - harmonySaseDefault: Use Harmony SASE default phone support - custom: Use custom phone numbers (requires supportPhoneNumbers) - hidden: Disable phone support  | 
**SupportPhoneNumbers** | Pointer to [**[]SupportPhoneNumber**](SupportPhoneNumber.md) | Custom phone numbers (1-3 items when phoneSupportType is &#39;custom&#39;, null otherwise) | [optional] 
**UserGuidesEnabled** | **bool** | Whether user guides and documentation are enabled | 
**LiveChatType** | **string** | Type of live chat support configured: - harmonySaseDefault: Use Harmony SASE default chat - custom: Use custom chat URL (requires liveChatCustomUrl) - hidden: Disable live chat support  | 
**LiveChatCustomUrl** | Pointer to **string** |  | [optional] 

## Methods

### NewSupportOptionsResponse

`func NewSupportOptionsResponse(phoneSupportType string, userGuidesEnabled bool, liveChatType string, ) *SupportOptionsResponse`

NewSupportOptionsResponse instantiates a new SupportOptionsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSupportOptionsResponseWithDefaults

`func NewSupportOptionsResponseWithDefaults() *SupportOptionsResponse`

NewSupportOptionsResponseWithDefaults instantiates a new SupportOptionsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPhoneSupportType

`func (o *SupportOptionsResponse) GetPhoneSupportType() string`

GetPhoneSupportType returns the PhoneSupportType field if non-nil, zero value otherwise.

### GetPhoneSupportTypeOk

`func (o *SupportOptionsResponse) GetPhoneSupportTypeOk() (*string, bool)`

GetPhoneSupportTypeOk returns a tuple with the PhoneSupportType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhoneSupportType

`func (o *SupportOptionsResponse) SetPhoneSupportType(v string)`

SetPhoneSupportType sets PhoneSupportType field to given value.


### GetSupportPhoneNumbers

`func (o *SupportOptionsResponse) GetSupportPhoneNumbers() []SupportPhoneNumber`

GetSupportPhoneNumbers returns the SupportPhoneNumbers field if non-nil, zero value otherwise.

### GetSupportPhoneNumbersOk

`func (o *SupportOptionsResponse) GetSupportPhoneNumbersOk() (*[]SupportPhoneNumber, bool)`

GetSupportPhoneNumbersOk returns a tuple with the SupportPhoneNumbers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSupportPhoneNumbers

`func (o *SupportOptionsResponse) SetSupportPhoneNumbers(v []SupportPhoneNumber)`

SetSupportPhoneNumbers sets SupportPhoneNumbers field to given value.

### HasSupportPhoneNumbers

`func (o *SupportOptionsResponse) HasSupportPhoneNumbers() bool`

HasSupportPhoneNumbers returns a boolean if a field has been set.

### SetSupportPhoneNumbersNil

`func (o *SupportOptionsResponse) SetSupportPhoneNumbersNil(b bool)`

 SetSupportPhoneNumbersNil sets the value for SupportPhoneNumbers to be an explicit nil

### UnsetSupportPhoneNumbers
`func (o *SupportOptionsResponse) UnsetSupportPhoneNumbers()`

UnsetSupportPhoneNumbers ensures that no value is present for SupportPhoneNumbers, not even an explicit nil
### GetUserGuidesEnabled

`func (o *SupportOptionsResponse) GetUserGuidesEnabled() bool`

GetUserGuidesEnabled returns the UserGuidesEnabled field if non-nil, zero value otherwise.

### GetUserGuidesEnabledOk

`func (o *SupportOptionsResponse) GetUserGuidesEnabledOk() (*bool, bool)`

GetUserGuidesEnabledOk returns a tuple with the UserGuidesEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserGuidesEnabled

`func (o *SupportOptionsResponse) SetUserGuidesEnabled(v bool)`

SetUserGuidesEnabled sets UserGuidesEnabled field to given value.


### GetLiveChatType

`func (o *SupportOptionsResponse) GetLiveChatType() string`

GetLiveChatType returns the LiveChatType field if non-nil, zero value otherwise.

### GetLiveChatTypeOk

`func (o *SupportOptionsResponse) GetLiveChatTypeOk() (*string, bool)`

GetLiveChatTypeOk returns a tuple with the LiveChatType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLiveChatType

`func (o *SupportOptionsResponse) SetLiveChatType(v string)`

SetLiveChatType sets LiveChatType field to given value.


### GetLiveChatCustomUrl

`func (o *SupportOptionsResponse) GetLiveChatCustomUrl() string`

GetLiveChatCustomUrl returns the LiveChatCustomUrl field if non-nil, zero value otherwise.

### GetLiveChatCustomUrlOk

`func (o *SupportOptionsResponse) GetLiveChatCustomUrlOk() (*string, bool)`

GetLiveChatCustomUrlOk returns a tuple with the LiveChatCustomUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLiveChatCustomUrl

`func (o *SupportOptionsResponse) SetLiveChatCustomUrl(v string)`

SetLiveChatCustomUrl sets LiveChatCustomUrl field to given value.

### HasLiveChatCustomUrl

`func (o *SupportOptionsResponse) HasLiveChatCustomUrl() bool`

HasLiveChatCustomUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


