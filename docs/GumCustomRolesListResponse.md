# GumCustomRolesListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Roles** | [**[]CustomRoleItem**](CustomRoleItem.md) |  | 
**Total** | **int32** |  | 

## Methods

### NewGumCustomRolesListResponse

`func NewGumCustomRolesListResponse(roles []CustomRoleItem, total int32, ) *GumCustomRolesListResponse`

NewGumCustomRolesListResponse instantiates a new GumCustomRolesListResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGumCustomRolesListResponseWithDefaults

`func NewGumCustomRolesListResponseWithDefaults() *GumCustomRolesListResponse`

NewGumCustomRolesListResponseWithDefaults instantiates a new GumCustomRolesListResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRoles

`func (o *GumCustomRolesListResponse) GetRoles() []CustomRoleItem`

GetRoles returns the Roles field if non-nil, zero value otherwise.

### GetRolesOk

`func (o *GumCustomRolesListResponse) GetRolesOk() (*[]CustomRoleItem, bool)`

GetRolesOk returns a tuple with the Roles field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoles

`func (o *GumCustomRolesListResponse) SetRoles(v []CustomRoleItem)`

SetRoles sets Roles field to given value.


### GetTotal

`func (o *GumCustomRolesListResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *GumCustomRolesListResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *GumCustomRolesListResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


