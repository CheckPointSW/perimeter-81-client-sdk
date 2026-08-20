# Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name of the group. | [optional] 
**IsDefault** | Pointer to **bool** | Indicates that the group is default. | [optional] 
**Applications** | Pointer to **[]string** | Group applications. | [optional] 
**Networks** | Pointer to **[]string** | Group networks. | [optional] 
**VpnLocations** | Pointer to **[]string** | Group VPN locations. | [optional] 
**Users** | Pointer to **[]string** | Group members. | [optional] 
**Id** | Pointer to **string** | Unique identifier of the group. | [optional] 

## Methods

### NewGroup

`func NewGroup() *Group`

NewGroup instantiates a new Group object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGroupWithDefaults

`func NewGroupWithDefaults() *Group`

NewGroupWithDefaults instantiates a new Group object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Group) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Group) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Group) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *Group) HasName() bool`

HasName returns a boolean if a field has been set.

### GetIsDefault

`func (o *Group) GetIsDefault() bool`

GetIsDefault returns the IsDefault field if non-nil, zero value otherwise.

### GetIsDefaultOk

`func (o *Group) GetIsDefaultOk() (*bool, bool)`

GetIsDefaultOk returns a tuple with the IsDefault field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsDefault

`func (o *Group) SetIsDefault(v bool)`

SetIsDefault sets IsDefault field to given value.

### HasIsDefault

`func (o *Group) HasIsDefault() bool`

HasIsDefault returns a boolean if a field has been set.

### GetApplications

`func (o *Group) GetApplications() []string`

GetApplications returns the Applications field if non-nil, zero value otherwise.

### GetApplicationsOk

`func (o *Group) GetApplicationsOk() (*[]string, bool)`

GetApplicationsOk returns a tuple with the Applications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplications

`func (o *Group) SetApplications(v []string)`

SetApplications sets Applications field to given value.

### HasApplications

`func (o *Group) HasApplications() bool`

HasApplications returns a boolean if a field has been set.

### GetNetworks

`func (o *Group) GetNetworks() []string`

GetNetworks returns the Networks field if non-nil, zero value otherwise.

### GetNetworksOk

`func (o *Group) GetNetworksOk() (*[]string, bool)`

GetNetworksOk returns a tuple with the Networks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetworks

`func (o *Group) SetNetworks(v []string)`

SetNetworks sets Networks field to given value.

### HasNetworks

`func (o *Group) HasNetworks() bool`

HasNetworks returns a boolean if a field has been set.

### GetVpnLocations

`func (o *Group) GetVpnLocations() []string`

GetVpnLocations returns the VpnLocations field if non-nil, zero value otherwise.

### GetVpnLocationsOk

`func (o *Group) GetVpnLocationsOk() (*[]string, bool)`

GetVpnLocationsOk returns a tuple with the VpnLocations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVpnLocations

`func (o *Group) SetVpnLocations(v []string)`

SetVpnLocations sets VpnLocations field to given value.

### HasVpnLocations

`func (o *Group) HasVpnLocations() bool`

HasVpnLocations returns a boolean if a field has been set.

### GetUsers

`func (o *Group) GetUsers() []string`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *Group) GetUsersOk() (*[]string, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *Group) SetUsers(v []string)`

SetUsers sets Users field to given value.

### HasUsers

`func (o *Group) HasUsers() bool`

HasUsers returns a boolean if a field has been set.

### GetId

`func (o *Group) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Group) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Group) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Group) HasId() bool`

HasId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


