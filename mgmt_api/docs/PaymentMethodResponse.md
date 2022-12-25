# PaymentMethodResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**data** | [**List[PaymentMethod]**](PaymentMethod.md) | Payment methods details. | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 
**types_with_errors** | **List[str]** | Payment method types with errors. | [optional] 

## Example

```python
from openapi_client.models.payment_method_response import PaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodResponse from a JSON string
payment_method_response_instance = PaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print PaymentMethodResponse.to_json()

# convert the object into a dict
payment_method_response_dict = payment_method_response_instance.to_dict()
# create an instance of PaymentMethodResponse from a dict
payment_method_response_form_dict = payment_method_response.from_dict(payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


