# \ApplicationsAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateApplication**](ApplicationsAPI.md#CreateApplication) | **Post** /v3/applications | Create Application
[**GetApplicationById**](ApplicationsAPI.md#GetApplicationById) | **Get** /v3/applications/{applicationId} | Get Application by ID
[**GetApplicationStatus**](ApplicationsAPI.md#GetApplicationStatus) | **Get** /v3/applications/status/{statusId} | Get status of Application creation process by statusId
[**GetApplications**](ApplicationsAPI.md#GetApplications) | **Get** /v3/applications | Get Applications list



## CreateApplication

> AsyncOperationResponse CreateApplication(ctx).CreateApplicationRequest(createApplicationRequest).Execute()

Create Application



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
	createApplicationRequest := openapiclient.createApplication_request{HttpCreateApplication: openapiclient.NewHttpCreateApplication("MyApplication", "Type_example", "ZwAeo5wqiF", openapiclient.CommonCreateApplication_host{FixedHost: openapiclient.NewFixedHost("Source_example", openapiclient.FixedHost_value{String: new(string)})}, openapiclient.CommonCreateApplication_port{FixedPort: openapiclient.NewFixedPort("Source_example", int32(443))}, []string{"Users_example"}, []string{"Groups_example"}, map[string]interface{}{"key": interface{}(123)}, *openapiclient.NewHttpAttributes())} // CreateApplicationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ApplicationsAPI.CreateApplication(context.Background()).CreateApplicationRequest(createApplicationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationsAPI.CreateApplication``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateApplication`: AsyncOperationResponse
	fmt.Fprintf(os.Stdout, "Response from `ApplicationsAPI.CreateApplication`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateApplicationRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md) |  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetApplicationById

> GetApplicationById200Response GetApplicationById(ctx, applicationId).Execute()

Get Application by ID



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
	applicationId := "applicationId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ApplicationsAPI.GetApplicationById(context.Background(), applicationId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationsAPI.GetApplicationById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetApplicationById`: GetApplicationById200Response
	fmt.Fprintf(os.Stdout, "Response from `ApplicationsAPI.GetApplicationById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**applicationId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetApplicationByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetApplicationById200Response**](GetApplicationById200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetApplicationStatus

> ApplicationStatusResponse GetApplicationStatus(ctx, statusId).Execute()

Get status of Application creation process by statusId



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
	statusId := "statusId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ApplicationsAPI.GetApplicationStatus(context.Background(), statusId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationsAPI.GetApplicationStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetApplicationStatus`: ApplicationStatusResponse
	fmt.Fprintf(os.Stdout, "Response from `ApplicationsAPI.GetApplicationStatus`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**statusId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetApplicationStatusRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ApplicationStatusResponse**](ApplicationStatusResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetApplications

> ApplicationsListPaginatedResponse GetApplications(ctx).Name(name).Host(host).Type_(type_).Page(page).Limit(limit).Sort(sort).Execute()

Get Applications list



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
	name := "name_example" // string | Application name to filter (optional)
	host := "host_example" // string | Application host to filter (optional)
	type_ := "http" // string | Application type to filter (optional)
	page := int32(56) // int32 | Specifies the current page of the paginated result set (optional)
	limit := int32(56) // int32 | Defines the number of results per page (optional)
	sort := "sort[name]=asc" // string | Sorts the results based on a specified field and order. Available fields for sorting are name, host and type. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ApplicationsAPI.GetApplications(context.Background()).Name(name).Host(host).Type_(type_).Page(page).Limit(limit).Sort(sort).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ApplicationsAPI.GetApplications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetApplications`: ApplicationsListPaginatedResponse
	fmt.Fprintf(os.Stdout, "Response from `ApplicationsAPI.GetApplications`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetApplicationsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** | Application name to filter | 
 **host** | **string** | Application host to filter | 
 **type_** | **string** | Application type to filter | 
 **page** | **int32** | Specifies the current page of the paginated result set | 
 **limit** | **int32** | Defines the number of results per page | 
 **sort** | **string** | Sorts the results based on a specified field and order. Available fields for sorting are name, host and type. | 

### Return type

[**ApplicationsListPaginatedResponse**](ApplicationsListPaginatedResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

