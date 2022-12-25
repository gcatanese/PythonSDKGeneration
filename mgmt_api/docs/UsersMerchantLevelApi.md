# openapi_client.UsersMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_merchant_id_users**](UsersMerchantLevelApi.md#get_merchants_merchant_id_users) | **GET** /merchants/{merchantId}/users | Get a list of users
[**get_merchants_merchant_id_users_user_id**](UsersMerchantLevelApi.md#get_merchants_merchant_id_users_user_id) | **GET** /merchants/{merchantId}/users/{userId} | Get user details
[**patch_merchants_merchant_id_users_user_id**](UsersMerchantLevelApi.md#patch_merchants_merchant_id_users_user_id) | **PATCH** /merchants/{merchantId}/users/{userId} | Update a user
[**post_merchants_merchant_id_users**](UsersMerchantLevelApi.md#post_merchants_merchant_id_users) | **POST** /merchants/{merchantId}/users | Create a new user


# **get_merchants_merchant_id_users**
> ListMerchantUsersResponse get_merchants_merchant_id_users(merchant_id, page_number=page_number, page_size=page_size)

Get a list of users

Returns a list of users associated with the `merchantId` specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. (optional)

    try:
        # Get a list of users
        api_response = api_instance.get_merchants_merchant_id_users(merchant_id, page_number=page_number, page_size=page_size)
        print("The response of UsersMerchantLevelApi->get_merchants_merchant_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->get_merchants_merchant_id_users: %s\n" % e)
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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. (optional)

    try:
        # Get a list of users
        api_response = api_instance.get_merchants_merchant_id_users(merchant_id, page_number=page_number, page_size=page_size)
        print("The response of UsersMerchantLevelApi->get_merchants_merchant_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->get_merchants_merchant_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique identifier of the merchant. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] 

### Return type

[**ListMerchantUsersResponse**](ListMerchantUsersResponse.md)

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

# **get_merchants_merchant_id_users_user_id**
> User get_merchants_merchant_id_users_user_id(merchant_id, user_id)

Get user details

Returns user details for the `userId` and the `merchantId` specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    user_id = 'user_id_example' # str | Unique identifier of the user.

    try:
        # Get user details
        api_response = api_instance.get_merchants_merchant_id_users_user_id(merchant_id, user_id)
        print("The response of UsersMerchantLevelApi->get_merchants_merchant_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->get_merchants_merchant_id_users_user_id: %s\n" % e)
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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    user_id = 'user_id_example' # str | Unique identifier of the user.

    try:
        # Get user details
        api_response = api_instance.get_merchants_merchant_id_users_user_id(merchant_id, user_id)
        print("The response of UsersMerchantLevelApi->get_merchants_merchant_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->get_merchants_merchant_id_users_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique identifier of the merchant. | 
 **user_id** | **str**| Unique identifier of the user. | 

### Return type

[**User**](User.md)

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

# **patch_merchants_merchant_id_users_user_id**
> User patch_merchants_merchant_id_users_user_id(merchant_id, user_id, update_merchant_user_request=update_merchant_user_request)

Update a user

Updates user details for the `userId` and the `merchantId` specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    user_id = 'user_id_example' # str | Unique identifier of the user.
    update_merchant_user_request = openapi_client.UpdateMerchantUserRequest() # UpdateMerchantUserRequest |  (optional)

    try:
        # Update a user
        api_response = api_instance.patch_merchants_merchant_id_users_user_id(merchant_id, user_id, update_merchant_user_request=update_merchant_user_request)
        print("The response of UsersMerchantLevelApi->patch_merchants_merchant_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->patch_merchants_merchant_id_users_user_id: %s\n" % e)
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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    user_id = 'user_id_example' # str | Unique identifier of the user.
    update_merchant_user_request = openapi_client.UpdateMerchantUserRequest() # UpdateMerchantUserRequest |  (optional)

    try:
        # Update a user
        api_response = api_instance.patch_merchants_merchant_id_users_user_id(merchant_id, user_id, update_merchant_user_request=update_merchant_user_request)
        print("The response of UsersMerchantLevelApi->patch_merchants_merchant_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->patch_merchants_merchant_id_users_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique identifier of the merchant. | 
 **user_id** | **str**| Unique identifier of the user. | 
 **update_merchant_user_request** | [**UpdateMerchantUserRequest**](UpdateMerchantUserRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **post_merchants_merchant_id_users**
> CreateUserResponse post_merchants_merchant_id_users(merchant_id, create_merchant_user_request=create_merchant_user_request)

Create a new user

Creates a user for the `merchantId` specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    create_merchant_user_request = openapi_client.CreateMerchantUserRequest() # CreateMerchantUserRequest |  (optional)

    try:
        # Create a new user
        api_response = api_instance.post_merchants_merchant_id_users(merchant_id, create_merchant_user_request=create_merchant_user_request)
        print("The response of UsersMerchantLevelApi->post_merchants_merchant_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->post_merchants_merchant_id_users: %s\n" % e)
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
    api_instance = openapi_client.UsersMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | Unique identifier of the merchant.
    create_merchant_user_request = openapi_client.CreateMerchantUserRequest() # CreateMerchantUserRequest |  (optional)

    try:
        # Create a new user
        api_response = api_instance.post_merchants_merchant_id_users(merchant_id, create_merchant_user_request=create_merchant_user_request)
        print("The response of UsersMerchantLevelApi->post_merchants_merchant_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersMerchantLevelApi->post_merchants_merchant_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Unique identifier of the merchant. | 
 **create_merchant_user_request** | [**CreateMerchantUserRequest**](CreateMerchantUserRequest.md)|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

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

