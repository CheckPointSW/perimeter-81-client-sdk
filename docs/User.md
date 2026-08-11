# User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InitialsColor** | Pointer to **string** |  | [optional] 
**InvitationAttempts** | Pointer to **int32** |  | [optional] 
**InvitationToken** | Pointer to **string** | Invitation token. | [optional] 
**Role** | Pointer to **string** | Reference ID to &#x60;Role&#x60;. | [optional] 
**Roles** | Pointer to **[]string** | Friendly names of the roles assigned to the user (built-in and custom). | [optional] 
**IdProviderGroups** | Pointer to **[]string** |  | [optional] 
**IdProviders** | Pointer to [**IdProviderMap**](IdProviderMap.md) |  | [optional] 
**InviteMessage** | Pointer to **string** | Invitation message sent to the user. | [optional] 
**Terminated** | **bool** | Indicates that the user has been deleted. | 
**Email** | **string** | User email. | 
**EmailVerified** | **bool** | Whether the user verified his email. | 
**Initials** | **string** | User initials. | 
**RoleName** | **string** | User role name. | 
**LastName** | **string** | User last name. | 
**FirstName** | **string** | User first name. | 
**Username** | **string** | User name. | 

## Methods

### NewUser

`func NewUser(terminated bool, email string, emailVerified bool, initials string, roleName string, lastName string, firstName string, username string, ) *User`

NewUser instantiates a new User object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserWithDefaults

`func NewUserWithDefaults() *User`

NewUserWithDefaults instantiates a new User object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInitialsColor

`func (o *User) GetInitialsColor() string`

GetInitialsColor returns the InitialsColor field if non-nil, zero value otherwise.

### GetInitialsColorOk

`func (o *User) GetInitialsColorOk() (*string, bool)`

GetInitialsColorOk returns a tuple with the InitialsColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitialsColor

`func (o *User) SetInitialsColor(v string)`

SetInitialsColor sets InitialsColor field to given value.

### HasInitialsColor

`func (o *User) HasInitialsColor() bool`

HasInitialsColor returns a boolean if a field has been set.

### GetInvitationAttempts

`func (o *User) GetInvitationAttempts() int32`

GetInvitationAttempts returns the InvitationAttempts field if non-nil, zero value otherwise.

### GetInvitationAttemptsOk

`func (o *User) GetInvitationAttemptsOk() (*int32, bool)`

GetInvitationAttemptsOk returns a tuple with the InvitationAttempts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvitationAttempts

`func (o *User) SetInvitationAttempts(v int32)`

SetInvitationAttempts sets InvitationAttempts field to given value.

### HasInvitationAttempts

`func (o *User) HasInvitationAttempts() bool`

HasInvitationAttempts returns a boolean if a field has been set.

### GetInvitationToken

`func (o *User) GetInvitationToken() string`

GetInvitationToken returns the InvitationToken field if non-nil, zero value otherwise.

### GetInvitationTokenOk

`func (o *User) GetInvitationTokenOk() (*string, bool)`

GetInvitationTokenOk returns a tuple with the InvitationToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvitationToken

`func (o *User) SetInvitationToken(v string)`

SetInvitationToken sets InvitationToken field to given value.

### HasInvitationToken

`func (o *User) HasInvitationToken() bool`

HasInvitationToken returns a boolean if a field has been set.

### GetRole

`func (o *User) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *User) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *User) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *User) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetRoles

`func (o *User) GetRoles() []string`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *User) GetRolesOk() (*[]string, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoles

`func (o *User) SetRoles(v []string)`

SetRoles sets Roles field to given value.

### HasRoles

`func (o *User) HasRoles() bool`

HasRoles returns a boolean if a field has been set.

### GetIdProviderGroups

`func (o *User) GetIdProviderGroups() []string`

GetIdProviderGroups returns the IdProviderGroups field if non-nil, zero value otherwise.

### GetIdProviderGroupsOk

`func (o *User) GetIdProviderGroupsOk() (*[]string, bool)`

GetIdProviderGroupsOk returns a tuple with the IdProviderGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdProviderGroups

`func (o *User) SetIdProviderGroups(v []string)`

SetIdProviderGroups sets IdProviderGroups field to given value.

### HasIdProviderGroups

`func (o *User) HasIdProviderGroups() bool`

HasIdProviderGroups returns a boolean if a field has been set.

### GetIdProviders

`func (o *User) GetIdProviders() IdProviderMap`

GetIdProviders returns the IdProviders field if non-nil, zero value otherwise.

### GetIdProvidersOk

`func (o *User) GetIdProvidersOk() (*IdProviderMap, bool)`

GetIdProvidersOk returns a tuple with the IdProviders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdProviders

`func (o *User) SetIdProviders(v IdProviderMap)`

SetIdProviders sets IdProviders field to given value.

### HasIdProviders

`func (o *User) HasIdProviders() bool`

HasIdProviders returns a boolean if a field has been set.

### GetInviteMessage

`func (o *User) GetInviteMessage() string`

GetInviteMessage returns the InviteMessage field if non-nil, zero value otherwise.

### GetInviteMessageOk

`func (o *User) GetInviteMessageOk() (*string, bool)`

GetInviteMessageOk returns a tuple with the InviteMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInviteMessage

`func (o *User) SetInviteMessage(v string)`

SetInviteMessage sets InviteMessage field to given value.

### HasInviteMessage

`func (o *User) HasInviteMessage() bool`

HasInviteMessage returns a boolean if a field has been set.

### GetTerminated

`func (o *User) GetTerminated() bool`

GetTerminated returns the Terminated field if non-nil, zero value otherwise.

### GetTerminatedOk

`func (o *User) GetTerminatedOk() (*bool, bool)`

GetTerminatedOk returns a tuple with the Terminated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTerminated

`func (o *User) SetTerminated(v bool)`

SetTerminated sets Terminated field to given value.


### GetEmail

`func (o *User) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *User) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *User) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetEmailVerified

`func (o *User) GetEmailVerified() bool`

GetEmailVerified returns the EmailVerified field if non-nil, zero value otherwise.

### GetEmailVerifiedOk

`func (o *User) GetEmailVerifiedOk() (*bool, bool)`

GetEmailVerifiedOk returns a tuple with the EmailVerified field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailVerified

`func (o *User) SetEmailVerified(v bool)`

SetEmailVerified sets EmailVerified field to given value.


### GetInitials

`func (o *User) GetInitials() string`

GetInitials returns the Initials field if non-nil, zero value otherwise.

### GetInitialsOk

`func (o *User) GetInitialsOk() (*string, bool)`

GetInitialsOk returns a tuple with the Initials field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitials

`func (o *User) SetInitials(v string)`

SetInitials sets Initials field to given value.


### GetRoleName

`func (o *User) GetRoleName() string`

GetRoleName returns the RoleName field if non-nil, zero value otherwise.

### GetRoleNameOk

`func (o *User) GetRoleNameOk() (*string, bool)`

GetRoleNameOk returns a tuple with the RoleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoleName

`func (o *User) SetRoleName(v string)`

SetRoleName sets RoleName field to given value.


### GetLastName

`func (o *User) GetLastName() string`

GetLastName returns the LastName field if non-nil, zero value otherwise.

### GetLastNameOk

`func (o *User) GetLastNameOk() (*string, bool)`

GetLastNameOk returns a tuple with the LastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastName

`func (o *User) SetLastName(v string)`

SetLastName sets LastName field to given value.


### GetFirstName

`func (o *User) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *User) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *User) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.


### GetUsername

`func (o *User) GetUsername() string`

GetUsername returns the Username field if non-nil, zero value otherwise.

### GetUsernameOk

`func (o *User) GetUsernameOk() (*string, bool)`

GetUsernameOk returns a tuple with the Username field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsername

`func (o *User) SetUsername(v string)`

SetUsername sets Username field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


