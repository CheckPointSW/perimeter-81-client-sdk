# \CustomRolesAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCustomRole**](CustomRolesAPI.md#CreateCustomRole) | **Post** /v3/gum/custom-roles | Create a new custom role
[**DeleteCustomRole**](CustomRolesAPI.md#DeleteCustomRole) | **Delete** /v3/gum/custom-roles/{roleId} | Delete a custom role
[**GetCustomRole**](CustomRolesAPI.md#GetCustomRole) | **Get** /v3/gum/custom-roles/{roleId} | Get a specific custom role by ID
[**GetCustomRoleCategories**](CustomRolesAPI.md#GetCustomRoleCategories) | **Get** /v3/gum/custom-roles/categories | Get all permission categories
[**ListCustomRoles**](CustomRolesAPI.md#ListCustomRoles) | **Get** /v3/gum/custom-roles | List all custom roles for tenant
[**UpdateCustomRole**](CustomRolesAPI.md#UpdateCustomRole) | **Put** /v3/gum/custom-roles/{roleId} | Update a custom role



## CreateCustomRole

> GumCustomRoleResponse CreateCustomRole(ctx).GumCreateCustomRoleRequest(gumCreateCustomRoleRequest).Execute()

Create a new custom role

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
	gumCreateCustomRoleRequest := *openapiclient.NewGumCreateCustomRoleRequest("Name_example", []openapiclient.CategoryEntry{*openapiclient.NewCategoryEntry("CategoryId_example", "Access_example")}) // GumCreateCustomRoleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CustomRolesAPI.CreateCustomRole(context.Background()).GumCreateCustomRoleRequest(gumCreateCustomRoleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.CreateCustomRole``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCustomRole`: GumCustomRoleResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomRolesAPI.CreateCustomRole`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCustomRoleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gumCreateCustomRoleRequest** | [**GumCreateCustomRoleRequest**](GumCreateCustomRoleRequest.md) |  | 

### Return type

[**GumCustomRoleResponse**](GumCustomRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCustomRole

> DeleteCustomRole(ctx, roleId).Execute()

Delete a custom role

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
	roleId := "roleId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CustomRolesAPI.DeleteCustomRole(context.Background(), roleId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.DeleteCustomRole``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**roleId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCustomRoleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


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


## GetCustomRole

> GumCustomRoleResponse GetCustomRole(ctx, roleId).Execute()

Get a specific custom role by ID

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
	roleId := "roleId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CustomRolesAPI.GetCustomRole(context.Background(), roleId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.GetCustomRole``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCustomRole`: GumCustomRoleResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomRolesAPI.GetCustomRole`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**roleId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCustomRoleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GumCustomRoleResponse**](GumCustomRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCustomRoleCategories

> GumCustomRoleCategoriesResponse GetCustomRoleCategories(ctx).Execute()

Get all permission categories

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
	resp, r, err := apiClient.CustomRolesAPI.GetCustomRoleCategories(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.GetCustomRoleCategories``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCustomRoleCategories`: GumCustomRoleCategoriesResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomRolesAPI.GetCustomRoleCategories`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetCustomRoleCategoriesRequest struct via the builder pattern


### Return type

[**GumCustomRoleCategoriesResponse**](GumCustomRoleCategoriesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListCustomRoles

> GumCustomRolesListResponse ListCustomRoles(ctx).Execute()

List all custom roles for tenant

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
	resp, r, err := apiClient.CustomRolesAPI.ListCustomRoles(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.ListCustomRoles``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListCustomRoles`: GumCustomRolesListResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomRolesAPI.ListCustomRoles`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListCustomRolesRequest struct via the builder pattern


### Return type

[**GumCustomRolesListResponse**](GumCustomRolesListResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCustomRole

> GumCustomRoleResponse UpdateCustomRole(ctx, roleId).GumUpdateCustomRoleRequest(gumUpdateCustomRoleRequest).Execute()

Update a custom role

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
	roleId := "roleId_example" // string | 
	gumUpdateCustomRoleRequest := *openapiclient.NewGumUpdateCustomRoleRequest() // GumUpdateCustomRoleRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CustomRolesAPI.UpdateCustomRole(context.Background(), roleId).GumUpdateCustomRoleRequest(gumUpdateCustomRoleRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CustomRolesAPI.UpdateCustomRole``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateCustomRole`: GumCustomRoleResponse
	fmt.Fprintf(os.Stdout, "Response from `CustomRolesAPI.UpdateCustomRole`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**roleId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCustomRoleRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **gumUpdateCustomRoleRequest** | [**GumUpdateCustomRoleRequest**](GumUpdateCustomRoleRequest.md) |  | 

### Return type

[**GumCustomRoleResponse**](GumCustomRoleResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

