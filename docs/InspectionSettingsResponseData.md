# InspectionSettingsResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ports** | Pointer to [**[]InspectionPort**](InspectionPort.md) |  | [optional] 
**InvalidCertificatesSettings** | Pointer to [**[]CertificateRule**](CertificateRule.md) |  | [optional] 
**RevocationCheckTimeoutMs** | Pointer to **int32** | Maximum time in milliseconds to wait for a certificate revocation check (OCSP/CRL). Returns the tenant&#39;s value, or the default (2000) when none is set. Omitted when certificate validation is not enabled for the tenant.  | [optional] 
**CrliteEnabled** | Pointer to **bool** | Whether CRLite is used for server certificate revocation checks. Returns the tenant&#39;s value, or true (default) when none is set. Omitted when certificate validation is not enabled for the tenant.  | [optional] 

## Methods

### NewInspectionSettingsResponseData

`func NewInspectionSettingsResponseData() *InspectionSettingsResponseData`

NewInspectionSettingsResponseData instantiates a new InspectionSettingsResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInspectionSettingsResponseDataWithDefaults

`func NewInspectionSettingsResponseDataWithDefaults() *InspectionSettingsResponseData`

NewInspectionSettingsResponseDataWithDefaults instantiates a new InspectionSettingsResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPorts

`func (o *InspectionSettingsResponseData) GetPorts() []InspectionPort`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *InspectionSettingsResponseData) GetPortsOk() (*[]InspectionPort, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *InspectionSettingsResponseData) SetPorts(v []InspectionPort)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *InspectionSettingsResponseData) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetInvalidCertificatesSettings

`func (o *InspectionSettingsResponseData) GetInvalidCertificatesSettings() []CertificateRule`

GetInvalidCertificatesSettings returns the InvalidCertificatesSettings field if non-nil, zero value otherwise.

### GetInvalidCertificatesSettingsOk

`func (o *InspectionSettingsResponseData) GetInvalidCertificatesSettingsOk() (*[]CertificateRule, bool)`

GetInvalidCertificatesSettingsOk returns a tuple with the InvalidCertificatesSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvalidCertificatesSettings

`func (o *InspectionSettingsResponseData) SetInvalidCertificatesSettings(v []CertificateRule)`

SetInvalidCertificatesSettings sets InvalidCertificatesSettings field to given value.

### HasInvalidCertificatesSettings

`func (o *InspectionSettingsResponseData) HasInvalidCertificatesSettings() bool`

HasInvalidCertificatesSettings returns a boolean if a field has been set.

### GetRevocationCheckTimeoutMs

`func (o *InspectionSettingsResponseData) GetRevocationCheckTimeoutMs() int32`

GetRevocationCheckTimeoutMs returns the RevocationCheckTimeoutMs field if non-nil, zero value otherwise.

### GetRevocationCheckTimeoutMsOk

`func (o *InspectionSettingsResponseData) GetRevocationCheckTimeoutMsOk() (*int32, bool)`

GetRevocationCheckTimeoutMsOk returns a tuple with the RevocationCheckTimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevocationCheckTimeoutMs

`func (o *InspectionSettingsResponseData) SetRevocationCheckTimeoutMs(v int32)`

SetRevocationCheckTimeoutMs sets RevocationCheckTimeoutMs field to given value.

### HasRevocationCheckTimeoutMs

`func (o *InspectionSettingsResponseData) HasRevocationCheckTimeoutMs() bool`

HasRevocationCheckTimeoutMs returns a boolean if a field has been set.

### GetCrliteEnabled

`func (o *InspectionSettingsResponseData) GetCrliteEnabled() bool`

GetCrliteEnabled returns the CrliteEnabled field if non-nil, zero value otherwise.

### GetCrliteEnabledOk

`func (o *InspectionSettingsResponseData) GetCrliteEnabledOk() (*bool, bool)`

GetCrliteEnabledOk returns a tuple with the CrliteEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrliteEnabled

`func (o *InspectionSettingsResponseData) SetCrliteEnabled(v bool)`

SetCrliteEnabled sets CrliteEnabled field to given value.

### HasCrliteEnabled

`func (o *InspectionSettingsResponseData) HasCrliteEnabled() bool`

HasCrliteEnabled returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


