# openapi_client.APIKeyCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_companies_company_id_api_credentials_api_credential_id_generate_api_key**](APIKeyCompanyLevelApi.md#post_companies_company_id_api_credentials_api_credential_id_generate_api_key) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key


# **post_companies_company_id_api_credentials_api_credential_id_generate_api_key**
> GenerateApiKeyResponse post_companies_company_id_api_credentials_api_credential_id_generate_api_key(company_id, api_credential_id)

Generate new API key

Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.APIKeyCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Generate new API key
        api_response = api_instance.post_companies_company_id_api_credentials_api_credential_id_generate_api_key(company_id, api_credential_id)
        print("The response of APIKeyCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_generate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_generate_api_key: %s\n" % e)
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
    api_instance = openapi_client.APIKeyCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Generate new API key
        api_response = api_instance.post_companies_company_id_api_credentials_api_credential_id_generate_api_key(company_id, api_credential_id)
        print("The response of APIKeyCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_generate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyCompanyLevelApi->post_companies_company_id_api_credentials_api_credential_id_generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 

### Return type

[**GenerateApiKeyResponse**](GenerateApiKeyResponse.md)

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

