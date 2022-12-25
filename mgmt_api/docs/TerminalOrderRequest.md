# TerminalOrderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_entity_id** | **str** | The identification of the billing entity to use for the order. | [optional] 
**customer_order_reference** | **str** | The merchant-defined purchase order reference. | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) | The products included in the order. | [optional] 
**shipping_location_id** | **str** | The identification of the shipping location to use for the order. | [optional] 
**tax_id** | **str** | The tax number of the billing entity. | [optional] 

## Example

```python
from openapi_client.models.terminal_order_request import TerminalOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalOrderRequest from a JSON string
terminal_order_request_instance = TerminalOrderRequest.from_json(json)
# print the JSON string representation of the object
print TerminalOrderRequest.to_json()

# convert the object into a dict
terminal_order_request_dict = terminal_order_request_instance.to_dict()
# create an instance of TerminalOrderRequest from a dict
terminal_order_request_form_dict = terminal_order_request.from_dict(terminal_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


