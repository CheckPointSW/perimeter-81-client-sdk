# UpdateFileAccessPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FileAccessRules** | [**[]FileAccessRule**](FileAccessRule.md) |  | 

## Methods

### NewUpdateFileAccessPolicyRequest

`func NewUpdateFileAccessPolicyRequest(fileAccessRules []FileAccessRule, ) *UpdateFileAccessPolicyRequest`

NewUpdateFileAccessPolicyRequest instantiates a new UpdateFileAccessPolicyRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateFileAccessPolicyRequestWithDefaults

`func NewUpdateFileAccessPolicyRequestWithDefaults() *UpdateFileAccessPolicyRequest`

NewUpdateFileAccessPolicyRequestWithDefaults instantiates a new UpdateFileAccessPolicyRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFileAccessRules

`func (o *UpdateFileAccessPolicyRequest) GetFileAccessRules() []FileAccessRule`

GetFileAccessRules returns the FileAccessRules field if non-nil, zero value otherwise.

### GetFileAccessRulesOk

`func (o *UpdateFileAccessPolicyRequest) GetFileAccessRulesOk() (*[]FileAccessRule, bool)`

GetFileAccessRulesOk returns a tuple with the FileAccessRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileAccessRules

`func (o *UpdateFileAccessPolicyRequest) SetFileAccessRules(v []FileAccessRule)`

SetFileAccessRules sets FileAccessRules field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


