# UpsertHttpsInspectionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BypassRules** | [**[]HttpsInspectionRule**](HttpsInspectionRule.md) |  | 
**CleanupBypassRuleDefaultAction** | Pointer to **string** | Optional. Default action for traffic not matched by any explicit bypass rule (the cleanup rule). Per-tenant setting — scope-agnostic. Accepted only when the tenant has the Inspection Policy feature enabled; otherwise the request is rejected with 422 VALIDATION_CLEANUP_ACTION_NOT_ALLOWED. Semantics: &#39;inspect&#39; (default) applies full HTTPS inspection to unmatched traffic; &#39;inspectNoDecrypt&#39; inspects without decrypting on the agent path; &#39;bypass&#39; causes unmatched traffic to skip HTTPS inspection entirely.  | [optional] 

## Methods

### NewUpsertHttpsInspectionPolicy

`func NewUpsertHttpsInspectionPolicy(bypassRules []HttpsInspectionRule, ) *UpsertHttpsInspectionPolicy`

NewUpsertHttpsInspectionPolicy instantiates a new UpsertHttpsInspectionPolicy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpsertHttpsInspectionPolicyWithDefaults

`func NewUpsertHttpsInspectionPolicyWithDefaults() *UpsertHttpsInspectionPolicy`

NewUpsertHttpsInspectionPolicyWithDefaults instantiates a new UpsertHttpsInspectionPolicy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBypassRules

`func (o *UpsertHttpsInspectionPolicy) GetBypassRules() []HttpsInspectionRule`

GetBypassRules returns the BypassRules field if non-nil, zero value otherwise.

### GetBypassRulesOk

`func (o *UpsertHttpsInspectionPolicy) GetBypassRulesOk() (*[]HttpsInspectionRule, bool)`

GetBypassRulesOk returns a tuple with the BypassRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBypassRules

`func (o *UpsertHttpsInspectionPolicy) SetBypassRules(v []HttpsInspectionRule)`

SetBypassRules sets BypassRules field to given value.


### GetCleanupBypassRuleDefaultAction

`func (o *UpsertHttpsInspectionPolicy) GetCleanupBypassRuleDefaultAction() string`

GetCleanupBypassRuleDefaultAction returns the CleanupBypassRuleDefaultAction field if non-nil, zero value otherwise.

### GetCleanupBypassRuleDefaultActionOk

`func (o *UpsertHttpsInspectionPolicy) GetCleanupBypassRuleDefaultActionOk() (*string, bool)`

GetCleanupBypassRuleDefaultActionOk returns a tuple with the CleanupBypassRuleDefaultAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCleanupBypassRuleDefaultAction

`func (o *UpsertHttpsInspectionPolicy) SetCleanupBypassRuleDefaultAction(v string)`

SetCleanupBypassRuleDefaultAction sets CleanupBypassRuleDefaultAction field to given value.

### HasCleanupBypassRuleDefaultAction

`func (o *UpsertHttpsInspectionPolicy) HasCleanupBypassRuleDefaultAction() bool`

HasCleanupBypassRuleDefaultAction returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


