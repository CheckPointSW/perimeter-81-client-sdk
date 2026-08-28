# UpdateAccessPolicyRulesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **int32** |  | [optional] 
**Data** | Pointer to [**AccessPolicyRulesGetResponseData**](AccessPolicyRulesGetResponseData.md) |  | [optional] 

## Methods

### NewUpdateAccessPolicyRulesResponse

`func NewUpdateAccessPolicyRulesResponse() *UpdateAccessPolicyRulesResponse`

NewUpdateAccessPolicyRulesResponse instantiates a new UpdateAccessPolicyRulesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateAccessPolicyRulesResponseWithDefaults

`func NewUpdateAccessPolicyRulesResponseWithDefaults() *UpdateAccessPolicyRulesResponse`

NewUpdateAccessPolicyRulesResponseWithDefaults instantiates a new UpdateAccessPolicyRulesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *UpdateAccessPolicyRulesResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateAccessPolicyRulesResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateAccessPolicyRulesResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateAccessPolicyRulesResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetData

`func (o *UpdateAccessPolicyRulesResponse) GetData() AccessPolicyRulesGetResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *UpdateAccessPolicyRulesResponse) GetDataOk() (*AccessPolicyRulesGetResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *UpdateAccessPolicyRulesResponse) SetData(v AccessPolicyRulesGetResponseData)`

SetData sets Data field to given value.

### HasData

`func (o *UpdateAccessPolicyRulesResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


