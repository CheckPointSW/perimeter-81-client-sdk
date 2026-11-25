# FileAccessConstraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**Value** | **[]string** | For type \&quot;family\&quot;: one or more of executable, archive, document, spreadsheet, script, image, video, audio, pdf. For type \&quot;customExtension\&quot;: one or more file extensions (e.g. \&quot;docx\&quot;, \&quot;xlsx\&quot;).  | 

## Methods

### NewFileAccessConstraint

`func NewFileAccessConstraint(type_ string, value []string, ) *FileAccessConstraint`

NewFileAccessConstraint instantiates a new FileAccessConstraint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileAccessConstraintWithDefaults

`func NewFileAccessConstraintWithDefaults() *FileAccessConstraint`

NewFileAccessConstraintWithDefaults instantiates a new FileAccessConstraint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *FileAccessConstraint) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FileAccessConstraint) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FileAccessConstraint) SetType(v string)`

SetType sets Type field to given value.


### GetValue

`func (o *FileAccessConstraint) GetValue() []string`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *FileAccessConstraint) GetValueOk() (*[]string, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *FileAccessConstraint) SetValue(v []string)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


