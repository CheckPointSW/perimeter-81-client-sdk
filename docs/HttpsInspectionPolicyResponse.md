# HttpsInspectionPolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **int32** |  | [optional] 
**Data** | Pointer to [**HttpsInspectionPolicyResponseData**](HttpsInspectionPolicyResponseData.md) |  | [optional] 

## Methods

### NewHttpsInspectionPolicyResponse

`func NewHttpsInspectionPolicyResponse() *HttpsInspectionPolicyResponse`

NewHttpsInspectionPolicyResponse instantiates a new HttpsInspectionPolicyResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHttpsInspectionPolicyResponseWithDefaults

`func NewHttpsInspectionPolicyResponseWithDefaults() *HttpsInspectionPolicyResponse`

NewHttpsInspectionPolicyResponseWithDefaults instantiates a new HttpsInspectionPolicyResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *HttpsInspectionPolicyResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *HttpsInspectionPolicyResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *HttpsInspectionPolicyResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *HttpsInspectionPolicyResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetData

`func (o *HttpsInspectionPolicyResponse) GetData() HttpsInspectionPolicyResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *HttpsInspectionPolicyResponse) GetDataOk() (*HttpsInspectionPolicyResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *HttpsInspectionPolicyResponse) SetData(v HttpsInspectionPolicyResponseData)`

SetData sets Data field to given value.

### HasData

`func (o *HttpsInspectionPolicyResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


