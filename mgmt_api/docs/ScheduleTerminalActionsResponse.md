# ScheduleTerminalActionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_details** | [**ScheduleTerminalActionsRequestActionDetails**](ScheduleTerminalActionsRequestActionDetails.md) |  | [optional] 
**items** | [**List[TerminalActionScheduleDetail]**](TerminalActionScheduleDetail.md) | A list containing a terminal ID and an action ID for each terminal that the action was scheduled for. | [optional] 
**scheduled_at** | **str** | The date and time when the action should happen.  Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+01:00**  The action is sent with the first [maintenance call](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api#when-actions-take-effect) after the specified date and time in the time zone of the terminal.  An empty value causes the action to be sent as soon as possible: at the next maintenance call. | [optional] 
**store_id** | **str** | The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the &#x60;terminalIds&#x60; list must be assigned to this store. | [optional] 
**terminal_ids** | **List[str]** | A list of unique IDs of the terminals that the action applies to. | [optional] 
**terminals_with_errors** | **Dict[str, List[str]]** | The validation errors that occurred in the list of terminals, and for each error the IDs of the terminals that the error applies to. | [optional] 
**total_errors** | **int** | The number of terminals for which scheduling the action failed. | [optional] 
**total_scheduled** | **int** | The number of terminals for which the action was successfully scheduled. This doesn&#39;t mean the action has happened yet. | [optional] 

## Example

```python
from openapi_client.models.schedule_terminal_actions_response import ScheduleTerminalActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTerminalActionsResponse from a JSON string
schedule_terminal_actions_response_instance = ScheduleTerminalActionsResponse.from_json(json)
# print the JSON string representation of the object
print ScheduleTerminalActionsResponse.to_json()

# convert the object into a dict
schedule_terminal_actions_response_dict = schedule_terminal_actions_response_instance.to_dict()
# create an instance of ScheduleTerminalActionsResponse from a dict
schedule_terminal_actions_response_form_dict = schedule_terminal_actions_response.from_dict(schedule_terminal_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


