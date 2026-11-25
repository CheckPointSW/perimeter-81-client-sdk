# NotificationPagesMessageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **int32** |  | 
**Data** | [**NotificationPagesMessageResponseData**](NotificationPagesMessageResponseData.md) |  | 

## Methods

### NewNotificationPagesMessageResponse

`func NewNotificationPagesMessageResponse(status int32, data NotificationPagesMessageResponseData, ) *NotificationPagesMessageResponse`

NewNotificationPagesMessageResponse instantiates a new NotificationPagesMessageResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNotificationPagesMessageResponseWithDefaults

`func NewNotificationPagesMessageResponseWithDefaults() *NotificationPagesMessageResponse`

NewNotificationPagesMessageResponseWithDefaults instantiates a new NotificationPagesMessageResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *NotificationPagesMessageResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *NotificationPagesMessageResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *NotificationPagesMessageResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.


### GetData

`func (o *NotificationPagesMessageResponse) GetData() NotificationPagesMessageResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *NotificationPagesMessageResponse) GetDataOk() (*NotificationPagesMessageResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *NotificationPagesMessageResponse) SetData(v NotificationPagesMessageResponseData)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


