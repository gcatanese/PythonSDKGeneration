# InvalidField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Description of the validation error. | 
**name** | **str** | The field that has an invalid value. | 
**value** | **str** | The invalid value. | 

## Example

```python
from openapi_client.models.invalid_field import InvalidField

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidField from a JSON string
invalid_field_instance = InvalidField.from_json(json)
# print the JSON string representation of the object
print InvalidField.to_json()

# convert the object into a dict
invalid_field_dict = invalid_field_instance.to_dict()
# create an instance of InvalidField from a dict
invalid_field_form_dict = invalid_field.from_dict(invalid_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


