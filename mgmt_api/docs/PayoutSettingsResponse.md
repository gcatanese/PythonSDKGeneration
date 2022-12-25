# PayoutSettingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PayoutSettings]**](PayoutSettings.md) | The list of payout accounts. | [optional] 

## Example

```python
from openapi_client.models.payout_settings_response import PayoutSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSettingsResponse from a JSON string
payout_settings_response_instance = PayoutSettingsResponse.from_json(json)
# print the JSON string representation of the object
print PayoutSettingsResponse.to_json()

# convert the object into a dict
payout_settings_response_dict = payout_settings_response_instance.to_dict()
# create an instance of PayoutSettingsResponse from a dict
payout_settings_response_form_dict = payout_settings_response.from_dict(payout_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


