# AllowedOriginsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AllowedOrigin]**](AllowedOrigin.md) | List of allowed origins. | [optional] 

## Example

```python
from openapi_client.models.allowed_origins_response import AllowedOriginsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedOriginsResponse from a JSON string
allowed_origins_response_instance = AllowedOriginsResponse.from_json(json)
# print the JSON string representation of the object
print AllowedOriginsResponse.to_json()

# convert the object into a dict
allowed_origins_response_dict = allowed_origins_response_instance.to_dict()
# create an instance of AllowedOriginsResponse from a dict
allowed_origins_response_form_dict = allowed_origins_response.from_dict(allowed_origins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


