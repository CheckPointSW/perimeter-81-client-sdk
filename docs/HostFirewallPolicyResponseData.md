# HostFirewallPolicyResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProtocolRules** | [**[]HostFirewallRule**](HostFirewallRule.md) |  | 
**Warnings** | Pointer to [**[]HostFirewallWarning**](HostFirewallWarning.md) | Non-blocking warnings returned on save (POST only) | [optional] 

## Methods

### NewHostFirewallPolicyResponseData

`func NewHostFirewallPolicyResponseData(protocolRules []HostFirewallRule, ) *HostFirewallPolicyResponseData`

NewHostFirewallPolicyResponseData instantiates a new HostFirewallPolicyResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHostFirewallPolicyResponseDataWithDefaults

`func NewHostFirewallPolicyResponseDataWithDefaults() *HostFirewallPolicyResponseData`

NewHostFirewallPolicyResponseDataWithDefaults instantiates a new HostFirewallPolicyResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProtocolRules

`func (o *HostFirewallPolicyResponseData) GetProtocolRules() []HostFirewallRule`

GetProtocolRules returns the ProtocolRules field if non-nil, zero value otherwise.

### GetProtocolRulesOk

`func (o *HostFirewallPolicyResponseData) GetProtocolRulesOk() (*[]HostFirewallRule, bool)`

GetProtocolRulesOk returns a tuple with the ProtocolRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocolRules

`func (o *HostFirewallPolicyResponseData) SetProtocolRules(v []HostFirewallRule)`

SetProtocolRules sets ProtocolRules field to given value.


### GetWarnings

`func (o *HostFirewallPolicyResponseData) GetWarnings() []HostFirewallWarning`

GetWarnings returns the Warnings field if non-nil, zero value otherwise.

### GetWarningsOk

`func (o *HostFirewallPolicyResponseData) GetWarningsOk() (*[]HostFirewallWarning, bool)`

GetWarningsOk returns a tuple with the Warnings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWarnings

`func (o *HostFirewallPolicyResponseData) SetWarnings(v []HostFirewallWarning)`

SetWarnings sets Warnings field to given value.

### HasWarnings

`func (o *HostFirewallPolicyResponseData) HasWarnings() bool`

HasWarnings returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


