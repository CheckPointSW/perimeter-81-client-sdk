# DBAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** |  | [optional] 
**Attributes** | Pointer to [**Address**](Address.md) |  | [optional] 

## Methods

### NewDBAddress

`func NewDBAddress() *DBAddress`

NewDBAddress instantiates a new DBAddress object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDBAddressWithDefaults

`func NewDBAddressWithDefaults() *DBAddress`

NewDBAddressWithDefaults instantiates a new DBAddress object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DBAddress) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DBAddress) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DBAddress) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *DBAddress) HasId() bool`

HasId returns a boolean if a field has been set.

### GetAttributes

`func (o *DBAddress) GetAttributes() Address`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *DBAddress) GetAttributesOk() (*Address, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *DBAddress) SetAttributes(v Address)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *DBAddress) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


