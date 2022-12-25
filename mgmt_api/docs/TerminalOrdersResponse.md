# TerminalOrdersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TerminalOrder]**](TerminalOrder.md) | List of orders for payment terminal packages and parts. | [optional] 

## Example

```python
from openapi_client.models.terminal_orders_response import TerminalOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalOrdersResponse from a JSON string
terminal_orders_response_instance = TerminalOrdersResponse.from_json(json)
# print the JSON string representation of the object
print TerminalOrdersResponse.to_json()

# convert the object into a dict
terminal_orders_response_dict = terminal_orders_response_instance.to_dict()
# create an instance of TerminalOrdersResponse from a dict
terminal_orders_response_form_dict = terminal_orders_response.from_dict(terminal_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


