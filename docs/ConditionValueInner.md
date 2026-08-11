# ConditionValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Weekdays** | **[]string** |  | 
**StartTime** | [**ConditionTime**](ConditionTime.md) |  | 
**EndTime** | [**ConditionTime**](ConditionTime.md) |  | 

## Methods

### NewConditionValueInner

`func NewConditionValueInner(weekdays []string, startTime ConditionTime, endTime ConditionTime, ) *ConditionValueInner`

NewConditionValueInner instantiates a new ConditionValueInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewConditionValueInnerWithDefaults

`func NewConditionValueInnerWithDefaults() *ConditionValueInner`

NewConditionValueInnerWithDefaults instantiates a new ConditionValueInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWeekdays

`func (o *ConditionValueInner) GetWeekdays() []string`

GetWeekdays returns the Weekdays field if non-nil, zero value otherwise.

### GetWeekdaysOk

`func (o *ConditionValueInner) GetWeekdaysOk() (*[]string, bool)`

GetWeekdaysOk returns a tuple with the Weekdays field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeekdays

`func (o *ConditionValueInner) SetWeekdays(v []string)`

SetWeekdays sets Weekdays field to given value.


### GetStartTime

`func (o *ConditionValueInner) GetStartTime() ConditionTime`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *ConditionValueInner) GetStartTimeOk() (*ConditionTime, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *ConditionValueInner) SetStartTime(v ConditionTime)`

SetStartTime sets StartTime field to given value.


### GetEndTime

`func (o *ConditionValueInner) GetEndTime() ConditionTime`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *ConditionValueInner) GetEndTimeOk() (*ConditionTime, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndTime

`func (o *ConditionValueInner) SetEndTime(v ConditionTime)`

SetEndTime sets EndTime field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


