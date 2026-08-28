# ApplicationControlResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **int32** |  | [optional] 
**Data** | Pointer to [**[]ApplicationControlApplication**](ApplicationControlApplication.md) |  | [optional] 

## Methods

### NewApplicationControlResponse

`func NewApplicationControlResponse() *ApplicationControlResponse`

NewApplicationControlResponse instantiates a new ApplicationControlResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApplicationControlResponseWithDefaults

`func NewApplicationControlResponseWithDefaults() *ApplicationControlResponse`

NewApplicationControlResponseWithDefaults instantiates a new ApplicationControlResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *ApplicationControlResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ApplicationControlResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ApplicationControlResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ApplicationControlResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetData

`func (o *ApplicationControlResponse) GetData() []ApplicationControlApplication`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ApplicationControlResponse) GetDataOk() (*[]ApplicationControlApplication, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ApplicationControlResponse) SetData(v []ApplicationControlApplication)`

SetData sets Data field to given value.

### HasData

`func (o *ApplicationControlResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


