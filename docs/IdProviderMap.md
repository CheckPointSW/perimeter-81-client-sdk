# IdProviderMap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AdLdap** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 
**AzureAD** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 
**Database** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 
**Gsuite** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 
**Okta** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 
**Saml** | Pointer to [**IdProvider**](IdProvider.md) |  | [optional] 

## Methods

### NewIdProviderMap

`func NewIdProviderMap() *IdProviderMap`

NewIdProviderMap instantiates a new IdProviderMap object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIdProviderMapWithDefaults

`func NewIdProviderMapWithDefaults() *IdProviderMap`

NewIdProviderMapWithDefaults instantiates a new IdProviderMap object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAdLdap

`func (o *IdProviderMap) GetAdLdap() IdProvider`

GetAdLdap returns the AdLdap field if non-nil, zero value otherwise.

### GetAdLdapOk

`func (o *IdProviderMap) GetAdLdapOk() (*IdProvider, bool)`

GetAdLdapOk returns a tuple with the AdLdap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdLdap

`func (o *IdProviderMap) SetAdLdap(v IdProvider)`

SetAdLdap sets AdLdap field to given value.

### HasAdLdap

`func (o *IdProviderMap) HasAdLdap() bool`

HasAdLdap returns a boolean if a field has been set.

### GetAzureAD

`func (o *IdProviderMap) GetAzureAD() IdProvider`

GetAzureAD returns the AzureAD field if non-nil, zero value otherwise.

### GetAzureADOk

`func (o *IdProviderMap) GetAzureADOk() (*IdProvider, bool)`

GetAzureADOk returns a tuple with the AzureAD field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAzureAD

`func (o *IdProviderMap) SetAzureAD(v IdProvider)`

SetAzureAD sets AzureAD field to given value.

### HasAzureAD

`func (o *IdProviderMap) HasAzureAD() bool`

HasAzureAD returns a boolean if a field has been set.

### GetDatabase

`func (o *IdProviderMap) GetDatabase() IdProvider`

GetDatabase returns the Database field if non-nil, zero value otherwise.

### GetDatabaseOk

`func (o *IdProviderMap) GetDatabaseOk() (*IdProvider, bool)`

GetDatabaseOk returns a tuple with the Database field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatabase

`func (o *IdProviderMap) SetDatabase(v IdProvider)`

SetDatabase sets Database field to given value.

### HasDatabase

`func (o *IdProviderMap) HasDatabase() bool`

HasDatabase returns a boolean if a field has been set.

### GetGsuite

`func (o *IdProviderMap) GetGsuite() IdProvider`

GetGsuite returns the Gsuite field if non-nil, zero value otherwise.

### GetGsuiteOk

`func (o *IdProviderMap) GetGsuiteOk() (*IdProvider, bool)`

GetGsuiteOk returns a tuple with the Gsuite field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGsuite

`func (o *IdProviderMap) SetGsuite(v IdProvider)`

SetGsuite sets Gsuite field to given value.

### HasGsuite

`func (o *IdProviderMap) HasGsuite() bool`

HasGsuite returns a boolean if a field has been set.

### GetOkta

`func (o *IdProviderMap) GetOkta() IdProvider`

GetOkta returns the Okta field if non-nil, zero value otherwise.

### GetOktaOk

`func (o *IdProviderMap) GetOktaOk() (*IdProvider, bool)`

GetOktaOk returns a tuple with the Okta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOkta

`func (o *IdProviderMap) SetOkta(v IdProvider)`

SetOkta sets Okta field to given value.

### HasOkta

`func (o *IdProviderMap) HasOkta() bool`

HasOkta returns a boolean if a field has been set.

### GetSaml

`func (o *IdProviderMap) GetSaml() IdProvider`

GetSaml returns the Saml field if non-nil, zero value otherwise.

### GetSamlOk

`func (o *IdProviderMap) GetSamlOk() (*IdProvider, bool)`

GetSamlOk returns a tuple with the Saml field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSaml

`func (o *IdProviderMap) SetSaml(v IdProvider)`

SetSaml sets Saml field to given value.

### HasSaml

`func (o *IdProviderMap) HasSaml() bool`

HasSaml returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


