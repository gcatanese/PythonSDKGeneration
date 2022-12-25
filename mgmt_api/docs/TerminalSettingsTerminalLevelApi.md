# openapi_client.TerminalSettingsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminals_terminal_id_terminal_logos**](TerminalSettingsTerminalLevelApi.md#get_terminals_terminal_id_terminal_logos) | **GET** /terminals/{terminalId}/terminalLogos | Get the terminal logo
[**get_terminals_terminal_id_terminal_settings**](TerminalSettingsTerminalLevelApi.md#get_terminals_terminal_id_terminal_settings) | **GET** /terminals/{terminalId}/terminalSettings | Get terminal settings
[**patch_terminals_terminal_id_terminal_logos**](TerminalSettingsTerminalLevelApi.md#patch_terminals_terminal_id_terminal_logos) | **PATCH** /terminals/{terminalId}/terminalLogos | Update the logo
[**patch_terminals_terminal_id_terminal_settings**](TerminalSettingsTerminalLevelApi.md#patch_terminals_terminal_id_terminal_settings) | **PATCH** /terminals/{terminalId}/terminalSettings | Update terminal settings


# **get_terminals_terminal_id_terminal_logos**
> Logo get_terminals_terminal_id_terminal_logos(terminal_id)

Get the terminal logo

Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.

    try:
        # Get the terminal logo
        api_response = api_instance.get_terminals_terminal_id_terminal_logos(terminal_id)
        print("The response of TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.

    try:
        # Get the terminal logo
        api_response = api_instance.get_terminals_terminal_id_terminal_logos(terminal_id)
        print("The response of TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| The unique identifier of the payment terminal. | 

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

# **get_terminals_terminal_id_terminal_settings**
> TerminalSettings get_terminals_terminal_id_terminal_settings(terminal_id)

Get terminal settings

Returns the settings that are configured for the payment terminal identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.

    try:
        # Get terminal settings
        api_response = api_instance.get_terminals_terminal_id_terminal_settings(terminal_id)
        print("The response of TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.

    try:
        # Get terminal settings
        api_response = api_instance.get_terminals_terminal_id_terminal_settings(terminal_id)
        print("The response of TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->get_terminals_terminal_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| The unique identifier of the payment terminal. | 

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

# **patch_terminals_terminal_id_terminal_logos**
> Logo patch_terminals_terminal_id_terminal_logos(terminal_id, logo=logo)

Update the logo

Updates the logo for the payment terminal identified in the path.  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the logo
        api_response = api_instance.patch_terminals_terminal_id_terminal_logos(terminal_id, logo=logo)
        print("The response of TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the logo
        api_response = api_instance.patch_terminals_terminal_id_terminal_logos(terminal_id, logo=logo)
        print("The response of TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| The unique identifier of the payment terminal. | 
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

# **patch_terminals_terminal_id_terminal_settings**
> TerminalSettings patch_terminals_terminal_id_terminal_settings(terminal_id, terminal_settings=terminal_settings)

Update terminal settings

Updates the settings that are configured for the payment terminal identified in the path.  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_terminals_terminal_id_terminal_settings(terminal_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsTerminalLevelApi(api_client)
    terminal_id = 'terminal_id_example' # str | The unique identifier of the payment terminal.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_terminals_terminal_id_terminal_settings(terminal_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsTerminalLevelApi->patch_terminals_terminal_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| The unique identifier of the payment terminal. | 
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

