# GumCreateCustomRoleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Categories** | [**[]CategoryEntry**](CategoryEntry.md) |  | 

## Methods

### NewGumCreateCustomRoleRequest

`func NewGumCreateCustomRoleRequest(name string, categories []CategoryEntry, ) *GumCreateCustomRoleRequest`

NewGumCreateCustomRoleRequest instantiates a new GumCreateCustomRoleRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGumCreateCustomRoleRequestWithDefaults

`func NewGumCreateCustomRoleRequestWithDefaults() *GumCreateCustomRoleRequest`

NewGumCreateCustomRoleRequestWithDefaults instantiates a new GumCreateCustomRoleRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *GumCreateCustomRoleRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GumCreateCustomRoleRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GumCreateCustomRoleRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *GumCreateCustomRoleRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *GumCreateCustomRoleRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *GumCreateCustomRoleRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *GumCreateCustomRoleRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetCategories

`func (o *GumCreateCustomRoleRequest) GetCategories() []CategoryEntry`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *GumCreateCustomRoleRequest) GetCategoriesOk() (*[]CategoryEntry, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *GumCreateCustomRoleRequest) SetCategories(v []CategoryEntry)`

SetCategories sets Categories field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


