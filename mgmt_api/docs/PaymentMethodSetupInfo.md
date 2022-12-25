# PaymentMethodSetupInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_pay** | [**ApplePayInfo**](ApplePayInfo.md) |  | [optional] 
**bcmc** | [**BcmcInfo**](BcmcInfo.md) |  | [optional] 
**business_line_id** | **str** | The unique identifier of the business line. | [optional] 
**cartes_bancaires** | [**CartesBancairesInfo**](CartesBancairesInfo.md) |  | [optional] 
**countries** | **List[str]** | The list of countries where a payment method is available. By default, all countries supported by the payment method. | [optional] 
**currencies** | **List[str]** | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. | [optional] 
**giro_pay** | [**GiroPayInfo**](GiroPayInfo.md) |  | [optional] 
**google_pay** | [**GooglePayInfo**](GooglePayInfo.md) |  | [optional] 
**klarna** | [**KlarnaInfo**](KlarnaInfo.md) |  | [optional] 
**paypal** | [**PayPalInfo**](PayPalInfo.md) |  | [optional] 
**shopper_interaction** | **str** | The sales channel. Required if the merchant account does not have a sales channel. When you provide this field, it overrides the default sales channel set on the merchant account.  Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**.  | [optional] 
**sofort** | [**SofortInfo**](SofortInfo.md) |  | [optional] 
**store_id** | **str** | The ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/post/stores__resParam_id), if any. | [optional] 
**swish** | [**SwishInfo**](SwishInfo.md) |  | [optional] 
**type** | **str** | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). | 

## Example

```python
from openapi_client.models.payment_method_setup_info import PaymentMethodSetupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSetupInfo from a JSON string
payment_method_setup_info_instance = PaymentMethodSetupInfo.from_json(json)
# print the JSON string representation of the object
print PaymentMethodSetupInfo.to_json()

# convert the object into a dict
payment_method_setup_info_dict = payment_method_setup_info_instance.to_dict()
# create an instance of PaymentMethodSetupInfo from a dict
payment_method_setup_info_form_dict = payment_method_setup_info.from_dict(payment_method_setup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


