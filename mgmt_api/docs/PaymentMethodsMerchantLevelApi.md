# openapi_client.PaymentMethodsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchants_merchant_id_payment_method_settings**](PaymentMethodsMerchantLevelApi.md#get_merchants_merchant_id_payment_method_settings) | **GET** /merchants/{merchantId}/paymentMethodSettings | Get all payment methods
[**get_merchants_merchant_id_payment_method_settings_payment_method_id**](PaymentMethodsMerchantLevelApi.md#get_merchants_merchant_id_payment_method_settings_payment_method_id) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Get payment method details
[**get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains**](PaymentMethodsMerchantLevelApi.md#get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | Get Apple Pay domains
[**patch_merchants_merchant_id_payment_method_settings_payment_method_id**](PaymentMethodsMerchantLevelApi.md#patch_merchants_merchant_id_payment_method_settings_payment_method_id) | **PATCH** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Update a payment method
[**post_merchants_merchant_id_payment_method_settings**](PaymentMethodsMerchantLevelApi.md#post_merchants_merchant_id_payment_method_settings) | **POST** /merchants/{merchantId}/paymentMethodSettings | Request a payment method
[**post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains**](PaymentMethodsMerchantLevelApi.md#post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains) | **POST** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | Add an Apple Pay domain


# **get_merchants_merchant_id_payment_method_settings**
> PaymentMethodResponse get_merchants_merchant_id_payment_method_settings(merchant_id, store_id=store_id, business_line_id=business_line_id, page_size=page_size, page_number=page_number)

Get all payment methods

Returns details for all payment methods of the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store for which to return the payment methods. (optional)
    business_line_id = 'business_line_id_example' # str | The unique identifier of the Business Line for which to return the payment methods. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    page_number = 56 # int | The number of the page to fetch. (optional)

    try:
        # Get all payment methods
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings(merchant_id, store_id=store_id, business_line_id=business_line_id, page_size=page_size, page_number=page_number)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    store_id = 'store_id_example' # str | The unique identifier of the store for which to return the payment methods. (optional)
    business_line_id = 'business_line_id_example' # str | The unique identifier of the Business Line for which to return the payment methods. (optional)
    page_size = 56 # int | The number of items to have on a page, maximum 100. The default is 10 items on a page. (optional)
    page_number = 56 # int | The number of the page to fetch. (optional)

    try:
        # Get all payment methods
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings(merchant_id, store_id=store_id, business_line_id=business_line_id, page_size=page_size, page_number=page_number)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **store_id** | **str**| The unique identifier of the store for which to return the payment methods. | [optional] 
 **business_line_id** | **str**| The unique identifier of the Business Line for which to return the payment methods. | [optional] 
 **page_size** | **int**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] 
 **page_number** | **int**| The number of the page to fetch. | [optional] 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

# **get_merchants_merchant_id_payment_method_settings_payment_method_id**
> PaymentMethod get_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id)

Get payment method details

Returns details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.

    try:
        # Get payment method details
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.

    try:
        # Get payment method details
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payment_method_id** | **str**| The unique identifier of the payment method. | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

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

# **get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains**
> ApplePayInfo get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(merchant_id, payment_method_id)

Get Apple Pay domains

Returns all Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.

    try:
        # Get Apple Pay domains
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(merchant_id, payment_method_id)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.

    try:
        # Get Apple Pay domains
        api_response = api_instance.get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(merchant_id, payment_method_id)
        print("The response of PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payment_method_id** | **str**| The unique identifier of the payment method. | 

### Return type

[**ApplePayInfo**](ApplePayInfo.md)

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

# **patch_merchants_merchant_id_payment_method_settings_payment_method_id**
> PaymentMethod patch_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id, update_payment_method_info=update_payment_method_info)

Update a payment method

Updates payment method details for the merchant account and the payment method identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.
    update_payment_method_info = openapi_client.UpdatePaymentMethodInfo() # UpdatePaymentMethodInfo |  (optional)

    try:
        # Update a payment method
        api_response = api_instance.patch_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id, update_payment_method_info=update_payment_method_info)
        print("The response of PaymentMethodsMerchantLevelApi->patch_merchants_merchant_id_payment_method_settings_payment_method_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->patch_merchants_merchant_id_payment_method_settings_payment_method_id: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.
    update_payment_method_info = openapi_client.UpdatePaymentMethodInfo() # UpdatePaymentMethodInfo |  (optional)

    try:
        # Update a payment method
        api_response = api_instance.patch_merchants_merchant_id_payment_method_settings_payment_method_id(merchant_id, payment_method_id, update_payment_method_info=update_payment_method_info)
        print("The response of PaymentMethodsMerchantLevelApi->patch_merchants_merchant_id_payment_method_settings_payment_method_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->patch_merchants_merchant_id_payment_method_settings_payment_method_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payment_method_id** | **str**| The unique identifier of the payment method. | 
 **update_payment_method_info** | [**UpdatePaymentMethodInfo**](UpdatePaymentMethodInfo.md)|  | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

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

# **post_merchants_merchant_id_payment_method_settings**
> PaymentMethod post_merchants_merchant_id_payment_method_settings(merchant_id, payment_method_setup_info=payment_method_setup_info)

Request a payment method

Sends a request to add a new payment method to the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_setup_info = openapi_client.PaymentMethodSetupInfo() # PaymentMethodSetupInfo |  (optional)

    try:
        # Request a payment method
        api_response = api_instance.post_merchants_merchant_id_payment_method_settings(merchant_id, payment_method_setup_info=payment_method_setup_info)
        print("The response of PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_setup_info = openapi_client.PaymentMethodSetupInfo() # PaymentMethodSetupInfo |  (optional)

    try:
        # Request a payment method
        api_response = api_instance.post_merchants_merchant_id_payment_method_settings(merchant_id, payment_method_setup_info=payment_method_setup_info)
        print("The response of PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payment_method_setup_info** | [**PaymentMethodSetupInfo**](PaymentMethodSetupInfo.md)|  | [optional] 

### Return type

[**PaymentMethod**](PaymentMethod.md)

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

# **post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains**
> object post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(merchant_id, payment_method_id, apple_pay_info=apple_pay_info)

Add an Apple Pay domain

Adds the new domain to the list of Apple Pay domains that are registered with the merchant account and the payment method identified in the path. For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/enable-apple-pay#register-merchant-domain).  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payment methods read and write 

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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.
    apple_pay_info = openapi_client.ApplePayInfo() # ApplePayInfo |  (optional)

    try:
        # Add an Apple Pay domain
        api_response = api_instance.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(merchant_id, payment_method_id, apple_pay_info=apple_pay_info)
        print("The response of PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains: %s\n" % e)
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
    api_instance = openapi_client.PaymentMethodsMerchantLevelApi(api_client)
    merchant_id = 'merchant_id_example' # str | The unique identifier of the merchant account.
    payment_method_id = 'payment_method_id_example' # str | The unique identifier of the payment method.
    apple_pay_info = openapi_client.ApplePayInfo() # ApplePayInfo |  (optional)

    try:
        # Add an Apple Pay domain
        api_response = api_instance.post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(merchant_id, payment_method_id, apple_pay_info=apple_pay_info)
        print("The response of PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsMerchantLevelApi->post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The unique identifier of the merchant account. | 
 **payment_method_id** | **str**| The unique identifier of the payment method. | 
 **apple_pay_info** | [**ApplePayInfo**](ApplePayInfo.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - the request has succeeded. |  -  |
**202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
**204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
**400** | Bad Request - a problem reading or understanding the request. |  -  |
**401** | Unauthorized - authentication required. |  -  |
**403** | Forbidden - insufficient permissions to process the request. |  -  |
**422** | Unprocessable Entity - a request validation error. |  -  |
**500** | Internal Server Error - the server could not process the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

