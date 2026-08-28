# DnsPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Public** | Pointer to [**DnsPolicyPublic**](DnsPolicyPublic.md) |  | [optional] 
**Private** | Pointer to [**DnsPolicyPrivate**](DnsPolicyPrivate.md) |  | [optional] 

## Methods

### NewDnsPolicy

`func NewDnsPolicy() *DnsPolicy`

NewDnsPolicy instantiates a new DnsPolicy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDnsPolicyWithDefaults

`func NewDnsPolicyWithDefaults() *DnsPolicy`

NewDnsPolicyWithDefaults instantiates a new DnsPolicy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPublic

`func (o *DnsPolicy) GetPublic() DnsPolicyPublic`

GetPublic returns the Public field if non-nil, zero value otherwise.

### GetPublicOk

`func (o *DnsPolicy) GetPublicOk() (*DnsPolicyPublic, bool)`

GetPublicOk returns a tuple with the Public field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublic

`func (o *DnsPolicy) SetPublic(v DnsPolicyPublic)`

SetPublic sets Public field to given value.

### HasPublic

`func (o *DnsPolicy) HasPublic() bool`

HasPublic returns a boolean if a field has been set.

### GetPrivate

`func (o *DnsPolicy) GetPrivate() DnsPolicyPrivate`

GetPrivate returns the Private field if non-nil, zero value otherwise.

### GetPrivateOk

`func (o *DnsPolicy) GetPrivateOk() (*DnsPolicyPrivate, bool)`

GetPrivateOk returns a tuple with the Private field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrivate

`func (o *DnsPolicy) SetPrivate(v DnsPolicyPrivate)`

SetPrivate sets Private field to given value.

### HasPrivate

`func (o *DnsPolicy) HasPrivate() bool`

HasPrivate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


