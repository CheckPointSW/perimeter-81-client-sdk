# GetUpdatableObjects200ResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to [**GetUpdatableObjects200ResponseDataInnerType**](GetUpdatableObjects200ResponseDataInnerType.md) |  | [optional] 
**CpId** | Pointer to **string** | Check Point object ID | [optional] 
**VendorId** | Pointer to **string** | Vendor identifier | [optional] 
**VendorParentId** | Pointer to **string** | Parent vendor identifier for hierarchical relationships | [optional] 
**VendorChildrenIds** | Pointer to **[]string** | Child vendor identifiers | [optional] 
**Name** | Pointer to **string** | Object name | [optional] 
**InheritDescription** | Pointer to **bool** | Whether to inherit description from parent | [optional] 
**InheritInfoText** | Pointer to **bool** | Whether to inherit info text from parent | [optional] 
**InheritInfoUrl** | Pointer to **bool** | Whether to inherit info URL from parent | [optional] 
**DataObjectsCount** | Pointer to **int32** | Number of data objects associated with this updatable object | [optional] 

## Methods

### NewGetUpdatableObjects200ResponseDataInner

`func NewGetUpdatableObjects200ResponseDataInner() *GetUpdatableObjects200ResponseDataInner`

NewGetUpdatableObjects200ResponseDataInner instantiates a new GetUpdatableObjects200ResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetUpdatableObjects200ResponseDataInnerWithDefaults

`func NewGetUpdatableObjects200ResponseDataInnerWithDefaults() *GetUpdatableObjects200ResponseDataInner`

NewGetUpdatableObjects200ResponseDataInnerWithDefaults instantiates a new GetUpdatableObjects200ResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *GetUpdatableObjects200ResponseDataInner) GetType() GetUpdatableObjects200ResponseDataInnerType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetTypeOk() (*GetUpdatableObjects200ResponseDataInnerType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *GetUpdatableObjects200ResponseDataInner) SetType(v GetUpdatableObjects200ResponseDataInnerType)`

SetType sets Type field to given value.

### HasType

`func (o *GetUpdatableObjects200ResponseDataInner) HasType() bool`

HasType returns a boolean if a field has been set.

### GetCpId

`func (o *GetUpdatableObjects200ResponseDataInner) GetCpId() string`

GetCpId returns the CpId field if non-nil, zero value otherwise.

### GetCpIdOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetCpIdOk() (*string, bool)`

GetCpIdOk returns a tuple with the CpId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCpId

`func (o *GetUpdatableObjects200ResponseDataInner) SetCpId(v string)`

SetCpId sets CpId field to given value.

### HasCpId

`func (o *GetUpdatableObjects200ResponseDataInner) HasCpId() bool`

HasCpId returns a boolean if a field has been set.

### GetVendorId

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorId() string`

GetVendorId returns the VendorId field if non-nil, zero value otherwise.

### GetVendorIdOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorIdOk() (*string, bool)`

GetVendorIdOk returns a tuple with the VendorId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVendorId

`func (o *GetUpdatableObjects200ResponseDataInner) SetVendorId(v string)`

SetVendorId sets VendorId field to given value.

### HasVendorId

`func (o *GetUpdatableObjects200ResponseDataInner) HasVendorId() bool`

HasVendorId returns a boolean if a field has been set.

### GetVendorParentId

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorParentId() string`

GetVendorParentId returns the VendorParentId field if non-nil, zero value otherwise.

### GetVendorParentIdOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorParentIdOk() (*string, bool)`

GetVendorParentIdOk returns a tuple with the VendorParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVendorParentId

`func (o *GetUpdatableObjects200ResponseDataInner) SetVendorParentId(v string)`

SetVendorParentId sets VendorParentId field to given value.

### HasVendorParentId

`func (o *GetUpdatableObjects200ResponseDataInner) HasVendorParentId() bool`

HasVendorParentId returns a boolean if a field has been set.

### GetVendorChildrenIds

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorChildrenIds() []string`

GetVendorChildrenIds returns the VendorChildrenIds field if non-nil, zero value otherwise.

### GetVendorChildrenIdsOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetVendorChildrenIdsOk() (*[]string, bool)`

GetVendorChildrenIdsOk returns a tuple with the VendorChildrenIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVendorChildrenIds

`func (o *GetUpdatableObjects200ResponseDataInner) SetVendorChildrenIds(v []string)`

SetVendorChildrenIds sets VendorChildrenIds field to given value.

### HasVendorChildrenIds

`func (o *GetUpdatableObjects200ResponseDataInner) HasVendorChildrenIds() bool`

HasVendorChildrenIds returns a boolean if a field has been set.

### GetName

`func (o *GetUpdatableObjects200ResponseDataInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetUpdatableObjects200ResponseDataInner) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *GetUpdatableObjects200ResponseDataInner) HasName() bool`

HasName returns a boolean if a field has been set.

### GetInheritDescription

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritDescription() bool`

GetInheritDescription returns the InheritDescription field if non-nil, zero value otherwise.

### GetInheritDescriptionOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritDescriptionOk() (*bool, bool)`

GetInheritDescriptionOk returns a tuple with the InheritDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritDescription

`func (o *GetUpdatableObjects200ResponseDataInner) SetInheritDescription(v bool)`

SetInheritDescription sets InheritDescription field to given value.

### HasInheritDescription

`func (o *GetUpdatableObjects200ResponseDataInner) HasInheritDescription() bool`

HasInheritDescription returns a boolean if a field has been set.

### GetInheritInfoText

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritInfoText() bool`

GetInheritInfoText returns the InheritInfoText field if non-nil, zero value otherwise.

### GetInheritInfoTextOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritInfoTextOk() (*bool, bool)`

GetInheritInfoTextOk returns a tuple with the InheritInfoText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritInfoText

`func (o *GetUpdatableObjects200ResponseDataInner) SetInheritInfoText(v bool)`

SetInheritInfoText sets InheritInfoText field to given value.

### HasInheritInfoText

`func (o *GetUpdatableObjects200ResponseDataInner) HasInheritInfoText() bool`

HasInheritInfoText returns a boolean if a field has been set.

### GetInheritInfoUrl

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritInfoUrl() bool`

GetInheritInfoUrl returns the InheritInfoUrl field if non-nil, zero value otherwise.

### GetInheritInfoUrlOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetInheritInfoUrlOk() (*bool, bool)`

GetInheritInfoUrlOk returns a tuple with the InheritInfoUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInheritInfoUrl

`func (o *GetUpdatableObjects200ResponseDataInner) SetInheritInfoUrl(v bool)`

SetInheritInfoUrl sets InheritInfoUrl field to given value.

### HasInheritInfoUrl

`func (o *GetUpdatableObjects200ResponseDataInner) HasInheritInfoUrl() bool`

HasInheritInfoUrl returns a boolean if a field has been set.

### GetDataObjectsCount

`func (o *GetUpdatableObjects200ResponseDataInner) GetDataObjectsCount() int32`

GetDataObjectsCount returns the DataObjectsCount field if non-nil, zero value otherwise.

### GetDataObjectsCountOk

`func (o *GetUpdatableObjects200ResponseDataInner) GetDataObjectsCountOk() (*int32, bool)`

GetDataObjectsCountOk returns a tuple with the DataObjectsCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataObjectsCount

`func (o *GetUpdatableObjects200ResponseDataInner) SetDataObjectsCount(v int32)`

SetDataObjectsCount sets DataObjectsCount field to given value.

### HasDataObjectsCount

`func (o *GetUpdatableObjects200ResponseDataInner) HasDataObjectsCount() bool`

HasDataObjectsCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


