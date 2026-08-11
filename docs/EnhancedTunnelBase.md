# EnhancedTunnelBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | **string** | Authentication type for tunnel (psk for pre-shared key, cert for certificate) | 
**Passphrase** | Pointer to **string** | Pre-shared key for tunnel authentication (8-64 characters). Required when authType is psk. | [optional] 
**CustomerRootCA** | Pointer to **string** | Customer root certificate authority. Required when authType is cert. | [optional] 
**RegionID** | **string** | Target region ID | 
**TunnelName** | **string** | Name of the static tunnel | 
**P81GatewaySubnets** | **[]string** | Harmony Sase gateway subnets | 
**RemoteGatewaySubnets** | **[]string** | Remote gateway subnets | 
**KeyExchange** | **string** | IKE version for key exchange | [default to "ikev2"]
**AdvancedSettings** | Pointer to [**IPSecAdvancedSettingsV23**](IPSecAdvancedSettingsV23.md) |  | [optional] 
**RoutingType** | Pointer to [**RoutingType**](RoutingType.md) |  | [optional] [default to ROUTE]
**PeakBandwidthMbps** | Pointer to **int32** | Expected peak throughput of the tunnel communication in Mbps. Typical connection will be of 1000Mbps. | [optional] [default to 1000]

## Methods

### NewEnhancedTunnelBase

`func NewEnhancedTunnelBase(authType string, regionID string, tunnelName string, p81GatewaySubnets []string, remoteGatewaySubnets []string, keyExchange string, ) *EnhancedTunnelBase`

NewEnhancedTunnelBase instantiates a new EnhancedTunnelBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEnhancedTunnelBaseWithDefaults

`func NewEnhancedTunnelBaseWithDefaults() *EnhancedTunnelBase`

NewEnhancedTunnelBaseWithDefaults instantiates a new EnhancedTunnelBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthType

`func (o *EnhancedTunnelBase) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *EnhancedTunnelBase) GetAuthTypeOk() (*string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthType

`func (o *EnhancedTunnelBase) SetAuthType(v string)`

SetAuthType sets AuthType field to given value.


### GetPassphrase

`func (o *EnhancedTunnelBase) GetPassphrase() string`

GetPassphrase returns the Passphrase field if non-nil, zero value otherwise.

### GetPassphraseOk

`func (o *EnhancedTunnelBase) GetPassphraseOk() (*string, bool)`

GetPassphraseOk returns a tuple with the Passphrase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassphrase

`func (o *EnhancedTunnelBase) SetPassphrase(v string)`

SetPassphrase sets Passphrase field to given value.

### HasPassphrase

`func (o *EnhancedTunnelBase) HasPassphrase() bool`

HasPassphrase returns a boolean if a field has been set.

### GetCustomerRootCA

`func (o *EnhancedTunnelBase) GetCustomerRootCA() string`

GetCustomerRootCA returns the CustomerRootCA field if non-nil, zero value otherwise.

### GetCustomerRootCAOk

`func (o *EnhancedTunnelBase) GetCustomerRootCAOk() (*string, bool)`

GetCustomerRootCAOk returns a tuple with the CustomerRootCA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerRootCA

`func (o *EnhancedTunnelBase) SetCustomerRootCA(v string)`

SetCustomerRootCA sets CustomerRootCA field to given value.

### HasCustomerRootCA

`func (o *EnhancedTunnelBase) HasCustomerRootCA() bool`

HasCustomerRootCA returns a boolean if a field has been set.

### GetRegionID

`func (o *EnhancedTunnelBase) GetRegionID() string`

GetRegionID returns the RegionID field if non-nil, zero value otherwise.

### GetRegionIDOk

`func (o *EnhancedTunnelBase) GetRegionIDOk() (*string, bool)`

GetRegionIDOk returns a tuple with the RegionID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionID

`func (o *EnhancedTunnelBase) SetRegionID(v string)`

SetRegionID sets RegionID field to given value.


### GetTunnelName

`func (o *EnhancedTunnelBase) GetTunnelName() string`

GetTunnelName returns the TunnelName field if non-nil, zero value otherwise.

### GetTunnelNameOk

`func (o *EnhancedTunnelBase) GetTunnelNameOk() (*string, bool)`

GetTunnelNameOk returns a tuple with the TunnelName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTunnelName

`func (o *EnhancedTunnelBase) SetTunnelName(v string)`

SetTunnelName sets TunnelName field to given value.


### GetP81GatewaySubnets

`func (o *EnhancedTunnelBase) GetP81GatewaySubnets() []string`

GetP81GatewaySubnets returns the P81GatewaySubnets field if non-nil, zero value otherwise.

### GetP81GatewaySubnetsOk

`func (o *EnhancedTunnelBase) GetP81GatewaySubnetsOk() (*[]string, bool)`

GetP81GatewaySubnetsOk returns a tuple with the P81GatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GatewaySubnets

`func (o *EnhancedTunnelBase) SetP81GatewaySubnets(v []string)`

SetP81GatewaySubnets sets P81GatewaySubnets field to given value.


### GetRemoteGatewaySubnets

`func (o *EnhancedTunnelBase) GetRemoteGatewaySubnets() []string`

GetRemoteGatewaySubnets returns the RemoteGatewaySubnets field if non-nil, zero value otherwise.

### GetRemoteGatewaySubnetsOk

`func (o *EnhancedTunnelBase) GetRemoteGatewaySubnetsOk() (*[]string, bool)`

GetRemoteGatewaySubnetsOk returns a tuple with the RemoteGatewaySubnets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGatewaySubnets

`func (o *EnhancedTunnelBase) SetRemoteGatewaySubnets(v []string)`

SetRemoteGatewaySubnets sets RemoteGatewaySubnets field to given value.


### GetKeyExchange

`func (o *EnhancedTunnelBase) GetKeyExchange() string`

GetKeyExchange returns the KeyExchange field if non-nil, zero value otherwise.

### GetKeyExchangeOk

`func (o *EnhancedTunnelBase) GetKeyExchangeOk() (*string, bool)`

GetKeyExchangeOk returns a tuple with the KeyExchange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyExchange

`func (o *EnhancedTunnelBase) SetKeyExchange(v string)`

SetKeyExchange sets KeyExchange field to given value.


### GetAdvancedSettings

`func (o *EnhancedTunnelBase) GetAdvancedSettings() IPSecAdvancedSettingsV23`

GetAdvancedSettings returns the AdvancedSettings field if non-nil, zero value otherwise.

### GetAdvancedSettingsOk

`func (o *EnhancedTunnelBase) GetAdvancedSettingsOk() (*IPSecAdvancedSettingsV23, bool)`

GetAdvancedSettingsOk returns a tuple with the AdvancedSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdvancedSettings

`func (o *EnhancedTunnelBase) SetAdvancedSettings(v IPSecAdvancedSettingsV23)`

SetAdvancedSettings sets AdvancedSettings field to given value.

### HasAdvancedSettings

`func (o *EnhancedTunnelBase) HasAdvancedSettings() bool`

HasAdvancedSettings returns a boolean if a field has been set.

### GetRoutingType

`func (o *EnhancedTunnelBase) GetRoutingType() RoutingType`

GetRoutingType returns the RoutingType field if non-nil, zero value otherwise.

### GetRoutingTypeOk

`func (o *EnhancedTunnelBase) GetRoutingTypeOk() (*RoutingType, bool)`

GetRoutingTypeOk returns a tuple with the RoutingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoutingType

`func (o *EnhancedTunnelBase) SetRoutingType(v RoutingType)`

SetRoutingType sets RoutingType field to given value.

### HasRoutingType

`func (o *EnhancedTunnelBase) HasRoutingType() bool`

HasRoutingType returns a boolean if a field has been set.

### GetPeakBandwidthMbps

`func (o *EnhancedTunnelBase) GetPeakBandwidthMbps() int32`

GetPeakBandwidthMbps returns the PeakBandwidthMbps field if non-nil, zero value otherwise.

### GetPeakBandwidthMbpsOk

`func (o *EnhancedTunnelBase) GetPeakBandwidthMbpsOk() (*int32, bool)`

GetPeakBandwidthMbpsOk returns a tuple with the PeakBandwidthMbps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPeakBandwidthMbps

`func (o *EnhancedTunnelBase) SetPeakBandwidthMbps(v int32)`

SetPeakBandwidthMbps sets PeakBandwidthMbps field to given value.

### HasPeakBandwidthMbps

`func (o *EnhancedTunnelBase) HasPeakBandwidthMbps() bool`

HasPeakBandwidthMbps returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


