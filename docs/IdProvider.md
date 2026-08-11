# IdProvider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | Pointer to **string** | User ID on the IDP side. | [optional] 
**Groups** | Pointer to **[]string** | List of group names on the IDP side. | [optional] 
**IdpConnName** | Pointer to **string** | IDP connection name. | [optional] 

## Methods

### NewIdProvider

`func NewIdProvider() *IdProvider`

NewIdProvider instantiates a new IdProvider object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIdProviderWithDefaults

`func NewIdProviderWithDefaults() *IdProvider`

NewIdProviderWithDefaults instantiates a new IdProvider object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *IdProvider) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *IdProvider) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *IdProvider) SetUserId(v string)`

SetUserId sets UserId field to given value.

### HasUserId

`func (o *IdProvider) HasUserId() bool`

HasUserId returns a boolean if a field has been set.

### GetGroups

`func (o *IdProvider) GetGroups() []string`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *IdProvider) GetGroupsOk() (*[]string, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *IdProvider) SetGroups(v []string)`

SetGroups sets Groups field to given value.

### HasGroups

`func (o *IdProvider) HasGroups() bool`

HasGroups returns a boolean if a field has been set.

### GetIdpConnName

`func (o *IdProvider) GetIdpConnName() string`

GetIdpConnName returns the IdpConnName field if non-nil, zero value otherwise.

### GetIdpConnNameOk

`func (o *IdProvider) GetIdpConnNameOk() (*string, bool)`

GetIdpConnNameOk returns a tuple with the IdpConnName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdpConnName

`func (o *IdProvider) SetIdpConnName(v string)`

SetIdpConnName sets IdpConnName field to given value.

### HasIdpConnName

`func (o *IdProvider) HasIdpConnName() bool`

HasIdpConnName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


