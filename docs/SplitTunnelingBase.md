# SplitTunnelingBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DefaultTunnelingMode** | **string** | via_tunnel: Tunnel all internet traffic via Cloud, except the destinations listed in exceptData. out_of_tunnel: Do not tunnel internet traffic via Cloud, except the destinations listed in exceptData  (i.e., only these destinations will be tunnelled).  | 
**ExceptData** | [**SplitTunnelingData**](SplitTunnelingData.md) |  | 

## Methods

### NewSplitTunnelingBase

`func NewSplitTunnelingBase(defaultTunnelingMode string, exceptData SplitTunnelingData, ) *SplitTunnelingBase`

NewSplitTunnelingBase instantiates a new SplitTunnelingBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSplitTunnelingBaseWithDefaults

`func NewSplitTunnelingBaseWithDefaults() *SplitTunnelingBase`

NewSplitTunnelingBaseWithDefaults instantiates a new SplitTunnelingBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDefaultTunnelingMode

`func (o *SplitTunnelingBase) GetDefaultTunnelingMode() string`

GetDefaultTunnelingMode returns the DefaultTunnelingMode field if non-nil, zero value otherwise.

### GetDefaultTunnelingModeOk

`func (o *SplitTunnelingBase) GetDefaultTunnelingModeOk() (*string, bool)`

GetDefaultTunnelingModeOk returns a tuple with the DefaultTunnelingMode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultTunnelingMode

`func (o *SplitTunnelingBase) SetDefaultTunnelingMode(v string)`

SetDefaultTunnelingMode sets DefaultTunnelingMode field to given value.


### GetExceptData

`func (o *SplitTunnelingBase) GetExceptData() SplitTunnelingData`

GetExceptData returns the ExceptData field if non-nil, zero value otherwise.

### GetExceptDataOk

`func (o *SplitTunnelingBase) GetExceptDataOk() (*SplitTunnelingData, bool)`

GetExceptDataOk returns a tuple with the ExceptData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExceptData

`func (o *SplitTunnelingBase) SetExceptData(v SplitTunnelingData)`

SetExceptData sets ExceptData field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


