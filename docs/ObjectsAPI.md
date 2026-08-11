# \ObjectsAPI

All URIs are relative to *https://virtserver.swaggerhub.com/perimeter81/public-api-yaml/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAddress**](ObjectsAPI.md#CreateAddress) | **Post** /v3/objects/addresses | Create address
[**DeleteAddress**](ObjectsAPI.md#DeleteAddress) | **Delete** /v3/objects/addresses/{addressId} | Delete address
[**DeleteObjectsServices**](ObjectsAPI.md#DeleteObjectsServices) | **Delete** /v3/objects/services/{objectId} | Delete Service object
[**GetAddresses**](ObjectsAPI.md#GetAddresses) | **Get** /v3/objects/addresses | Get list of addresses
[**GetApplicationControlApplications**](ObjectsAPI.md#GetApplicationControlApplications) | **Get** /v3/objects/application-control/application | Get all applications available in Application Control applications
[**GetObjectsServices**](ObjectsAPI.md#GetObjectsServices) | **Get** /v3/objects/services | Get object services
[**GetUpdatableObjects**](ObjectsAPI.md#GetUpdatableObjects) | **Get** /v3/objects/updatable-objects | 
[**GetWebCategories**](ObjectsAPI.md#GetWebCategories) | **Get** /v3/objects/web-category | Get all Web categories
[**PostObjectsServices**](ObjectsAPI.md#PostObjectsServices) | **Post** /v3/objects/services | Create new Service object
[**PutObjectsServices**](ObjectsAPI.md#PutObjectsServices) | **Put** /v3/objects/services/{objectId} | Update Service object
[**UpdateAddress**](ObjectsAPI.md#UpdateAddress) | **Put** /v3/objects/addresses/{id} | Update address



## CreateAddress

> DBAddress CreateAddress(ctx).Address(address).Execute()

Create address

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
	address := *openapiclient.NewAddress() // Address | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.CreateAddress(context.Background()).Address(address).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.CreateAddress``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAddress`: DBAddress
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.CreateAddress`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](Address.md) |  | 

### Return type

[**DBAddress**](DBAddress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAddress

> DeleteAddress(ctx, addressId).Execute()

Delete address

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
	addressId := "addressId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ObjectsAPI.DeleteAddress(context.Background(), addressId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.DeleteAddress``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**addressId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteObjectsServices

> DeleteObjectsServices(ctx, objectId).Execute()

Delete Service object



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
	objectId := "objectId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ObjectsAPI.DeleteObjectsServices(context.Background(), objectId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.DeleteObjectsServices``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**objectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteObjectsServicesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAddresses

> AddressList GetAddresses(ctx).Page(page).Limit(limit).IncludeControlled(includeControlled).Execute()

Get list of addresses

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
	page := int32(56) // int32 |  (optional) (default to 1)
	limit := int32(56) // int32 |  (optional) (default to 500)
	includeControlled := "includeControlled_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.GetAddresses(context.Background()).Page(page).Limit(limit).IncludeControlled(includeControlled).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.GetAddresses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAddresses`: AddressList
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.GetAddresses`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAddressesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int32** |  | [default to 1]
 **limit** | **int32** |  | [default to 500]
 **includeControlled** | **string** |  | 

### Return type

[**AddressList**](AddressList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetApplicationControlApplications

> ApplicationControlResponse GetApplicationControlApplications(ctx).Execute()

Get all applications available in Application Control applications



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
	resp, r, err := apiClient.ObjectsAPI.GetApplicationControlApplications(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.GetApplicationControlApplications``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetApplicationControlApplications`: ApplicationControlResponse
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.GetApplicationControlApplications`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetApplicationControlApplicationsRequest struct via the builder pattern


### Return type

[**ApplicationControlResponse**](ApplicationControlResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetObjectsServices

> ObjectsServicesResponse GetObjectsServices(ctx).Execute()

Get object services



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
	resp, r, err := apiClient.ObjectsAPI.GetObjectsServices(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.GetObjectsServices``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetObjectsServices`: ObjectsServicesResponse
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.GetObjectsServices`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetObjectsServicesRequest struct via the builder pattern


### Return type

[**ObjectsServicesResponse**](ObjectsServicesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUpdatableObjects

> GetUpdatableObjects200Response GetUpdatableObjects(ctx).Name(name).CpId(cpId).Type_(type_).Page(page).Limit(limit).Sort(sort).Execute()



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
	name := "name_example" // string | object name (optional)
	cpId := []string{"Inner_example"} // []string | Filters the results to include only updatable objects that match the specified Check Point object ID. (optional)
	type_ := "splitTunneling" // string | Filters updatable objects by feature category, reflecting differences in object support across categories. splitTunneling: Objects compatible with Split Tunneling configuration. internetAccess: Objects compatible with Internet Access policy. If not provided, returns all objects regardless of feature type.  (optional)
	page := int32(56) // int32 | the page number to retrieve from the paginated results. Default is 1. (optional)
	limit := int32(56) // int32 | size of page (optional)
	sort := "sort_example" // string | sorts the results based on a specified field and order. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.GetUpdatableObjects(context.Background()).Name(name).CpId(cpId).Type_(type_).Page(page).Limit(limit).Sort(sort).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.GetUpdatableObjects``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUpdatableObjects`: GetUpdatableObjects200Response
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.GetUpdatableObjects`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetUpdatableObjectsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **string** | object name | 
 **cpId** | **[]string** | Filters the results to include only updatable objects that match the specified Check Point object ID. | 
 **type_** | **string** | Filters updatable objects by feature category, reflecting differences in object support across categories. splitTunneling: Objects compatible with Split Tunneling configuration. internetAccess: Objects compatible with Internet Access policy. If not provided, returns all objects regardless of feature type.  | 
 **page** | **int32** | the page number to retrieve from the paginated results. Default is 1. | 
 **limit** | **int32** | size of page | 
 **sort** | **string** | sorts the results based on a specified field and order. | 

### Return type

[**GetUpdatableObjects200Response**](GetUpdatableObjects200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetWebCategories

> WebCategoryResponse GetWebCategories(ctx).Execute()

Get all Web categories



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
	resp, r, err := apiClient.ObjectsAPI.GetWebCategories(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.GetWebCategories``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWebCategories`: WebCategoryResponse
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.GetWebCategories`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebCategoriesRequest struct via the builder pattern


### Return type

[**WebCategoryResponse**](WebCategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PostObjectsServices

> PostObjectsServices201Response PostObjectsServices(ctx).ObjectsServicesRequestObj(objectsServicesRequestObj).Execute()

Create new Service object



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
	objectsServicesRequestObj := *openapiclient.NewObjectsServicesRequestObj("Name_example", []openapiclient.ObjectsServicesProtocolRequestObj{*openapiclient.NewObjectsServicesProtocolRequestObj("Protocol_example")}) // ObjectsServicesRequestObj | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.PostObjectsServices(context.Background()).ObjectsServicesRequestObj(objectsServicesRequestObj).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.PostObjectsServices``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PostObjectsServices`: PostObjectsServices201Response
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.PostObjectsServices`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiPostObjectsServicesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objectsServicesRequestObj** | [**ObjectsServicesRequestObj**](ObjectsServicesRequestObj.md) |  | 

### Return type

[**PostObjectsServices201Response**](PostObjectsServices201Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PutObjectsServices

> ObjectsServicesResponseObj PutObjectsServices(ctx, objectId).ObjectsServicesRequestObj(objectsServicesRequestObj).Execute()

Update Service object



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
	objectId := "objectId_example" // string | 
	objectsServicesRequestObj := *openapiclient.NewObjectsServicesRequestObj("Name_example", []openapiclient.ObjectsServicesProtocolRequestObj{*openapiclient.NewObjectsServicesProtocolRequestObj("Protocol_example")}) // ObjectsServicesRequestObj | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.PutObjectsServices(context.Background(), objectId).ObjectsServicesRequestObj(objectsServicesRequestObj).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.PutObjectsServices``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PutObjectsServices`: ObjectsServicesResponseObj
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.PutObjectsServices`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**objectId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiPutObjectsServicesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **objectsServicesRequestObj** | [**ObjectsServicesRequestObj**](ObjectsServicesRequestObj.md) |  | 

### Return type

**ObjectsServicesResponseObj**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAddress

> DBAddress UpdateAddress(ctx, id).Address(address).Execute()

Update address

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
	id := "id_example" // string | 
	address := *openapiclient.NewAddress() // Address | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ObjectsAPI.UpdateAddress(context.Background(), id).Address(address).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ObjectsAPI.UpdateAddress``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAddress`: DBAddress
	fmt.Fprintf(os.Stdout, "Response from `ObjectsAPI.UpdateAddress`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAddressRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **address** | [**Address**](Address.md) |  | 

### Return type

[**DBAddress**](DBAddress.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

