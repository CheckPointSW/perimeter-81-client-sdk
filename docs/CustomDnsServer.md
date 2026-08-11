# CustomDnsServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Address** | **string** | IP address of the DNS server | 
**IsTLS** | **bool** | Indicates if DNS-over-TLS is used | 

## Methods

### NewCustomDnsServer

`func NewCustomDnsServer(address string, isTLS bool, ) *CustomDnsServer`

NewCustomDnsServer instantiates a new CustomDnsServer object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsServerWithDefaults

`func NewCustomDnsServerWithDefaults() *CustomDnsServer`

NewCustomDnsServerWithDefaults instantiates a new CustomDnsServer object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddress

`func (o *CustomDnsServer) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *CustomDnsServer) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *CustomDnsServer) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetIsTLS

`func (o *CustomDnsServer) GetIsTLS() bool`

GetIsTLS returns the IsTLS field if non-nil, zero value otherwise.

### GetIsTLSOk

`func (o *CustomDnsServer) GetIsTLSOk() (*bool, bool)`

GetIsTLSOk returns a tuple with the IsTLS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsTLS

`func (o *CustomDnsServer) SetIsTLS(v bool)`

SetIsTLS sets IsTLS field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


