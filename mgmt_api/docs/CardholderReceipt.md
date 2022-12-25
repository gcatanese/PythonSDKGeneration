# CardholderReceipt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_for_authorized_receipt** | **str** | A custom header to show on the shopper receipt for an authorised transaction. Allows one or two comma-separated header lines, and blank lines. For example, &#x60;header,header,filler&#x60; | [optional] 

## Example

```python
from openapi_client.models.cardholder_receipt import CardholderReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of CardholderReceipt from a JSON string
cardholder_receipt_instance = CardholderReceipt.from_json(json)
# print the JSON string representation of the object
print CardholderReceipt.to_json()

# convert the object into a dict
cardholder_receipt_dict = cardholder_receipt_instance.to_dict()
# create an instance of CardholderReceipt from a dict
cardholder_receipt_form_dict = cardholder_receipt.from_dict(cardholder_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


