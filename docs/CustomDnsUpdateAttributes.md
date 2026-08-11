# CustomDnsUpdateAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Servers** | [**[]CustomDnsServer**](CustomDnsServer.md) | Private DNS servers. Required, and must contain at least one entry when enabled is true. | 
**SearchDomains** | **[]string** | DNS search domains. Required — send an empty array if you have none. Omitting it on update is rejected with 400; a non-empty value fully replaces any existing search domains. | 
**DnsPolicy** | Pointer to [**DnsPolicy**](DnsPolicy.md) |  | [optional] 

## Methods

### NewCustomDnsUpdateAttributes

`func NewCustomDnsUpdateAttributes(servers []CustomDnsServer, searchDomains []string, ) *CustomDnsUpdateAttributes`

NewCustomDnsUpdateAttributes instantiates a new CustomDnsUpdateAttributes object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomDnsUpdateAttributesWithDefaults

`func NewCustomDnsUpdateAttributesWithDefaults() *CustomDnsUpdateAttributes`

NewCustomDnsUpdateAttributesWithDefaults instantiates a new CustomDnsUpdateAttributes object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetServers

`func (o *CustomDnsUpdateAttributes) GetServers() []CustomDnsServer`

GetServers returns the Servers field if non-nil, zero value otherwise.

### GetServersOk

`func (o *CustomDnsUpdateAttributes) GetServersOk() (*[]CustomDnsServer, bool)`

GetServersOk returns a tuple with the Servers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetServers

`func (o *CustomDnsUpdateAttributes) SetServers(v []CustomDnsServer)`

SetServers sets Servers field to given value.


### GetSearchDomains

`func (o *CustomDnsUpdateAttributes) GetSearchDomains() []string`

GetSearchDomains returns the SearchDomains field if non-nil, zero value otherwise.

### GetSearchDomainsOk

`func (o *CustomDnsUpdateAttributes) GetSearchDomainsOk() (*[]string, bool)`

GetSearchDomainsOk returns a tuple with the SearchDomains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSearchDomains

`func (o *CustomDnsUpdateAttributes) SetSearchDomains(v []string)`

SetSearchDomains sets SearchDomains field to given value.


### GetDnsPolicy

`func (o *CustomDnsUpdateAttributes) GetDnsPolicy() DnsPolicy`

GetDnsPolicy returns the DnsPolicy field if non-nil, zero value otherwise.

### GetDnsPolicyOk

`func (o *CustomDnsUpdateAttributes) GetDnsPolicyOk() (*DnsPolicy, bool)`

GetDnsPolicyOk returns a tuple with the DnsPolicy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDnsPolicy

`func (o *CustomDnsUpdateAttributes) SetDnsPolicy(v DnsPolicy)`

SetDnsPolicy sets DnsPolicy field to given value.

### HasDnsPolicy

`func (o *CustomDnsUpdateAttributes) HasDnsPolicy() bool`

HasDnsPolicy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


