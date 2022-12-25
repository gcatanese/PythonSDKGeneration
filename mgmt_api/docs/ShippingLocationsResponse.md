# ShippingLocationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ShippingLocation]**](ShippingLocation.md) | Physical locations where orders can be shipped to. | [optional] 

## Example

```python
from openapi_client.models.shipping_locations_response import ShippingLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLocationsResponse from a JSON string
shipping_locations_response_instance = ShippingLocationsResponse.from_json(json)
# print the JSON string representation of the object
print ShippingLocationsResponse.to_json()

# convert the object into a dict
shipping_locations_response_dict = shipping_locations_response_instance.to_dict()
# create an instance of ShippingLocationsResponse from a dict
shipping_locations_response_form_dict = shipping_locations_response.from_dict(shipping_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


