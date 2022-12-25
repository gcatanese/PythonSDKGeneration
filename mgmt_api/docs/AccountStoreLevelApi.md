# openapi_client.AccountStoreLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_merchant_id_stores**](AccountStoreLevelApi.md#get_merchants_merchant_id_stores) | **GET** /merchants/{merchantId}/stores | Get a list of stores
[**get_merchants_merchant_id_stores_store_id**](AccountStoreLevelApi.md#get_merchants_merchant_id_stores_store_id) | **GET** /merchants/{merchantId}/stores/{storeId} | Get a store
[**get_stores**](AccountStoreLevelApi.md#get_stores) | **GET** /stores | Get a list of stores
[**get_stores_store_id**](AccountStoreLevelApi.md#get_stores_store_id) | **GET** /stores/{storeId} | Get a store
[**patch_merchants_merchant_id_stores_store_id**](AccountStoreLevelApi.md#patch_merchants_merchant_id_stores_store_id) | **PATCH** /merchants/{merchantId}/stores/{storeId} | Update a store
[**patch_stores_store_id**](AccountStoreLevelApi.md#patch_stores_store_id) | **PATCH** /stores/{storeId} | Update a store
[**post_merchants_merchant_id_stores**](AccountStoreLevelApi.md#post_merchants_merchant_id_stores) | **POST** /merchants/{merchantId}/stores | Create a store
[**post_stores**](AccountStoreLevelApi.md#post_stores) | **POST** /stores | Create a store


# **get_merchants_merchant_id_stores**
> ListStoresResponse get_merchants_merchant_id_stores(merchant_id, page_number=page_number, page_size=page_size, reference=reference)

Get a list of stores

Returns a list of stores for the merchant account identified in the path. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    reference = 'reference_example' # str | The reference of the store. (optional)

    try:
        # Get a list of stores
        api_response = api_instance.get_merchants_merchant_id_stores(merchant_id, page_number=page_number, page_size=page_size, reference=reference)
        print("The response of AccountStoreLevelApi->get_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_merchants_merchant_id_stores: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    reference = 'reference_example' # str | The reference of the store. (optional)

    try:
        # Get a list of stores
        api_response = api_instance.get_merchants_merchant_id_stores(merchant_id, page_number=page_number, page_size=page_size, reference=reference)
        print("The response of AccountStoreLevelApi->get_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_merchants_merchant_id_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **reference** | **str**| The reference of the store. | [optional] 

### Return type

[**ListStoresResponse**](ListStoresResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchants_merchant_id_stores_store_id**
> Store get_merchants_merchant_id_stores_store_id(merchant_id, store_id)

Get a store

Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get a store
        api_response = api_instance.get_merchants_merchant_id_stores_store_id(merchant_id, store_id)
        print("The response of AccountStoreLevelApi->get_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_merchants_merchant_id_stores_store_id: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get a store
        api_response = api_instance.get_merchants_merchant_id_stores_store_id(merchant_id, store_id)
        print("The response of AccountStoreLevelApi->get_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_merchants_merchant_id_stores_store_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **store_id** | **str**| The unique identifier of the store. | 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stores**
> ListStoresResponse get_stores(page_number=page_number, page_size=page_size, reference=reference, merchant_id=merchant_id)

Get a list of stores

Returns a list of stores. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    reference = 'reference_example' # str | The reference of the store. (optional)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account. (optional)

    try:
        # Get a list of stores
        api_response = api_instance.get_stores(page_number=page_number, page_size=page_size, reference=reference, merchant_id=merchant_id)
        print("The response of AccountStoreLevelApi->get_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_stores: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    reference = 'reference_example' # str | The reference of the store. (optional)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account. (optional)

    try:
        # Get a list of stores
        api_response = api_instance.get_stores(page_number=page_number, page_size=page_size, reference=reference, merchant_id=merchant_id)
        print("The response of AccountStoreLevelApi->get_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **reference** | **str**| The reference of the store. | [optional] 
 **merchant_id** | **str**| The unique identifier of the merchant account. | [optional] 

### Return type

[**ListStoresResponse**](ListStoresResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stores_store_id**
> Store get_stores_store_id(store_id)

Get a store

Returns the details of the store identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get a store
        api_response = api_instance.get_stores_store_id(store_id)
        print("The response of AccountStoreLevelApi->get_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_stores_store_id: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get a store
        api_response = api_instance.get_stores_store_id(store_id)
        print("The response of AccountStoreLevelApi->get_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->get_stores_store_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_merchants_merchant_id_stores_store_id**
> Store patch_merchants_merchant_id_stores_store_id(merchant_id, store_id, update_store_request=update_store_request)

Update a store

Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store.
    update_store_request = openapi_client.UpdateStoreRequest() # UpdateStoreRequest |  (optional)

    try:
        # Update a store
        api_response = api_instance.patch_merchants_merchant_id_stores_store_id(merchant_id, store_id, update_store_request=update_store_request)
        print("The response of AccountStoreLevelApi->patch_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->patch_merchants_merchant_id_stores_store_id: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store.
    update_store_request = openapi_client.UpdateStoreRequest() # UpdateStoreRequest |  (optional)

    try:
        # Update a store
        api_response = api_instance.patch_merchants_merchant_id_stores_store_id(merchant_id, store_id, update_store_request=update_store_request)
        print("The response of AccountStoreLevelApi->patch_merchants_merchant_id_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->patch_merchants_merchant_id_stores_store_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **store_id** | **str**| The unique identifier of the store. | 
 **update_store_request** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_stores_store_id**
> Store patch_stores_store_id(store_id, update_store_request=update_store_request)

Update a store

Updates the store identified in the path. You can only update some store parameters.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    update_store_request = openapi_client.UpdateStoreRequest() # UpdateStoreRequest |  (optional)

    try:
        # Update a store
        api_response = api_instance.patch_stores_store_id(store_id, update_store_request=update_store_request)
        print("The response of AccountStoreLevelApi->patch_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->patch_stores_store_id: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    update_store_request = openapi_client.UpdateStoreRequest() # UpdateStoreRequest |  (optional)

    try:
        # Update a store
        api_response = api_instance.patch_stores_store_id(store_id, update_store_request=update_store_request)
        print("The response of AccountStoreLevelApi->patch_stores_store_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->patch_stores_store_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 
 **update_store_request** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_merchants_merchant_id_stores**
> Store post_merchants_merchant_id_stores(merchant_id, store_creation_request=store_creation_request)

Create a store

Creates a store for the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_creation_request = openapi_client.StoreCreationRequest() # StoreCreationRequest |  (optional)

    try:
        # Create a store
        api_response = api_instance.post_merchants_merchant_id_stores(merchant_id, store_creation_request=store_creation_request)
        print("The response of AccountStoreLevelApi->post_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->post_merchants_merchant_id_stores: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_creation_request = openapi_client.StoreCreationRequest() # StoreCreationRequest |  (optional)

    try:
        # Create a store
        api_response = api_instance.post_merchants_merchant_id_stores(merchant_id, store_creation_request=store_creation_request)
        print("The response of AccountStoreLevelApi->post_merchants_merchant_id_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->post_merchants_merchant_id_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **store_creation_request** | [**StoreCreationRequest**](StoreCreationRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_stores**
> Store post_stores(store_creation_with_merchant_code_request=store_creation_with_merchant_code_request)

Create a store

Creates a store for the merchant account specified in the request.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Stores read and write

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_creation_with_merchant_code_request = openapi_client.StoreCreationWithMerchantCodeRequest() # StoreCreationWithMerchantCodeRequest |  (optional)

    try:
        # Create a store
        api_response = api_instance.post_stores(store_creation_with_merchant_code_request=store_creation_with_merchant_code_request)
        print("The response of AccountStoreLevelApi->post_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->post_stores: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://management-test.adyen.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://management-test.adyen.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountStoreLevelApi(api_client)
    store_creation_with_merchant_code_request = openapi_client.StoreCreationWithMerchantCodeRequest() # StoreCreationWithMerchantCodeRequest |  (optional)

    try:
        # Create a store
        api_response = api_instance.post_stores(store_creation_with_merchant_code_request=store_creation_with_merchant_code_request)
        print("The response of AccountStoreLevelApi->post_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountStoreLevelApi->post_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_creation_with_merchant_code_request** | [**StoreCreationWithMerchantCodeRequest**](StoreCreationWithMerchantCodeRequest.md)|  | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

