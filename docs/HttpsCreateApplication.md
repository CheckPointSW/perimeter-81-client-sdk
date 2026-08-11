# HttpsCreateApplication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Application name | 
**Type** | **string** | Application type | 
**Network** | **string** | Application network ID. To get the ID use endpoint &#39;/networks&#39; with [network:read] permission. | 
**Host** | [**CommonCreateApplicationHost**](CommonCreateApplicationHost.md) |  | 
**Port** | [**CommonCreateApplicationPort**](CommonCreateApplicationPort.md) |  | 
**Users** | **[]string** |  | 
**Groups** | **[]string** |  | 
**Headers** | **map[string]interface{}** | Application specific headers. Keys must not contain . and $ | 
**Attributes** | [**HttpsAttributes**](HttpsAttributes.md) |  | 

## Methods

### NewHttpsCreateApplication

`func NewHttpsCreateApplication(name string, type_ string, network string, host CommonCreateApplicationHost, port CommonCreateApplicationPort, users []string, groups []string, headers map[string]interface{}, attributes HttpsAttributes, ) *HttpsCreateApplication`

NewHttpsCreateApplication instantiates a new HttpsCreateApplication object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHttpsCreateApplicationWithDefaults

`func NewHttpsCreateApplicationWithDefaults() *HttpsCreateApplication`

NewHttpsCreateApplicationWithDefaults instantiates a new HttpsCreateApplication object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *HttpsCreateApplication) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *HttpsCreateApplication) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *HttpsCreateApplication) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *HttpsCreateApplication) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *HttpsCreateApplication) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *HttpsCreateApplication) SetType(v string)`

SetType sets Type field to given value.


### GetNetwork

`func (o *HttpsCreateApplication) GetNetwork() string`

GetNetwork returns the Network field if non-nil, zero value otherwise.

### GetNetworkOk

`func (o *HttpsCreateApplication) GetNetworkOk() (*string, bool)`

GetNetworkOk returns a tuple with the Network field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetwork

`func (o *HttpsCreateApplication) SetNetwork(v string)`

SetNetwork sets Network field to given value.


### GetHost

`func (o *HttpsCreateApplication) GetHost() CommonCreateApplicationHost`

GetHost returns the Host field if non-nil, zero value otherwise.

### GetHostOk

`func (o *HttpsCreateApplication) GetHostOk() (*CommonCreateApplicationHost, bool)`

GetHostOk returns a tuple with the Host field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHost

`func (o *HttpsCreateApplication) SetHost(v CommonCreateApplicationHost)`

SetHost sets Host field to given value.


### GetPort

`func (o *HttpsCreateApplication) GetPort() CommonCreateApplicationPort`

GetPort returns the Port field if non-nil, zero value otherwise.

### GetPortOk

`func (o *HttpsCreateApplication) GetPortOk() (*CommonCreateApplicationPort, bool)`

GetPortOk returns a tuple with the Port field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPort

`func (o *HttpsCreateApplication) SetPort(v CommonCreateApplicationPort)`

SetPort sets Port field to given value.


### GetUsers

`func (o *HttpsCreateApplication) GetUsers() []string`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *HttpsCreateApplication) GetUsersOk() (*[]string, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *HttpsCreateApplication) SetUsers(v []string)`

SetUsers sets Users field to given value.


### GetGroups

`func (o *HttpsCreateApplication) GetGroups() []string`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *HttpsCreateApplication) GetGroupsOk() (*[]string, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *HttpsCreateApplication) SetGroups(v []string)`

SetGroups sets Groups field to given value.


### GetHeaders

`func (o *HttpsCreateApplication) GetHeaders() map[string]interface{}`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *HttpsCreateApplication) GetHeadersOk() (*map[string]interface{}, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *HttpsCreateApplication) SetHeaders(v map[string]interface{})`

SetHeaders sets Headers field to given value.


### GetAttributes

`func (o *HttpsCreateApplication) GetAttributes() HttpsAttributes`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *HttpsCreateApplication) GetAttributesOk() (*HttpsAttributes, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *HttpsCreateApplication) SetAttributes(v HttpsAttributes)`

SetAttributes sets Attributes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


