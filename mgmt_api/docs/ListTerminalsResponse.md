# ListTerminalsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Terminal]**](Terminal.md) | The list of terminals. | [optional] 

## Example

```python
from openapi_client.models.list_terminals_response import ListTerminalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTerminalsResponse from a JSON string
list_terminals_response_instance = ListTerminalsResponse.from_json(json)
# print the JSON string representation of the object
print ListTerminalsResponse.to_json()

# convert the object into a dict
list_terminals_response_dict = list_terminals_response_instance.to_dict()
# create an instance of ListTerminalsResponse from a dict
list_terminals_response_form_dict = list_terminals_response.from_dict(list_terminals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


