# WebCategory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Web Category ID | 
**Name** | **string** | Web Category name | 
**Codes** | Pointer to **[]string** | Web Category code identifiers | [optional] 

## Methods

### NewWebCategory

`func NewWebCategory(id string, name string, ) *WebCategory`

NewWebCategory instantiates a new WebCategory object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebCategoryWithDefaults

`func NewWebCategoryWithDefaults() *WebCategory`

NewWebCategoryWithDefaults instantiates a new WebCategory object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WebCategory) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WebCategory) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WebCategory) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *WebCategory) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *WebCategory) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *WebCategory) SetName(v string)`

SetName sets Name field to given value.


### GetCodes

`func (o *WebCategory) GetCodes() []string`

GetCodes returns the Codes field if non-nil, zero value otherwise.

### GetCodesOk

`func (o *WebCategory) GetCodesOk() (*[]string, bool)`

GetCodesOk returns a tuple with the Codes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodes

`func (o *WebCategory) SetCodes(v []string)`

SetCodes sets Codes field to given value.

### HasCodes

`func (o *WebCategory) HasCodes() bool`

HasCodes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


