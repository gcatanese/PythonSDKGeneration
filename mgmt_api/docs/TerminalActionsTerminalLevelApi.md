# openapi_client.TerminalActionsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_terminals_schedule_actions**](TerminalActionsTerminalLevelApi.md#post_terminals_schedule_actions) | **POST** /terminals/scheduleActions | Create a terminal action


# **post_terminals_schedule_actions**
> ScheduleTerminalActionsResponse post_terminals_schedule_actions(schedule_terminal_actions_request=schedule_terminal_actions_request)

Create a terminal action

Schedules a [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) by specifying the action and the terminals that the action must be applied to.   The following restrictions apply: * You can schedule only one action at a time. For example, to install a new app version and remove an old app version, you have to make two API requests.  * The maximum number of terminals in a request is **100**. For example, to apply an action to 250 terminals, you have to divide the terminals over three API requests.  * If there is an error with one or more terminal IDs in the request, the action is scheduled for none of the terminals. You need to fix the error and try again.   To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read and write

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
    api_instance = openapi_client.TerminalActionsTerminalLevelApi(api_client)
    schedule_terminal_actions_request = openapi_client.ScheduleTerminalActionsRequest() # ScheduleTerminalActionsRequest |  (optional)

    try:
        # Create a terminal action
        api_response = api_instance.post_terminals_schedule_actions(schedule_terminal_actions_request=schedule_terminal_actions_request)
        print("The response of TerminalActionsTerminalLevelApi->post_terminals_schedule_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsTerminalLevelApi->post_terminals_schedule_actions: %s\n" % e)
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
    api_instance = openapi_client.TerminalActionsTerminalLevelApi(api_client)
    schedule_terminal_actions_request = openapi_client.ScheduleTerminalActionsRequest() # ScheduleTerminalActionsRequest |  (optional)

    try:
        # Create a terminal action
        api_response = api_instance.post_terminals_schedule_actions(schedule_terminal_actions_request=schedule_terminal_actions_request)
        print("The response of TerminalActionsTerminalLevelApi->post_terminals_schedule_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalActionsTerminalLevelApi->post_terminals_schedule_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_terminal_actions_request** | [**ScheduleTerminalActionsRequest**](ScheduleTerminalActionsRequest.md)|  | [optional] 

### Return type

[**ScheduleTerminalActionsResponse**](ScheduleTerminalActionsResponse.md)

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

