# TerminalOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_entity** | [**BillingEntity**](BillingEntity.md) |  | [optional] 
**customer_order_reference** | **str** | The merchant-defined purchase order number. This will be printed on the packing list. | [optional] 
**id** | **str** | The unique identifier of the order. | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) | The products included in the order. | [optional] 
**order_date** | **str** | The date and time that the order was placed, in UTC ISO 8601 format. For example, \&quot;2011-12-03T10:15:30Z\&quot;. | [optional] 
**shipping_location** | [**ShippingLocation**](ShippingLocation.md) |  | [optional] 
**status** | **str** | The processing status of the order. | [optional] 
**tracking_url** | **str** | The URL, provided by the carrier company, where the shipment can be tracked. | [optional] 

## Example

```python
from openapi_client.models.terminal_order import TerminalOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalOrder from a JSON string
terminal_order_instance = TerminalOrder.from_json(json)
# print the JSON string representation of the object
print TerminalOrder.to_json()

# convert the object into a dict
terminal_order_dict = terminal_order_instance.to_dict()
# create an instance of TerminalOrder from a dict
terminal_order_form_dict = terminal_order.from_dict(terminal_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


