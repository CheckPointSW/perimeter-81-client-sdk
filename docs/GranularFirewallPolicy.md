# GranularFirewallPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** | Indicates whether the policy is enabled. | 
**Allowed** | **bool** | Defines the default policy action. When true, traffic is allowed; when false, traffic is blocked. | 
**Id** | **string** | Unique network policy ID. | 
**PolicyLoggingEnabled** | **bool** | whether logging is enabled at the policy level. | 
**PolicyRules** | [**[]GranularFirewallPolicyRule**](GranularFirewallPolicyRule.md) | List of policy rules. | 

## Methods

### NewGranularFirewallPolicy

`func NewGranularFirewallPolicy(enabled bool, allowed bool, id string, policyLoggingEnabled bool, policyRules []GranularFirewallPolicyRule, ) *GranularFirewallPolicy`

NewGranularFirewallPolicy instantiates a new GranularFirewallPolicy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGranularFirewallPolicyWithDefaults

`func NewGranularFirewallPolicyWithDefaults() *GranularFirewallPolicy`

NewGranularFirewallPolicyWithDefaults instantiates a new GranularFirewallPolicy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *GranularFirewallPolicy) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *GranularFirewallPolicy) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *GranularFirewallPolicy) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetAllowed

`func (o *GranularFirewallPolicy) GetAllowed() bool`

GetAllowed returns the Allowed field if non-nil, zero value otherwise.

### GetAllowedOk

`func (o *GranularFirewallPolicy) GetAllowedOk() (*bool, bool)`

GetAllowedOk returns a tuple with the Allowed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowed

`func (o *GranularFirewallPolicy) SetAllowed(v bool)`

SetAllowed sets Allowed field to given value.


### GetId

`func (o *GranularFirewallPolicy) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GranularFirewallPolicy) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GranularFirewallPolicy) SetId(v string)`

SetId sets Id field to given value.


### GetPolicyLoggingEnabled

`func (o *GranularFirewallPolicy) GetPolicyLoggingEnabled() bool`

GetPolicyLoggingEnabled returns the PolicyLoggingEnabled field if non-nil, zero value otherwise.

### GetPolicyLoggingEnabledOk

`func (o *GranularFirewallPolicy) GetPolicyLoggingEnabledOk() (*bool, bool)`

GetPolicyLoggingEnabledOk returns a tuple with the PolicyLoggingEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPolicyLoggingEnabled

`func (o *GranularFirewallPolicy) SetPolicyLoggingEnabled(v bool)`

SetPolicyLoggingEnabled sets PolicyLoggingEnabled field to given value.


### GetPolicyRules

`func (o *GranularFirewallPolicy) GetPolicyRules() []GranularFirewallPolicyRule`

GetPolicyRules returns the PolicyRules field if non-nil, zero value otherwise.

### GetPolicyRulesOk

`func (o *GranularFirewallPolicy) GetPolicyRulesOk() (*[]GranularFirewallPolicyRule, bool)`

GetPolicyRulesOk returns a tuple with the PolicyRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPolicyRules

`func (o *GranularFirewallPolicy) SetPolicyRules(v []GranularFirewallPolicyRule)`

SetPolicyRules sets PolicyRules field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


