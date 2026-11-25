# InspectionPort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Protocol** | **string** |  | 
**Port** | **int32** |  | 
**Description** | Pointer to **string** |  | [optional] 

## Methods

### NewInspectionPort

`func NewInspectionPort(protocol string, port int32, ) *InspectionPort`

NewInspectionPort instantiates a new InspectionPort object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInspectionPortWithDefaults

`func NewInspectionPortWithDefaults() *InspectionPort`

NewInspectionPortWithDefaults instantiates a new InspectionPort object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProtocol

`func (o *InspectionPort) GetProtocol() string`

GetProtocol returns the Protocol field if non-nil, zero value otherwise.

### GetProtocolOk

`func (o *InspectionPort) GetProtocolOk() (*string, bool)`

GetProtocolOk returns a tuple with the Protocol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProtocol

`func (o *InspectionPort) SetProtocol(v string)`

SetProtocol sets Protocol field to given value.


### GetPort

`func (o *InspectionPort) GetPort() int32`

GetPort returns the Port field if non-nil, zero value otherwise.

### GetPortOk

`func (o *InspectionPort) GetPortOk() (*int32, bool)`

GetPortOk returns a tuple with the Port field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPort

`func (o *InspectionPort) SetPort(v int32)`

SetPort sets Port field to given value.


### GetDescription

`func (o *InspectionPort) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *InspectionPort) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *InspectionPort) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *InspectionPort) HasDescription() bool`

HasDescription returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


