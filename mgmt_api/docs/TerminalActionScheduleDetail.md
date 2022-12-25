# TerminalActionScheduleDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the action on the specified terminal. | [optional] 
**terminal_id** | **str** | The unique ID of the terminal that the action applies to. | [optional] 

## Example

```python
from openapi_client.models.terminal_action_schedule_detail import TerminalActionScheduleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalActionScheduleDetail from a JSON string
terminal_action_schedule_detail_instance = TerminalActionScheduleDetail.from_json(json)
# print the JSON string representation of the object
print TerminalActionScheduleDetail.to_json()

# convert the object into a dict
terminal_action_schedule_detail_dict = terminal_action_schedule_detail_instance.to_dict()
# create an instance of TerminalActionScheduleDetail from a dict
terminal_action_schedule_detail_form_dict = terminal_action_schedule_detail.from_dict(terminal_action_schedule_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


