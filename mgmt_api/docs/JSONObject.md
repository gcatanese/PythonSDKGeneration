# JSONObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | [**List[JSONPath]**](JSONPath.md) |  | [optional] 
**root_path** | [**JSONPath**](JSONPath.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_object import JSONObject

# TODO update the JSON string below
json = "{}"
# create an instance of JSONObject from a JSON string
json_object_instance = JSONObject.from_json(json)
# print the JSON string representation of the object
print JSONObject.to_json()

# convert the object into a dict
json_object_dict = json_object_instance.to_dict()
# create an instance of JSONObject from a dict
json_object_form_dict = json_object.from_dict(json_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


