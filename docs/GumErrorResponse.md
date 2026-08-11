# GumErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Body** | Pointer to **string** | Error message. | [optional] 
**StatusCode** | Pointer to **int32** | HTTP status code. | [optional] 

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

### GetBody

`func (o *GumErrorResponse) GetBody() string`

GetBody returns the Body field if non-nil, zero value otherwise.

### GetBodyOk

`func (o *GumErrorResponse) GetBodyOk() (*string, bool)`

GetBodyOk returns a tuple with the Body field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBody

`func (o *GumErrorResponse) SetBody(v string)`

SetBody sets Body field to given value.

### HasBody

`func (o *GumErrorResponse) HasBody() bool`

HasBody returns a boolean if a field has been set.

### GetStatusCode

`func (o *GumErrorResponse) GetStatusCode() int32`

GetStatusCode returns the StatusCode field if non-nil, zero value otherwise.

### GetStatusCodeOk

`func (o *GumErrorResponse) GetStatusCodeOk() (*int32, bool)`

GetStatusCodeOk returns a tuple with the StatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCode

`func (o *GumErrorResponse) SetStatusCode(v int32)`

SetStatusCode sets StatusCode field to given value.

### HasStatusCode

`func (o *GumErrorResponse) HasStatusCode() bool`

HasStatusCode returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


