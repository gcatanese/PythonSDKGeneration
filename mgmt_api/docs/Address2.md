# Address2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The name of the city. | [optional] 
**country** | **str** | The two-letter country code in [ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. | 
**line1** | **str** | The street address. | [optional] 
**line2** | **str** | Second address line. | [optional] 
**line3** | **str** | Third address line. | [optional] 
**postal_code** | **str** | The postal code. | [optional] 
**state_or_province** | **str** | The state or province code as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Required for the following countries:  - Australia - Brazil - Canada - India - Mexico - New Zealand - United States | [optional] 

## Example

```python
from openapi_client.models.address2 import Address2

# TODO update the JSON string below
json = "{}"
# create an instance of Address2 from a JSON string
address2_instance = Address2.from_json(json)
# print the JSON string representation of the object
print Address2.to_json()

# convert the object into a dict
address2_dict = address2_instance.to_dict()
# create an instance of Address2 from a dict
address2_form_dict = address2.from_dict(address2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


