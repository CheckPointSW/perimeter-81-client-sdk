# HostFirewallRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**Priority** | **int32** |  | 
**Status** | **string** |  | 
**Action** | **string** |  | 
**Log** | Pointer to **string** |  | [optional] 
**Sources** | [**[]HostFirewallSource**](HostFirewallSource.md) |  | 
**Services** | [**[]HostFirewallService**](HostFirewallService.md) |  | 
**Destinations** | [**[]HostFirewallDestination**](HostFirewallDestination.md) |  | 

## Methods

### NewHostFirewallRule

`func NewHostFirewallRule(id string, name string, priority int32, status string, action string, sources []HostFirewallSource, services []HostFirewallService, destinations []HostFirewallDestination, ) *HostFirewallRule`

NewHostFirewallRule instantiates a new HostFirewallRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHostFirewallRuleWithDefaults

`func NewHostFirewallRuleWithDefaults() *HostFirewallRule`

NewHostFirewallRuleWithDefaults instantiates a new HostFirewallRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *HostFirewallRule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *HostFirewallRule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *HostFirewallRule) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *HostFirewallRule) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *HostFirewallRule) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *HostFirewallRule) SetName(v string)`

SetName sets Name field to given value.


### GetPriority

`func (o *HostFirewallRule) GetPriority() int32`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *HostFirewallRule) GetPriorityOk() (*int32, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *HostFirewallRule) SetPriority(v int32)`

SetPriority sets Priority field to given value.


### GetStatus

`func (o *HostFirewallRule) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HostFirewallRule) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HostFirewallRule) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetAction

`func (o *HostFirewallRule) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *HostFirewallRule) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *HostFirewallRule) SetAction(v string)`

SetAction sets Action field to given value.


### GetLog

`func (o *HostFirewallRule) GetLog() string`

GetLog returns the Log field if non-nil, zero value otherwise.

### GetLogOk

`func (o *HostFirewallRule) GetLogOk() (*string, bool)`

GetLogOk returns a tuple with the Log field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLog

`func (o *HostFirewallRule) SetLog(v string)`

SetLog sets Log field to given value.

### HasLog

`func (o *HostFirewallRule) HasLog() bool`

HasLog returns a boolean if a field has been set.

### GetSources

`func (o *HostFirewallRule) GetSources() []HostFirewallSource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *HostFirewallRule) GetSourcesOk() (*[]HostFirewallSource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *HostFirewallRule) SetSources(v []HostFirewallSource)`

SetSources sets Sources field to given value.


### GetServices

`func (o *HostFirewallRule) GetServices() []HostFirewallService`

GetServices returns the Services field if non-nil, zero value otherwise.

### GetServicesOk

`func (o *HostFirewallRule) GetServicesOk() (*[]HostFirewallService, bool)`

GetServicesOk returns a tuple with the Services field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServices

`func (o *HostFirewallRule) SetServices(v []HostFirewallService)`

SetServices sets Services field to given value.


### GetDestinations

`func (o *HostFirewallRule) GetDestinations() []HostFirewallDestination`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *HostFirewallRule) GetDestinationsOk() (*[]HostFirewallDestination, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *HostFirewallRule) SetDestinations(v []HostFirewallDestination)`

SetDestinations sets Destinations field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


