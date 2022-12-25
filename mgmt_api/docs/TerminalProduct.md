# TerminalProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Information about items included and integration options. | [optional] 
**id** | **str** | The unique identifier of the product. | [optional] 
**items_included** | **List[str]** | A list of parts included in the terminal package. | [optional] 
**name** | **str** | The descriptive name of the product. | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 

## Example

```python
from openapi_client.models.terminal_product import TerminalProduct

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalProduct from a JSON string
terminal_product_instance = TerminalProduct.from_json(json)
# print the JSON string representation of the object
print TerminalProduct.to_json()

# convert the object into a dict
terminal_product_dict = terminal_product_instance.to_dict()
# create an instance of TerminalProduct from a dict
terminal_product_form_dict = terminal_product.from_dict(terminal_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


