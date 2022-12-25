# UpdatePayoutSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if payouts to this bank account are enabled. Default: **true**.  To receive payouts into this bank account, both &#x60;enabled&#x60; and &#x60;allowed&#x60; must be **true**. | [optional] 

## Example

```python
from openapi_client.models.update_payout_settings_request import UpdatePayoutSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePayoutSettingsRequest from a JSON string
update_payout_settings_request_instance = UpdatePayoutSettingsRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePayoutSettingsRequest.to_json()

# convert the object into a dict
update_payout_settings_request_dict = update_payout_settings_request_instance.to_dict()
# create an instance of UpdatePayoutSettingsRequest from a dict
update_payout_settings_request_form_dict = update_payout_settings_request.from_dict(update_payout_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


