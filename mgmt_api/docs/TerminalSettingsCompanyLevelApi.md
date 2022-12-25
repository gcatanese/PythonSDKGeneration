# openapi_client.TerminalSettingsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies_company_id_terminal_logos**](TerminalSettingsCompanyLevelApi.md#get_companies_company_id_terminal_logos) | **GET** /companies/{companyId}/terminalLogos | Get the terminal logo
[**get_companies_company_id_terminal_settings**](TerminalSettingsCompanyLevelApi.md#get_companies_company_id_terminal_settings) | **GET** /companies/{companyId}/terminalSettings | Get terminal settings
[**patch_companies_company_id_terminal_logos**](TerminalSettingsCompanyLevelApi.md#patch_companies_company_id_terminal_logos) | **PATCH** /companies/{companyId}/terminalLogos | Update the terminal logo
[**patch_companies_company_id_terminal_settings**](TerminalSettingsCompanyLevelApi.md#patch_companies_company_id_terminal_settings) | **PATCH** /companies/{companyId}/terminalSettings | Update terminal settings


# **get_companies_company_id_terminal_logos**
> Logo get_companies_company_id_terminal_logos(company_id, model=model)

Get the terminal logo

Returns the logo that is configured for a specific payment terminal model at the company identified in the path. You must specify the terminal model as a query parameter.   The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_companies_company_id_terminal_logos(company_id, model=model)
        print("The response of TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)

    try:
        # Get the terminal logo
        api_response = api_instance.get_companies_company_id_terminal_logos(company_id, model=model)
        print("The response of TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
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

# **get_companies_company_id_terminal_settings**
> TerminalSettings get_companies_company_id_terminal_settings(company_id)

Get terminal settings

Returns the payment terminal settings that are configured for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.

    try:
        # Get terminal settings
        api_response = api_instance.get_companies_company_id_terminal_settings(company_id)
        print("The response of TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.

    try:
        # Get terminal settings
        api_response = api_instance.get_companies_company_id_terminal_settings(company_id)
        print("The response of TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->get_companies_company_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 

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

# **patch_companies_company_id_terminal_logos**
> Logo patch_companies_company_id_terminal_logos(company_id, model=model, logo=logo)

Update the terminal logo

Updates the logo that is configured for a specific payment terminal model at the company identified in the path. You must specify the terminal model as a query parameter. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the Adyen PSP level, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_companies_company_id_terminal_logos(company_id, model=model, logo=logo)
        print("The response of TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_logos: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    model = 'model_example' # str | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. (optional)
    logo = openapi_client.Logo() # Logo |  (optional)

    try:
        # Update the terminal logo
        api_response = api_instance.patch_companies_company_id_terminal_logos(company_id, model=model, logo=logo)
        print("The response of TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_logos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
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

# **patch_companies_company_id_terminal_settings**
> TerminalSettings patch_companies_company_id_terminal_settings(company_id, terminal_settings=terminal_settings)

Update terminal settings

Updates payment terminal settings for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from the Adyen PSP level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_companies_company_id_terminal_settings(company_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_settings: %s\n" % e)
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
    api_instance = openapi_client.TerminalSettingsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    terminal_settings = openapi_client.TerminalSettings() # TerminalSettings |  (optional)

    try:
        # Update terminal settings
        api_response = api_instance.patch_companies_company_id_terminal_settings(company_id, terminal_settings=terminal_settings)
        print("The response of TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalSettingsCompanyLevelApi->patch_companies_company_id_terminal_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
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

