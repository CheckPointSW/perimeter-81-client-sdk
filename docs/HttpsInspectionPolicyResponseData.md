# HttpsInspectionPolicyResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BypassRules** | Pointer to [**[]HttpsInspectionRule**](HttpsInspectionRule.md) |  | [optional] 
**ControlledBy** | Pointer to **string** | Indicates whether the policy is controlled by Quantum or Hsase | [optional] 
**CleanupBypassRuleDefaultAction** | Pointer to **string** | Echoes the persisted cleanup default action after the upsert so callers don&#39;t need a follow-up GET. Included in the response only when the tenant has the Inspection Policy feature enabled; when the feature is off the field is omitted entirely. Defaults to \&quot;inspect\&quot; when the tenant has the feature enabled but hasn&#39;t configured a specific value.  | [optional] 

## Methods

### NewHttpsInspectionPolicyResponseData

`func NewHttpsInspectionPolicyResponseData() *HttpsInspectionPolicyResponseData`

NewHttpsInspectionPolicyResponseData instantiates a new HttpsInspectionPolicyResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHttpsInspectionPolicyResponseDataWithDefaults

`func NewHttpsInspectionPolicyResponseDataWithDefaults() *HttpsInspectionPolicyResponseData`

NewHttpsInspectionPolicyResponseDataWithDefaults instantiates a new HttpsInspectionPolicyResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBypassRules

`func (o *HttpsInspectionPolicyResponseData) GetBypassRules() []HttpsInspectionRule`

GetBypassRules returns the BypassRules field if non-nil, zero value otherwise.

### GetBypassRulesOk

`func (o *HttpsInspectionPolicyResponseData) GetBypassRulesOk() (*[]HttpsInspectionRule, bool)`

GetBypassRulesOk returns a tuple with the BypassRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBypassRules

`func (o *HttpsInspectionPolicyResponseData) SetBypassRules(v []HttpsInspectionRule)`

SetBypassRules sets BypassRules field to given value.

### HasBypassRules

`func (o *HttpsInspectionPolicyResponseData) HasBypassRules() bool`

HasBypassRules returns a boolean if a field has been set.

### GetControlledBy

`func (o *HttpsInspectionPolicyResponseData) GetControlledBy() string`

GetControlledBy returns the ControlledBy field if non-nil, zero value otherwise.

### GetControlledByOk

`func (o *HttpsInspectionPolicyResponseData) GetControlledByOk() (*string, bool)`

GetControlledByOk returns a tuple with the ControlledBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlledBy

`func (o *HttpsInspectionPolicyResponseData) SetControlledBy(v string)`

SetControlledBy sets ControlledBy field to given value.

### HasControlledBy

`func (o *HttpsInspectionPolicyResponseData) HasControlledBy() bool`

HasControlledBy returns a boolean if a field has been set.

### GetCleanupBypassRuleDefaultAction

`func (o *HttpsInspectionPolicyResponseData) GetCleanupBypassRuleDefaultAction() string`

GetCleanupBypassRuleDefaultAction returns the CleanupBypassRuleDefaultAction field if non-nil, zero value otherwise.

### GetCleanupBypassRuleDefaultActionOk

`func (o *HttpsInspectionPolicyResponseData) GetCleanupBypassRuleDefaultActionOk() (*string, bool)`

GetCleanupBypassRuleDefaultActionOk returns a tuple with the CleanupBypassRuleDefaultAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCleanupBypassRuleDefaultAction

`func (o *HttpsInspectionPolicyResponseData) SetCleanupBypassRuleDefaultAction(v string)`

SetCleanupBypassRuleDefaultAction sets CleanupBypassRuleDefaultAction field to given value.

### HasCleanupBypassRuleDefaultAction

`func (o *HttpsInspectionPolicyResponseData) HasCleanupBypassRuleDefaultAction() bool`

HasCleanupBypassRuleDefaultAction returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


