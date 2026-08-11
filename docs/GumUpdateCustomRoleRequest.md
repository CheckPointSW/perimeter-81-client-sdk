# GumUpdateCustomRoleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** |  | [optional] 
**Description** | Pointer to **string** |  | [optional] 
**Categories** | Pointer to [**[]CategoryEntry**](CategoryEntry.md) |  | [optional] 

## Methods

### NewGumUpdateCustomRoleRequest

`func NewGumUpdateCustomRoleRequest() *GumUpdateCustomRoleRequest`

NewGumUpdateCustomRoleRequest instantiates a new GumUpdateCustomRoleRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGumUpdateCustomRoleRequestWithDefaults

`func NewGumUpdateCustomRoleRequestWithDefaults() *GumUpdateCustomRoleRequest`

NewGumUpdateCustomRoleRequestWithDefaults instantiates a new GumUpdateCustomRoleRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *GumUpdateCustomRoleRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GumUpdateCustomRoleRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GumUpdateCustomRoleRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *GumUpdateCustomRoleRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *GumUpdateCustomRoleRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *GumUpdateCustomRoleRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *GumUpdateCustomRoleRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *GumUpdateCustomRoleRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCategories

`func (o *GumUpdateCustomRoleRequest) GetCategories() []CategoryEntry`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *GumUpdateCustomRoleRequest) GetCategoriesOk() (*[]CategoryEntry, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *GumUpdateCustomRoleRequest) SetCategories(v []CategoryEntry)`

SetCategories sets Categories field to given value.

### HasCategories

`func (o *GumUpdateCustomRoleRequest) HasCategories() bool`

HasCategories returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


