# openapi_client.TerminalOrdersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_companies_company_id_billing_entities**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_billing_entities) | **GET** /companies/{companyId}/billingEntities | Get a list of billing entities
[**get_companies_company_id_shipping_locations**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_shipping_locations) | **GET** /companies/{companyId}/shippingLocations | Get a list of shipping locations
[**get_companies_company_id_terminal_models**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_terminal_models) | **GET** /companies/{companyId}/terminalModels | Get a list of terminal models
[**get_companies_company_id_terminal_orders**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_terminal_orders) | **GET** /companies/{companyId}/terminalOrders | Get a list of orders
[**get_companies_company_id_terminal_orders_order_id**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_terminal_orders_order_id) | **GET** /companies/{companyId}/terminalOrders/{orderId} | Get an order
[**get_companies_company_id_terminal_products**](TerminalOrdersCompanyLevelApi.md#get_companies_company_id_terminal_products) | **GET** /companies/{companyId}/terminalProducts | Get a list of terminal products
[**patch_companies_company_id_terminal_orders_order_id**](TerminalOrdersCompanyLevelApi.md#patch_companies_company_id_terminal_orders_order_id) | **PATCH** /companies/{companyId}/terminalOrders/{orderId} | Update an order
[**post_companies_company_id_shipping_locations**](TerminalOrdersCompanyLevelApi.md#post_companies_company_id_shipping_locations) | **POST** /companies/{companyId}/shippingLocations | Create a shipping location
[**post_companies_company_id_terminal_orders**](TerminalOrdersCompanyLevelApi.md#post_companies_company_id_terminal_orders) | **POST** /companies/{companyId}/terminalOrders | Create an order
[**post_companies_company_id_terminal_orders_order_id_cancel**](TerminalOrdersCompanyLevelApi.md#post_companies_company_id_terminal_orders_order_id_cancel) | **POST** /companies/{companyId}/terminalOrders/{orderId}/cancel | Cancel an order


# **get_companies_company_id_billing_entities**
> BillingEntitiesResponse get_companies_company_id_billing_entities(company_id, name=name)

Get a list of billing entities

Returns the billing entities of the company identified in the path and all merchant accounts belonging to the company. A billing entity is a legal entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    name = 'name_example' # str | The name of the billing entity. (optional)

    try:
        # Get a list of billing entities
        api_response = api_instance.get_companies_company_id_billing_entities(company_id, name=name)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_billing_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_billing_entities: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    name = 'name_example' # str | The name of the billing entity. (optional)

    try:
        # Get a list of billing entities
        api_response = api_instance.get_companies_company_id_billing_entities(company_id, name=name)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_billing_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_billing_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **name** | **str**| The name of the billing entity. | [optional] 

### Return type

[**BillingEntitiesResponse**](BillingEntitiesResponse.md)

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

# **get_companies_company_id_shipping_locations**
> ShippingLocationsResponse get_companies_company_id_shipping_locations(company_id, name=name, offset=offset, limit=limit)

Get a list of shipping locations

Returns the shipping locations for the company identified in the path and all merchant accounts belonging to the company. A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    name = 'name_example' # str | The name of the shipping location. (optional)
    offset = 56 # int | The number of locations to skip. (optional)
    limit = 56 # int | The number of locations to return. (optional)

    try:
        # Get a list of shipping locations
        api_response = api_instance.get_companies_company_id_shipping_locations(company_id, name=name, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_shipping_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_shipping_locations: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    name = 'name_example' # str | The name of the shipping location. (optional)
    offset = 56 # int | The number of locations to skip. (optional)
    limit = 56 # int | The number of locations to return. (optional)

    try:
        # Get a list of shipping locations
        api_response = api_instance.get_companies_company_id_shipping_locations(company_id, name=name, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_shipping_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_shipping_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **name** | **str**| The name of the shipping location. | [optional] 
 **offset** | **int**| The number of locations to skip. | [optional] 
 **limit** | **int**| The number of locations to return. | [optional] 

### Return type

[**ShippingLocationsResponse**](ShippingLocationsResponse.md)

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

# **get_companies_company_id_terminal_models**
> TerminalModelsResponse get_companies_company_id_terminal_models(company_id)

Get a list of terminal models

Returns a list of payment terminal models that the company identified in the path has access to. The response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a list of products for ordering.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.

    try:
        # Get a list of terminal models
        api_response = api_instance.get_companies_company_id_terminal_models(company_id)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_models: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.

    try:
        # Get a list of terminal models
        api_response = api_instance.get_companies_company_id_terminal_models(company_id)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 

### Return type

[**TerminalModelsResponse**](TerminalModelsResponse.md)

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

# **get_companies_company_id_terminal_orders**
> TerminalOrdersResponse get_companies_company_id_terminal_orders(company_id, customer_order_reference=customer_order_reference, status=status, offset=offset, limit=limit)

Get a list of orders

Returns a lists of terminal products orders for the company identified in the path. To filter the list, use one or more of the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    customer_order_reference = 'customer_order_reference_example' # str | Your purchase order number. (optional)
    status = 'status_example' # str | The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. (optional)
    offset = 56 # int | The number of orders to skip. (optional)
    limit = 56 # int | The number of orders to return. (optional)

    try:
        # Get a list of orders
        api_response = api_instance.get_companies_company_id_terminal_orders(company_id, customer_order_reference=customer_order_reference, status=status, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    customer_order_reference = 'customer_order_reference_example' # str | Your purchase order number. (optional)
    status = 'status_example' # str | The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. (optional)
    offset = 56 # int | The number of orders to skip. (optional)
    limit = 56 # int | The number of orders to return. (optional)

    try:
        # Get a list of orders
        api_response = api_instance.get_companies_company_id_terminal_orders(company_id, customer_order_reference=customer_order_reference, status=status, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **customer_order_reference** | **str**| Your purchase order number. | [optional] 
 **status** | **str**| The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. | [optional] 
 **offset** | **int**| The number of orders to skip. | [optional] 
 **limit** | **int**| The number of orders to return. | [optional] 

### Return type

[**TerminalOrdersResponse**](TerminalOrdersResponse.md)

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

# **get_companies_company_id_terminal_orders_order_id**
> TerminalOrder get_companies_company_id_terminal_orders_order_id(company_id, order_id)

Get an order

Returns the details of the terminal products order identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.

    try:
        # Get an order
        api_response = api_instance.get_companies_company_id_terminal_orders_order_id(company_id, order_id)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders_order_id: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.

    try:
        # Get an order
        api_response = api_instance.get_companies_company_id_terminal_orders_order_id(company_id, order_id)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_orders_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **order_id** | **str**| The unique identifier of the order. | 

### Return type

[**TerminalOrder**](TerminalOrder.md)

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

# **get_companies_company_id_terminal_products**
> TerminalProductsResponse get_companies_company_id_terminal_products(company_id, country=country, terminal_model_id=terminal_model_id, offset=offset, limit=limit)

Get a list of terminal products

Returns a list of payment terminal packages and parts that the company identified in the path has access to.  To filter the list, use one or more of the query parameters. The `country` query parameter is required.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    country = 'country_example' # str | The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** (optional)
    terminal_model_id = 'terminal_model_id_example' # str | The terminal model to return products for. Use the ID returned in the [GET `/terminalModels`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminalModels) response. For example, **Verifone.M400** (optional)
    offset = 56 # int | The number of products to skip. (optional)
    limit = 56 # int | The number of products to return. (optional)

    try:
        # Get a list of terminal products
        api_response = api_instance.get_companies_company_id_terminal_products(company_id, country=country, terminal_model_id=terminal_model_id, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_products: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    country = 'country_example' # str | The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** (optional)
    terminal_model_id = 'terminal_model_id_example' # str | The terminal model to return products for. Use the ID returned in the [GET `/terminalModels`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminalModels) response. For example, **Verifone.M400** (optional)
    offset = 56 # int | The number of products to skip. (optional)
    limit = 56 # int | The number of products to return. (optional)

    try:
        # Get a list of terminal products
        api_response = api_instance.get_companies_company_id_terminal_products(company_id, country=country, terminal_model_id=terminal_model_id, offset=offset, limit=limit)
        print("The response of TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->get_companies_company_id_terminal_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **country** | **str**| The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** | [optional] 
 **terminal_model_id** | **str**| The terminal model to return products for. Use the ID returned in the [GET &#x60;/terminalModels&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminalModels) response. For example, **Verifone.M400** | [optional] 
 **offset** | **int**| The number of products to skip. | [optional] 
 **limit** | **int**| The number of products to return. | [optional] 

### Return type

[**TerminalProductsResponse**](TerminalProductsResponse.md)

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

# **patch_companies_company_id_terminal_orders_order_id**
> TerminalOrder patch_companies_company_id_terminal_orders_order_id(company_id, order_id, terminal_order_request=terminal_order_request)

Update an order

Updates the terminal products order identified in the path. Updating is only possible while the order has the status **Placed**.  The request body only needs to contain what you want to change.  However, to update the products in the `items` array, you must provide the entire array. For example, if the array has three items:  To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.
    terminal_order_request = openapi_client.TerminalOrderRequest() # TerminalOrderRequest |  (optional)

    try:
        # Update an order
        api_response = api_instance.patch_companies_company_id_terminal_orders_order_id(company_id, order_id, terminal_order_request=terminal_order_request)
        print("The response of TerminalOrdersCompanyLevelApi->patch_companies_company_id_terminal_orders_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->patch_companies_company_id_terminal_orders_order_id: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.
    terminal_order_request = openapi_client.TerminalOrderRequest() # TerminalOrderRequest |  (optional)

    try:
        # Update an order
        api_response = api_instance.patch_companies_company_id_terminal_orders_order_id(company_id, order_id, terminal_order_request=terminal_order_request)
        print("The response of TerminalOrdersCompanyLevelApi->patch_companies_company_id_terminal_orders_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->patch_companies_company_id_terminal_orders_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **order_id** | **str**| The unique identifier of the order. | 
 **terminal_order_request** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] 

### Return type

[**TerminalOrder**](TerminalOrder.md)

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

# **post_companies_company_id_shipping_locations**
> ShippingLocation post_companies_company_id_shipping_locations(company_id, shipping_location=shipping_location)

Create a shipping location

Creates a shipping location for the company identified in the path. A shipping location defines an address where orders can be delivered.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    shipping_location = openapi_client.ShippingLocation() # ShippingLocation |  (optional)

    try:
        # Create a shipping location
        api_response = api_instance.post_companies_company_id_shipping_locations(company_id, shipping_location=shipping_location)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_shipping_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_shipping_locations: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    shipping_location = openapi_client.ShippingLocation() # ShippingLocation |  (optional)

    try:
        # Create a shipping location
        api_response = api_instance.post_companies_company_id_shipping_locations(company_id, shipping_location=shipping_location)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_shipping_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_shipping_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **shipping_location** | [**ShippingLocation**](ShippingLocation.md)|  | [optional] 

### Return type

[**ShippingLocation**](ShippingLocation.md)

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

# **post_companies_company_id_terminal_orders**
> TerminalOrder post_companies_company_id_terminal_orders(company_id, terminal_order_request=terminal_order_request)

Create an order

Creates an order for payment terminal products for the company identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    terminal_order_request = openapi_client.TerminalOrderRequest() # TerminalOrderRequest |  (optional)

    try:
        # Create an order
        api_response = api_instance.post_companies_company_id_terminal_orders(company_id, terminal_order_request=terminal_order_request)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    terminal_order_request = openapi_client.TerminalOrderRequest() # TerminalOrderRequest |  (optional)

    try:
        # Create an order
        api_response = api_instance.post_companies_company_id_terminal_orders(company_id, terminal_order_request=terminal_order_request)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **terminal_order_request** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] 

### Return type

[**TerminalOrder**](TerminalOrder.md)

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

# **post_companies_company_id_terminal_orders_order_id_cancel**
> TerminalOrder post_companies_company_id_terminal_orders_order_id_cancel(company_id, order_id)

Cancel an order

Cancels the terminal products order identified in the path. Cancelling is only possible while the order has the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.

    try:
        # Cancel an order
        api_response = api_instance.post_companies_company_id_terminal_orders_order_id_cancel(company_id, order_id)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders_order_id_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders_order_id_cancel: %s\n" % e)
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
    api_instance = openapi_client.TerminalOrdersCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    order_id = 'order_id_example' # str | The unique identifier of the order.

    try:
        # Cancel an order
        api_response = api_instance.post_companies_company_id_terminal_orders_order_id_cancel(company_id, order_id)
        print("The response of TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders_order_id_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalOrdersCompanyLevelApi->post_companies_company_id_terminal_orders_order_id_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **order_id** | **str**| The unique identifier of the order. | 

### Return type

[**TerminalOrder**](TerminalOrder.md)

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

