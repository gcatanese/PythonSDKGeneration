# TerminalModelsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IdName]**](IdName.md) | The terminal models that the API credential has access to. | [optional] 

## Example

```python
from openapi_client.models.terminal_models_response import TerminalModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalModelsResponse from a JSON string
terminal_models_response_instance = TerminalModelsResponse.from_json(json)
# print the JSON string representation of the object
print TerminalModelsResponse.to_json()

# convert the object into a dict
terminal_models_response_dict = terminal_models_response_instance.to_dict()
# create an instance of TerminalModelsResponse from a dict
terminal_models_response_form_dict = terminal_models_response.from_dict(terminal_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


