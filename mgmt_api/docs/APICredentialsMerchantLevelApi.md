# openapi_client.APICredentialsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_merchant_id_api_credentials**](APICredentialsMerchantLevelApi.md#get_merchants_merchant_id_api_credentials) | **GET** /merchants/{merchantId}/apiCredentials | Get a list of API credentials
[**get_merchants_merchant_id_api_credentials_api_credential_id**](APICredentialsMerchantLevelApi.md#get_merchants_merchant_id_api_credentials_api_credential_id) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Get an API credential
[**patch_merchants_merchant_id_api_credentials_api_credential_id**](APICredentialsMerchantLevelApi.md#patch_merchants_merchant_id_api_credentials_api_credential_id) | **PATCH** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Update an API credential
[**post_merchants_merchant_id_api_credentials**](APICredentialsMerchantLevelApi.md#post_merchants_merchant_id_api_credentials) | **POST** /merchants/{merchantId}/apiCredentials | Create an API credential


# **get_merchants_merchant_id_api_credentials**
> ListMerchantApiCredentialsResponse get_merchants_merchant_id_api_credentials(merchant_id, page_number=page_number, page_size=page_size)

Get a list of API credentials

Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the merchant account. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)

    try:
        # Get a list of API credentials
        api_response = api_instance.get_merchants_merchant_id_api_credentials(merchant_id, page_number=page_number, page_size=page_size)
        print("The response of APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials: %s\n" % e)
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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)

    try:
        # Get a list of API credentials
        api_response = api_instance.get_merchants_merchant_id_api_credentials(merchant_id, page_number=page_number, page_size=page_size)
        print("The response of APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListMerchantApiCredentialsResponse**](ListMerchantApiCredentialsResponse.md)

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

# **get_merchants_merchant_id_api_credentials_api_credential_id**
> ApiCredential get_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id)

Get an API credential

Returns the [API credential](https://docs.adyen.com/development-resources/api-credentials) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Get an API credential
        api_response = api_instance.get_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id)
        print("The response of APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials_api_credential_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials_api_credential_id: %s\n" % e)
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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Get an API credential
        api_response = api_instance.get_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id)
        print("The response of APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials_api_credential_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->get_merchants_merchant_id_api_credentials_api_credential_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 

### Return type

[**ApiCredential**](ApiCredential.md)

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

# **patch_merchants_merchant_id_api_credentials_api_credential_id**
> ApiCredential patch_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id, update_merchant_api_credential_request=update_merchant_api_credential_request)

Update an API credential

Changes the API credential's roles, or allowed origins. The request has the new values for the fields you want to change. The response contains the full updated API credential, including the new values from the request.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    update_merchant_api_credential_request = openapi_client.UpdateMerchantApiCredentialRequest() # UpdateMerchantApiCredentialRequest |  (optional)

    try:
        # Update an API credential
        api_response = api_instance.patch_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id, update_merchant_api_credential_request=update_merchant_api_credential_request)
        print("The response of APICredentialsMerchantLevelApi->patch_merchants_merchant_id_api_credentials_api_credential_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->patch_merchants_merchant_id_api_credentials_api_credential_id: %s\n" % e)
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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.
    update_merchant_api_credential_request = openapi_client.UpdateMerchantApiCredentialRequest() # UpdateMerchantApiCredentialRequest |  (optional)

    try:
        # Update an API credential
        api_response = api_instance.patch_merchants_merchant_id_api_credentials_api_credential_id(merchant_id, api_credential_id, update_merchant_api_credential_request=update_merchant_api_credential_request)
        print("The response of APICredentialsMerchantLevelApi->patch_merchants_merchant_id_api_credentials_api_credential_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->patch_merchants_merchant_id_api_credentials_api_credential_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 
 **update_merchant_api_credential_request** | [**UpdateMerchantApiCredentialRequest**](UpdateMerchantApiCredentialRequest.md)|  | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

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

# **post_merchants_merchant_id_api_credentials**
> CreateApiCredentialResponse post_merchants_merchant_id_api_credentials(merchant_id, create_merchant_api_credential_request=create_merchant_api_credential_request)

Create an API credential

Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify the roles and allowed origins for the new API credential.  The response includes the: * [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication. * [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication. * [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.  > Make sure you store the API key securely in your system. You won't be able to retrieve it later.  If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    create_merchant_api_credential_request = openapi_client.CreateMerchantApiCredentialRequest() # CreateMerchantApiCredentialRequest |  (optional)

    try:
        # Create an API credential
        api_response = api_instance.post_merchants_merchant_id_api_credentials(merchant_id, create_merchant_api_credential_request=create_merchant_api_credential_request)
        print("The response of APICredentialsMerchantLevelApi->post_merchants_merchant_id_api_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->post_merchants_merchant_id_api_credentials: %s\n" % e)
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
    api_instance = openapi_client.APICredentialsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    create_merchant_api_credential_request = openapi_client.CreateMerchantApiCredentialRequest() # CreateMerchantApiCredentialRequest |  (optional)

    try:
        # Create an API credential
        api_response = api_instance.post_merchants_merchant_id_api_credentials(merchant_id, create_merchant_api_credential_request=create_merchant_api_credential_request)
        print("The response of APICredentialsMerchantLevelApi->post_merchants_merchant_id_api_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICredentialsMerchantLevelApi->post_merchants_merchant_id_api_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **create_merchant_api_credential_request** | [**CreateMerchantApiCredentialRequest**](CreateMerchantApiCredentialRequest.md)|  | [optional] 

### Return type

[**CreateApiCredentialResponse**](CreateApiCredentialResponse.md)

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

