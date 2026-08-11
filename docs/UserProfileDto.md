# UserProfileDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FirstName** | Pointer to **string** |  | [optional] 
**LastName** | Pointer to **string** |  | [optional] 
**RoleName** | Pointer to **string** |  | [optional] [default to ""]
**Phone** | Pointer to **string** |  | [optional] 

## Methods

### NewUserProfileDto

`func NewUserProfileDto() *UserProfileDto`

NewUserProfileDto instantiates a new UserProfileDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserProfileDtoWithDefaults

`func NewUserProfileDtoWithDefaults() *UserProfileDto`

NewUserProfileDtoWithDefaults instantiates a new UserProfileDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFirstName

`func (o *UserProfileDto) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *UserProfileDto) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *UserProfileDto) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.

### HasFirstName

`func (o *UserProfileDto) HasFirstName() bool`

HasFirstName returns a boolean if a field has been set.

### GetLastName

`func (o *UserProfileDto) GetLastName() string`

GetLastName returns the LastName field if non-nil, zero value otherwise.

### GetLastNameOk

`func (o *UserProfileDto) GetLastNameOk() (*string, bool)`

GetLastNameOk returns a tuple with the LastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastName

`func (o *UserProfileDto) SetLastName(v string)`

SetLastName sets LastName field to given value.

### HasLastName

`func (o *UserProfileDto) HasLastName() bool`

HasLastName returns a boolean if a field has been set.

### GetRoleName

`func (o *UserProfileDto) GetRoleName() string`

GetRoleName returns the RoleName field if non-nil, zero value otherwise.

### GetRoleNameOk

`func (o *UserProfileDto) GetRoleNameOk() (*string, bool)`

GetRoleNameOk returns a tuple with the RoleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoleName

`func (o *UserProfileDto) SetRoleName(v string)`

SetRoleName sets RoleName field to given value.

### HasRoleName

`func (o *UserProfileDto) HasRoleName() bool`

HasRoleName returns a boolean if a field has been set.

### GetPhone

`func (o *UserProfileDto) GetPhone() string`

GetPhone returns the Phone field if non-nil, zero value otherwise.

### GetPhoneOk

`func (o *UserProfileDto) GetPhoneOk() (*string, bool)`

GetPhoneOk returns a tuple with the Phone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhone

`func (o *UserProfileDto) SetPhone(v string)`

SetPhone sets Phone field to given value.

### HasPhone

`func (o *UserProfileDto) HasPhone() bool`

HasPhone returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


