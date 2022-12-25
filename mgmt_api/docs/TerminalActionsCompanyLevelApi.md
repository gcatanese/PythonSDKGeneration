# openapi_client.TerminalActionsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies_company_id_android_apps**](TerminalActionsCompanyLevelApi.md#get_companies_company_id_android_apps) | **GET** /companies/{companyId}/androidApps | Get a list of Android apps
[**get_companies_company_id_android_certificates**](TerminalActionsCompanyLevelApi.md#get_companies_company_id_android_certificates) | **GET** /companies/{companyId}/androidCertificates | Get a list of Android certificates
[**get_companies_company_id_terminal_actions**](TerminalActionsCompanyLevelApi.md#get_companies_company_id_terminal_actions) | **GET** /companies/{companyId}/terminalActions | Get a list of terminal actions
[**get_companies_company_id_terminal_actions_action_id**](TerminalActionsCompanyLevelApi.md#get_companies_company_id_terminal_actions_action_id) | **GET** /companies/{companyId}/terminalActions/{actionId} | Get terminal action


# **get_companies_company_id_android_apps**
> AndroidAppsResponse get_companies_company_id_android_apps(company_id, page_number=page_number, page_size=page_size)

Get a list of Android apps

Returns a list of the Android apps that are available for the company identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of Android apps
        api_response = api_instance.get_companies_company_id_android_apps(company_id, page_number=page_number, page_size=page_size)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_android_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_android_apps: %s\n" % e)
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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of Android apps
        api_response = api_instance.get_companies_company_id_android_apps(company_id, page_number=page_number, page_size=page_size)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_android_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_android_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 

### Return type

[**AndroidAppsResponse**](AndroidAppsResponse.md)

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

# **get_companies_company_id_android_certificates**
> AndroidCertificatesResponse get_companies_company_id_android_certificates(company_id, page_number=page_number, page_size=page_size)

Get a list of Android certificates

Returns a list of the Android certificates that are available for the company identified in the path. Typically, these certificates enable running apps on Android payment terminals. The certifcates in the list have been uploaded to Adyen and can be installed or uninstalled on Android terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of Android certificates
        api_response = api_instance.get_companies_company_id_android_certificates(company_id, page_number=page_number, page_size=page_size)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_android_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_android_certificates: %s\n" % e)
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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of Android certificates
        api_response = api_instance.get_companies_company_id_android_certificates(company_id, page_number=page_number, page_size=page_size)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_android_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_android_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 

### Return type

[**AndroidCertificatesResponse**](AndroidCertificatesResponse.md)

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

# **get_companies_company_id_terminal_actions**
> ListExternalTerminalActionsResponse get_companies_company_id_terminal_actions(company_id, page_number=page_number, page_size=page_size, status=status, type=type)

Get a list of terminal actions

Returns the [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) that have been scheduled for the company identified in the path.The response doesn't include actions that are scheduled by Adyen. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)
    status = 'status_example' # str | Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**. (optional)
    type = 'type_example' # str | Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**. (optional)

    try:
        # Get a list of terminal actions
        api_response = api_instance.get_companies_company_id_terminal_actions(company_id, page_number=page_number, page_size=page_size, status=status, type=type)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions: %s\n" % e)
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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)
    status = 'status_example' # str | Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**. (optional)
    type = 'type_example' # str | Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**. (optional)

    try:
        # Get a list of terminal actions
        api_response = api_instance.get_companies_company_id_terminal_actions(company_id, page_number=page_number, page_size=page_size, status=status, type=type)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 
 **status** | **str**| Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**. | [optional] 
 **type** | **str**| Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**. | [optional] 

### Return type

[**ListExternalTerminalActionsResponse**](ListExternalTerminalActionsResponse.md)

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

# **get_companies_company_id_terminal_actions_action_id**
> ExternalTerminalAction get_companies_company_id_terminal_actions_action_id(company_id, action_id)

Get terminal action

Returns the details of the [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) identified in the path. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    action_id = 'action_id_example' # str | The unique identifier of the terminal action.

    try:
        # Get terminal action
        api_response = api_instance.get_companies_company_id_terminal_actions_action_id(company_id, action_id)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions_action_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions_action_id: %s\n" % e)
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
    api_instance = openapi_client.TerminalActionsCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    action_id = 'action_id_example' # str | The unique identifier of the terminal action.

    try:
        # Get terminal action
        api_response = api_instance.get_companies_company_id_terminal_actions_action_id(company_id, action_id)
        print("The response of TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions_action_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsCompanyLevelApi->get_companies_company_id_terminal_actions_action_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **action_id** | **str**| The unique identifier of the terminal action. | 

### Return type

[**ExternalTerminalAction**](ExternalTerminalAction.md)

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

