# ListExternalTerminalActionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExternalTerminalAction]**](ExternalTerminalAction.md) | The list of terminal actions. | [optional] 

## Example

```python
from openapi_client.models.list_external_terminal_actions_response import ListExternalTerminalActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExternalTerminalActionsResponse from a JSON string
list_external_terminal_actions_response_instance = ListExternalTerminalActionsResponse.from_json(json)
# print the JSON string representation of the object
print ListExternalTerminalActionsResponse.to_json()

# convert the object into a dict
list_external_terminal_actions_response_dict = list_external_terminal_actions_response_instance.to_dict()
# create an instance of ListExternalTerminalActionsResponse from a dict
list_external_terminal_actions_response_form_dict = list_external_terminal_actions_response.from_dict(list_external_terminal_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


