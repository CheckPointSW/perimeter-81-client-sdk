# FileAccessSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Users** | Pointer to **[]string** | Array of user IDs | [optional] 
**Groups** | Pointer to **[]string** | Array of group IDs | [optional] 

## Methods

### NewFileAccessSource

`func NewFileAccessSource() *FileAccessSource`

NewFileAccessSource instantiates a new FileAccessSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileAccessSourceWithDefaults

`func NewFileAccessSourceWithDefaults() *FileAccessSource`

NewFileAccessSourceWithDefaults instantiates a new FileAccessSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUsers

`func (o *FileAccessSource) GetUsers() []string`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *FileAccessSource) GetUsersOk() (*[]string, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *FileAccessSource) SetUsers(v []string)`

SetUsers sets Users field to given value.

### HasUsers

`func (o *FileAccessSource) HasUsers() bool`

HasUsers returns a boolean if a field has been set.

### GetGroups

`func (o *FileAccessSource) GetGroups() []string`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *FileAccessSource) GetGroupsOk() (*[]string, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *FileAccessSource) SetGroups(v []string)`

SetGroups sets Groups field to given value.

### HasGroups

`func (o *FileAccessSource) HasGroups() bool`

HasGroups returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


