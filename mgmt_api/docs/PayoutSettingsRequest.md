# PayoutSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if payouts to this bank account are enabled. Default: **true**.  To receive payouts into this bank account, both &#x60;enabled&#x60; and &#x60;allowed&#x60; must be **true**. | [optional] 
**enabled_from_date** | **str** | The date when Adyen starts paying out to this bank account.  Format: [ISO 8601](https://www.w3.org/TR/NOTE-datetime), for example, **2019-11-23T12:25:28Z** or **2020-05-27T20:25:28+08:00**.  If not specified, the &#x60;enabled&#x60; field indicates if payouts are enabled for this bank account.  If a date is specified and:  * &#x60;enabled&#x60;: **true**, payouts are enabled starting the specified date. * &#x60;enabled&#x60;: **false**, payouts are disabled until the specified date. On the specified date, &#x60;enabled&#x60; changes to **true** and this field is reset to **null**. | [optional] 
**transfer_instrument_id** | **str** | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the bank account. | 

## Example

```python
from openapi_client.models.payout_settings_request import PayoutSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSettingsRequest from a JSON string
payout_settings_request_instance = PayoutSettingsRequest.from_json(json)
# print the JSON string representation of the object
print PayoutSettingsRequest.to_json()

# convert the object into a dict
payout_settings_request_dict = payout_settings_request_instance.to_dict()
# create an instance of PayoutSettingsRequest from a dict
payout_settings_request_form_dict = payout_settings_request.from_dict(payout_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


