# GranularFirewallPolicyRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Unique policy rule ID. | [optional] 
**Name** | **string** | Name of the policy rule. | 
**Enabled** | **bool** | Enables or disables the rule on the firewall. When set to true, the rule is active; when false, the rule is inactive. | 
**Allowed** | **bool** | Determines the rule action. When set to true, traffic is allowed; when false, traffic is blocked. | 
**Sources** | [**SourcesAndDestinations**](SourcesAndDestinations.md) |  | 
**Destinations** | [**SourcesAndDestinations**](SourcesAndDestinations.md) |  | 
**Services** | Pointer to **[]string** | List of service object IDs. | [optional] 
**LogEnabled** | **bool** | whether logging is enabled for this rule. | 

## Methods

### NewGranularFirewallPolicyRule

`func NewGranularFirewallPolicyRule(name string, enabled bool, allowed bool, sources SourcesAndDestinations, destinations SourcesAndDestinations, logEnabled bool, ) *GranularFirewallPolicyRule`

NewGranularFirewallPolicyRule instantiates a new GranularFirewallPolicyRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGranularFirewallPolicyRuleWithDefaults

`func NewGranularFirewallPolicyRuleWithDefaults() *GranularFirewallPolicyRule`

NewGranularFirewallPolicyRuleWithDefaults instantiates a new GranularFirewallPolicyRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GranularFirewallPolicyRule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GranularFirewallPolicyRule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GranularFirewallPolicyRule) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *GranularFirewallPolicyRule) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *GranularFirewallPolicyRule) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GranularFirewallPolicyRule) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GranularFirewallPolicyRule) SetName(v string)`

SetName sets Name field to given value.


### GetEnabled

`func (o *GranularFirewallPolicyRule) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *GranularFirewallPolicyRule) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *GranularFirewallPolicyRule) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetAllowed

`func (o *GranularFirewallPolicyRule) GetAllowed() bool`

GetAllowed returns the Allowed field if non-nil, zero value otherwise.

### GetAllowedOk

`func (o *GranularFirewallPolicyRule) GetAllowedOk() (*bool, bool)`

GetAllowedOk returns a tuple with the Allowed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowed

`func (o *GranularFirewallPolicyRule) SetAllowed(v bool)`

SetAllowed sets Allowed field to given value.


### GetSources

`func (o *GranularFirewallPolicyRule) GetSources() SourcesAndDestinations`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *GranularFirewallPolicyRule) GetSourcesOk() (*SourcesAndDestinations, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *GranularFirewallPolicyRule) SetSources(v SourcesAndDestinations)`

SetSources sets Sources field to given value.


### GetDestinations

`func (o *GranularFirewallPolicyRule) GetDestinations() SourcesAndDestinations`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *GranularFirewallPolicyRule) GetDestinationsOk() (*SourcesAndDestinations, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *GranularFirewallPolicyRule) SetDestinations(v SourcesAndDestinations)`

SetDestinations sets Destinations field to given value.


### GetServices

`func (o *GranularFirewallPolicyRule) GetServices() []string`

GetServices returns the Services field if non-nil, zero value otherwise.

### GetServicesOk

`func (o *GranularFirewallPolicyRule) GetServicesOk() (*[]string, bool)`

GetServicesOk returns a tuple with the Services field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServices

`func (o *GranularFirewallPolicyRule) SetServices(v []string)`

SetServices sets Services field to given value.

### HasServices

`func (o *GranularFirewallPolicyRule) HasServices() bool`

HasServices returns a boolean if a field has been set.

### GetLogEnabled

`func (o *GranularFirewallPolicyRule) GetLogEnabled() bool`

GetLogEnabled returns the LogEnabled field if non-nil, zero value otherwise.

### GetLogEnabledOk

`func (o *GranularFirewallPolicyRule) GetLogEnabledOk() (*bool, bool)`

GetLogEnabledOk returns a tuple with the LogEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogEnabled

`func (o *GranularFirewallPolicyRule) SetLogEnabled(v bool)`

SetLogEnabled sets LogEnabled field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


