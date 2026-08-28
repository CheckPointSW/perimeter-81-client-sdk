# DnsPolicyPrivate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Mode** | **string** | DNS resolution mode for private domains | 
**PublicFallback** | **bool** | Whether to fall back to public DNS if private DNS fails | 
**Domains** | **[]string** | List of private domains | 

## Methods

### NewDnsPolicyPrivate

`func NewDnsPolicyPrivate(mode string, publicFallback bool, domains []string, ) *DnsPolicyPrivate`

NewDnsPolicyPrivate instantiates a new DnsPolicyPrivate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDnsPolicyPrivateWithDefaults

`func NewDnsPolicyPrivateWithDefaults() *DnsPolicyPrivate`

NewDnsPolicyPrivateWithDefaults instantiates a new DnsPolicyPrivate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMode

`func (o *DnsPolicyPrivate) GetMode() string`

GetMode returns the Mode field if non-nil, zero value otherwise.

### GetModeOk

`func (o *DnsPolicyPrivate) GetModeOk() (*string, bool)`

GetModeOk returns a tuple with the Mode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMode

`func (o *DnsPolicyPrivate) SetMode(v string)`

SetMode sets Mode field to given value.


### GetPublicFallback

`func (o *DnsPolicyPrivate) GetPublicFallback() bool`

GetPublicFallback returns the PublicFallback field if non-nil, zero value otherwise.

### GetPublicFallbackOk

`func (o *DnsPolicyPrivate) GetPublicFallbackOk() (*bool, bool)`

GetPublicFallbackOk returns a tuple with the PublicFallback field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicFallback

`func (o *DnsPolicyPrivate) SetPublicFallback(v bool)`

SetPublicFallback sets PublicFallback field to given value.


### GetDomains

`func (o *DnsPolicyPrivate) GetDomains() []string`

GetDomains returns the Domains field if non-nil, zero value otherwise.

### GetDomainsOk

`func (o *DnsPolicyPrivate) GetDomainsOk() (*[]string, bool)`

GetDomainsOk returns a tuple with the Domains field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomains

`func (o *DnsPolicyPrivate) SetDomains(v []string)`

SetDomains sets Domains field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


