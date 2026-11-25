# EnhancedIPSecSharedSettingsUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**P81GatewaySubnets** | **[]string** | Traffic selectors for the Check Point SASE side of the tunnel, meaning the subnets reachable *through* the SASE network. Must be CIDR notation. Only two values are accepted: either \&quot;0.0.0.0/0\&quot;, to route all traffic through the tunnel, or the network&#39;s own subnet.  | 
**RemoteGatewaySubnets** | **[]string** | Traffic selectors for the customer side of the tunnel, meaning the on-premises subnets reachable *behind* the remote gateway. Values must be in CIDR notation.  | 
**Features** | Pointer to [**NetworkFeaturesCreate**](NetworkFeaturesCreate.md) |  | [optional] 
**PeakBandwidthMbps** | Pointer to **int32** | Deprecated: ignored for non-China regions. China regions still use this field. Expected peak throughput of the tunnel in Mbps. A typical connection is 1000. Consumes bandwidth licenses, so set it no higher than the tunnel needs.  | [optional] [default to 1000]

## Methods

### NewEnhancedIPSecSharedSettingsUpdate

`func NewEnhancedIPSecSharedSettingsUpdate(p81GatewaySubnets []string, remoteGatewaySubnets []string, ) *EnhancedIPSecSharedSettingsUpdate`

NewEnhancedIPSecSharedSettingsUpdate instantiates a new EnhancedIPSecSharedSettingsUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEnhancedIPSecSharedSettingsUpdateWithDefaults

`func NewEnhancedIPSecSharedSettingsUpdateWithDefaults() *EnhancedIPSecSharedSettingsUpdate`

NewEnhancedIPSecSharedSettingsUpdateWithDefaults instantiates a new EnhancedIPSecSharedSettingsUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81GatewaySubnets() []string`

GetP81GatewaySubnets returns the P81GatewaySubnets field if non-nil, zero value otherwise.

### GetP81GatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetP81GatewaySubnetsOk() (*[]string, bool)`

GetP81GatewaySubnetsOk returns a tuple with the P81GatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) SetP81GatewaySubnets(v []string)`

SetP81GatewaySubnets sets P81GatewaySubnets field to given value.


### GetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) GetRemoteGatewaySubnets() []string`

GetRemoteGatewaySubnets returns the RemoteGatewaySubnets field if non-nil, zero value otherwise.

### GetRemoteGatewaySubnetsOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetRemoteGatewaySubnetsOk() (*[]string, bool)`

GetRemoteGatewaySubnetsOk returns a tuple with the RemoteGatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGatewaySubnets

`func (o *EnhancedIPSecSharedSettingsUpdate) SetRemoteGatewaySubnets(v []string)`

SetRemoteGatewaySubnets sets RemoteGatewaySubnets field to given value.


### GetFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) GetFeatures() NetworkFeaturesCreate`

GetFeatures returns the Features field if non-nil, zero value otherwise.

### GetFeaturesOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetFeaturesOk() (*NetworkFeaturesCreate, bool)`

GetFeaturesOk returns a tuple with the Features field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) SetFeatures(v NetworkFeaturesCreate)`

SetFeatures sets Features field to given value.

### HasFeatures

`func (o *EnhancedIPSecSharedSettingsUpdate) HasFeatures() bool`

HasFeatures returns a boolean if a field has been set.

### GetPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsUpdate) GetPeakBandwidthMbps() int32`

GetPeakBandwidthMbps returns the PeakBandwidthMbps field if non-nil, zero value otherwise.

### GetPeakBandwidthMbpsOk

`func (o *EnhancedIPSecSharedSettingsUpdate) GetPeakBandwidthMbpsOk() (*int32, bool)`

GetPeakBandwidthMbpsOk returns a tuple with the PeakBandwidthMbps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsUpdate) SetPeakBandwidthMbps(v int32)`

SetPeakBandwidthMbps sets PeakBandwidthMbps field to given value.

### HasPeakBandwidthMbps

`func (o *EnhancedIPSecSharedSettingsUpdate) HasPeakBandwidthMbps() bool`

HasPeakBandwidthMbps returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


