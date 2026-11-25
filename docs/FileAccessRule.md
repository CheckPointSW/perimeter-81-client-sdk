# FileAccessRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Rule ID (optional in requests, auto-generated for new rules) | [optional] 
**Name** | **string** | Rule name | 
**Status** | **string** | Rule status | 
**Priority** | **int32** | Rule priority. Updated automatically when rules are created/updated | 
**Action** | **string** | Rule action | 
**Activity** | **[]string** | Activities this rule applies to (at least one required) | 
**Sources** | [**FileAccessSource**](FileAccessSource.md) |  | 
**Destinations** | [**FileAccessDestination**](FileAccessDestination.md) |  | 
**FileConstraints** | [**[]FileAccessConstraint**](FileAccessConstraint.md) | File constraints (empty array means any file) | 

## Methods

### NewFileAccessRule

`func NewFileAccessRule(name string, status string, priority int32, action string, activity []string, sources FileAccessSource, destinations FileAccessDestination, fileConstraints []FileAccessConstraint, ) *FileAccessRule`

NewFileAccessRule instantiates a new FileAccessRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileAccessRuleWithDefaults

`func NewFileAccessRuleWithDefaults() *FileAccessRule`

NewFileAccessRuleWithDefaults instantiates a new FileAccessRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FileAccessRule) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FileAccessRule) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FileAccessRule) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *FileAccessRule) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *FileAccessRule) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *FileAccessRule) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *FileAccessRule) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *FileAccessRule) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *FileAccessRule) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *FileAccessRule) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetPriority

`func (o *FileAccessRule) GetPriority() int32`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *FileAccessRule) GetPriorityOk() (*int32, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *FileAccessRule) SetPriority(v int32)`

SetPriority sets Priority field to given value.


### GetAction

`func (o *FileAccessRule) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *FileAccessRule) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *FileAccessRule) SetAction(v string)`

SetAction sets Action field to given value.


### GetActivity

`func (o *FileAccessRule) GetActivity() []string`

GetActivity returns the Activity field if non-nil, zero value otherwise.

### GetActivityOk

`func (o *FileAccessRule) GetActivityOk() (*[]string, bool)`

GetActivityOk returns a tuple with the Activity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivity

`func (o *FileAccessRule) SetActivity(v []string)`

SetActivity sets Activity field to given value.


### GetSources

`func (o *FileAccessRule) GetSources() FileAccessSource`

GetSources returns the Sources field if non-nil, zero value otherwise.

### GetSourcesOk

`func (o *FileAccessRule) GetSourcesOk() (*FileAccessSource, bool)`

GetSourcesOk returns a tuple with the Sources field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSources

`func (o *FileAccessRule) SetSources(v FileAccessSource)`

SetSources sets Sources field to given value.


### GetDestinations

`func (o *FileAccessRule) GetDestinations() FileAccessDestination`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *FileAccessRule) GetDestinationsOk() (*FileAccessDestination, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *FileAccessRule) SetDestinations(v FileAccessDestination)`

SetDestinations sets Destinations field to given value.


### GetFileConstraints

`func (o *FileAccessRule) GetFileConstraints() []FileAccessConstraint`

GetFileConstraints returns the FileConstraints field if non-nil, zero value otherwise.

### GetFileConstraintsOk

`func (o *FileAccessRule) GetFileConstraintsOk() (*[]FileAccessConstraint, bool)`

GetFileConstraintsOk returns a tuple with the FileConstraints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFileConstraints

`func (o *FileAccessRule) SetFileConstraints(v []FileAccessConstraint)`

SetFileConstraints sets FileConstraints field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


