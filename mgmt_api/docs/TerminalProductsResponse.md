# TerminalProductsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TerminalProduct]**](TerminalProduct.md) | Terminal products that can be ordered. | [optional] 

## Example

```python
from openapi_client.models.terminal_products_response import TerminalProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalProductsResponse from a JSON string
terminal_products_response_instance = TerminalProductsResponse.from_json(json)
# print the JSON string representation of the object
print TerminalProductsResponse.to_json()

# convert the object into a dict
terminal_products_response_dict = terminal_products_response_instance.to_dict()
# create an instance of TerminalProductsResponse from a dict
terminal_products_response_form_dict = terminal_products_response.from_dict(terminal_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


