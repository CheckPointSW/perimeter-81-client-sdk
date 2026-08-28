# AuthorizeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GrantType** | **string** | Grant type for authentication | 
**ApiKey** | **string** | API key for authentication | 

## Methods

### NewAuthorizeRequest

`func NewAuthorizeRequest(grantType string, apiKey string, ) *AuthorizeRequest`

NewAuthorizeRequest instantiates a new AuthorizeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuthorizeRequestWithDefaults

`func NewAuthorizeRequestWithDefaults() *AuthorizeRequest`

NewAuthorizeRequestWithDefaults instantiates a new AuthorizeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGrantType

`func (o *AuthorizeRequest) GetGrantType() string`

GetGrantType returns the GrantType field if non-nil, zero value otherwise.

### GetGrantTypeOk

`func (o *AuthorizeRequest) GetGrantTypeOk() (*string, bool)`

GetGrantTypeOk returns a tuple with the GrantType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantType

`func (o *AuthorizeRequest) SetGrantType(v string)`

SetGrantType sets GrantType field to given value.


### GetApiKey

`func (o *AuthorizeRequest) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *AuthorizeRequest) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *AuthorizeRequest) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


