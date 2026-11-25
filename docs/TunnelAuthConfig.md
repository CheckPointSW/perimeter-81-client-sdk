# TunnelAuthConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuthType** | Pointer to **string** | Authentication method for the tunnel. \&quot;psk\&quot; (pre-shared key) requires &#x60;passphrase&#x60; and forbids &#x60;customerRootCA&#x60;; \&quot;cert\&quot; (certificate) requires &#x60;customerRootCA&#x60; and forbids &#x60;passphrase&#x60;.  | [optional] 
**Passphrase** | Pointer to **string** | Pre-shared key for tunnel authentication. Required when &#x60;authType&#x60; is \&quot;psk\&quot;, and must be omitted when &#x60;authType&#x60; is \&quot;cert\&quot;. 8-64 characters, using letters, digits, \&quot;.\&quot; and \&quot;_\&quot; only; the first character cannot be \&quot;0\&quot;.  | [optional] 
**CustomerRootCA** | Pointer to **string** | ID of a CA certificate stored in the certificate store. Exactly 10 characters. Required when &#x60;authType&#x60; is \&quot;cert\&quot;, and must be omitted when &#x60;authType&#x60; is \&quot;psk\&quot;.  | [optional] 

## Methods

### NewTunnelAuthConfig

`func NewTunnelAuthConfig() *TunnelAuthConfig`

NewTunnelAuthConfig instantiates a new TunnelAuthConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTunnelAuthConfigWithDefaults

`func NewTunnelAuthConfigWithDefaults() *TunnelAuthConfig`

NewTunnelAuthConfigWithDefaults instantiates a new TunnelAuthConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthType

`func (o *TunnelAuthConfig) GetAuthType() string`

GetAuthType returns the AuthType field if non-nil, zero value otherwise.

### GetAuthTypeOk

`func (o *TunnelAuthConfig) GetAuthTypeOk() (*string, bool)`

GetAuthTypeOk returns a tuple with the AuthType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthType

`func (o *TunnelAuthConfig) SetAuthType(v string)`

SetAuthType sets AuthType field to given value.

### HasAuthType

`func (o *TunnelAuthConfig) HasAuthType() bool`

HasAuthType returns a boolean if a field has been set.

### GetPassphrase

`func (o *TunnelAuthConfig) GetPassphrase() string`

GetPassphrase returns the Passphrase field if non-nil, zero value otherwise.

### GetPassphraseOk

`func (o *TunnelAuthConfig) GetPassphraseOk() (*string, bool)`

GetPassphraseOk returns a tuple with the Passphrase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPassphrase

`func (o *TunnelAuthConfig) SetPassphrase(v string)`

SetPassphrase sets Passphrase field to given value.

### HasPassphrase

`func (o *TunnelAuthConfig) HasPassphrase() bool`

HasPassphrase returns a boolean if a field has been set.

### GetCustomerRootCA

`func (o *TunnelAuthConfig) GetCustomerRootCA() string`

GetCustomerRootCA returns the CustomerRootCA field if non-nil, zero value otherwise.

### GetCustomerRootCAOk

`func (o *TunnelAuthConfig) GetCustomerRootCAOk() (*string, bool)`

GetCustomerRootCAOk returns a tuple with the CustomerRootCA field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomerRootCA

`func (o *TunnelAuthConfig) SetCustomerRootCA(v string)`

SetCustomerRootCA sets CustomerRootCA field to given value.

### HasCustomerRootCA

`func (o *TunnelAuthConfig) HasCustomerRootCA() bool`

HasCustomerRootCA returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


