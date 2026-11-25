# CustomUrlWriteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Display name, unique per tenant, compared case-insensitively | 
**Description** | Pointer to **string** | Defaults to an empty string | [optional] 
**EntryType** | Pointer to **string** | Kind of entries this object holds. Fixed after creation. regex requires advanced matching to be enabled for the tenant. | [optional] [default to "url"]
**Urls** | Pointer to **[]string** | Entries of a url object, at least one and at most 5000: a host without a protocol, optionally with a port, a path and a query (host[:port][/path][?name&#x3D;value&amp;...]), and a leading *. wildcard. A query parameter name, compared without regard to case, is not repeated within an entry. A port or a query requires advanced matching to be enabled for the tenant. | [optional] 
**UrlPatterns** | Pointer to **[]string** | Entries of a regex object, at least one and at most 100: RE2 regular expressions, kept exactly as written. | [optional] 

## Methods

### NewCustomUrlWriteRequest

`func NewCustomUrlWriteRequest(name string, ) *CustomUrlWriteRequest`

NewCustomUrlWriteRequest instantiates a new CustomUrlWriteRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomUrlWriteRequestWithDefaults

`func NewCustomUrlWriteRequestWithDefaults() *CustomUrlWriteRequest`

NewCustomUrlWriteRequestWithDefaults instantiates a new CustomUrlWriteRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CustomUrlWriteRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CustomUrlWriteRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CustomUrlWriteRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CustomUrlWriteRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CustomUrlWriteRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CustomUrlWriteRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CustomUrlWriteRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEntryType

`func (o *CustomUrlWriteRequest) GetEntryType() string`

GetEntryType returns the EntryType field if non-nil, zero value otherwise.

### GetEntryTypeOk

`func (o *CustomUrlWriteRequest) GetEntryTypeOk() (*string, bool)`

GetEntryTypeOk returns a tuple with the EntryType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntryType

`func (o *CustomUrlWriteRequest) SetEntryType(v string)`

SetEntryType sets EntryType field to given value.

### HasEntryType

`func (o *CustomUrlWriteRequest) HasEntryType() bool`

HasEntryType returns a boolean if a field has been set.

### GetUrls

`func (o *CustomUrlWriteRequest) GetUrls() []string`

GetUrls returns the Urls field if non-nil, zero value otherwise.

### GetUrlsOk

`func (o *CustomUrlWriteRequest) GetUrlsOk() (*[]string, bool)`

GetUrlsOk returns a tuple with the Urls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrls

`func (o *CustomUrlWriteRequest) SetUrls(v []string)`

SetUrls sets Urls field to given value.

### HasUrls

`func (o *CustomUrlWriteRequest) HasUrls() bool`

HasUrls returns a boolean if a field has been set.

### GetUrlPatterns

`func (o *CustomUrlWriteRequest) GetUrlPatterns() []string`

GetUrlPatterns returns the UrlPatterns field if non-nil, zero value otherwise.

### GetUrlPatternsOk

`func (o *CustomUrlWriteRequest) GetUrlPatternsOk() (*[]string, bool)`

GetUrlPatternsOk returns a tuple with the UrlPatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrlPatterns

`func (o *CustomUrlWriteRequest) SetUrlPatterns(v []string)`

SetUrlPatterns sets UrlPatterns field to given value.

### HasUrlPatterns

`func (o *CustomUrlWriteRequest) HasUrlPatterns() bool`

HasUrlPatterns returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


