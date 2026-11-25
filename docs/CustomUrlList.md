# CustomUrlList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | [**[]CustomUrl**](CustomUrl.md) |  | 
**Page** | **int32** | Current page number | 
**TotalPage** | **int32** | Total number of pages | 
**ItemsTotal** | **int32** | Total number of items across all pages | 

## Methods

### NewCustomUrlList

`func NewCustomUrlList(data []CustomUrl, page int32, totalPage int32, itemsTotal int32, ) *CustomUrlList`

NewCustomUrlList instantiates a new CustomUrlList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomUrlListWithDefaults

`func NewCustomUrlListWithDefaults() *CustomUrlList`

NewCustomUrlListWithDefaults instantiates a new CustomUrlList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetData

`func (o *CustomUrlList) GetData() []CustomUrl`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *CustomUrlList) GetDataOk() (*[]CustomUrl, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *CustomUrlList) SetData(v []CustomUrl)`

SetData sets Data field to given value.


### GetPage

`func (o *CustomUrlList) GetPage() int32`

GetPage returns the Page field if non-nil, zero value otherwise.

### GetPageOk

`func (o *CustomUrlList) GetPageOk() (*int32, bool)`

GetPageOk returns a tuple with the Page field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPage

`func (o *CustomUrlList) SetPage(v int32)`

SetPage sets Page field to given value.


### GetTotalPage

`func (o *CustomUrlList) GetTotalPage() int32`

GetTotalPage returns the TotalPage field if non-nil, zero value otherwise.

### GetTotalPageOk

`func (o *CustomUrlList) GetTotalPageOk() (*int32, bool)`

GetTotalPageOk returns a tuple with the TotalPage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalPage

`func (o *CustomUrlList) SetTotalPage(v int32)`

SetTotalPage sets TotalPage field to given value.


### GetItemsTotal

`func (o *CustomUrlList) GetItemsTotal() int32`

GetItemsTotal returns the ItemsTotal field if non-nil, zero value otherwise.

### GetItemsTotalOk

`func (o *CustomUrlList) GetItemsTotalOk() (*int32, bool)`

GetItemsTotalOk returns a tuple with the ItemsTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemsTotal

`func (o *CustomUrlList) SetItemsTotal(v int32)`

SetItemsTotal sets ItemsTotal field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


