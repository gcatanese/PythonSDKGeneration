# openapi_client.TerminalSettingsStoreLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_merchant_id_stores_reference_terminal_logos**](TerminalSettingsStoreLevelApi.md#get_merchants_merchant_id_stores_reference_terminal_logos) | **GET** /merchants/{merchantId}/stores/{reference}/terminalLogos | Get the terminal logo
[**get_merchants_merchant_id_stores_reference_terminal_settings**](TerminalSettingsStoreLevelApi.md#get_merchants_merchant_id_stores_reference_terminal_settings) | **GET** /merchants/{merchantId}/stores/{reference}/terminalSettings | Get terminal settings
[**get_stores_store_id_terminal_logos**](TerminalSettingsStoreLevelApi.md#get_stores_store_id_terminal_logos) | **GET** /stores/{storeId}/terminalLogos | Get the terminal logo
[**get_stores_store_id_terminal_settings**](TerminalSettingsStoreLevelApi.md#get_stores_store_id_terminal_settings) | **GET** /stores/{storeId}/terminalSettings | Get terminal settings
[**patch_merchants_merchant_id_stores_reference_terminal_logos**](TerminalSettingsStoreLevelApi.md#patch_merchants_merchant_id_stores_reference_terminal_logos) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalLogos | Update the terminal logo
[**patch_merchants_merchant_id_stores_reference_terminal_settings**](TerminalSettingsStoreLevelApi.md#patch_merchants_merchant_id_stores_reference_terminal_settings) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalSettings | Update terminal settings
[**patch_stores_store_id_terminal_logos**](TerminalSettingsStoreLevelApi.md#patch_stores_store_id_terminal_logos) | **PATCH** /stores/{storeId}/terminalLogos | Update the terminal logo
[**patch_stores_store_id_terminal_settings**](TerminalSettingsStoreLevelApi.md#patch_stores_store_id_terminal_settings) | **PATCH** /stores/{storeId}/terminalSettings | Update terminal settings


# **get_merchants_merchant_id_stores_reference_terminal_logos**
> Logo get_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model)

Get the terminal logo

Returns the logo that is configured for a specific payment terminal model at the store identified in the path. You must specify the terminal model as a query parameter.  The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the store, unless a different logo is configured for an individual terminal.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model)
        print("The response of TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model)
        print("The response of TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **reference** | **str**| The reference that identifies the store. | 
 **model** | **str**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. | [optional] 

### Return type

[**Logo**](Logo.md)

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

# **get_merchants_merchant_id_stores_reference_terminal_settings**
> TerminalSettings get_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference)

Get terminal settings

Returns the payment terminal settings that are configured for the store identified in the path. These settings apply to all terminals under the store unless different values are configured for an individual terminal.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.

    try:
        # Get terminal settings
        api_response = api_instance.get_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference)
        print("The response of TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.

    try:
        # Get terminal settings
        api_response = api_instance.get_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference)
        print("The response of TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_merchants_merchant_id_stores_reference_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **reference** | **str**| The reference that identifies the store. | 

### Return type

[**TerminalSettings**](TerminalSettings.md)

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

# **get_stores_store_id_terminal_logos**
> Logo get_stores_store_id_terminal_logos(store_id, model=model)

Get the terminal logo

Returns the logo that is configured for a specific payment terminal model at the store identified in the path. The terminal model must be specified as a query parameter.   The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of that model under the store unless a different logo is configured for an individual terminal.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_stores_store_id_terminal_logos(store_id, model=model)
        print("The response of TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_stores_store_id_terminal_logos(store_id, model=model)
        print("The response of TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 
 **model** | **str**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. | [optional] 

### Return type

[**Logo**](Logo.md)

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

# **get_stores_store_id_terminal_settings**
> TerminalSettings get_stores_store_id_terminal_settings(store_id)

Get terminal settings

Returns the payment terminal settings that are configured for the store identified in the path. These settings apply to all terminals under the store unless different values are configured for an individual terminal.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get terminal settings
        api_response = api_instance.get_stores_store_id_terminal_settings(store_id)
        print("The response of TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.

    try:
        # Get terminal settings
        api_response = api_instance.get_stores_store_id_terminal_settings(store_id)
        print("The response of TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->get_stores_store_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 

### Return type

[**TerminalSettings**](TerminalSettings.md)

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

# **patch_merchants_merchant_id_stores_reference_terminal_logos**
> Logo patch_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model, logo=logo)

Update the terminal logo

Updates the logo that is configured for a specific payment terminal model at the store identified in the path. You must specify the terminal model as a query parameter. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified model under the store, unless a different logo is configured for an individual terminal.   * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model, logo=logo)
        print("The response of TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_merchants_merchant_id_stores_reference_terminal_logos(merchant_id, reference, model=model, logo=logo)
        print("The response of TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **reference** | **str**| The reference that identifies the store. | 
 **model** | **str**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T | [optional] 
 **logo** | [**Logo**](Logo.md)|  | [optional] 

### Return type

[**Logo**](Logo.md)

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

# **patch_merchants_merchant_id_stores_reference_terminal_settings**
> TerminalSettings patch_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference, terminal_settings=terminal_settings)

Update terminal settings

Updates payment terminal settings for the store identified in the path. These settings apply to all terminals under the store, unless different values are configured for an individual terminal.  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    reference = 'reference_example' # str | The reference that identifies the store.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_merchants_merchant_id_stores_reference_terminal_settings(merchant_id, reference, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_merchants_merchant_id_stores_reference_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **reference** | **str**| The reference that identifies the store. | 
 **terminal_settings** | [**TerminalSettings**](TerminalSettings.md)|  | [optional] 

### Return type

[**TerminalSettings**](TerminalSettings.md)

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

# **patch_stores_store_id_terminal_logos**
> Logo patch_stores_store_id_terminal_logos(store_id, model=model, logo=logo)

Update the terminal logo

Updates the logo that is configured for a specific payment terminal model at the store identified in the path. You must specify the terminal model as a query parameter. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified model under the store, unless a different logo is configured for an individual terminal.   * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (merchant or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_stores_store_id_terminal_logos(store_id, model=model, logo=logo)
        print("The response of TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_stores_store_id_terminal_logos(store_id, model=model, logo=logo)
        print("The response of TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 
 **model** | **str**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. | [optional] 
 **logo** | [**Logo**](Logo.md)|  | [optional] 

### Return type

[**Logo**](Logo.md)

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

# **patch_stores_store_id_terminal_settings**
> TerminalSettings patch_stores_store_id_terminal_settings(store_id, terminal_settings=terminal_settings)

Update terminal settings

Updates payment terminal settings for the store identified in the path. These settings apply to all terminals under the store, unless different values are configured for an individual terminal.  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_stores_store_id_terminal_settings(store_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsStoreLevelApi(api_client)
    store_id = 'store_id_example' # str | The unique identifier of the store.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_stores_store_id_terminal_settings(store_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsStoreLevelApi->patch_stores_store_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The unique identifier of the store. | 
 **terminal_settings** | [**TerminalSettings**](TerminalSettings.md)|  | [optional] 

### Return type

[**TerminalSettings**](TerminalSettings.md)

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

