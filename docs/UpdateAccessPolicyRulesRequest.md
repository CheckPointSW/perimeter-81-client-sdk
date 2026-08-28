# UpdateAccessPolicyRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WebRules** | [**[]AccessPolicyRule**](AccessPolicyRule.md) |  | 

## Methods

### NewUpdateAccessPolicyRulesRequest

`func NewUpdateAccessPolicyRulesRequest(webRules []AccessPolicyRule, ) *UpdateAccessPolicyRulesRequest`

NewUpdateAccessPolicyRulesRequest instantiates a new UpdateAccessPolicyRulesRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateAccessPolicyRulesRequestWithDefaults

`func NewUpdateAccessPolicyRulesRequestWithDefaults() *UpdateAccessPolicyRulesRequest`

NewUpdateAccessPolicyRulesRequestWithDefaults instantiates a new UpdateAccessPolicyRulesRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWebRules

`func (o *UpdateAccessPolicyRulesRequest) GetWebRules() []AccessPolicyRule`

GetWebRules returns the WebRules field if non-nil, zero value otherwise.

### GetWebRulesOk

`func (o *UpdateAccessPolicyRulesRequest) GetWebRulesOk() (*[]AccessPolicyRule, bool)`

GetWebRulesOk returns a tuple with the WebRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebRules

`func (o *UpdateAccessPolicyRulesRequest) SetWebRules(v []AccessPolicyRule)`

SetWebRules sets WebRules field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


