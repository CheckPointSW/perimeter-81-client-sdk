# PermissionCategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | Pointer to **string** | Category slug identifier (e.g. &#39;network_deployment&#39;) | [optional] 
**DisplayName** | **string** |  | 
**GroupName** | Pointer to **string** | Parent group slug (e.g. &#39;network&#39;, &#39;system_management&#39;) | [optional] 
**GroupDisplayName** | **string** |  | 
**GroupSortOrder** | **int32** |  | 
**SortOrder** | **int32** |  | 
**ReadPermissions** | **[]string** |  | 
**ManagePermissions** | **[]string** |  | 

## Methods

### NewPermissionCategory

`func NewPermissionCategory(id string, displayName string, groupDisplayName string, groupSortOrder int32, sortOrder int32, readPermissions []string, managePermissions []string, ) *PermissionCategory`

NewPermissionCategory instantiates a new PermissionCategory object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPermissionCategoryWithDefaults

`func NewPermissionCategoryWithDefaults() *PermissionCategory`

NewPermissionCategoryWithDefaults instantiates a new PermissionCategory object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PermissionCategory) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PermissionCategory) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PermissionCategory) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *PermissionCategory) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PermissionCategory) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PermissionCategory) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PermissionCategory) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDisplayName

`func (o *PermissionCategory) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *PermissionCategory) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *PermissionCategory) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### GetGroupName

`func (o *PermissionCategory) GetGroupName() string`

GetGroupName returns the GroupName field if non-nil, zero value otherwise.

### GetGroupNameOk

`func (o *PermissionCategory) GetGroupNameOk() (*string, bool)`

GetGroupNameOk returns a tuple with the GroupName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupName

`func (o *PermissionCategory) SetGroupName(v string)`

SetGroupName sets GroupName field to given value.

### HasGroupName

`func (o *PermissionCategory) HasGroupName() bool`

HasGroupName returns a boolean if a field has been set.

### GetGroupDisplayName

`func (o *PermissionCategory) GetGroupDisplayName() string`

GetGroupDisplayName returns the GroupDisplayName field if non-nil, zero value otherwise.

### GetGroupDisplayNameOk

`func (o *PermissionCategory) GetGroupDisplayNameOk() (*string, bool)`

GetGroupDisplayNameOk returns a tuple with the GroupDisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupDisplayName

`func (o *PermissionCategory) SetGroupDisplayName(v string)`

SetGroupDisplayName sets GroupDisplayName field to given value.


### GetGroupSortOrder

`func (o *PermissionCategory) GetGroupSortOrder() int32`

GetGroupSortOrder returns the GroupSortOrder field if non-nil, zero value otherwise.

### GetGroupSortOrderOk

`func (o *PermissionCategory) GetGroupSortOrderOk() (*int32, bool)`

GetGroupSortOrderOk returns a tuple with the GroupSortOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupSortOrder

`func (o *PermissionCategory) SetGroupSortOrder(v int32)`

SetGroupSortOrder sets GroupSortOrder field to given value.


### GetSortOrder

`func (o *PermissionCategory) GetSortOrder() int32`

GetSortOrder returns the SortOrder field if non-nil, zero value otherwise.

### GetSortOrderOk

`func (o *PermissionCategory) GetSortOrderOk() (*int32, bool)`

GetSortOrderOk returns a tuple with the SortOrder field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSortOrder

`func (o *PermissionCategory) SetSortOrder(v int32)`

SetSortOrder sets SortOrder field to given value.


### GetReadPermissions

`func (o *PermissionCategory) GetReadPermissions() []string`

GetReadPermissions returns the ReadPermissions field if non-nil, zero value otherwise.

### GetReadPermissionsOk

`func (o *PermissionCategory) GetReadPermissionsOk() (*[]string, bool)`

GetReadPermissionsOk returns a tuple with the ReadPermissions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReadPermissions

`func (o *PermissionCategory) SetReadPermissions(v []string)`

SetReadPermissions sets ReadPermissions field to given value.


### GetManagePermissions

`func (o *PermissionCategory) GetManagePermissions() []string`

GetManagePermissions returns the ManagePermissions field if non-nil, zero value otherwise.

### GetManagePermissionsOk

`func (o *PermissionCategory) GetManagePermissionsOk() (*[]string, bool)`

GetManagePermissionsOk returns a tuple with the ManagePermissions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManagePermissions

`func (o *PermissionCategory) SetManagePermissions(v []string)`

SetManagePermissions sets ManagePermissions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


