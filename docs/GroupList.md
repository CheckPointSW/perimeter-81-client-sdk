# GroupList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | [**[]Group**](Group.md) | List of groups. | 
**Page** | **int32** | Page number. | 
**TotalPage** | **int32** | Total pages in list. | 
**ItemsTotal** | **int32** | Items in total. | 

## Methods

### NewGroupList

`func NewGroupList(data []Group, page int32, totalPage int32, itemsTotal int32, ) *GroupList`

NewGroupList instantiates a new GroupList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGroupListWithDefaults

`func NewGroupListWithDefaults() *GroupList`

NewGroupListWithDefaults instantiates a new GroupList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetData

`func (o *GroupList) GetData() []Group`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *GroupList) GetDataOk() (*[]Group, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *GroupList) SetData(v []Group)`

SetData sets Data field to given value.


### GetPage

`func (o *GroupList) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *GroupList) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *GroupList) SetPage(v int32)`

SetPage sets Page field to given value.


### GetTotalPage

`func (o *GroupList) GetTotalPage() int32`

GetTotalPage returns the TotalPage field if non-nil, zero value otherwise.

### GetTotalPageOk

`func (o *GroupList) GetTotalPageOk() (*int32, bool)`

GetTotalPageOk returns a tuple with the TotalPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPage

`func (o *GroupList) SetTotalPage(v int32)`

SetTotalPage sets TotalPage field to given value.


### GetItemsTotal

`func (o *GroupList) GetItemsTotal() int32`

GetItemsTotal returns the ItemsTotal field if non-nil, zero value otherwise.

### GetItemsTotalOk

`func (o *GroupList) GetItemsTotalOk() (*int32, bool)`

GetItemsTotalOk returns a tuple with the ItemsTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemsTotal

`func (o *GroupList) SetItemsTotal(v int32)`

SetItemsTotal sets ItemsTotal field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


