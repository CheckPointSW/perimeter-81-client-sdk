# \InternetAccessPoliciesAPI

All URIs are relative to *https://public-apigw.us.sase.checkpoint.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteAccessPolicy**](InternetAccessPoliciesAPI.md#DeleteAccessPolicy) | **Delete** /v3/ia/access/policy | Delete all access policy rules
[**DeleteDlpSettings**](InternetAccessPoliciesAPI.md#DeleteDlpSettings) | **Delete** /v3/ia/dlp-settings | Reset DLP settings
[**DeleteFileAccessPolicy**](InternetAccessPoliciesAPI.md#DeleteFileAccessPolicy) | **Delete** /v3/ia/file-access/policy | Delete all file access policy rules
[**DeleteHostFirewallPolicy**](InternetAccessPoliciesAPI.md#DeleteHostFirewallPolicy) | **Delete** /v3/ia/host-firewall/policy | Delete all host firewall rules
[**DeleteHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#DeleteHttpsInspectionPolicy) | **Delete** /v3/ia/https-inspection/policy | Delete all HTTPS Inspection policy rules
[**DeleteInspectionSettings**](InternetAccessPoliciesAPI.md#DeleteInspectionSettings) | **Delete** /v3/ia/inspection-settings | Reset traffic inspection settings
[**DeleteNotificationPages**](InternetAccessPoliciesAPI.md#DeleteNotificationPages) | **Delete** /v3/ia/notification-pages | Delete notification pages
[**GetAccessPolicy**](InternetAccessPoliciesAPI.md#GetAccessPolicy) | **Get** /v3/ia/access/policy | Get all access policy rules
[**GetDlpSettings**](InternetAccessPoliciesAPI.md#GetDlpSettings) | **Get** /v3/ia/dlp-settings | Get DLP settings
[**GetFileAccessPolicy**](InternetAccessPoliciesAPI.md#GetFileAccessPolicy) | **Get** /v3/ia/file-access/policy | Get all file access policy rules
[**GetHostFirewallPolicy**](InternetAccessPoliciesAPI.md#GetHostFirewallPolicy) | **Get** /v3/ia/host-firewall/policy | Get all host firewall rules
[**GetHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#GetHttpsInspectionPolicy) | **Get** /v3/ia/https-inspection/policy | Get all HTTPS Inspection policy rules
[**GetIAStatus**](InternetAccessPoliciesAPI.md#GetIAStatus) | **Get** /v3/ia/status | Get Internet Access security enforcement status
[**GetInspectionSettings**](InternetAccessPoliciesAPI.md#GetInspectionSettings) | **Get** /v3/ia/inspection-settings | Get traffic inspection settings
[**GetNotificationPages**](InternetAccessPoliciesAPI.md#GetNotificationPages) | **Get** /v3/ia/notification-pages | Get notification pages
[**SetIAStatus**](InternetAccessPoliciesAPI.md#SetIAStatus) | **Post** /v3/ia/status | Update Internet Access security enforcement status
[**UpdateAccessPolicy**](InternetAccessPoliciesAPI.md#UpdateAccessPolicy) | **Post** /v3/ia/access/policy | Update/Create all access policy rules
[**UpdateDlpSettings**](InternetAccessPoliciesAPI.md#UpdateDlpSettings) | **Post** /v3/ia/dlp-settings | Update DLP settings
[**UpdateFileAccessPolicy**](InternetAccessPoliciesAPI.md#UpdateFileAccessPolicy) | **Post** /v3/ia/file-access/policy | Update/Create all file access policy rules
[**UpdateHostFirewallPolicy**](InternetAccessPoliciesAPI.md#UpdateHostFirewallPolicy) | **Post** /v3/ia/host-firewall/policy | Update/Create all host firewall rules
[**UpdateHttpsInspectionPolicy**](InternetAccessPoliciesAPI.md#UpdateHttpsInspectionPolicy) | **Post** /v3/ia/https-inspection/policy | Update/Create all HTTPS Inspection policy rules
[**UpdateInspectionSettings**](InternetAccessPoliciesAPI.md#UpdateInspectionSettings) | **Post** /v3/ia/inspection-settings | Update traffic inspection settings
[**UpdateNotificationPages**](InternetAccessPoliciesAPI.md#UpdateNotificationPages) | **Post** /v3/ia/notification-pages | Create or update notification pages



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


## DeleteDlpSettings

> DeleteDlpSettings(ctx).Execute()

Reset DLP settings



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
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteDlpSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteDlpSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDlpSettingsRequest struct via the builder pattern


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


## DeleteFileAccessPolicy

> DeleteFileAccessPolicy(ctx).Execute()

Delete all file access policy rules



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
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteFileAccessPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteFileAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteFileAccessPolicyRequest struct via the builder pattern


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


## DeleteHostFirewallPolicy

> DeleteHostFirewallPolicy(ctx).DeleteHostFirewallPolicyRequest(deleteHostFirewallPolicyRequest).Execute()

Delete all host firewall rules



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
	deleteHostFirewallPolicyRequest := *openapiclient.NewDeleteHostFirewallPolicyRequest() // DeleteHostFirewallPolicyRequest |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteHostFirewallPolicy(context.Background()).DeleteHostFirewallPolicyRequest(deleteHostFirewallPolicyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteHostFirewallPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteHostFirewallPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleteHostFirewallPolicyRequest** | [**DeleteHostFirewallPolicyRequest**](DeleteHostFirewallPolicyRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
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


## DeleteInspectionSettings

> DeleteInspectionSettings(ctx).Execute()

Reset traffic inspection settings



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
	r, err := apiClient.InternetAccessPoliciesAPI.DeleteInspectionSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteInspectionSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteInspectionSettingsRequest struct via the builder pattern


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


## DeleteNotificationPages

> NotificationPagesMessageResponse DeleteNotificationPages(ctx).Execute()

Delete notification pages



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.DeleteNotificationPages(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.DeleteNotificationPages``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteNotificationPages`: NotificationPagesMessageResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.DeleteNotificationPages`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteNotificationPagesRequest struct via the builder pattern


### Return type

[**NotificationPagesMessageResponse**](NotificationPagesMessageResponse.md)

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


## GetDlpSettings

> DlpSettingsResponse GetDlpSettings(ctx).Execute()

Get DLP settings



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetDlpSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetDlpSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDlpSettings`: DlpSettingsResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetDlpSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetDlpSettingsRequest struct via the builder pattern


### Return type

[**DlpSettingsResponse**](DlpSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetFileAccessPolicy

> FileAccessPolicyGetResponse GetFileAccessPolicy(ctx).Execute()

Get all file access policy rules



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetFileAccessPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetFileAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetFileAccessPolicy`: FileAccessPolicyGetResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetFileAccessPolicy`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetFileAccessPolicyRequest struct via the builder pattern


### Return type

[**FileAccessPolicyGetResponse**](FileAccessPolicyGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetHostFirewallPolicy

> HostFirewallPolicyResponse GetHostFirewallPolicy(ctx).Execute()

Get all host firewall rules



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetHostFirewallPolicy(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetHostFirewallPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetHostFirewallPolicy`: HostFirewallPolicyResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetHostFirewallPolicy`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetHostFirewallPolicyRequest struct via the builder pattern


### Return type

[**HostFirewallPolicyResponse**](HostFirewallPolicyResponse.md)

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


## GetInspectionSettings

> InspectionSettingsResponse GetInspectionSettings(ctx).Execute()

Get traffic inspection settings



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetInspectionSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetInspectionSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetInspectionSettings`: InspectionSettingsResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetInspectionSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetInspectionSettingsRequest struct via the builder pattern


### Return type

[**InspectionSettingsResponse**](InspectionSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetNotificationPages

> NotificationPagesGetResponse GetNotificationPages(ctx).Execute()

Get notification pages



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
	resp, r, err := apiClient.InternetAccessPoliciesAPI.GetNotificationPages(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.GetNotificationPages``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNotificationPages`: NotificationPagesGetResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.GetNotificationPages`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetNotificationPagesRequest struct via the builder pattern


### Return type

[**NotificationPagesGetResponse**](NotificationPagesGetResponse.md)

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


## UpdateDlpSettings

> DlpSettingsResponse UpdateDlpSettings(ctx).UpdateDlpSettingsRequest(updateDlpSettingsRequest).Execute()

Update DLP settings



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
	updateDlpSettingsRequest := *openapiclient.NewUpdateDlpSettingsRequest(openapiclient.DlpFailType("open")) // UpdateDlpSettingsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateDlpSettings(context.Background()).UpdateDlpSettingsRequest(updateDlpSettingsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateDlpSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateDlpSettings`: DlpSettingsResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateDlpSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDlpSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateDlpSettingsRequest** | [**UpdateDlpSettingsRequest**](UpdateDlpSettingsRequest.md) |  | 

### Return type

[**DlpSettingsResponse**](DlpSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateFileAccessPolicy

> FileAccessPolicyGetResponse UpdateFileAccessPolicy(ctx).UpdateFileAccessPolicyRequest(updateFileAccessPolicyRequest).Execute()

Update/Create all file access policy rules



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
	updateFileAccessPolicyRequest := *openapiclient.NewUpdateFileAccessPolicyRequest([]openapiclient.FileAccessRule{*openapiclient.NewFileAccessRule("Name_example", "Status_example", int32(123), "Action_example", []string{"Activity_example"}, *openapiclient.NewFileAccessSource(), *openapiclient.NewFileAccessDestination(), []openapiclient.FileAccessConstraint{*openapiclient.NewFileAccessConstraint("Type_example", []string{"Value_example"})})}) // UpdateFileAccessPolicyRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateFileAccessPolicy(context.Background()).UpdateFileAccessPolicyRequest(updateFileAccessPolicyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateFileAccessPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateFileAccessPolicy`: FileAccessPolicyGetResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateFileAccessPolicy`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateFileAccessPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateFileAccessPolicyRequest** | [**UpdateFileAccessPolicyRequest**](UpdateFileAccessPolicyRequest.md) |  | 

### Return type

[**FileAccessPolicyGetResponse**](FileAccessPolicyGetResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateHostFirewallPolicy

> HostFirewallPolicyResponse UpdateHostFirewallPolicy(ctx).UpdateHostFirewallPolicyRequest(updateHostFirewallPolicyRequest).Execute()

Update/Create all host firewall rules



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
	updateHostFirewallPolicyRequest := *openapiclient.NewUpdateHostFirewallPolicyRequest([]openapiclient.HostFirewallRuleInput{*openapiclient.NewHostFirewallRuleInput("Name_example", "Action_example", []openapiclient.HostFirewallSource{*openapiclient.NewHostFirewallSource("Type_example", []string{"Value_example"})}, []openapiclient.HostFirewallService{*openapiclient.NewHostFirewallService("Type_example", []string{"Value_example"})}, []openapiclient.HostFirewallDestination{*openapiclient.NewHostFirewallDestination("Type_example", []string{"Value_example"})})}) // UpdateHostFirewallPolicyRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateHostFirewallPolicy(context.Background()).UpdateHostFirewallPolicyRequest(updateHostFirewallPolicyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateHostFirewallPolicy``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateHostFirewallPolicy`: HostFirewallPolicyResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateHostFirewallPolicy`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateHostFirewallPolicyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateHostFirewallPolicyRequest** | [**UpdateHostFirewallPolicyRequest**](UpdateHostFirewallPolicyRequest.md) |  | 

### Return type

[**HostFirewallPolicyResponse**](HostFirewallPolicyResponse.md)

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


## UpdateInspectionSettings

> InspectionSettingsResponse UpdateInspectionSettings(ctx).UpdateInspectionSettingsRequest(updateInspectionSettingsRequest).Execute()

Update traffic inspection settings



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
	updateInspectionSettingsRequest := *openapiclient.NewUpdateInspectionSettingsRequest() // UpdateInspectionSettingsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateInspectionSettings(context.Background()).UpdateInspectionSettingsRequest(updateInspectionSettingsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateInspectionSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateInspectionSettings`: InspectionSettingsResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateInspectionSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateInspectionSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateInspectionSettingsRequest** | [**UpdateInspectionSettingsRequest**](UpdateInspectionSettingsRequest.md) |  | 

### Return type

[**InspectionSettingsResponse**](InspectionSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateNotificationPages

> NotificationPagesMessageResponse UpdateNotificationPages(ctx).UpdateNotificationPagesRequest(updateNotificationPagesRequest).Execute()

Create or update notification pages



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
	updateNotificationPagesRequest := *openapiclient.NewUpdateNotificationPagesRequest() // UpdateNotificationPagesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InternetAccessPoliciesAPI.UpdateNotificationPages(context.Background()).UpdateNotificationPagesRequest(updateNotificationPagesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InternetAccessPoliciesAPI.UpdateNotificationPages``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateNotificationPages`: NotificationPagesMessageResponse
	fmt.Fprintf(os.Stdout, "Response from `InternetAccessPoliciesAPI.UpdateNotificationPages`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateNotificationPagesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateNotificationPagesRequest** | [**UpdateNotificationPagesRequest**](UpdateNotificationPagesRequest.md) |  | 

### Return type

[**NotificationPagesMessageResponse**](NotificationPagesMessageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

