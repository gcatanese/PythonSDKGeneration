# AllowedOrigin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | [optional] 
**domain** | **str** | Domain of the allowed origin. | 
**id** | **str** | Unique identifier of the allowed origin. | [optional] 

## Example

```python
from openapi_client.models.allowed_origin import AllowedOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedOrigin from a JSON string
allowed_origin_instance = AllowedOrigin.from_json(json)
# print the JSON string representation of the object
print AllowedOrigin.to_json()

# convert the object into a dict
allowed_origin_dict = allowed_origin_instance.to_dict()
# create an instance of AllowedOrigin from a dict
allowed_origin_form_dict = allowed_origin.from_dict(allowed_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


