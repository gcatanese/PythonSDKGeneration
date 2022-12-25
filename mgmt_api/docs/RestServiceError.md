# RestServiceError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | 
**error_code** | **str** | A code that identifies the problem type. | 
**instance** | **str** | A unique URI that identifies the specific occurrence of the problem. | [optional] 
**invalid_fields** | [**List[InvalidField]**](InvalidField.md) | Detailed explanation of each validation error, when applicable. | [optional] 
**request_id** | **str** | A unique reference for the request, essentially the same as &#x60;pspReference&#x60;. | [optional] 
**response** | [**JSONObject**](JSONObject.md) |  | [optional] 
**status** | **int** | The HTTP status code. | 
**title** | **str** | A short, human-readable summary of the problem type. | 
**type** | **str** | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. | 

## Example

```python
from openapi_client.models.rest_service_error import RestServiceError

# TODO update the JSON string below
json = "{}"
# create an instance of RestServiceError from a JSON string
rest_service_error_instance = RestServiceError.from_json(json)
# print the JSON string representation of the object
print RestServiceError.to_json()

# convert the object into a dict
rest_service_error_dict = rest_service_error_instance.to_dict()
# create an instance of RestServiceError from a dict
rest_service_error_form_dict = rest_service_error.from_dict(rest_service_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


