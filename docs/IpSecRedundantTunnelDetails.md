# IPSecRedundantTunnelDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Passphrase** | **string** | Pre-shared key for tunnel authentication. 8-64 characters, using letters, digits, \&quot;.\&quot; and \&quot;_\&quot; only; the first character cannot be \&quot;0\&quot;.  | 
**P81GWInternalIP** | **string** |  | 
**RemoteGWInternalIP** | **string** |  | 
**RemotePublicIP** | **string** |  | 
**RemoteASN** | **int32** | BGP ASN of the remote gateway. Must differ from the ASN of the Check Point SASE side (&#x60;p81ASN&#x60; in &#x60;sharedSettings&#x60;).  | 
**RemoteID** | **string** | IKE identity presented by the remote gateway. Either an IP address or an alphanumeric string of 3-25 characters. It must match the local identity configured on the remote device, otherwise phase 1 negotiation fails.  | 

## Methods

### NewIPSecRedundantTunnelDetails

`func NewIPSecRedundantTunnelDetails(passphrase string, p81GWInternalIP string, remoteGWInternalIP string, remotePublicIP string, remoteASN int32, remoteID string, ) *IPSecRedundantTunnelDetails`

NewIPSecRedundantTunnelDetails instantiates a new IPSecRedundantTunnelDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIPSecRedundantTunnelDetailsWithDefaults

`func NewIPSecRedundantTunnelDetailsWithDefaults() *IPSecRedundantTunnelDetails`

NewIPSecRedundantTunnelDetailsWithDefaults instantiates a new IPSecRedundantTunnelDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPassphrase

`func (o *IPSecRedundantTunnelDetails) GetPassphrase() string`

GetPassphrase returns the Passphrase field if non-nil, zero value otherwise.

### GetPassphraseOk

`func (o *IPSecRedundantTunnelDetails) GetPassphraseOk() (*string, bool)`

GetPassphraseOk returns a tuple with the Passphrase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassphrase

`func (o *IPSecRedundantTunnelDetails) SetPassphrase(v string)`

SetPassphrase sets Passphrase field to given value.


### GetP81GWInternalIP

`func (o *IPSecRedundantTunnelDetails) GetP81GWInternalIP() string`

GetP81GWInternalIP returns the P81GWInternalIP field if non-nil, zero value otherwise.

### GetP81GWInternalIPOk

`func (o *IPSecRedundantTunnelDetails) GetP81GWInternalIPOk() (*string, bool)`

GetP81GWInternalIPOk returns a tuple with the P81GWInternalIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetP81GWInternalIP

`func (o *IPSecRedundantTunnelDetails) SetP81GWInternalIP(v string)`

SetP81GWInternalIP sets P81GWInternalIP field to given value.


### GetRemoteGWInternalIP

`func (o *IPSecRedundantTunnelDetails) GetRemoteGWInternalIP() string`

GetRemoteGWInternalIP returns the RemoteGWInternalIP field if non-nil, zero value otherwise.

### GetRemoteGWInternalIPOk

`func (o *IPSecRedundantTunnelDetails) GetRemoteGWInternalIPOk() (*string, bool)`

GetRemoteGWInternalIPOk returns a tuple with the RemoteGWInternalIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteGWInternalIP

`func (o *IPSecRedundantTunnelDetails) SetRemoteGWInternalIP(v string)`

SetRemoteGWInternalIP sets RemoteGWInternalIP field to given value.


### GetRemotePublicIP

`func (o *IPSecRedundantTunnelDetails) GetRemotePublicIP() string`

GetRemotePublicIP returns the RemotePublicIP field if non-nil, zero value otherwise.

### GetRemotePublicIPOk

`func (o *IPSecRedundantTunnelDetails) GetRemotePublicIPOk() (*string, bool)`

GetRemotePublicIPOk returns a tuple with the RemotePublicIP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemotePublicIP

`func (o *IPSecRedundantTunnelDetails) SetRemotePublicIP(v string)`

SetRemotePublicIP sets RemotePublicIP field to given value.


### GetRemoteASN

`func (o *IPSecRedundantTunnelDetails) GetRemoteASN() int32`

GetRemoteASN returns the RemoteASN field if non-nil, zero value otherwise.

### GetRemoteASNOk

`func (o *IPSecRedundantTunnelDetails) GetRemoteASNOk() (*int32, bool)`

GetRemoteASNOk returns a tuple with the RemoteASN field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteASN

`func (o *IPSecRedundantTunnelDetails) SetRemoteASN(v int32)`

SetRemoteASN sets RemoteASN field to given value.


### GetRemoteID

`func (o *IPSecRedundantTunnelDetails) GetRemoteID() string`

GetRemoteID returns the RemoteID field if non-nil, zero value otherwise.

### GetRemoteIDOk

`func (o *IPSecRedundantTunnelDetails) GetRemoteIDOk() (*string, bool)`

GetRemoteIDOk returns a tuple with the RemoteID field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemoteID

`func (o *IPSecRedundantTunnelDetails) SetRemoteID(v string)`

SetRemoteID sets RemoteID field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


