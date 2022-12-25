# Opi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_pay_at_table** | **bool** | Indicates if Pay at Table is enabled. | [optional] 
**pay_at_table_store_number** | **str** | The store number to use for Pay at Table. | [optional] 
**pay_at_table_url** | **str** | The URL and port number used for Pay at Table communication. | [optional] 

## Example

```python
from openapi_client.models.opi import Opi

# TODO update the JSON string below
json = "{}"
# create an instance of Opi from a JSON string
opi_instance = Opi.from_json(json)
# print the JSON string representation of the object
print Opi.to_json()

# convert the object into a dict
opi_dict = opi_instance.to_dict()
# create an instance of Opi from a dict
opi_form_dict = opi.from_dict(opi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


