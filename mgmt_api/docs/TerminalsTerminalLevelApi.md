# openapi_client.TerminalsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminals**](TerminalsTerminalLevelApi.md#get_terminals) | **GET** /terminals | Get a list of terminals


# **get_terminals**
> ListTerminalsResponse get_terminals(search_query=search_query, countries=countries, merchant_ids=merchant_ids, store_ids=store_ids, brand_models=brand_models, page_number=page_number, page_size=page_size)

Get a list of terminals

Returns the payment terminals that the API credential has access to and that match the query parameters.  When using `searchQuery`, other query parameters are ignored.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * POS Terminal Management API * Management API—Terminal settings read

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
    api_instance = openapi_client.TerminalsTerminalLevelApi(api_client)
    search_query = 'search_query_example' # str | Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored. (optional)
    countries = 'countries_example' # str | Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). (optional)
    merchant_ids = 'merchant_ids_example' # str | Returns terminals that belong to the merchant accounts specified by their unique merchant account ID. (optional)
    store_ids = 'store_ids_example' # str | Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID. (optional)
    brand_models = 'brand_models_example' # str | Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*. (optional)
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of terminals
        api_response = api_instance.get_terminals(search_query=search_query, countries=countries, merchant_ids=merchant_ids, store_ids=store_ids, brand_models=brand_models, page_number=page_number, page_size=page_size)
        print("The response of TerminalsTerminalLevelApi->get_terminals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsTerminalLevelApi->get_terminals: %s\n" % e)
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
    api_instance = openapi_client.TerminalsTerminalLevelApi(api_client)
    search_query = 'search_query_example' # str | Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored. (optional)
    countries = 'countries_example' # str | Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). (optional)
    merchant_ids = 'merchant_ids_example' # str | Returns terminals that belong to the merchant accounts specified by their unique merchant account ID. (optional)
    store_ids = 'store_ids_example' # str | Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID. (optional)
    brand_models = 'brand_models_example' # str | Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*. (optional)
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 20 items on a page. (optional)

    try:
        # Get a list of terminals
        api_response = api_instance.get_terminals(search_query=search_query, countries=countries, merchant_ids=merchant_ids, store_ids=store_ids, brand_models=brand_models, page_number=page_number, page_size=page_size)
        print("The response of TerminalsTerminalLevelApi->get_terminals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsTerminalLevelApi->get_terminals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**| Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored. | [optional] 
 **countries** | **str**| Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | [optional] 
 **merchant_ids** | **str**| Returns terminals that belong to the merchant accounts specified by their unique merchant account ID. | [optional] 
 **store_ids** | **str**| Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID. | [optional] 
 **brand_models** | **str**| Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*. | [optional] 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 

### Return type

[**ListTerminalsResponse**](ListTerminalsResponse.md)

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

