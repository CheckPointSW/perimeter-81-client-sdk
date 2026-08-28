# IAErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | Pointer to **int32** | HTTP status code (e.g., 422, 500, 403) | [optional] 
**Code** | Pointer to **int32** | Same as status | [optional] 
**Message** | Pointer to **string** | Error message or message code | [optional] 
**MessageCode** | Pointer to **string** | Standardized error code constant | [optional] 
**IsP81Error** | Pointer to **bool** | The marker flag | [optional] 
**TenantId** | Pointer to **string** | Tenant ID (optional) | [optional] 
**AccountId** | Pointer to **string** | Account ID (optional) | [optional] 
**UserId** | Pointer to **string** | User ID (optional) | [optional] 
**Data** | Pointer to [**IAErrorResponseData**](IAErrorResponseData.md) |  | [optional] 

## Methods

### NewIAErrorResponse

`func NewIAErrorResponse() *IAErrorResponse`

NewIAErrorResponse instantiates a new IAErrorResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIAErrorResponseWithDefaults

`func NewIAErrorResponseWithDefaults() *IAErrorResponse`

NewIAErrorResponseWithDefaults instantiates a new IAErrorResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *IAErrorResponse) GetStatus() int32`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *IAErrorResponse) GetStatusOk() (*int32, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *IAErrorResponse) SetStatus(v int32)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *IAErrorResponse) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetCode

`func (o *IAErrorResponse) GetCode() int32`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *IAErrorResponse) GetCodeOk() (*int32, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *IAErrorResponse) SetCode(v int32)`

SetCode sets Code field to given value.

### HasCode

`func (o *IAErrorResponse) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetMessage

`func (o *IAErrorResponse) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *IAErrorResponse) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *IAErrorResponse) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *IAErrorResponse) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetMessageCode

`func (o *IAErrorResponse) GetMessageCode() string`

GetMessageCode returns the MessageCode field if non-nil, zero value otherwise.

### GetMessageCodeOk

`func (o *IAErrorResponse) GetMessageCodeOk() (*string, bool)`

GetMessageCodeOk returns a tuple with the MessageCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageCode

`func (o *IAErrorResponse) SetMessageCode(v string)`

SetMessageCode sets MessageCode field to given value.

### HasMessageCode

`func (o *IAErrorResponse) HasMessageCode() bool`

HasMessageCode returns a boolean if a field has been set.

### GetIsP81Error

`func (o *IAErrorResponse) GetIsP81Error() bool`

GetIsP81Error returns the IsP81Error field if non-nil, zero value otherwise.

### GetIsP81ErrorOk

`func (o *IAErrorResponse) GetIsP81ErrorOk() (*bool, bool)`

GetIsP81ErrorOk returns a tuple with the IsP81Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsP81Error

`func (o *IAErrorResponse) SetIsP81Error(v bool)`

SetIsP81Error sets IsP81Error field to given value.

### HasIsP81Error

`func (o *IAErrorResponse) HasIsP81Error() bool`

HasIsP81Error returns a boolean if a field has been set.

### GetTenantId

`func (o *IAErrorResponse) GetTenantId() string`

GetTenantId returns the TenantId field if non-nil, zero value otherwise.

### GetTenantIdOk

`func (o *IAErrorResponse) GetTenantIdOk() (*string, bool)`

GetTenantIdOk returns a tuple with the TenantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenantId

`func (o *IAErrorResponse) SetTenantId(v string)`

SetTenantId sets TenantId field to given value.

### HasTenantId

`func (o *IAErrorResponse) HasTenantId() bool`

HasTenantId returns a boolean if a field has been set.

### GetAccountId

`func (o *IAErrorResponse) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *IAErrorResponse) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *IAErrorResponse) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.

### HasAccountId

`func (o *IAErrorResponse) HasAccountId() bool`

HasAccountId returns a boolean if a field has been set.

### GetUserId

`func (o *IAErrorResponse) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *IAErrorResponse) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *IAErrorResponse) SetUserId(v string)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *IAErrorResponse) HasUserId() bool`

HasUserId returns a boolean if a field has been set.

### GetData

`func (o *IAErrorResponse) GetData() IAErrorResponseData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *IAErrorResponse) GetDataOk() (*IAErrorResponseData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *IAErrorResponse) SetData(v IAErrorResponseData)`

SetData sets Data field to given value.

### HasData

`func (o *IAErrorResponse) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


