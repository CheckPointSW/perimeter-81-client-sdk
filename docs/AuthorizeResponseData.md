# AuthorizeResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TokenType** | **string** | Token type | 
**AccessToken** | **string** | JWT access token | 
**AccessTokenExpire** | **int32** | Unix timestamp when access token expires | 
**TenantId** | **string** | Tenant identifier | 
**SessionId** | **string** | Encrypted session identifier | 

## Methods

### NewAuthorizeResponseData

`func NewAuthorizeResponseData(tokenType string, accessToken string, accessTokenExpire int32, tenantId string, sessionId string, ) *AuthorizeResponseData`

NewAuthorizeResponseData instantiates a new AuthorizeResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuthorizeResponseDataWithDefaults

`func NewAuthorizeResponseDataWithDefaults() *AuthorizeResponseData`

NewAuthorizeResponseDataWithDefaults instantiates a new AuthorizeResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTokenType

`func (o *AuthorizeResponseData) GetTokenType() string`

GetTokenType returns the TokenType field if non-nil, zero value otherwise.

### GetTokenTypeOk

`func (o *AuthorizeResponseData) GetTokenTypeOk() (*string, bool)`

GetTokenTypeOk returns a tuple with the TokenType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenType

`func (o *AuthorizeResponseData) SetTokenType(v string)`

SetTokenType sets TokenType field to given value.


### GetAccessToken

`func (o *AuthorizeResponseData) GetAccessToken() string`

GetAccessToken returns the AccessToken field if non-nil, zero value otherwise.

### GetAccessTokenOk

`func (o *AuthorizeResponseData) GetAccessTokenOk() (*string, bool)`

GetAccessTokenOk returns a tuple with the AccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessToken

`func (o *AuthorizeResponseData) SetAccessToken(v string)`

SetAccessToken sets AccessToken field to given value.


### GetAccessTokenExpire

`func (o *AuthorizeResponseData) GetAccessTokenExpire() int32`

GetAccessTokenExpire returns the AccessTokenExpire field if non-nil, zero value otherwise.

### GetAccessTokenExpireOk

`func (o *AuthorizeResponseData) GetAccessTokenExpireOk() (*int32, bool)`

GetAccessTokenExpireOk returns a tuple with the AccessTokenExpire field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessTokenExpire

`func (o *AuthorizeResponseData) SetAccessTokenExpire(v int32)`

SetAccessTokenExpire sets AccessTokenExpire field to given value.


### GetTenantId

`func (o *AuthorizeResponseData) GetTenantId() string`

GetTenantId returns the TenantId field if non-nil, zero value otherwise.

### GetTenantIdOk

`func (o *AuthorizeResponseData) GetTenantIdOk() (*string, bool)`

GetTenantIdOk returns a tuple with the TenantId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTenantId

`func (o *AuthorizeResponseData) SetTenantId(v string)`

SetTenantId sets TenantId field to given value.


### GetSessionId

`func (o *AuthorizeResponseData) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *AuthorizeResponseData) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *AuthorizeResponseData) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


