# ExternalTerminalAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The type of terminal action: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, or **UninstallAndroidCertificate**. | [optional] 
**config** | **str** | Technical information about the terminal action. | [optional] 
**confirmed_at** | **datetime** | The date and time when the action was carried out. | [optional] 
**id** | **str** | The unique ID of the terminal action. | [optional] 
**result** | **str** | The result message for the action. | [optional] 
**scheduled_at** | **datetime** | The date and time when the action was scheduled to happen. | [optional] 
**status** | **str** | The status of the terminal action: **pending**, **successful**, **failed**, **cancelled**, or **tryLater**. | [optional] 
**terminal_id** | **str** | The unique ID of the terminal that the action applies to. | [optional] 

## Example

```python
from openapi_client.models.external_terminal_action import ExternalTerminalAction

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTerminalAction from a JSON string
external_terminal_action_instance = ExternalTerminalAction.from_json(json)
# print the JSON string representation of the object
print ExternalTerminalAction.to_json()

# convert the object into a dict
external_terminal_action_dict = external_terminal_action_instance.to_dict()
# create an instance of ExternalTerminalAction from a dict
external_terminal_action_form_dict = external_terminal_action.from_dict(external_terminal_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


