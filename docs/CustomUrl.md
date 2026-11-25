# CustomUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the custom URL object | 
**Name** | **string** | Display name | 
**Description** | Pointer to **string** | Optional free-text description | [optional] 
**EntryType** | **string** | Kind of entries this object holds. Objects created before the type existed are url objects | 
**Urls** | **[]string** | Entries of a url object; empty on a regex object | 
**UrlPatterns** | **[]string** | Entries of a regex object; empty on a url object | 
**ControlledBy** | **string** | Read-only. Determines mutability via this API | 
**CreatedAt** | **time.Time** |  | 
**UpdatedAt** | **time.Time** |  | 

## Methods

### NewCustomUrl

`func NewCustomUrl(id string, name string, entryType string, urls []string, urlPatterns []string, controlledBy string, createdAt time.Time, updatedAt time.Time, ) *CustomUrl`

NewCustomUrl instantiates a new CustomUrl object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCustomUrlWithDefaults

`func NewCustomUrlWithDefaults() *CustomUrl`

NewCustomUrlWithDefaults instantiates a new CustomUrl object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CustomUrl) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CustomUrl) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CustomUrl) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *CustomUrl) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CustomUrl) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CustomUrl) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CustomUrl) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CustomUrl) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CustomUrl) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CustomUrl) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetEntryType

`func (o *CustomUrl) GetEntryType() string`

GetEntryType returns the EntryType field if non-nil, zero value otherwise.

### GetEntryTypeOk

`func (o *CustomUrl) GetEntryTypeOk() (*string, bool)`

GetEntryTypeOk returns a tuple with the EntryType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntryType

`func (o *CustomUrl) SetEntryType(v string)`

SetEntryType sets EntryType field to given value.


### GetUrls

`func (o *CustomUrl) GetUrls() []string`

GetUrls returns the Urls field if non-nil, zero value otherwise.

### GetUrlsOk

`func (o *CustomUrl) GetUrlsOk() (*[]string, bool)`

GetUrlsOk returns a tuple with the Urls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrls

`func (o *CustomUrl) SetUrls(v []string)`

SetUrls sets Urls field to given value.


### GetUrlPatterns

`func (o *CustomUrl) GetUrlPatterns() []string`

GetUrlPatterns returns the UrlPatterns field if non-nil, zero value otherwise.

### GetUrlPatternsOk

`func (o *CustomUrl) GetUrlPatternsOk() (*[]string, bool)`

GetUrlPatternsOk returns a tuple with the UrlPatterns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrlPatterns

`func (o *CustomUrl) SetUrlPatterns(v []string)`

SetUrlPatterns sets UrlPatterns field to given value.


### GetControlledBy

`func (o *CustomUrl) GetControlledBy() string`

GetControlledBy returns the ControlledBy field if non-nil, zero value otherwise.

### GetControlledByOk

`func (o *CustomUrl) GetControlledByOk() (*string, bool)`

GetControlledByOk returns a tuple with the ControlledBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetControlledBy

`func (o *CustomUrl) SetControlledBy(v string)`

SetControlledBy sets ControlledBy field to given value.


### GetCreatedAt

`func (o *CustomUrl) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CustomUrl) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CustomUrl) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *CustomUrl) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CustomUrl) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CustomUrl) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


