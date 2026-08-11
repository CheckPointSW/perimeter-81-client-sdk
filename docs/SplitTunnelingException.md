# SplitTunnelingException

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Type of destination. | [default to "cidr"]
**Destination** | **string** | IP or CIDR string, e.g. \&quot;10.1.2.0/24\&quot; or \&quot;10.1.2.3/32\&quot;. | 

## Methods

### NewSplitTunnelingException

`func NewSplitTunnelingException(type_ string, destination string, ) *SplitTunnelingException`

NewSplitTunnelingException instantiates a new SplitTunnelingException object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSplitTunnelingExceptionWithDefaults

`func NewSplitTunnelingExceptionWithDefaults() *SplitTunnelingException`

NewSplitTunnelingExceptionWithDefaults instantiates a new SplitTunnelingException object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *SplitTunnelingException) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SplitTunnelingException) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SplitTunnelingException) SetType(v string)`

SetType sets Type field to given value.


### GetDestination

`func (o *SplitTunnelingException) GetDestination() string`

GetDestination returns the Destination field if non-nil, zero value otherwise.

### GetDestinationOk

`func (o *SplitTunnelingException) GetDestinationOk() (*string, bool)`

GetDestinationOk returns a tuple with the Destination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestination

`func (o *SplitTunnelingException) SetDestination(v string)`

SetDestination sets Destination field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


