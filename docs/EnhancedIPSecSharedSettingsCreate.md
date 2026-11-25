# EnhancedIPSecSharedSettingsCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**P81GatewaySubnets** | **[]string** | Traffic selectors for the Check Point SASE side of the tunnel, meaning the subnets reachable *through* the SASE network. Must be CIDR notation. Only two values are accepted: either \&quot;0.0.0.0/0\&quot;, to route all traffic through the tunnel, or the network&#39;s own subnet.  | 
**RemoteGatewaySubnets** | **[]string** | Traffic selectors for the customer side of the tunnel, meaning the on-premises subnets reachable *behind* the remote gateway. Values must be in CIDR notation.  | 
**Features** | [**NetworkFeaturesCreate**](NetworkFeaturesCreate.md) |  | 
**LeftASN** | **int32** | BGP ASN of the Check Point SASE side of the tunnel. The first dynamic tunnel created on a network fixes the network&#39;s ASN; every later dynamic tunnel on that network must send the same value. The ASN can never be changed once set.  | 
**PeakBandwidthMbps** | Pointer to **int32** | Deprecated: ignored for non-China regions. China regions still use this field. Expected peak throughput of the tunnel in Mbps. A typical connection is 1000. Consumes bandwidth licenses, so set it no higher than the tunnel needs.  | [optional] [default to 1000]

## Methods

### NewEnhancedIPSecSharedSettingsCreate

`func NewEnhancedIPSecSharedSettingsCreate(p81GatewaySubnets []string, remoteGatewaySubnets []string, features NetworkFeaturesCreate, leftASN int32, ) *EnhancedIPSecSharedSettingsCreate`

NewEnhancedIPSecSharedSettingsCreate instantiates a new EnhancedIPSecSharedSettingsCreate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEnhancedIPSecSharedSettingsCreateWithDefaults

`func NewEnhancedIPSecSharedSettingsCreateWithDefaults() *EnhancedIPSecSharedSettingsCreate`

NewEnhancedIPSecSharedSettingsCreateWithDefaults instantiates a new EnhancedIPSecSharedSettingsCreate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsCreate) GetP81GatewaySubnets() []string`

GetP81GatewaySubnets returns the P81GatewaySubnets field if non-nil, zero value otherwise.

### GetP81GatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsCreate) GetP81GatewaySubnetsOk() (*[]string, bool)`

GetP81GatewaySubnetsOk returns a tuple with the P81GatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsCreate) SetP81GatewaySubnets(v []string)`

SetP81GatewaySubnets sets P81GatewaySubnets field to given value.


### GetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsCreate) GetRemoteGatewaySubnets() []string`

GetRemoteGatewaySubnets returns the RemoteGatewaySubnets field if non-nil, zero value otherwise.

### GetRemoteGatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsCreate) GetRemoteGatewaySubnetsOk() (*[]string, bool)`

GetRemoteGatewaySubnetsOk returns a tuple with the RemoteGatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsCreate) SetRemoteGatewaySubnets(v []string)`

SetRemoteGatewaySubnets sets RemoteGatewaySubnets field to given value.


### GetFeatures

`func (o *EnhancedIPSecSharedSettingsCreate) GetFeatures() NetworkFeaturesCreate`

GetFeatures returns the Features field if non-nil, zero value otherwise.

### GetFeaturesOk

`func (o *EnhancedIPSecSharedSettingsCreate) GetFeaturesOk() (*NetworkFeaturesCreate, bool)`

GetFeaturesOk returns a tuple with the Features field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeatures

`func (o *EnhancedIPSecSharedSettingsCreate) SetFeatures(v NetworkFeaturesCreate)`

SetFeatures sets Features field to given value.


### GetLeftASN

`func (o *EnhancedIPSecSharedSettingsCreate) GetLeftASN() int32`

GetLeftASN returns the LeftASN field if non-nil, zero value otherwise.

### GetLeftASNOk

`func (o *EnhancedIPSecSharedSettingsCreate) GetLeftASNOk() (*int32, bool)`

GetLeftASNOk returns a tuple with the LeftASN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLeftASN

`func (o *EnhancedIPSecSharedSettingsCreate) SetLeftASN(v int32)`

SetLeftASN sets LeftASN field to given value.


### GetPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsCreate) GetPeakBandwidthMbps() int32`

GetPeakBandwidthMbps returns the PeakBandwidthMbps field if non-nil, zero value otherwise.

### GetPeakBandwidthMbpsOk

`func (o *EnhancedIPSecSharedSettingsCreate) GetPeakBandwidthMbpsOk() (*int32, bool)`

GetPeakBandwidthMbpsOk returns a tuple with the PeakBandwidthMbps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsCreate) SetPeakBandwidthMbps(v int32)`

SetPeakBandwidthMbps sets PeakBandwidthMbps field to given value.

### HasPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsCreate) HasPeakBandwidthMbps() bool`

HasPeakBandwidthMbps returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


