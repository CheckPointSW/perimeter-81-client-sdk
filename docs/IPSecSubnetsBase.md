# IPSecSubnetsBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**P81GatewaySubnets** | **[]string** | Traffic selectors for the Check Point SASE side of the tunnel, meaning the subnets reachable *through* the SASE network. Must be CIDR notation. Only two values are accepted: either \&quot;0.0.0.0/0\&quot;, to route all traffic through the tunnel, or the network&#39;s own subnet.  | 
**RemoteGatewaySubnets** | **[]string** | Traffic selectors for the customer side of the tunnel, meaning the on-premises subnets reachable *behind* the remote gateway. Values must be in CIDR notation.  | 

## Methods

### NewIPSecSubnetsBase

`func NewIPSecSubnetsBase(p81GatewaySubnets []string, remoteGatewaySubnets []string, ) *IPSecSubnetsBase`

NewIPSecSubnetsBase instantiates a new IPSecSubnetsBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIPSecSubnetsBaseWithDefaults

`func NewIPSecSubnetsBaseWithDefaults() *IPSecSubnetsBase`

NewIPSecSubnetsBaseWithDefaults instantiates a new IPSecSubnetsBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetP81GatewaySubnets

`func (o *IPSecSubnetsBase) GetP81GatewaySubnets() []string`

GetP81GatewaySubnets returns the P81GatewaySubnets field if non-nil, zero value otherwise.

### GetP81GatewaySubnetsOk

`func (o *IPSecSubnetsBase) GetP81GatewaySubnetsOk() (*[]string, bool)`

GetP81GatewaySubnetsOk returns a tuple with the P81GatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GatewaySubnets

`func (o *IPSecSubnetsBase) SetP81GatewaySubnets(v []string)`

SetP81GatewaySubnets sets P81GatewaySubnets field to given value.


### GetRemoteGatewaySubnets

`func (o *IPSecSubnetsBase) GetRemoteGatewaySubnets() []string`

GetRemoteGatewaySubnets returns the RemoteGatewaySubnets field if non-nil, zero value otherwise.

### GetRemoteGatewaySubnetsOk

`func (o *IPSecSubnetsBase) GetRemoteGatewaySubnetsOk() (*[]string, bool)`

GetRemoteGatewaySubnetsOk returns a tuple with the RemoteGatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGatewaySubnets

`func (o *IPSecSubnetsBase) SetRemoteGatewaySubnets(v []string)`

SetRemoteGatewaySubnets sets RemoteGatewaySubnets field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


