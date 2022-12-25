# UpdatableAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The name of the city. | [optional] 
**line1** | **str** | The street address. | [optional] 
**line2** | **str** | Second address line. | [optional] 
**line3** | **str** | Third address line. | [optional] 
**postal_code** | **str** | The postal code. | [optional] 
**state_or_province** | **str** | The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Required for the following countries:  - Australia - Brazil - Canada - India - Mexico - New Zealand - United States | [optional] 

## Example

```python
from openapi_client.models.updatable_address import UpdatableAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatableAddress from a JSON string
updatable_address_instance = UpdatableAddress.from_json(json)
# print the JSON string representation of the object
print UpdatableAddress.to_json()

# convert the object into a dict
updatable_address_dict = updatable_address_instance.to_dict()
# create an instance of UpdatableAddress from a dict
updatable_address_form_dict = updatable_address.from_dict(updatable_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


