# Contact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The individual&#39;s email address. | [optional] 
**first_name** | **str** | The individual&#39;s first name. | [optional] 
**infix** | **str** | The infix in the individual&#39;s name, if any. | [optional] 
**last_name** | **str** | The individual&#39;s last name. | [optional] 
**phone_number** | **str** | The individual&#39;s phone number, specified as 10-14 digits with an optional &#x60;+&#x60; prefix. | [optional] 

## Example

```python
from openapi_client.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_form_dict = contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


