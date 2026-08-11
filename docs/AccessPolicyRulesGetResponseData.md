# AccessPolicyRulesGetResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WebRules** | Pointer to [**[]AccessPolicyRule**](AccessPolicyRule.md) |  | [optional] 
**ControlledBy** | Pointer to **string** | Indicates whether the policy is controlled by Quantum or Hsase | [optional] 

## Methods

### NewAccessPolicyRulesGetResponseData

`func NewAccessPolicyRulesGetResponseData() *AccessPolicyRulesGetResponseData`

NewAccessPolicyRulesGetResponseData instantiates a new AccessPolicyRulesGetResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccessPolicyRulesGetResponseDataWithDefaults

`func NewAccessPolicyRulesGetResponseDataWithDefaults() *AccessPolicyRulesGetResponseData`

NewAccessPolicyRulesGetResponseDataWithDefaults instantiates a new AccessPolicyRulesGetResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWebRules

`func (o *AccessPolicyRulesGetResponseData) GetWebRules() []AccessPolicyRule`

GetWebRules returns the WebRules field if non-nil, zero value otherwise.

### GetWebRulesOk

`func (o *AccessPolicyRulesGetResponseData) GetWebRulesOk() (*[]AccessPolicyRule, bool)`

GetWebRulesOk returns a tuple with the WebRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebRules

`func (o *AccessPolicyRulesGetResponseData) SetWebRules(v []AccessPolicyRule)`

SetWebRules sets WebRules field to given value.

### HasWebRules

`func (o *AccessPolicyRulesGetResponseData) HasWebRules() bool`

HasWebRules returns a boolean if a field has been set.

### GetControlledBy

`func (o *AccessPolicyRulesGetResponseData) GetControlledBy() string`

GetControlledBy returns the ControlledBy field if non-nil, zero value otherwise.

### GetControlledByOk

`func (o *AccessPolicyRulesGetResponseData) GetControlledByOk() (*string, bool)`

GetControlledByOk returns a tuple with the ControlledBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlledBy

`func (o *AccessPolicyRulesGetResponseData) SetControlledBy(v string)`

SetControlledBy sets ControlledBy field to given value.

### HasControlledBy

`func (o *AccessPolicyRulesGetResponseData) HasControlledBy() bool`

HasControlledBy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


