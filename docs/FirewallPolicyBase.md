# FirewallPolicyBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | **bool** | Indicates whether the policy is enabled. | 
**Allowed** | **bool** | Defines the default policy action. When true, traffic is allowed; when false, traffic is blocked. | 
**Id** | **string** | Unique network policy ID. | 

## Methods

### NewFirewallPolicyBase

`func NewFirewallPolicyBase(enabled bool, allowed bool, id string, ) *FirewallPolicyBase`

NewFirewallPolicyBase instantiates a new FirewallPolicyBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFirewallPolicyBaseWithDefaults

`func NewFirewallPolicyBaseWithDefaults() *FirewallPolicyBase`

NewFirewallPolicyBaseWithDefaults instantiates a new FirewallPolicyBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *FirewallPolicyBase) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *FirewallPolicyBase) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *FirewallPolicyBase) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetAllowed

`func (o *FirewallPolicyBase) GetAllowed() bool`

GetAllowed returns the Allowed field if non-nil, zero value otherwise.

### GetAllowedOk

`func (o *FirewallPolicyBase) GetAllowedOk() (*bool, bool)`

GetAllowedOk returns a tuple with the Allowed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowed

`func (o *FirewallPolicyBase) SetAllowed(v bool)`

SetAllowed sets Allowed field to given value.


### GetId

`func (o *FirewallPolicyBase) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FirewallPolicyBase) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FirewallPolicyBase) SetId(v string)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


