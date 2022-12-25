# AdditionalSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_event_codes** | **List[str]** | Object containing list of event codes for which the notifcation will be sent.  | [optional] 
**properties** | **Dict[str, bool]** | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled. For example, &#x60;captureDelayHours&#x60;: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. | [optional] 

## Example

```python
from openapi_client.models.additional_settings import AdditionalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalSettings from a JSON string
additional_settings_instance = AdditionalSettings.from_json(json)
# print the JSON string representation of the object
print AdditionalSettings.to_json()

# convert the object into a dict
additional_settings_dict = additional_settings_instance.to_dict()
# create an instance of AdditionalSettings from a dict
additional_settings_form_dict = additional_settings.from_dict(additional_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


