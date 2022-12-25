# openapi_client.WebhooksCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_companies_company_id_webhooks_webhook_id**](WebhooksCompanyLevelApi.md#delete_companies_company_id_webhooks_webhook_id) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook
[**get_companies_company_id_webhooks**](WebhooksCompanyLevelApi.md#get_companies_company_id_webhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks
[**get_companies_company_id_webhooks_webhook_id**](WebhooksCompanyLevelApi.md#get_companies_company_id_webhooks_webhook_id) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook
[**patch_companies_company_id_webhooks_webhook_id**](WebhooksCompanyLevelApi.md#patch_companies_company_id_webhooks_webhook_id) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook
[**post_companies_company_id_webhooks**](WebhooksCompanyLevelApi.md#post_companies_company_id_webhooks) | **POST** /companies/{companyId}/webhooks | Set up a webhook
[**post_companies_company_id_webhooks_webhook_id_generate_hmac**](WebhooksCompanyLevelApi.md#post_companies_company_id_webhooks_webhook_id_generate_hmac) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**post_companies_company_id_webhooks_webhook_id_test**](WebhooksCompanyLevelApi.md#post_companies_company_id_webhooks_webhook_id_test) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook


# **delete_companies_company_id_webhooks_webhook_id**
> delete_companies_company_id_webhooks_webhook_id(company_id, webhook_id)

Remove a webhook

Remove the configuration for the webhook identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Remove a webhook
        api_instance.delete_companies_company_id_webhooks_webhook_id(company_id, webhook_id)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->delete_companies_company_id_webhooks_webhook_id: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Remove a webhook
        api_instance.delete_companies_company_id_webhooks_webhook_id(company_id, webhook_id)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->delete_companies_company_id_webhooks_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **webhook_id** | **str**| Unique identifier of the webhook configuration. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_companies_company_id_webhooks**
> ListWebhooksResponse get_companies_company_id_webhooks(company_id, page_number=page_number, page_size=page_size)

List all webhooks

Lists all webhook configurations for the company account.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)

    try:
        # List all webhooks
        api_response = api_instance.get_companies_company_id_webhooks(company_id, page_number=page_number, page_size=page_size)
        print("The response of WebhooksCompanyLevelApi->get_companies_company_id_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->get_companies_company_id_webhooks: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    page_number = 56 # int | The number of the page to fetch. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)

    try:
        # List all webhooks
        api_response = api_instance.get_companies_company_id_webhooks(company_id, page_number=page_number, page_size=page_size)
        print("The response of WebhooksCompanyLevelApi->get_companies_company_id_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->get_companies_company_id_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **page_number** | **int**| The number of the page to fetch. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

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

# **get_companies_company_id_webhooks_webhook_id**
> Webhook get_companies_company_id_webhooks_webhook_id(company_id, webhook_id)

Get a webhook

Returns the configuration for the webhook identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Get a webhook
        api_response = api_instance.get_companies_company_id_webhooks_webhook_id(company_id, webhook_id)
        print("The response of WebhooksCompanyLevelApi->get_companies_company_id_webhooks_webhook_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->get_companies_company_id_webhooks_webhook_id: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Get a webhook
        api_response = api_instance.get_companies_company_id_webhooks_webhook_id(company_id, webhook_id)
        print("The response of WebhooksCompanyLevelApi->get_companies_company_id_webhooks_webhook_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->get_companies_company_id_webhooks_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **webhook_id** | **str**| Unique identifier of the webhook configuration. | 

### Return type

[**Webhook**](Webhook.md)

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

# **patch_companies_company_id_webhooks_webhook_id**
> Webhook patch_companies_company_id_webhooks_webhook_id(company_id, webhook_id, update_company_webhook_request=update_company_webhook_request)

Update a webhook

Make changes to the configuration of the webhook identified in the path. The request contains the new values you want to have in the webhook configuration. The response contains the full configuration for the webhook, which includes the new values from the request.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.
    update_company_webhook_request = openapi_client.UpdateCompanyWebhookRequest() # UpdateCompanyWebhookRequest |  (optional)

    try:
        # Update a webhook
        api_response = api_instance.patch_companies_company_id_webhooks_webhook_id(company_id, webhook_id, update_company_webhook_request=update_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->patch_companies_company_id_webhooks_webhook_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->patch_companies_company_id_webhooks_webhook_id: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.
    update_company_webhook_request = openapi_client.UpdateCompanyWebhookRequest() # UpdateCompanyWebhookRequest |  (optional)

    try:
        # Update a webhook
        api_response = api_instance.patch_companies_company_id_webhooks_webhook_id(company_id, webhook_id, update_company_webhook_request=update_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->patch_companies_company_id_webhooks_webhook_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->patch_companies_company_id_webhooks_webhook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **webhook_id** | **str**| Unique identifier of the webhook configuration. | 
 **update_company_webhook_request** | [**UpdateCompanyWebhookRequest**](UpdateCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

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

# **post_companies_company_id_webhooks**
> Webhook post_companies_company_id_webhooks(company_id, create_company_webhook_request=create_company_webhook_request)

Set up a webhook

Subscribe to receive webhook notifications about events related to your company account. You can add basic authentication to make sure the data is secure.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    create_company_webhook_request = openapi_client.CreateCompanyWebhookRequest() # CreateCompanyWebhookRequest |  (optional)

    try:
        # Set up a webhook
        api_response = api_instance.post_companies_company_id_webhooks(company_id, create_company_webhook_request=create_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    create_company_webhook_request = openapi_client.CreateCompanyWebhookRequest() # CreateCompanyWebhookRequest |  (optional)

    try:
        # Set up a webhook
        api_response = api_instance.post_companies_company_id_webhooks(company_id, create_company_webhook_request=create_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). | 
 **create_company_webhook_request** | [**CreateCompanyWebhookRequest**](CreateCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

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

# **post_companies_company_id_webhooks_webhook_id_generate_hmac**
> GenerateHmacKeyResponse post_companies_company_id_webhooks_webhook_id_generate_hmac(company_id, webhook_id)

Generate an HMAC key

Returns an [HMAC key](https://en.wikipedia.org/wiki/HMAC) for the webhook identified in the path. This key allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you start receiving [HMAC-signed notifications](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures) from Adyen. Find out more about how to [verify HMAC signatures](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Generate an HMAC key
        api_response = api_instance.post_companies_company_id_webhooks_webhook_id_generate_hmac(company_id, webhook_id)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_generate_hmac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_generate_hmac: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.

    try:
        # Generate an HMAC key
        api_response = api_instance.post_companies_company_id_webhooks_webhook_id_generate_hmac(company_id, webhook_id)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_generate_hmac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_generate_hmac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **webhook_id** | **str**| Unique identifier of the webhook configuration. | 

### Return type

[**GenerateHmacKeyResponse**](GenerateHmacKeyResponse.md)

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

# **post_companies_company_id_webhooks_webhook_id_test**
> TestWebhookResponse post_companies_company_id_webhooks_webhook_id_test(company_id, webhook_id, test_company_webhook_request=test_company_webhook_request)

Test a webhook

Sends sample notifications to test if the webhook is set up correctly.  We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the webhook is configured for more than 20 merchant accounts, use the `merchantIds` array to specify a subset of the merchant accounts for which to send test notifications.  We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.  The response describes the result of the test. The `status` field tells you if the test was successful or not. You can use the other response fields to troubleshoot unsuccessful tests.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.
    test_company_webhook_request = openapi_client.TestCompanyWebhookRequest() # TestCompanyWebhookRequest |  (optional)

    try:
        # Test a webhook
        api_response = api_instance.post_companies_company_id_webhooks_webhook_id_test(company_id, webhook_id, test_company_webhook_request=test_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_test: %s\n" % e)
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
    api_instance = openapi_client.WebhooksCompanyLevelApi(api_client)
    company_id = 'company_id_example' # str | The unique identifier of the company account.
    webhook_id = 'webhook_id_example' # str | Unique identifier of the webhook configuration.
    test_company_webhook_request = openapi_client.TestCompanyWebhookRequest() # TestCompanyWebhookRequest |  (optional)

    try:
        # Test a webhook
        api_response = api_instance.post_companies_company_id_webhooks_webhook_id_test(company_id, webhook_id, test_company_webhook_request=test_company_webhook_request)
        print("The response of WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksCompanyLevelApi->post_companies_company_id_webhooks_webhook_id_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The unique identifier of the company account. | 
 **webhook_id** | **str**| Unique identifier of the webhook configuration. | 
 **test_company_webhook_request** | [**TestCompanyWebhookRequest**](TestCompanyWebhookRequest.md)|  | [optional] 

### Return type

[**TestWebhookResponse**](TestWebhookResponse.md)

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

