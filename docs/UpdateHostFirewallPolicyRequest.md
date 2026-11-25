# UpdateHostFirewallPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProtocolRules** | [**[]HostFirewallRuleInput**](HostFirewallRuleInput.md) | Full list of rules. An empty array deletes all rules. | 

## Methods

### NewUpdateHostFirewallPolicyRequest

`func NewUpdateHostFirewallPolicyRequest(protocolRules []HostFirewallRuleInput, ) *UpdateHostFirewallPolicyRequest`

NewUpdateHostFirewallPolicyRequest instantiates a new UpdateHostFirewallPolicyRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateHostFirewallPolicyRequestWithDefaults

`func NewUpdateHostFirewallPolicyRequestWithDefaults() *UpdateHostFirewallPolicyRequest`

NewUpdateHostFirewallPolicyRequestWithDefaults instantiates a new UpdateHostFirewallPolicyRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProtocolRules

`func (o *UpdateHostFirewallPolicyRequest) GetProtocolRules() []HostFirewallRuleInput`

GetProtocolRules returns the ProtocolRules field if non-nil, zero value otherwise.

### GetProtocolRulesOk

`func (o *UpdateHostFirewallPolicyRequest) GetProtocolRulesOk() (*[]HostFirewallRuleInput, bool)`

GetProtocolRulesOk returns a tuple with the ProtocolRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocolRules

`func (o *UpdateHostFirewallPolicyRequest) SetProtocolRules(v []HostFirewallRuleInput)`

SetProtocolRules sets ProtocolRules field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


