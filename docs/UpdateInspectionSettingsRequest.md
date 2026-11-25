# UpdateInspectionSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ports** | Pointer to [**[]InspectionPort**](InspectionPort.md) |  | [optional] 
**InvalidCertificatesSettings** | Pointer to [**[]CertificateRule**](CertificateRule.md) |  | [optional] 
**RevocationCheckTimeoutMs** | Pointer to **int32** | Maximum time in milliseconds to wait for a certificate revocation check (OCSP/CRL). A check that does not finish in time is treated as revocationCheckFailed. Rejected with 403 when certificate validation is not enabled for the tenant.  | [optional] 
**CrliteEnabled** | Pointer to **bool** | Whether CRLite is used for server certificate revocation checks. Omitting it keeps the stored value. A non-boolean value is rejected with 422. Rejected with 403 when certificate validation is not enabled for the tenant.  | [optional] 

## Methods

### NewUpdateInspectionSettingsRequest

`func NewUpdateInspectionSettingsRequest() *UpdateInspectionSettingsRequest`

NewUpdateInspectionSettingsRequest instantiates a new UpdateInspectionSettingsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateInspectionSettingsRequestWithDefaults

`func NewUpdateInspectionSettingsRequestWithDefaults() *UpdateInspectionSettingsRequest`

NewUpdateInspectionSettingsRequestWithDefaults instantiates a new UpdateInspectionSettingsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPorts

`func (o *UpdateInspectionSettingsRequest) GetPorts() []InspectionPort`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *UpdateInspectionSettingsRequest) GetPortsOk() (*[]InspectionPort, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *UpdateInspectionSettingsRequest) SetPorts(v []InspectionPort)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *UpdateInspectionSettingsRequest) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetInvalidCertificatesSettings

`func (o *UpdateInspectionSettingsRequest) GetInvalidCertificatesSettings() []CertificateRule`

GetInvalidCertificatesSettings returns the InvalidCertificatesSettings field if non-nil, zero value otherwise.

### GetInvalidCertificatesSettingsOk

`func (o *UpdateInspectionSettingsRequest) GetInvalidCertificatesSettingsOk() (*[]CertificateRule, bool)`

GetInvalidCertificatesSettingsOk returns a tuple with the InvalidCertificatesSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvalidCertificatesSettings

`func (o *UpdateInspectionSettingsRequest) SetInvalidCertificatesSettings(v []CertificateRule)`

SetInvalidCertificatesSettings sets InvalidCertificatesSettings field to given value.

### HasInvalidCertificatesSettings

`func (o *UpdateInspectionSettingsRequest) HasInvalidCertificatesSettings() bool`

HasInvalidCertificatesSettings returns a boolean if a field has been set.

### GetRevocationCheckTimeoutMs

`func (o *UpdateInspectionSettingsRequest) GetRevocationCheckTimeoutMs() int32`

GetRevocationCheckTimeoutMs returns the RevocationCheckTimeoutMs field if non-nil, zero value otherwise.

### GetRevocationCheckTimeoutMsOk

`func (o *UpdateInspectionSettingsRequest) GetRevocationCheckTimeoutMsOk() (*int32, bool)`

GetRevocationCheckTimeoutMsOk returns a tuple with the RevocationCheckTimeoutMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevocationCheckTimeoutMs

`func (o *UpdateInspectionSettingsRequest) SetRevocationCheckTimeoutMs(v int32)`

SetRevocationCheckTimeoutMs sets RevocationCheckTimeoutMs field to given value.

### HasRevocationCheckTimeoutMs

`func (o *UpdateInspectionSettingsRequest) HasRevocationCheckTimeoutMs() bool`

HasRevocationCheckTimeoutMs returns a boolean if a field has been set.

### GetCrliteEnabled

`func (o *UpdateInspectionSettingsRequest) GetCrliteEnabled() bool`

GetCrliteEnabled returns the CrliteEnabled field if non-nil, zero value otherwise.

### GetCrliteEnabledOk

`func (o *UpdateInspectionSettingsRequest) GetCrliteEnabledOk() (*bool, bool)`

GetCrliteEnabledOk returns a tuple with the CrliteEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCrliteEnabled

`func (o *UpdateInspectionSettingsRequest) SetCrliteEnabled(v bool)`

SetCrliteEnabled sets CrliteEnabled field to given value.

### HasCrliteEnabled

`func (o *UpdateInspectionSettingsRequest) HasCrliteEnabled() bool`

HasCrliteEnabled returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


