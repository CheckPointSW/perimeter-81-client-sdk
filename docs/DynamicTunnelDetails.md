# DynamicTunnelDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | **string** | Authentication type for tunnel (psk for pre-shared key, cert for certificate) | 
**Passphrase** | Pointer to **string** | Pre-shared key for tunnel authentication (8-64 characters). Required when authType is psk. | [optional] 
**CustomerRootCA** | Pointer to **string** | Customer root certificate authority. Required when authType is cert. | [optional] 
**RegionID** | **string** | Dynamic tunnel enhanced region ID | 
**P81GWInternalIP** | **string** | Harmony Sase gateway internal IP address | 
**RemoteGWInternalIP** | **string** | Remote gateway internal IP address | 
**RemotePublicIP** | **string** | Remote gateway public IP address | 
**RemoteASN** | **int32** | Autonomous System Number (ASN) for BGP routing. It will be automatically assigned an ASN once creating the first dynamic tunnel in this network. The network ASN can never be changed once it is set. | 
**RemoteID** | **string** | Remote gateway ID | 
**RoutingType** | [**RoutingType**](RoutingType.md) |  | [default to ROUTINGTYPE_ROUTE]

## Methods

### NewDynamicTunnelDetails

`func NewDynamicTunnelDetails(authType string, regionID string, p81GWInternalIP string, remoteGWInternalIP string, remotePublicIP string, remoteASN int32, remoteID string, routingType RoutingType, ) *DynamicTunnelDetails`

NewDynamicTunnelDetails instantiates a new DynamicTunnelDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDynamicTunnelDetailsWithDefaults

`func NewDynamicTunnelDetailsWithDefaults() *DynamicTunnelDetails`

NewDynamicTunnelDetailsWithDefaults instantiates a new DynamicTunnelDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthType

`func (o *DynamicTunnelDetails) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *DynamicTunnelDetails) GetAuthTypeOk() (*string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthType

`func (o *DynamicTunnelDetails) SetAuthType(v string)`

SetAuthType sets AuthType field to given value.


### GetPassphrase

`func (o *DynamicTunnelDetails) GetPassphrase() string`

GetPassphrase returns the Passphrase field if non-nil, zero value otherwise.

### GetPassphraseOk

`func (o *DynamicTunnelDetails) GetPassphraseOk() (*string, bool)`

GetPassphraseOk returns a tuple with the Passphrase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassphrase

`func (o *DynamicTunnelDetails) SetPassphrase(v string)`

SetPassphrase sets Passphrase field to given value.

### HasPassphrase

`func (o *DynamicTunnelDetails) HasPassphrase() bool`

HasPassphrase returns a boolean if a field has been set.

### GetCustomerRootCA

`func (o *DynamicTunnelDetails) GetCustomerRootCA() string`

GetCustomerRootCA returns the CustomerRootCA field if non-nil, zero value otherwise.

### GetCustomerRootCAOk

`func (o *DynamicTunnelDetails) GetCustomerRootCAOk() (*string, bool)`

GetCustomerRootCAOk returns a tuple with the CustomerRootCA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerRootCA

`func (o *DynamicTunnelDetails) SetCustomerRootCA(v string)`

SetCustomerRootCA sets CustomerRootCA field to given value.

### HasCustomerRootCA

`func (o *DynamicTunnelDetails) HasCustomerRootCA() bool`

HasCustomerRootCA returns a boolean if a field has been set.

### GetRegionID

`func (o *DynamicTunnelDetails) GetRegionID() string`

GetRegionID returns the RegionID field if non-nil, zero value otherwise.

### GetRegionIDOk

`func (o *DynamicTunnelDetails) GetRegionIDOk() (*string, bool)`

GetRegionIDOk returns a tuple with the RegionID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegionID

`func (o *DynamicTunnelDetails) SetRegionID(v string)`

SetRegionID sets RegionID field to given value.


### GetP81GWInternalIP

`func (o *DynamicTunnelDetails) GetP81GWInternalIP() string`

GetP81GWInternalIP returns the P81GWInternalIP field if non-nil, zero value otherwise.

### GetP81GWInternalIPOk

`func (o *DynamicTunnelDetails) GetP81GWInternalIPOk() (*string, bool)`

GetP81GWInternalIPOk returns a tuple with the P81GWInternalIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GWInternalIP

`func (o *DynamicTunnelDetails) SetP81GWInternalIP(v string)`

SetP81GWInternalIP sets P81GWInternalIP field to given value.


### GetRemoteGWInternalIP

`func (o *DynamicTunnelDetails) GetRemoteGWInternalIP() string`

GetRemoteGWInternalIP returns the RemoteGWInternalIP field if non-nil, zero value otherwise.

### GetRemoteGWInternalIPOk

`func (o *DynamicTunnelDetails) GetRemoteGWInternalIPOk() (*string, bool)`

GetRemoteGWInternalIPOk returns a tuple with the RemoteGWInternalIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGWInternalIP

`func (o *DynamicTunnelDetails) SetRemoteGWInternalIP(v string)`

SetRemoteGWInternalIP sets RemoteGWInternalIP field to given value.


### GetRemotePublicIP

`func (o *DynamicTunnelDetails) GetRemotePublicIP() string`

GetRemotePublicIP returns the RemotePublicIP field if non-nil, zero value otherwise.

### GetRemotePublicIPOk

`func (o *DynamicTunnelDetails) GetRemotePublicIPOk() (*string, bool)`

GetRemotePublicIPOk returns a tuple with the RemotePublicIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemotePublicIP

`func (o *DynamicTunnelDetails) SetRemotePublicIP(v string)`

SetRemotePublicIP sets RemotePublicIP field to given value.


### GetRemoteASN

`func (o *DynamicTunnelDetails) GetRemoteASN() int32`

GetRemoteASN returns the RemoteASN field if non-nil, zero value otherwise.

### GetRemoteASNOk

`func (o *DynamicTunnelDetails) GetRemoteASNOk() (*int32, bool)`

GetRemoteASNOk returns a tuple with the RemoteASN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteASN

`func (o *DynamicTunnelDetails) SetRemoteASN(v int32)`

SetRemoteASN sets RemoteASN field to given value.


### GetRemoteID

`func (o *DynamicTunnelDetails) GetRemoteID() string`

GetRemoteID returns the RemoteID field if non-nil, zero value otherwise.

### GetRemoteIDOk

`func (o *DynamicTunnelDetails) GetRemoteIDOk() (*string, bool)`

GetRemoteIDOk returns a tuple with the RemoteID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteID

`func (o *DynamicTunnelDetails) SetRemoteID(v string)`

SetRemoteID sets RemoteID field to given value.


### GetRoutingType

`func (o *DynamicTunnelDetails) GetRoutingType() RoutingType`

GetRoutingType returns the RoutingType field if non-nil, zero value otherwise.

### GetRoutingTypeOk

`func (o *DynamicTunnelDetails) GetRoutingTypeOk() (*RoutingType, bool)`

GetRoutingTypeOk returns a tuple with the RoutingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoutingType

`func (o *DynamicTunnelDetails) SetRoutingType(v RoutingType)`

SetRoutingType sets RoutingType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


