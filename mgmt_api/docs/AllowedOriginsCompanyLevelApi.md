# openapi_client.AllowedOriginsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id**](AllowedOriginsCompanyLevelApi.md#delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id) | **DELETE** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin
[**get_companies_company_id_api_credentials_api_credential_id_allowed_origins**](AllowedOriginsCompanyLevelApi.md#get_companies_company_id_api_credentials_api_credential_id_allowed_origins) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins
[**get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id**](AllowedOriginsCompanyLevelApi.md#get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin
[**post_companies_company_id_api_credentials_api_credential_id_allowed_origins**](AllowedOriginsCompanyLevelApi.md#post_companies_company_id_api_credentials_api_credential_id_allowed_origins) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin


# **delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id**
> delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)

Delete an allowed origin

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    origin_id = 'origin_id_example' # str | Unique identifier of the allowed origin.

    try:
        # Delete an allowed origin
        api_instance.delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id: %s\n" % e)
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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    origin_id = 'origin_id_example' # str | Unique identifier of the allowed origin.

    try:
        # Delete an allowed origin
        api_instance.delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->delete_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 
 **origin_id** | **str**| Unique identifier of the allowed origin. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_companies_company_id_api_credentials_api_credential_id_allowed_origins**
> AllowedOriginsResponse get_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id)

Get a list of allowed origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Get a list of allowed origins
        api_response = api_instance.get_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id)
        print("The response of AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins: %s\n" % e)
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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Get a list of allowed origins
        api_response = api_instance.get_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id)
        print("The response of AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

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

# **get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id**
> AllowedOrigin get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)

Get an allowed origin

Returns the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    origin_id = 'origin_id_example' # str | Unique identifier of the allowed origin.

    try:
        # Get an allowed origin
        api_response = api_instance.get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)
        print("The response of AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id: %s\n" % e)
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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    origin_id = 'origin_id_example' # str | Unique identifier of the allowed origin.

    try:
        # Get an allowed origin
        api_response = api_instance.get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id(company_id, api_credential_id, origin_id)
        print("The response of AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->get_companies_company_id_api_credentials_api_credential_id_allowed_origins_origin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 
 **origin_id** | **str**| Unique identifier of the allowed origin. | 

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

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

# **post_companies_company_id_api_credentials_api_credential_id_allowed_origins**
> AllowedOriginsResponse post_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id, allowed_origin=allowed_origin)

Create an allowed origin

Adds a new [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) to the API credential's list of allowed origins.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    allowed_origin = openapi_client.AllowedOrigin() # AllowedOrigin |  (optional)

    try:
        # Create an allowed origin
        api_response = api_instance.post_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id, allowed_origin=allowed_origin)
        print("The response of AllowedOriginsCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_allowed_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_allowed_origins: %s\n" % e)
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
    api_instance = openapi_client.AllowedOriginsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    allowed_origin = openapi_client.AllowedOrigin() # AllowedOrigin |  (optional)

    try:
        # Create an allowed origin
        api_response = api_instance.post_companies_company_id_api_credentials_api_credential_id_allowed_origins(company_id, api_credential_id, allowed_origin=allowed_origin)
        print("The response of AllowedOriginsCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_allowed_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedOriginsCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_allowed_origins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 
 **allowed_origin** | [**AllowedOrigin**](AllowedOrigin.md)|  | [optional] 

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

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

