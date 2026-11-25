# CertificateRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CertificateError** | **string** |  | 
**Action** | **string** |  | 
**Log** | **bool** |  | 

## Methods

### NewCertificateRule

`func NewCertificateRule(certificateError string, action string, log bool, ) *CertificateRule`

NewCertificateRule instantiates a new CertificateRule object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCertificateRuleWithDefaults

`func NewCertificateRuleWithDefaults() *CertificateRule`

NewCertificateRuleWithDefaults instantiates a new CertificateRule object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCertificateError

`func (o *CertificateRule) GetCertificateError() string`

GetCertificateError returns the CertificateError field if non-nil, zero value otherwise.

### GetCertificateErrorOk

`func (o *CertificateRule) GetCertificateErrorOk() (*string, bool)`

GetCertificateErrorOk returns a tuple with the CertificateError field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCertificateError

`func (o *CertificateRule) SetCertificateError(v string)`

SetCertificateError sets CertificateError field to given value.


### GetAction

`func (o *CertificateRule) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *CertificateRule) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *CertificateRule) SetAction(v string)`

SetAction sets Action field to given value.


### GetLog

`func (o *CertificateRule) GetLog() bool`

GetLog returns the Log field if non-nil, zero value otherwise.

### GetLogOk

`func (o *CertificateRule) GetLogOk() (*bool, bool)`

GetLogOk returns a tuple with the Log field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLog

`func (o *CertificateRule) SetLog(v bool)`

SetLog sets Log field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


