# CustomDnsAttributesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Servers** | Pointer to [**[]CustomDnsServer**](CustomDnsServer.md) | Private DNS servers | [optional] 
**SearchDomains** | Pointer to **[]string** | DNS search domains for domain resolution | [optional] 
**DnsPolicy** | Pointer to [**DnsPolicyResponse**](DnsPolicyResponse.md) |  | [optional] 

## Methods

### NewCustomDnsAttributesResponse

`func NewCustomDnsAttributesResponse() *CustomDnsAttributesResponse`

NewCustomDnsAttributesResponse instantiates a new CustomDnsAttributesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsAttributesResponseWithDefaults

`func NewCustomDnsAttributesResponseWithDefaults() *CustomDnsAttributesResponse`

NewCustomDnsAttributesResponseWithDefaults instantiates a new CustomDnsAttributesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetServers

`func (o *CustomDnsAttributesResponse) GetServers() []CustomDnsServer`

GetServers returns the Servers field if non-nil, zero value otherwise.

### GetServersOk

`func (o *CustomDnsAttributesResponse) GetServersOk() (*[]CustomDnsServer, bool)`

GetServersOk returns a tuple with the Servers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServers

`func (o *CustomDnsAttributesResponse) SetServers(v []CustomDnsServer)`

SetServers sets Servers field to given value.

### HasServers

`func (o *CustomDnsAttributesResponse) HasServers() bool`

HasServers returns a boolean if a field has been set.

### GetSearchDomains

`func (o *CustomDnsAttributesResponse) GetSearchDomains() []string`

GetSearchDomains returns the SearchDomains field if non-nil, zero value otherwise.

### GetSearchDomainsOk

`func (o *CustomDnsAttributesResponse) GetSearchDomainsOk() (*[]string, bool)`

GetSearchDomainsOk returns a tuple with the SearchDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSearchDomains

`func (o *CustomDnsAttributesResponse) SetSearchDomains(v []string)`

SetSearchDomains sets SearchDomains field to given value.

### HasSearchDomains

`func (o *CustomDnsAttributesResponse) HasSearchDomains() bool`

HasSearchDomains returns a boolean if a field has been set.

### GetDnsPolicy

`func (o *CustomDnsAttributesResponse) GetDnsPolicy() DnsPolicyResponse`

GetDnsPolicy returns the DnsPolicy field if non-nil, zero value otherwise.

### GetDnsPolicyOk

`func (o *CustomDnsAttributesResponse) GetDnsPolicyOk() (*DnsPolicyResponse, bool)`

GetDnsPolicyOk returns a tuple with the DnsPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsPolicy

`func (o *CustomDnsAttributesResponse) SetDnsPolicy(v DnsPolicyResponse)`

SetDnsPolicy sets DnsPolicy field to given value.

### HasDnsPolicy

`func (o *CustomDnsAttributesResponse) HasDnsPolicy() bool`

HasDnsPolicy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


