# Address


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The name of the city. | [optional] 
**company_name** | **str** | The name of the company. | [optional] 
**country** | **str** | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. | [optional] 
**postal_code** | **str** | The postal code. | [optional] 
**state_or_province** | **str** | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.   Applicable for the following countries: - Australia - Brazil - Canada - India - Mexico - New Zealand - United States | [optional] 
**street_address** | **str** | The name of the street, and the house or building number. | [optional] 
**street_address2** | **str** | Additional address details, if any. | [optional] 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print Address.to_json()

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_form_dict = address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


