# HostFirewallRuleInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Rule ID (optional in requests, auto-generated for new rules) | [optional] 
**Name** | **string** |  | 
**Priority** | Pointer to **int32** | Ignored in requests. Priority is assigned from the order of the array (first &#x3D; highest) and returned in responses. | [optional] 
**Status** | Pointer to **string** |  | [optional] 
**Action** | **string** |  | 
**Log** | Pointer to **string** |  | [optional] 
**Sources** | [**[]HostFirewallSource**](HostFirewallSource.md) |  | 
**Services** | [**[]HostFirewallService**](HostFirewallService.md) | Must contain at least one service; an empty array returns 422 (VALIDATION_HOST_FIREWALL_SERVICE_REQUIRED). | 
**Destinations** | [**[]HostFirewallDestination**](HostFirewallDestination.md) |  | 

## Methods

### NewHostFirewallRuleInput

`func NewHostFirewallRuleInput(name string, action string, sources []HostFirewallSource, services []HostFirewallService, destinations []HostFirewallDestination, ) *HostFirewallRuleInput`

NewHostFirewallRuleInput instantiates a new HostFirewallRuleInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHostFirewallRuleInputWithDefaults

`func NewHostFirewallRuleInputWithDefaults() *HostFirewallRuleInput`

NewHostFirewallRuleInputWithDefaults instantiates a new HostFirewallRuleInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *HostFirewallRuleInput) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *HostFirewallRuleInput) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *HostFirewallRuleInput) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *HostFirewallRuleInput) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *HostFirewallRuleInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *HostFirewallRuleInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *HostFirewallRuleInput) SetName(v string)`

SetName sets Name field to given value.


### GetPriority

`func (o *HostFirewallRuleInput) GetPriority() int32`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *HostFirewallRuleInput) GetPriorityOk() (*int32, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *HostFirewallRuleInput) SetPriority(v int32)`

SetPriority sets Priority field to given value.

### HasPriority

`func (o *HostFirewallRuleInput) HasPriority() bool`

HasPriority returns a boolean if a field has been set.

### GetStatus

`func (o *HostFirewallRuleInput) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HostFirewallRuleInput) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HostFirewallRuleInput) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *HostFirewallRuleInput) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetAction

`func (o *HostFirewallRuleInput) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *HostFirewallRuleInput) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *HostFirewallRuleInput) SetAction(v string)`

SetAction sets Action field to given value.


### GetLog

`func (o *HostFirewallRuleInput) GetLog() string`

GetLog returns the Log field if non-nil, zero value otherwise.

### GetLogOk

`func (o *HostFirewallRuleInput) GetLogOk() (*string, bool)`

GetLogOk returns a tuple with the Log field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLog

`func (o *HostFirewallRuleInput) SetLog(v string)`

SetLog sets Log field to given value.

### HasLog

`func (o *HostFirewallRuleInput) HasLog() bool`

HasLog returns a boolean if a field has been set.

### GetSources

`func (o *HostFirewallRuleInput) GetSources() []HostFirewallSource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *HostFirewallRuleInput) GetSourcesOk() (*[]HostFirewallSource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *HostFirewallRuleInput) SetSources(v []HostFirewallSource)`

SetSources sets Sources field to given value.


### GetServices

`func (o *HostFirewallRuleInput) GetServices() []HostFirewallService`

GetServices returns the Services field if non-nil, zero value otherwise.

### GetServicesOk

`func (o *HostFirewallRuleInput) GetServicesOk() (*[]HostFirewallService, bool)`

GetServicesOk returns a tuple with the Services field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServices

`func (o *HostFirewallRuleInput) SetServices(v []HostFirewallService)`

SetServices sets Services field to given value.


### GetDestinations

`func (o *HostFirewallRuleInput) GetDestinations() []HostFirewallDestination`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *HostFirewallRuleInput) GetDestinationsOk() (*[]HostFirewallDestination, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *HostFirewallRuleInput) SetDestinations(v []HostFirewallDestination)`

SetDestinations sets Destinations field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


