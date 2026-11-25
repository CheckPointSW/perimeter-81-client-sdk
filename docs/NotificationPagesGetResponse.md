# NotificationPagesGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **int32** |  | 
**Data** | [**NotificationPagesGetResponseData**](NotificationPagesGetResponseData.md) |  | 

## Methods

### NewNotificationPagesGetResponse

`func NewNotificationPagesGetResponse(status int32, data NotificationPagesGetResponseData, ) *NotificationPagesGetResponse`

NewNotificationPagesGetResponse instantiates a new NotificationPagesGetResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNotificationPagesGetResponseWithDefaults

`func NewNotificationPagesGetResponseWithDefaults() *NotificationPagesGetResponse`

NewNotificationPagesGetResponseWithDefaults instantiates a new NotificationPagesGetResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *NotificationPagesGetResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *NotificationPagesGetResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *NotificationPagesGetResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.


### GetData

`func (o *NotificationPagesGetResponse) GetData() NotificationPagesGetResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *NotificationPagesGetResponse) GetDataOk() (*NotificationPagesGetResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *NotificationPagesGetResponse) SetData(v NotificationPagesGetResponseData)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


