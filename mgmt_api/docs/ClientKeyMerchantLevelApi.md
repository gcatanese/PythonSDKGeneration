# openapi_client.ClientKeyMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key**](ClientKeyMerchantLevelApi.md#post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key


# **post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key**
> GenerateClientKeyResponse post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key(merchant_id, api_credential_id)

Generate new client key

Returns a new [client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works) for the API credential identified in the path. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

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
    api_instance = openapi_client.ClientKeyMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Generate new client key
        api_response = api_instance.post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key(merchant_id, api_credential_id)
        print("The response of ClientKeyMerchantLevelApi->post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientKeyMerchantLevelApi->post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key: %s\n" % e)
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
    api_instance = openapi_client.ClientKeyMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    api_credential_id = 'api_credential_id_example' # str | Unique identifier of the API credential.

    try:
        # Generate new client key
        api_response = api_instance.post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key(merchant_id, api_credential_id)
        print("The response of ClientKeyMerchantLevelApi->post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientKeyMerchantLevelApi->post_merchants_merchant_id_api_credentials_api_credential_id_generate_client_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **api_credential_id** | **str**| Unique identifier of the API credential. | 

### Return type

[**GenerateClientKeyResponse**](GenerateClientKeyResponse.md)

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

