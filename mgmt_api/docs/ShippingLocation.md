# ShippingLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**id** | **str** | The unique identifier of the shipping location, for use as &#x60;shippingLocationId&#x60; when creating an order. | [optional] 
**name** | **str** | The unique name of the shipping location. | [optional] 

## Example

```python
from openapi_client.models.shipping_location import ShippingLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLocation from a JSON string
shipping_location_instance = ShippingLocation.from_json(json)
# print the JSON string representation of the object
print ShippingLocation.to_json()

# convert the object into a dict
shipping_location_dict = shipping_location_instance.to_dict()
# create an instance of ShippingLocation from a dict
shipping_location_form_dict = shipping_location.from_dict(shipping_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


