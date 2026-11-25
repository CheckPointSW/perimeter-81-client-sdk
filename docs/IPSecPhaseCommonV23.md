# IPSecPhaseCommonV23

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**KeyExchangeMethod** | Pointer to **[]string** | Key exchange algorithms offered for this phase. If provided, must contain at least one algorithm, and the remote gateway must support one of the values listed.  | [optional] 

## Methods

### NewIPSecPhaseCommonV23

`func NewIPSecPhaseCommonV23() *IPSecPhaseCommonV23`

NewIPSecPhaseCommonV23 instantiates a new IPSecPhaseCommonV23 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIPSecPhaseCommonV23WithDefaults

`func NewIPSecPhaseCommonV23WithDefaults() *IPSecPhaseCommonV23`

NewIPSecPhaseCommonV23WithDefaults instantiates a new IPSecPhaseCommonV23 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKeyExchangeMethod

`func (o *IPSecPhaseCommonV23) GetKeyExchangeMethod() []string`

GetKeyExchangeMethod returns the KeyExchangeMethod field if non-nil, zero value otherwise.

### GetKeyExchangeMethodOk

`func (o *IPSecPhaseCommonV23) GetKeyExchangeMethodOk() (*[]string, bool)`

GetKeyExchangeMethodOk returns a tuple with the KeyExchangeMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyExchangeMethod

`func (o *IPSecPhaseCommonV23) SetKeyExchangeMethod(v []string)`

SetKeyExchangeMethod sets KeyExchangeMethod field to given value.

### HasKeyExchangeMethod

`func (o *IPSecPhaseCommonV23) HasKeyExchangeMethod() bool`

HasKeyExchangeMethod returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


