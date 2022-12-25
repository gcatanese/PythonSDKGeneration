# PaymentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your merchant account. | [optional] 
**apple_pay** | [**ApplePayInfo**](ApplePayInfo.md) |  | [optional] 
**bcmc** | [**BcmcInfo**](BcmcInfo.md) |  | [optional] 
**business_line_id** | **str** | The unique identifier of the business line. | [optional] 
**cartes_bancaires** | [**CartesBancairesInfo**](CartesBancairesInfo.md) |  | [optional] 
**countries** | **List[str]** | The list of countries where a payment method is available. By default, all countries supported by the payment method. | [optional] 
**currencies** | **List[str]** | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. | [optional] 
**enabled** | **bool** | Indicates whether the payment method is enabled (**true**) or disabled (**false**). | [optional] 
**giro_pay** | [**GiroPayInfo**](GiroPayInfo.md) |  | [optional] 
**google_pay** | [**GooglePayInfo**](GooglePayInfo.md) |  | [optional] 
**id** | **str** | The identifier of the resource. | 
**klarna** | [**KlarnaInfo**](KlarnaInfo.md) |  | [optional] 
**paypal** | [**PayPalInfo**](PayPalInfo.md) |  | [optional] 
**shopper_interaction** | **str** | The sales channel. | [optional] 
**sofort** | [**SofortInfo**](SofortInfo.md) |  | [optional] 
**store_id** | **str** | The ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/post/stores__resParam_id), if any. | [optional] 
**swish** | [**SwishInfo**](SwishInfo.md) |  | [optional] 
**type** | **str** | Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). | [optional] 
**verification_status** | **str** | Payment method status. Possible values: * **valid** * **pending** * **invalid** * **rejected** | [optional] 

## Example

```python
from openapi_client.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print PaymentMethod.to_json()

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_form_dict = payment_method.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


