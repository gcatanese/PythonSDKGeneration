# openapi_client.PayoutSettingsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_merchants_merchant_id_payout_settings_payout_settings_id**](PayoutSettingsMerchantLevelApi.md#delete_merchants_merchant_id_payout_settings_payout_settings_id) | **DELETE** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Delete a payout setting
[**get_merchants_merchant_id_payout_settings**](PayoutSettingsMerchantLevelApi.md#get_merchants_merchant_id_payout_settings) | **GET** /merchants/{merchantId}/payoutSettings | Get a list of payout settings
[**get_merchants_merchant_id_payout_settings_payout_settings_id**](PayoutSettingsMerchantLevelApi.md#get_merchants_merchant_id_payout_settings_payout_settings_id) | **GET** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Get a payout setting
[**patch_merchants_merchant_id_payout_settings_payout_settings_id**](PayoutSettingsMerchantLevelApi.md#patch_merchants_merchant_id_payout_settings_payout_settings_id) | **PATCH** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Update a payout setting
[**post_merchants_merchant_id_payout_settings**](PayoutSettingsMerchantLevelApi.md#post_merchants_merchant_id_payout_settings) | **POST** /merchants/{merchantId}/payoutSettings | Add a payout setting


# **delete_merchants_merchant_id_payout_settings_payout_settings_id**
> object delete_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)

Delete a payout setting

Deletes the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.

    try:
        # Delete a payout setting
        api_response = api_instance.delete_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)
        print("The response of PayoutSettingsMerchantLevelApi->delete_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->delete_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.

    try:
        # Delete a payout setting
        api_response = api_instance.delete_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)
        print("The response of PayoutSettingsMerchantLevelApi->delete_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->delete_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payout_settings_id** | **str**| The unique identifier of the payout setting. | 

### Return type

**object**

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

# **get_merchants_merchant_id_payout_settings**
> PayoutSettingsResponse get_merchants_merchant_id_payout_settings(merchant_id)

Get a list of payout settings

Returns the list of payout settings for the merchant account identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.

    try:
        # Get a list of payout settings
        api_response = api_instance.get_merchants_merchant_id_payout_settings(merchant_id)
        print("The response of PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings: %s\n" % e)
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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.

    try:
        # Get a list of payout settings
        api_response = api_instance.get_merchants_merchant_id_payout_settings(merchant_id)
        print("The response of PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 

### Return type

[**PayoutSettingsResponse**](PayoutSettingsResponse.md)

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

# **get_merchants_merchant_id_payout_settings_payout_settings_id**
> PayoutSettings get_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)

Get a payout setting

Returns the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.

    try:
        # Get a payout setting
        api_response = api_instance.get_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)
        print("The response of PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.

    try:
        # Get a payout setting
        api_response = api_instance.get_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id)
        print("The response of PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->get_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payout_settings_id** | **str**| The unique identifier of the payout setting. | 

### Return type

[**PayoutSettings**](PayoutSettings.md)

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

# **patch_merchants_merchant_id_payout_settings_payout_settings_id**
> PayoutSettings patch_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id, update_payout_settings_request=update_payout_settings_request)

Update a payout setting

Updates the payout setting identified in the path. You can enable or disable the payout setting.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.
    update_payout_settings_request = openapi_client.UpdatePayoutSettingsRequest() # UpdatePayoutSettingsRequest |  (optional)

    try:
        # Update a payout setting
        api_response = api_instance.patch_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id, update_payout_settings_request=update_payout_settings_request)
        print("The response of PayoutSettingsMerchantLevelApi->patch_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->patch_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_id = 'payout_settings_id_example' # str | The unique identifier of the payout setting.
    update_payout_settings_request = openapi_client.UpdatePayoutSettingsRequest() # UpdatePayoutSettingsRequest |  (optional)

    try:
        # Update a payout setting
        api_response = api_instance.patch_merchants_merchant_id_payout_settings_payout_settings_id(merchant_id, payout_settings_id, update_payout_settings_request=update_payout_settings_request)
        print("The response of PayoutSettingsMerchantLevelApi->patch_merchants_merchant_id_payout_settings_payout_settings_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->patch_merchants_merchant_id_payout_settings_payout_settings_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payout_settings_id** | **str**| The unique identifier of the payout setting. | 
 **update_payout_settings_request** | [**UpdatePayoutSettingsRequest**](UpdatePayoutSettingsRequest.md)|  | [optional] 

### Return type

[**PayoutSettings**](PayoutSettings.md)

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

# **post_merchants_merchant_id_payout_settings**
> PayoutSettings post_merchants_merchant_id_payout_settings(merchant_id, payout_settings_request=payout_settings_request)

Add a payout setting

Sends a request to add a payout setting for the merchant account specified in the path. A payout setting links the merchant account to the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.  If you're accepting payments in multiple currencies, you may add multiple payout settings for the merchant account.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_request = openapi_client.PayoutSettingsRequest() # PayoutSettingsRequest |  (optional)

    try:
        # Add a payout setting
        api_response = api_instance.post_merchants_merchant_id_payout_settings(merchant_id, payout_settings_request=payout_settings_request)
        print("The response of PayoutSettingsMerchantLevelApi->post_merchants_merchant_id_payout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->post_merchants_merchant_id_payout_settings: %s\n" % e)
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
    api_instance = openapi_client.PayoutSettingsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payout_settings_request = openapi_client.PayoutSettingsRequest() # PayoutSettingsRequest |  (optional)

    try:
        # Add a payout setting
        api_response = api_instance.post_merchants_merchant_id_payout_settings(merchant_id, payout_settings_request=payout_settings_request)
        print("The response of PayoutSettingsMerchantLevelApi->post_merchants_merchant_id_payout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutSettingsMerchantLevelApi->post_merchants_merchant_id_payout_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payout_settings_request** | [**PayoutSettingsRequest**](PayoutSettingsRequest.md)|  | [optional] 

### Return type

[**PayoutSettings**](PayoutSettings.md)

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

