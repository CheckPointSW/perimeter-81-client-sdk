# UrlObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EntryType** | Pointer to **string** |  | [optional] 
**Urls** | **[]string** |  | 
**UrlPatterns** | Pointer to **[]string** |  | [optional] 

## Methods

### NewUrlObject

`func NewUrlObject(urls []string, ) *UrlObject`

NewUrlObject instantiates a new UrlObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUrlObjectWithDefaults

`func NewUrlObjectWithDefaults() *UrlObject`

NewUrlObjectWithDefaults instantiates a new UrlObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntryType

`func (o *UrlObject) GetEntryType() string`

GetEntryType returns the EntryType field if non-nil, zero value otherwise.

### GetEntryTypeOk

`func (o *UrlObject) GetEntryTypeOk() (*string, bool)`

GetEntryTypeOk returns a tuple with the EntryType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntryType

`func (o *UrlObject) SetEntryType(v string)`

SetEntryType sets EntryType field to given value.

### HasEntryType

`func (o *UrlObject) HasEntryType() bool`

HasEntryType returns a boolean if a field has been set.

### GetUrls

`func (o *UrlObject) GetUrls() []string`

GetUrls returns the Urls field if non-nil, zero value otherwise.

### GetUrlsOk

`func (o *UrlObject) GetUrlsOk() (*[]string, bool)`

GetUrlsOk returns a tuple with the Urls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrls

`func (o *UrlObject) SetUrls(v []string)`

SetUrls sets Urls field to given value.


### GetUrlPatterns

`func (o *UrlObject) GetUrlPatterns() []string`

GetUrlPatterns returns the UrlPatterns field if non-nil, zero value otherwise.

### GetUrlPatternsOk

`func (o *UrlObject) GetUrlPatternsOk() (*[]string, bool)`

GetUrlPatternsOk returns a tuple with the UrlPatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrlPatterns

`func (o *UrlObject) SetUrlPatterns(v []string)`

SetUrlPatterns sets UrlPatterns field to given value.

### HasUrlPatterns

`func (o *UrlObject) HasUrlPatterns() bool`

HasUrlPatterns returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


