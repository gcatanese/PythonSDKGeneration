# openapi_client.UsersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies_company_id_users**](UsersCompanyLevelApi.md#get_companies_company_id_users) | **GET** /companies/{companyId}/users | Get a list of users
[**get_companies_company_id_users_user_id**](UsersCompanyLevelApi.md#get_companies_company_id_users_user_id) | **GET** /companies/{companyId}/users/{userId} | Get user details
[**patch_companies_company_id_users_user_id**](UsersCompanyLevelApi.md#patch_companies_company_id_users_user_id) | **PATCH** /companies/{companyId}/users/{userId} | Update user details
[**post_companies_company_id_users**](UsersCompanyLevelApi.md#post_companies_company_id_users) | **POST** /companies/{companyId}/users | Create a new user


# **get_companies_company_id_users**
> ListCompanyUsersResponse get_companies_company_id_users(company_id, page_number=page_number, page_size=page_size)

Get a list of users

Returns the list of users for the `companyId` identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to return. (optional)
    page_size = 56 # int | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. (optional)

    try:
        # Get a list of users
        api_response = api_instance.get_companies_company_id_users(company_id, page_number=page_number, page_size=page_size)
        print("The response of UsersCompanyLevelApi->get_companies_company_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->get_companies_company_id_users: %s\n" % e)
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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to return. (optional)
    page_size = 56 # int | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. (optional)

    try:
        # Get a list of users
        api_response = api_instance.get_companies_company_id_users(company_id, page_number=page_number, page_size=page_size)
        print("The response of UsersCompanyLevelApi->get_companies_company_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->get_companies_company_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **page_number** | **int**| The number of the page to return. | [optional] 
 **page_size** | **int**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] 

### Return type

[**ListCompanyUsersResponse**](ListCompanyUsersResponse.md)

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

# **get_companies_company_id_users_user_id**
> CompanyUser get_companies_company_id_users_user_id(company_id, user_id)

Get user details

Returns user details for the `userId` and the `companyId` identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user details
        api_response = api_instance.get_companies_company_id_users_user_id(company_id, user_id)
        print("The response of UsersCompanyLevelApi->get_companies_company_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->get_companies_company_id_users_user_id: %s\n" % e)
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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    user_id = 'user_id_example' # str | The unique identifier of the user.

    try:
        # Get user details
        api_response = api_instance.get_companies_company_id_users_user_id(company_id, user_id)
        print("The response of UsersCompanyLevelApi->get_companies_company_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->get_companies_company_id_users_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **user_id** | **str**| The unique identifier of the user. | 

### Return type

[**CompanyUser**](CompanyUser.md)

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

# **patch_companies_company_id_users_user_id**
> CompanyUser patch_companies_company_id_users_user_id(company_id, user_id, update_company_user_request=update_company_user_request)

Update user details

Updates user details for the `userId` and the `companyId` identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_company_user_request = openapi_client.UpdateCompanyUserRequest() # UpdateCompanyUserRequest |  (optional)

    try:
        # Update user details
        api_response = api_instance.patch_companies_company_id_users_user_id(company_id, user_id, update_company_user_request=update_company_user_request)
        print("The response of UsersCompanyLevelApi->patch_companies_company_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->patch_companies_company_id_users_user_id: %s\n" % e)
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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    user_id = 'user_id_example' # str | The unique identifier of the user.
    update_company_user_request = openapi_client.UpdateCompanyUserRequest() # UpdateCompanyUserRequest |  (optional)

    try:
        # Update user details
        api_response = api_instance.patch_companies_company_id_users_user_id(company_id, user_id, update_company_user_request=update_company_user_request)
        print("The response of UsersCompanyLevelApi->patch_companies_company_id_users_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->patch_companies_company_id_users_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **user_id** | **str**| The unique identifier of the user. | 
 **update_company_user_request** | [**UpdateCompanyUserRequest**](UpdateCompanyUserRequest.md)|  | [optional] 

### Return type

[**CompanyUser**](CompanyUser.md)

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

# **post_companies_company_id_users**
> CreateCompanyUserResponse post_companies_company_id_users(company_id, create_company_user_request=create_company_user_request)

Create a new user

Creates the user for the `companyId` identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    create_company_user_request = openapi_client.CreateCompanyUserRequest() # CreateCompanyUserRequest |  (optional)

    try:
        # Create a new user
        api_response = api_instance.post_companies_company_id_users(company_id, create_company_user_request=create_company_user_request)
        print("The response of UsersCompanyLevelApi->post_companies_company_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->post_companies_company_id_users: %s\n" % e)
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
    api_instance = openapi_client.UsersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    create_company_user_request = openapi_client.CreateCompanyUserRequest() # CreateCompanyUserRequest |  (optional)

    try:
        # Create a new user
        api_response = api_instance.post_companies_company_id_users(company_id, create_company_user_request=create_company_user_request)
        print("The response of UsersCompanyLevelApi->post_companies_company_id_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCompanyLevelApi->post_companies_company_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **create_company_user_request** | [**CreateCompanyUserRequest**](CreateCompanyUserRequest.md)|  | [optional] 

### Return type

[**CreateCompanyUserResponse**](CreateCompanyUserResponse.md)

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

