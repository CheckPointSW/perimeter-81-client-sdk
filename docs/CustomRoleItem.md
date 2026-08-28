# CustomRoleItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Categories** | [**[]CategoryEntry**](CategoryEntry.md) |  | 
**CPRoleId** | Pointer to **string** | Identifier of the associated CPM role (pending value until role creation in CPM completes) | [optional] 
**CreatedAt** | Pointer to **time.Time** |  | [optional] 
**UpdatedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewCustomRoleItem

`func NewCustomRoleItem(id string, name string, categories []CategoryEntry, ) *CustomRoleItem`

NewCustomRoleItem instantiates a new CustomRoleItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomRoleItemWithDefaults

`func NewCustomRoleItemWithDefaults() *CustomRoleItem`

NewCustomRoleItemWithDefaults instantiates a new CustomRoleItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CustomRoleItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CustomRoleItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CustomRoleItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *CustomRoleItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CustomRoleItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CustomRoleItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CustomRoleItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CustomRoleItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CustomRoleItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CustomRoleItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCategories

`func (o *CustomRoleItem) GetCategories() []CategoryEntry`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *CustomRoleItem) GetCategoriesOk() (*[]CategoryEntry, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *CustomRoleItem) SetCategories(v []CategoryEntry)`

SetCategories sets Categories field to given value.


### GetCPRoleId

`func (o *CustomRoleItem) GetCPRoleId() string`

GetCPRoleId returns the CPRoleId field if non-nil, zero value otherwise.

### GetCPRoleIdOk

`func (o *CustomRoleItem) GetCPRoleIdOk() (*string, bool)`

GetCPRoleIdOk returns a tuple with the CPRoleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCPRoleId

`func (o *CustomRoleItem) SetCPRoleId(v string)`

SetCPRoleId sets CPRoleId field to given value.

### HasCPRoleId

`func (o *CustomRoleItem) HasCPRoleId() bool`

HasCPRoleId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *CustomRoleItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CustomRoleItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CustomRoleItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *CustomRoleItem) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *CustomRoleItem) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CustomRoleItem) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CustomRoleItem) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *CustomRoleItem) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


