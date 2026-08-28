# CustomDnsAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Servers** | Pointer to [**[]CustomDnsServer**](CustomDnsServer.md) | Private DNS servers | [optional] 
**SearchDomains** | Pointer to **[]string** | DNS search domains for domain resolution | [optional] 
**DnsPolicy** | Pointer to [**DnsPolicy**](DnsPolicy.md) |  | [optional] 

## Methods

### NewCustomDnsAttributes

`func NewCustomDnsAttributes() *CustomDnsAttributes`

NewCustomDnsAttributes instantiates a new CustomDnsAttributes object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsAttributesWithDefaults

`func NewCustomDnsAttributesWithDefaults() *CustomDnsAttributes`

NewCustomDnsAttributesWithDefaults instantiates a new CustomDnsAttributes object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetServers

`func (o *CustomDnsAttributes) GetServers() []CustomDnsServer`

GetServers returns the Servers field if non-nil, zero value otherwise.

### GetServersOk

`func (o *CustomDnsAttributes) GetServersOk() (*[]CustomDnsServer, bool)`

GetServersOk returns a tuple with the Servers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServers

`func (o *CustomDnsAttributes) SetServers(v []CustomDnsServer)`

SetServers sets Servers field to given value.

### HasServers

`func (o *CustomDnsAttributes) HasServers() bool`

HasServers returns a boolean if a field has been set.

### GetSearchDomains

`func (o *CustomDnsAttributes) GetSearchDomains() []string`

GetSearchDomains returns the SearchDomains field if non-nil, zero value otherwise.

### GetSearchDomainsOk

`func (o *CustomDnsAttributes) GetSearchDomainsOk() (*[]string, bool)`

GetSearchDomainsOk returns a tuple with the SearchDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSearchDomains

`func (o *CustomDnsAttributes) SetSearchDomains(v []string)`

SetSearchDomains sets SearchDomains field to given value.

### HasSearchDomains

`func (o *CustomDnsAttributes) HasSearchDomains() bool`

HasSearchDomains returns a boolean if a field has been set.

### GetDnsPolicy

`func (o *CustomDnsAttributes) GetDnsPolicy() DnsPolicy`

GetDnsPolicy returns the DnsPolicy field if non-nil, zero value otherwise.

### GetDnsPolicyOk

`func (o *CustomDnsAttributes) GetDnsPolicyOk() (*DnsPolicy, bool)`

GetDnsPolicyOk returns a tuple with the DnsPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsPolicy

`func (o *CustomDnsAttributes) SetDnsPolicy(v DnsPolicy)`

SetDnsPolicy sets DnsPolicy field to given value.

### HasDnsPolicy

`func (o *CustomDnsAttributes) HasDnsPolicy() bool`

HasDnsPolicy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


