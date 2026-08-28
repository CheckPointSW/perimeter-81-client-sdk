# DnsPolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Public** | Pointer to [**DnsPolicyPublic**](DnsPolicyPublic.md) |  | [optional] 
**Private** | Pointer to [**DnsPolicyResponseAllOfPrivate**](DnsPolicyResponseAllOfPrivate.md) |  | [optional] 

## Methods

### NewDnsPolicyResponse

`func NewDnsPolicyResponse() *DnsPolicyResponse`

NewDnsPolicyResponse instantiates a new DnsPolicyResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDnsPolicyResponseWithDefaults

`func NewDnsPolicyResponseWithDefaults() *DnsPolicyResponse`

NewDnsPolicyResponseWithDefaults instantiates a new DnsPolicyResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPublic

`func (o *DnsPolicyResponse) GetPublic() DnsPolicyPublic`

GetPublic returns the Public field if non-nil, zero value otherwise.

### GetPublicOk

`func (o *DnsPolicyResponse) GetPublicOk() (*DnsPolicyPublic, bool)`

GetPublicOk returns a tuple with the Public field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublic

`func (o *DnsPolicyResponse) SetPublic(v DnsPolicyPublic)`

SetPublic sets Public field to given value.

### HasPublic

`func (o *DnsPolicyResponse) HasPublic() bool`

HasPublic returns a boolean if a field has been set.

### GetPrivate

`func (o *DnsPolicyResponse) GetPrivate() DnsPolicyResponseAllOfPrivate`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *DnsPolicyResponse) GetPrivateOk() (*DnsPolicyResponseAllOfPrivate, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *DnsPolicyResponse) SetPrivate(v DnsPolicyResponseAllOfPrivate)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *DnsPolicyResponse) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


