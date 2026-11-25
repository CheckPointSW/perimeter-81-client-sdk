# RegexObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EntryType** | **string** |  | 
**Urls** | Pointer to **[]string** |  | [optional] 
**UrlPatterns** | **[]string** |  | 

## Methods

### NewRegexObject

`func NewRegexObject(entryType string, urlPatterns []string, ) *RegexObject`

NewRegexObject instantiates a new RegexObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegexObjectWithDefaults

`func NewRegexObjectWithDefaults() *RegexObject`

NewRegexObjectWithDefaults instantiates a new RegexObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntryType

`func (o *RegexObject) GetEntryType() string`

GetEntryType returns the EntryType field if non-nil, zero value otherwise.

### GetEntryTypeOk

`func (o *RegexObject) GetEntryTypeOk() (*string, bool)`

GetEntryTypeOk returns a tuple with the EntryType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntryType

`func (o *RegexObject) SetEntryType(v string)`

SetEntryType sets EntryType field to given value.


### GetUrls

`func (o *RegexObject) GetUrls() []string`

GetUrls returns the Urls field if non-nil, zero value otherwise.

### GetUrlsOk

`func (o *RegexObject) GetUrlsOk() (*[]string, bool)`

GetUrlsOk returns a tuple with the Urls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrls

`func (o *RegexObject) SetUrls(v []string)`

SetUrls sets Urls field to given value.

### HasUrls

`func (o *RegexObject) HasUrls() bool`

HasUrls returns a boolean if a field has been set.

### GetUrlPatterns

`func (o *RegexObject) GetUrlPatterns() []string`

GetUrlPatterns returns the UrlPatterns field if non-nil, zero value otherwise.

### GetUrlPatternsOk

`func (o *RegexObject) GetUrlPatternsOk() (*[]string, bool)`

GetUrlPatternsOk returns a tuple with the UrlPatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrlPatterns

`func (o *RegexObject) SetUrlPatterns(v []string)`

SetUrlPatterns sets UrlPatterns field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


