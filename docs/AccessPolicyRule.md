# AccessPolicyRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Rule ID (optional in requests, auto-generated for new rules) | [optional] 
**Name** | **string** | Rule name (cannot contain &lt; or &gt; characters) | 
**AppliedOn** | **string** | Where the rule is applied: Agents, Sites, or Both | 
**Action** | **string** | Rule action. &#39;redirect&#39; requires the Redirect feature; when the feature is not enabled for the tenant, adding or changing a rule that redirects is rejected with 422 VALIDATION_REDIRECT_NOT_ENABLED. | 
**RedirectUrl** | Pointer to **string** | Absolute http or https URL the user is redirected to, up to 2048 characters and without a username or password. Required for &#39;redirect&#39; rules and for &#39;block&#39; rules with redirectAction &#39;afterBlockPage&#39;, otherwise the request is rejected with 422 VALIDATION_INVALID_REDIRECT_URL. On any other rule a valid URL is stored without taking effect, and applies again if the rule is switched back to redirecting.  | [optional] 
**RedirectAction** | Pointer to **string** | Optional. Send &#39;afterBlockPage&#39;, with redirectUrl, to make a &#39;block&#39; rule show the block page and then redirect; &#39;none&#39; (the default) means it does not redirect. Leave it out on &#39;redirect&#39; rules — the service always sets &#39;immediate&#39;. Any other combination is rejected with 422 VALIDATION_INVALID_REDIRECT_ACTION, or VALIDATION_REDIRECT_NOT_ALLOWED_FOR_ACTION on &#39;allow&#39; and &#39;warning&#39; rules.  | [optional] 
**Conditions** | [**[]Condition**](Condition.md) | Optional time-based conditions, default is an empty array (no time constraints) | 
**Destinations** | [**[]AccessPolicyDestination**](AccessPolicyDestination.md) | List of destination objects | 
**Sources** | [**[]AccessPolicySource**](AccessPolicySource.md) | List of source objects | 
**Log** | Pointer to **string** | Logging mode (optional) – If not specified, the service automatically sets the logging mode based on the rule action: Disabled for Allow actions, and SummaryWithUrls for Block, Warning and Redirect actions | [optional] 
**Status** | **string** | Rule status | 
**Priority** | **int32** | Rule priority. Updated automatically when rules are created/updated | 

## Methods

### NewAccessPolicyRule

`func NewAccessPolicyRule(name string, appliedOn string, action string, conditions []Condition, destinations []AccessPolicyDestination, sources []AccessPolicySource, status string, priority int32, ) *AccessPolicyRule`

NewAccessPolicyRule instantiates a new AccessPolicyRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccessPolicyRuleWithDefaults

`func NewAccessPolicyRuleWithDefaults() *AccessPolicyRule`

NewAccessPolicyRuleWithDefaults instantiates a new AccessPolicyRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AccessPolicyRule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AccessPolicyRule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AccessPolicyRule) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *AccessPolicyRule) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *AccessPolicyRule) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AccessPolicyRule) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AccessPolicyRule) SetName(v string)`

SetName sets Name field to given value.


### GetAppliedOn

`func (o *AccessPolicyRule) GetAppliedOn() string`

GetAppliedOn returns the AppliedOn field if non-nil, zero value otherwise.

### GetAppliedOnOk

`func (o *AccessPolicyRule) GetAppliedOnOk() (*string, bool)`

GetAppliedOnOk returns a tuple with the AppliedOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppliedOn

`func (o *AccessPolicyRule) SetAppliedOn(v string)`

SetAppliedOn sets AppliedOn field to given value.


### GetAction

`func (o *AccessPolicyRule) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *AccessPolicyRule) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *AccessPolicyRule) SetAction(v string)`

SetAction sets Action field to given value.


### GetRedirectUrl

`func (o *AccessPolicyRule) GetRedirectUrl() string`

GetRedirectUrl returns the RedirectUrl field if non-nil, zero value otherwise.

### GetRedirectUrlOk

`func (o *AccessPolicyRule) GetRedirectUrlOk() (*string, bool)`

GetRedirectUrlOk returns a tuple with the RedirectUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUrl

`func (o *AccessPolicyRule) SetRedirectUrl(v string)`

SetRedirectUrl sets RedirectUrl field to given value.

### HasRedirectUrl

`func (o *AccessPolicyRule) HasRedirectUrl() bool`

HasRedirectUrl returns a boolean if a field has been set.

### GetRedirectAction

`func (o *AccessPolicyRule) GetRedirectAction() string`

GetRedirectAction returns the RedirectAction field if non-nil, zero value otherwise.

### GetRedirectActionOk

`func (o *AccessPolicyRule) GetRedirectActionOk() (*string, bool)`

GetRedirectActionOk returns a tuple with the RedirectAction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectAction

`func (o *AccessPolicyRule) SetRedirectAction(v string)`

SetRedirectAction sets RedirectAction field to given value.

### HasRedirectAction

`func (o *AccessPolicyRule) HasRedirectAction() bool`

HasRedirectAction returns a boolean if a field has been set.

### GetConditions

`func (o *AccessPolicyRule) GetConditions() []Condition`

GetConditions returns the Conditions field if non-nil, zero value otherwise.

### GetConditionsOk

`func (o *AccessPolicyRule) GetConditionsOk() (*[]Condition, bool)`

GetConditionsOk returns a tuple with the Conditions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConditions

`func (o *AccessPolicyRule) SetConditions(v []Condition)`

SetConditions sets Conditions field to given value.


### GetDestinations

`func (o *AccessPolicyRule) GetDestinations() []AccessPolicyDestination`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *AccessPolicyRule) GetDestinationsOk() (*[]AccessPolicyDestination, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *AccessPolicyRule) SetDestinations(v []AccessPolicyDestination)`

SetDestinations sets Destinations field to given value.


### GetSources

`func (o *AccessPolicyRule) GetSources() []AccessPolicySource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *AccessPolicyRule) GetSourcesOk() (*[]AccessPolicySource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *AccessPolicyRule) SetSources(v []AccessPolicySource)`

SetSources sets Sources field to given value.


### GetLog

`func (o *AccessPolicyRule) GetLog() string`

GetLog returns the Log field if non-nil, zero value otherwise.

### GetLogOk

`func (o *AccessPolicyRule) GetLogOk() (*string, bool)`

GetLogOk returns a tuple with the Log field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLog

`func (o *AccessPolicyRule) SetLog(v string)`

SetLog sets Log field to given value.

### HasLog

`func (o *AccessPolicyRule) HasLog() bool`

HasLog returns a boolean if a field has been set.

### GetStatus

`func (o *AccessPolicyRule) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *AccessPolicyRule) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *AccessPolicyRule) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetPriority

`func (o *AccessPolicyRule) GetPriority() int32`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *AccessPolicyRule) GetPriorityOk() (*int32, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *AccessPolicyRule) SetPriority(v int32)`

SetPriority sets Priority field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


