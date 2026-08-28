# \InternetAccessPoliciesAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteAccessPolicy**](InternetAccessPoliciesAPI.md#DeleteAccessPolicy) | **Delete** /v3/ia/access/policy | Delete all access policy rules
[**DeleteHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#DeleteHttpsInspectionPolicy) | **Delete** /v3/ia/https-inspection/policy | Delete all HTTPS Inspection policy rules
[**GetAccessPolicy**](InternetAccessPoliciesAPI.md#GetAccessPolicy) | **Get** /v3/ia/access/policy | Get all access policy rules
[**GetHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#GetHttpsInspectionPolicy) | **Get** /v3/ia/https-inspection/policy | Get all HTTPS Inspection policy rules
[**GetIAStatus**](InternetAccessPoliciesAPI.md#GetIAStatus) | **Get** /v3/ia/status | Get Internet Access security enforcement status
[**SetIAStatus**](InternetAccessPoliciesAPI.md#SetIAStatus) | **Post** /v3/ia/status | Update Internet Access security enforcement status
[**UpdateAccessPolicy**](InternetAccessPoliciesAPI.md#UpdateAccessPolicy) | **Post** /v3/ia/access/policy | Update/Create all access policy rules
[**UpdateHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#UpdateHttpsInspectionPolicy) | **Post** /v3/ia/https-inspection/policy | Update/Create all HTTPS Inspection policy rules



## DeleteAccessPolicy

> DeleteAccessPolicy(ctx).Execute()

Delete all access policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteAccessPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAccessPolicyRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteHttpsInspectionPolicy

> DeleteHttpsInspectionPolicy(ctx).Execute()

Delete all HTTPS Inspection policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteHttpsInspectionPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteHttpsInspectionPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteHttpsInspectionPolicyRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAccessPolicy

> AccessPolicyRulesGetResponse GetAccessPolicy(ctx).Execute()

Get all access policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetAccessPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccessPolicy`: AccessPolicyRulesGetResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetAccessPolicy`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccessPolicyRequest struct via the builder pattern


### Return type

[**AccessPolicyRulesGetResponse**](AccessPolicyRulesGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHttpsInspectionPolicy

> HttpsInspectionPolicyGetResponse GetHttpsInspectionPolicy(ctx).Execute()

Get all HTTPS Inspection policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetHttpsInspectionPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetHttpsInspectionPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHttpsInspectionPolicy`: HttpsInspectionPolicyGetResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetHttpsInspectionPolicy`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetHttpsInspectionPolicyRequest struct via the builder pattern


### Return type

[**HttpsInspectionPolicyGetResponse**](HttpsInspectionPolicyGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetIAStatus

> GetIAStatus200Response GetIAStatus(ctx).Execute()

Get Internet Access security enforcement status



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetIAStatus(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetIAStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIAStatus`: GetIAStatus200Response
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetIAStatus`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetIAStatusRequest struct via the builder pattern


### Return type

[**GetIAStatus200Response**](GetIAStatus200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SetIAStatus

> SetIAStatusRequest SetIAStatus(ctx).SetIAStatusRequest(setIAStatusRequest).Execute()

Update Internet Access security enforcement status



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {
	setIAStatusRequest := *openapiclient.NewSetIAStatusRequest() // SetIAStatusRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.SetIAStatus(context.Background()).SetIAStatusRequest(setIAStatusRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.SetIAStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SetIAStatus`: SetIAStatusRequest
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.SetIAStatus`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSetIAStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setIAStatusRequest** | [**SetIAStatusRequest**](SetIAStatusRequest.md) |  | 

### Return type

[**SetIAStatusRequest**](SetIAStatusRequest.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAccessPolicy

> UpdateAccessPolicyRulesResponse UpdateAccessPolicy(ctx).UpdateAccessPolicyRulesRequest(updateAccessPolicyRulesRequest).Execute()

Update/Create all access policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {
	updateAccessPolicyRulesRequest := *openapiclient.NewUpdateAccessPolicyRulesRequest([]openapiclient.AccessPolicyRule{*openapiclient.NewAccessPolicyRule("Name_example", "AppliedOn_example", "Action_example", []openapiclient.Condition{*openapiclient.NewCondition("Type_example", []openapiclient.ConditionValueInner{*openapiclient.NewConditionValueInner([]string{"Weekdays_example"}, *openapiclient.NewConditionTime(int32(123), int32(123)), *openapiclient.NewConditionTime(int32(123), int32(123)))})}, []openapiclient.AccessPolicyDestination{*openapiclient.NewAccessPolicyDestination("Type_example", []string{"Value_example"})}, []openapiclient.AccessPolicySource{*openapiclient.NewAccessPolicySource("Type_example", []string{"Value_example"})}, "Status_example", int32(123))}) // UpdateAccessPolicyRulesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateAccessPolicy(context.Background()).UpdateAccessPolicyRulesRequest(updateAccessPolicyRulesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAccessPolicy`: UpdateAccessPolicyRulesResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateAccessPolicy`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAccessPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateAccessPolicyRulesRequest** | [**UpdateAccessPolicyRulesRequest**](UpdateAccessPolicyRulesRequest.md) |  | 

### Return type

[**UpdateAccessPolicyRulesResponse**](UpdateAccessPolicyRulesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateHttpsInspectionPolicy

> HttpsInspectionPolicyResponse UpdateHttpsInspectionPolicy(ctx).UpsertHttpsInspectionPolicy(upsertHttpsInspectionPolicy).Execute()

Update/Create all HTTPS Inspection policy rules



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/CheckPointSW/perimeter-81-client-sdk/v3"
)

func main() {
	upsertHttpsInspectionPolicy := *openapiclient.NewUpsertHttpsInspectionPolicy([]openapiclient.HttpsInspectionRule{*openapiclient.NewHttpsInspectionRule("Name_example", "AppliedOn_example", int32(123), []openapiclient.HttpsInspectionSource{*openapiclient.NewHttpsInspectionSource("Type_example", []string{"Value_example"})}, []openapiclient.HttpsInspectionDestination{*openapiclient.NewHttpsInspectionDestination("Type_example", []string{"Value_example"})}, "Status_example")}) // UpsertHttpsInspectionPolicy | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateHttpsInspectionPolicy(context.Background()).UpsertHttpsInspectionPolicy(upsertHttpsInspectionPolicy).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateHttpsInspectionPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateHttpsInspectionPolicy`: HttpsInspectionPolicyResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateHttpsInspectionPolicy`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateHttpsInspectionPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsertHttpsInspectionPolicy** | [**UpsertHttpsInspectionPolicy**](UpsertHttpsInspectionPolicy.md) |  | 

### Return type

[**HttpsInspectionPolicyResponse**](HttpsInspectionPolicyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

