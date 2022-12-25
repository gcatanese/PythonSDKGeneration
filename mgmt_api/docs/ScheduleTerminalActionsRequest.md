# ScheduleTerminalActionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_details** | [**ScheduleTerminalActionsRequestActionDetails**](ScheduleTerminalActionsRequestActionDetails.md) |  | [optional] 
**scheduled_at** | **str** | The date and time when the action should happen.  Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+01:00**  The action is sent with the first [maintenance call](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api#when-actions-take-effect) after the specified date and time in the time zone of the terminal.  An empty value causes the action to be sent as soon as possible: at the next maintenance call. | [optional] 
**store_id** | **str** | The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the &#x60;terminalIds&#x60; list must be assigned to this store. | [optional] 
**terminal_ids** | **List[str]** | A list of unique IDs of the terminals to apply the action to. You can extract the IDs from the [GET &#x60;/terminals&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminals) response. Maximum length: 100 IDs. | [optional] 

## Example

```python
from openapi_client.models.schedule_terminal_actions_request import ScheduleTerminalActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTerminalActionsRequest from a JSON string
schedule_terminal_actions_request_instance = ScheduleTerminalActionsRequest.from_json(json)
# print the JSON string representation of the object
print ScheduleTerminalActionsRequest.to_json()

# convert the object into a dict
schedule_terminal_actions_request_dict = schedule_terminal_actions_request_instance.to_dict()
# create an instance of ScheduleTerminalActionsRequest from a dict
schedule_terminal_actions_request_form_dict = schedule_terminal_actions_request.from_dict(schedule_terminal_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


