# ScheduleTerminalActionsRequestActionDetails

Information about the action to take.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The unique identifier of the app to be uninstalled. | [optional] 
**type** | **str** | Type of terminal action: Uninstall an Android certificate. | [optional] [default to 'UninstallAndroidCertificate']
**certificate_id** | **str** | The unique identifier of the certificate to be uninstalled. | [optional] 
**update_at_first_maintenance_call** | **bool** | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. | [optional] 

## Example

```python
from openapi_client.models.schedule_terminal_actions_request_action_details import ScheduleTerminalActionsRequestActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTerminalActionsRequestActionDetails from a JSON string
schedule_terminal_actions_request_action_details_instance = ScheduleTerminalActionsRequestActionDetails.from_json(json)
# print the JSON string representation of the object
print ScheduleTerminalActionsRequestActionDetails.to_json()

# convert the object into a dict
schedule_terminal_actions_request_action_details_dict = schedule_terminal_actions_request_action_details_instance.to_dict()
# create an instance of ScheduleTerminalActionsRequestActionDetails from a dict
schedule_terminal_actions_request_action_details_form_dict = schedule_terminal_actions_request_action_details.from_dict(schedule_terminal_actions_request_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


