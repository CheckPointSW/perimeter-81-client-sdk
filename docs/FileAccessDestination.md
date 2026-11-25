# FileAccessDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CustomUrls** | Pointer to **[]string** | Array of custom URL IDs | [optional] 
**Categories** | Pointer to **[]string** | Array of web category IDs | [optional] 
**ApplicationControlApplications** | Pointer to **[]string** | Array of application control application IDs | [optional] 
**UpdatableObjects** | Pointer to **[]string** | Array of updatable object IDs | [optional] 

## Methods

### NewFileAccessDestination

`func NewFileAccessDestination() *FileAccessDestination`

NewFileAccessDestination instantiates a new FileAccessDestination object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileAccessDestinationWithDefaults

`func NewFileAccessDestinationWithDefaults() *FileAccessDestination`

NewFileAccessDestinationWithDefaults instantiates a new FileAccessDestination object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCustomUrls

`func (o *FileAccessDestination) GetCustomUrls() []string`

GetCustomUrls returns the CustomUrls field if non-nil, zero value otherwise.

### GetCustomUrlsOk

`func (o *FileAccessDestination) GetCustomUrlsOk() (*[]string, bool)`

GetCustomUrlsOk returns a tuple with the CustomUrls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomUrls

`func (o *FileAccessDestination) SetCustomUrls(v []string)`

SetCustomUrls sets CustomUrls field to given value.

### HasCustomUrls

`func (o *FileAccessDestination) HasCustomUrls() bool`

HasCustomUrls returns a boolean if a field has been set.

### GetCategories

`func (o *FileAccessDestination) GetCategories() []string`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *FileAccessDestination) GetCategoriesOk() (*[]string, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *FileAccessDestination) SetCategories(v []string)`

SetCategories sets Categories field to given value.

### HasCategories

`func (o *FileAccessDestination) HasCategories() bool`

HasCategories returns a boolean if a field has been set.

### GetApplicationControlApplications

`func (o *FileAccessDestination) GetApplicationControlApplications() []string`

GetApplicationControlApplications returns the ApplicationControlApplications field if non-nil, zero value otherwise.

### GetApplicationControlApplicationsOk

`func (o *FileAccessDestination) GetApplicationControlApplicationsOk() (*[]string, bool)`

GetApplicationControlApplicationsOk returns a tuple with the ApplicationControlApplications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplicationControlApplications

`func (o *FileAccessDestination) SetApplicationControlApplications(v []string)`

SetApplicationControlApplications sets ApplicationControlApplications field to given value.

### HasApplicationControlApplications

`func (o *FileAccessDestination) HasApplicationControlApplications() bool`

HasApplicationControlApplications returns a boolean if a field has been set.

### GetUpdatableObjects

`func (o *FileAccessDestination) GetUpdatableObjects() []string`

GetUpdatableObjects returns the UpdatableObjects field if non-nil, zero value otherwise.

### GetUpdatableObjectsOk

`func (o *FileAccessDestination) GetUpdatableObjectsOk() (*[]string, bool)`

GetUpdatableObjectsOk returns a tuple with the UpdatableObjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatableObjects

`func (o *FileAccessDestination) SetUpdatableObjects(v []string)`

SetUpdatableObjects sets UpdatableObjects field to given value.

### HasUpdatableObjects

`func (o *FileAccessDestination) HasUpdatableObjects() bool`

HasUpdatableObjects returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


