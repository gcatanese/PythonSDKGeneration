# UpdatePaymentMethodInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | The list of countries where a payment method is available. By default, all countries supported by the payment method. | [optional] 
**currencies** | **List[str]** | The list of currencies that a payment method supports. By default, all currencies supported by the payment method. | [optional] 
**enabled** | **bool** | Indicates whether the payment method is enabled (**true**) or disabled (**false**). | [optional] 
**shopper_statement** | [**ShopperStatement**](ShopperStatement.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_payment_method_info import UpdatePaymentMethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentMethodInfo from a JSON string
update_payment_method_info_instance = UpdatePaymentMethodInfo.from_json(json)
# print the JSON string representation of the object
print UpdatePaymentMethodInfo.to_json()

# convert the object into a dict
update_payment_method_info_dict = update_payment_method_info_instance.to_dict()
# create an instance of UpdatePaymentMethodInfo from a dict
update_payment_method_info_form_dict = update_payment_method_info.from_dict(update_payment_method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


