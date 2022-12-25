# AdditionalSettingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_event_codes** | **List[str]** | Object containing list of event codes for which the notifcation will not be sent.  | [optional] 
**include_event_codes** | **List[str]** | Object containing list of event codes for which the notifcation will be sent.  | [optional] 
**properties** | **Dict[str, bool]** | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled. For example, &#x60;captureDelayHours&#x60;: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. | [optional] 

## Example

```python
from openapi_client.models.additional_settings_response import AdditionalSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalSettingsResponse from a JSON string
additional_settings_response_instance = AdditionalSettingsResponse.from_json(json)
# print the JSON string representation of the object
print AdditionalSettingsResponse.to_json()

# convert the object into a dict
additional_settings_response_dict = additional_settings_response_instance.to_dict()
# create an instance of AdditionalSettingsResponse from a dict
additional_settings_response_form_dict = additional_settings_response.from_dict(additional_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


