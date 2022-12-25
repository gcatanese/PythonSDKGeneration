# ReceiptPrinting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_approved** | **bool** | Print a merchant receipt when the payment is approved. | [optional] 
**merchant_cancelled** | **bool** | Print a merchant receipt when the transaction is cancelled. | [optional] 
**merchant_capture_approved** | **bool** | Print a merchant receipt when capturing the payment is approved. | [optional] 
**merchant_capture_refused** | **bool** | Print a merchant receipt when capturing the payment is refused. | [optional] 
**merchant_refund_approved** | **bool** | Print a merchant receipt when the refund is approved. | [optional] 
**merchant_refund_refused** | **bool** | Print a merchant receipt when the refund is refused. | [optional] 
**merchant_refused** | **bool** | Print a merchant receipt when the payment is refused. | [optional] 
**merchant_void** | **bool** | Print a merchant receipt when a previous transaction is voided. | [optional] 
**shopper_approved** | **bool** | Print a shopper receipt when the payment is approved. | [optional] 
**shopper_cancelled** | **bool** | Print a shopper receipt when the transaction is cancelled. | [optional] 
**shopper_capture_approved** | **bool** | Print a shopper receipt when capturing the payment is approved. | [optional] 
**shopper_capture_refused** | **bool** | Print a shopper receipt when capturing the payment is refused. | [optional] 
**shopper_refund_approved** | **bool** | Print a shopper receipt when the refund is approved. | [optional] 
**shopper_refund_refused** | **bool** | Print a shopper receipt when the refund is refused. | [optional] 
**shopper_refused** | **bool** | Print a shopper receipt when the payment is refused. | [optional] 
**shopper_void** | **bool** | Print a shopper receipt when a previous transaction is voided. | [optional] 

## Example

```python
from openapi_client.models.receipt_printing import ReceiptPrinting

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptPrinting from a JSON string
receipt_printing_instance = ReceiptPrinting.from_json(json)
# print the JSON string representation of the object
print ReceiptPrinting.to_json()

# convert the object into a dict
receipt_printing_dict = receipt_printing_instance.to_dict()
# create an instance of ReceiptPrinting from a dict
receipt_printing_form_dict = receipt_printing.from_dict(receipt_printing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


