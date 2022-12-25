# ReceiptOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** | The receipt logo converted to a Base64-encoded string. The image must be a .bmp file of &lt; 256 KB, dimensions 240 (H) x 384 (W) px. | [optional] 
**qr_code_data** | **str** | Data to print on the receipt as a QR code. This can include static text and the following variables:  - &#x60;${merchantreference}&#x60;: the merchant reference of the transaction. - &#x60;${pspreference}&#x60;: the PSP reference of the transaction.   For example, **http://www.example.com/order/${pspreference}/${merchantreference}**. | [optional] 

## Example

```python
from openapi_client.models.receipt_options import ReceiptOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptOptions from a JSON string
receipt_options_instance = ReceiptOptions.from_json(json)
# print the JSON string representation of the object
print ReceiptOptions.to_json()

# convert the object into a dict
receipt_options_dict = receipt_options_instance.to_dict()
# create an instance of ReceiptOptions from a dict
receipt_options_form_dict = receipt_options.from_dict(receipt_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


