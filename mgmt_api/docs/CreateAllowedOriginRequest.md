# CreateAllowedOriginRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | [optional] 
**domain** | **str** | Domain of the allowed origin. | 
**id** | **str** | Unique identifier of the allowed origin. | [optional] 

## Example

```python
from openapi_client.models.create_allowed_origin_request import CreateAllowedOriginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAllowedOriginRequest from a JSON string
create_allowed_origin_request_instance = CreateAllowedOriginRequest.from_json(json)
# print the JSON string representation of the object
print CreateAllowedOriginRequest.to_json()

# convert the object into a dict
create_allowed_origin_request_dict = create_allowed_origin_request_instance.to_dict()
# create an instance of CreateAllowedOriginRequest from a dict
create_allowed_origin_request_form_dict = create_allowed_origin_request.from_dict(create_allowed_origin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


