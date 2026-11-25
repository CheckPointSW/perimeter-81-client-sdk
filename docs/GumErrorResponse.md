# GumErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | Pointer to **string** | Human-readable error message. | [optional] 
**MessageCode** | Pointer to **string** | Stable machine-readable error code — one of INTERNAL_SERVER_ERROR, BAD_REQUEST, NOT_IMPLEMENTED_ERROR, NOT_FOUND, VALIDATION_SCHEMA_ERROR, PRECONDITION_FAILED, CONFLICT, UNAUTHORIZED. Mirrors common/src/libs/exceptions/ErrorCodes.ts, which is the source of truth; these values are a caller-visible contract. | [optional] 

## Methods

### NewGumErrorResponse

`func NewGumErrorResponse() *GumErrorResponse`

NewGumErrorResponse instantiates a new GumErrorResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGumErrorResponseWithDefaults

`func NewGumErrorResponseWithDefaults() *GumErrorResponse`

NewGumErrorResponseWithDefaults instantiates a new GumErrorResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *GumErrorResponse) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *GumErrorResponse) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *GumErrorResponse) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *GumErrorResponse) HasMessage() bool`

HasMessage returns a boolean if a field has been set.

### GetMessageCode

`func (o *GumErrorResponse) GetMessageCode() string`

GetMessageCode returns the MessageCode field if non-nil, zero value otherwise.

### GetMessageCodeOk

`func (o *GumErrorResponse) GetMessageCodeOk() (*string, bool)`

GetMessageCodeOk returns a tuple with the MessageCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageCode

`func (o *GumErrorResponse) SetMessageCode(v string)`

SetMessageCode sets MessageCode field to given value.

### HasMessageCode

`func (o *GumErrorResponse) HasMessageCode() bool`

HasMessageCode returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


