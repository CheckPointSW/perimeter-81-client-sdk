# HostFirewallWarning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Field** | **string** |  | 
**Message** | **string** |  | 
**Tier** | **int32** |  | 
**Ports** | **[]int32** |  | 
**RuleName** | Pointer to **string** |  | [optional] 
**RuleIndex** | Pointer to **int32** |  | [optional] 

## Methods

### NewHostFirewallWarning

`func NewHostFirewallWarning(field string, message string, tier int32, ports []int32, ) *HostFirewallWarning`

NewHostFirewallWarning instantiates a new HostFirewallWarning object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHostFirewallWarningWithDefaults

`func NewHostFirewallWarningWithDefaults() *HostFirewallWarning`

NewHostFirewallWarningWithDefaults instantiates a new HostFirewallWarning object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetField

`func (o *HostFirewallWarning) GetField() string`

GetField returns the Field field if non-nil, zero value otherwise.

### GetFieldOk

`func (o *HostFirewallWarning) GetFieldOk() (*string, bool)`

GetFieldOk returns a tuple with the Field field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetField

`func (o *HostFirewallWarning) SetField(v string)`

SetField sets Field field to given value.


### GetMessage

`func (o *HostFirewallWarning) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *HostFirewallWarning) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *HostFirewallWarning) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetTier

`func (o *HostFirewallWarning) GetTier() int32`

GetTier returns the Tier field if non-nil, zero value otherwise.

### GetTierOk

`func (o *HostFirewallWarning) GetTierOk() (*int32, bool)`

GetTierOk returns a tuple with the Tier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier

`func (o *HostFirewallWarning) SetTier(v int32)`

SetTier sets Tier field to given value.


### GetPorts

`func (o *HostFirewallWarning) GetPorts() []int32`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *HostFirewallWarning) GetPortsOk() (*[]int32, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *HostFirewallWarning) SetPorts(v []int32)`

SetPorts sets Ports field to given value.


### GetRuleName

`func (o *HostFirewallWarning) GetRuleName() string`

GetRuleName returns the RuleName field if non-nil, zero value otherwise.

### GetRuleNameOk

`func (o *HostFirewallWarning) GetRuleNameOk() (*string, bool)`

GetRuleNameOk returns a tuple with the RuleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleName

`func (o *HostFirewallWarning) SetRuleName(v string)`

SetRuleName sets RuleName field to given value.

### HasRuleName

`func (o *HostFirewallWarning) HasRuleName() bool`

HasRuleName returns a boolean if a field has been set.

### GetRuleIndex

`func (o *HostFirewallWarning) GetRuleIndex() int32`

GetRuleIndex returns the RuleIndex field if non-nil, zero value otherwise.

### GetRuleIndexOk

`func (o *HostFirewallWarning) GetRuleIndexOk() (*int32, bool)`

GetRuleIndexOk returns a tuple with the RuleIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRuleIndex

`func (o *HostFirewallWarning) SetRuleIndex(v int32)`

SetRuleIndex sets RuleIndex field to given value.

### HasRuleIndex

`func (o *HostFirewallWarning) HasRuleIndex() bool`

HasRuleIndex returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


