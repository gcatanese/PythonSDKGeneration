# JSONPath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.json_path import JSONPath

# TODO update the JSON string below
json = "{}"
# create an instance of JSONPath from a JSON string
json_path_instance = JSONPath.from_json(json)
# print the JSON string representation of the object
print JSONPath.to_json()

# convert the object into a dict
json_path_dict = json_path_instance.to_dict()
# create an instance of JSONPath from a dict
json_path_form_dict = json_path.from_dict(json_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


