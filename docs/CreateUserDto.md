# CreateUserDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IdpType** | Pointer to **string** | Identity provider type. | [optional] [default to "database"]
**AccessGroups** | Pointer to **[]string** | List of access group IDs. | [optional] 
**Email** | **string** | User email. | 
**EmailVerified** | Pointer to **bool** | Skips email verification if set to &#x60;true&#x60;. | [optional] [default to false]
**InviteMessage** | **string** | Invitation message that will be sent by email. | 
**ProfileData** | Pointer to [**UserProfileDto**](UserProfileDto.md) |  | [optional] 

## Methods

### NewCreateUserDto

`func NewCreateUserDto(email string, inviteMessage string, ) *CreateUserDto`

NewCreateUserDto instantiates a new CreateUserDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateUserDtoWithDefaults

`func NewCreateUserDtoWithDefaults() *CreateUserDto`

NewCreateUserDtoWithDefaults instantiates a new CreateUserDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdpType

`func (o *CreateUserDto) GetIdpType() string`

GetIdpType returns the IdpType field if non-nil, zero value otherwise.

### GetIdpTypeOk

`func (o *CreateUserDto) GetIdpTypeOk() (*string, bool)`

GetIdpTypeOk returns a tuple with the IdpType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdpType

`func (o *CreateUserDto) SetIdpType(v string)`

SetIdpType sets IdpType field to given value.

### HasIdpType

`func (o *CreateUserDto) HasIdpType() bool`

HasIdpType returns a boolean if a field has been set.

### GetAccessGroups

`func (o *CreateUserDto) GetAccessGroups() []string`

GetAccessGroups returns the AccessGroups field if non-nil, zero value otherwise.

### GetAccessGroupsOk

`func (o *CreateUserDto) GetAccessGroupsOk() (*[]string, bool)`

GetAccessGroupsOk returns a tuple with the AccessGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessGroups

`func (o *CreateUserDto) SetAccessGroups(v []string)`

SetAccessGroups sets AccessGroups field to given value.

### HasAccessGroups

`func (o *CreateUserDto) HasAccessGroups() bool`

HasAccessGroups returns a boolean if a field has been set.

### GetEmail

`func (o *CreateUserDto) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateUserDto) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateUserDto) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetEmailVerified

`func (o *CreateUserDto) GetEmailVerified() bool`

GetEmailVerified returns the EmailVerified field if non-nil, zero value otherwise.

### GetEmailVerifiedOk

`func (o *CreateUserDto) GetEmailVerifiedOk() (*bool, bool)`

GetEmailVerifiedOk returns a tuple with the EmailVerified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailVerified

`func (o *CreateUserDto) SetEmailVerified(v bool)`

SetEmailVerified sets EmailVerified field to given value.

### HasEmailVerified

`func (o *CreateUserDto) HasEmailVerified() bool`

HasEmailVerified returns a boolean if a field has been set.

### GetInviteMessage

`func (o *CreateUserDto) GetInviteMessage() string`

GetInviteMessage returns the InviteMessage field if non-nil, zero value otherwise.

### GetInviteMessageOk

`func (o *CreateUserDto) GetInviteMessageOk() (*string, bool)`

GetInviteMessageOk returns a tuple with the InviteMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInviteMessage

`func (o *CreateUserDto) SetInviteMessage(v string)`

SetInviteMessage sets InviteMessage field to given value.


### GetProfileData

`func (o *CreateUserDto) GetProfileData() UserProfileDto`

GetProfileData returns the ProfileData field if non-nil, zero value otherwise.

### GetProfileDataOk

`func (o *CreateUserDto) GetProfileDataOk() (*UserProfileDto, bool)`

GetProfileDataOk returns a tuple with the ProfileData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProfileData

`func (o *CreateUserDto) SetProfileData(v UserProfileDto)`

SetProfileData sets ProfileData field to given value.

### HasProfileData

`func (o *CreateUserDto) HasProfileData() bool`

HasProfileData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


