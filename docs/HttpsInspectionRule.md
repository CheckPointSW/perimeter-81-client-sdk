# HttpsInspectionRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Rule ID (optional in requests, auto-generated for new rules) | [optional] 
**Name** | **string** | Rule name (cannot contain &lt; or &gt; characters) | 
**AppliedOn** | **string** | Where the rule is applied: Agents, Sites, or Both | 
**Priority** | **int32** | Rule priority. Updated automatically when rules are created/updated | 
**Sources** | [**[]HttpsInspectionSource**](HttpsInspectionSource.md) | List of source objects | 
**Destinations** | [**[]HttpsInspectionDestination**](HttpsInspectionDestination.md) | List of destination objects | 
**Action** | Pointer to **string** | Bypass or HTTPS Inspection action (optional, default: &#39;bypass&#39;). &#39;inspect&#39; is always valid for &#39;sites&#39; appliedOn. When the Inspection Policy feature is enabled, &#39;inspect&#39; is also valid on &#39;agents&#39; and &#39;both&#39;. &#39;inspectNoDecrypt&#39; requires the Inspection Policy feature and is only valid on &#39;agents&#39; appliedOn (rejected on &#39;sites&#39; and &#39;both&#39; regardless of the feature). | [optional] 
**Log** | Pointer to **string** | HTTPS Inspection logging (optional) is disabled by default and is supported only for rules applied to agents | [optional] 
**Status** | **string** | Rule status | 

## Methods

### NewHttpsInspectionRule

`func NewHttpsInspectionRule(name string, appliedOn string, priority int32, sources []HttpsInspectionSource, destinations []HttpsInspectionDestination, status string, ) *HttpsInspectionRule`

NewHttpsInspectionRule instantiates a new HttpsInspectionRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHttpsInspectionRuleWithDefaults

`func NewHttpsInspectionRuleWithDefaults() *HttpsInspectionRule`

NewHttpsInspectionRuleWithDefaults instantiates a new HttpsInspectionRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *HttpsInspectionRule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *HttpsInspectionRule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *HttpsInspectionRule) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *HttpsInspectionRule) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *HttpsInspectionRule) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *HttpsInspectionRule) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *HttpsInspectionRule) SetName(v string)`

SetName sets Name field to given value.


### GetAppliedOn

`func (o *HttpsInspectionRule) GetAppliedOn() string`

GetAppliedOn returns the AppliedOn field if non-nil, zero value otherwise.

### GetAppliedOnOk

`func (o *HttpsInspectionRule) GetAppliedOnOk() (*string, bool)`

GetAppliedOnOk returns a tuple with the AppliedOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppliedOn

`func (o *HttpsInspectionRule) SetAppliedOn(v string)`

SetAppliedOn sets AppliedOn field to given value.


### GetPriority

`func (o *HttpsInspectionRule) GetPriority() int32`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *HttpsInspectionRule) GetPriorityOk() (*int32, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *HttpsInspectionRule) SetPriority(v int32)`

SetPriority sets Priority field to given value.


### GetSources

`func (o *HttpsInspectionRule) GetSources() []HttpsInspectionSource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *HttpsInspectionRule) GetSourcesOk() (*[]HttpsInspectionSource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *HttpsInspectionRule) SetSources(v []HttpsInspectionSource)`

SetSources sets Sources field to given value.


### GetDestinations

`func (o *HttpsInspectionRule) GetDestinations() []HttpsInspectionDestination`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *HttpsInspectionRule) GetDestinationsOk() (*[]HttpsInspectionDestination, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *HttpsInspectionRule) SetDestinations(v []HttpsInspectionDestination)`

SetDestinations sets Destinations field to given value.


### GetAction

`func (o *HttpsInspectionRule) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *HttpsInspectionRule) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *HttpsInspectionRule) SetAction(v string)`

SetAction sets Action field to given value.

### HasAction

`func (o *HttpsInspectionRule) HasAction() bool`

HasAction returns a boolean if a field has been set.

### GetLog

`func (o *HttpsInspectionRule) GetLog() string`

GetLog returns the Log field if non-nil, zero value otherwise.

### GetLogOk

`func (o *HttpsInspectionRule) GetLogOk() (*string, bool)`

GetLogOk returns a tuple with the Log field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLog

`func (o *HttpsInspectionRule) SetLog(v string)`

SetLog sets Log field to given value.

### HasLog

`func (o *HttpsInspectionRule) HasLog() bool`

HasLog returns a boolean if a field has been set.

### GetStatus

`func (o *HttpsInspectionRule) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HttpsInspectionRule) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HttpsInspectionRule) SetStatus(v string)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


