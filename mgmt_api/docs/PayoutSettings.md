# PayoutSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | Indicates if payouts to the bank account are allowed. This value is set automatically based on the status of the verification process. The value is:  * **true** if &#x60;verificationStatus&#x60; is **valid**. * **false** for all other values. | [optional] 
**enabled** | **bool** | Indicates if payouts to this bank account are enabled. Default: **true**.  To receive payouts into this bank account, both &#x60;enabled&#x60; and &#x60;allowed&#x60; must be **true**. | [optional] 
**enabled_from_date** | **str** | The date when Adyen starts paying out to this bank account.  Format: [ISO 8601](https://www.w3.org/TR/NOTE-datetime), for example, **2019-11-23T12:25:28Z** or **2020-05-27T20:25:28+08:00**.  If not specified, the &#x60;enabled&#x60; field indicates if payouts are enabled for this bank account.  If a date is specified and:  * &#x60;enabled&#x60;: **true**, payouts are enabled starting the specified date. * &#x60;enabled&#x60;: **false**, payouts are disabled until the specified date. On the specified date, &#x60;enabled&#x60; changes to **true** and this field is reset to **null**. | [optional] 
**id** | **str** | The unique identifier of the payout setting. | 
**priority** | **str** | Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the [payout frequency](https://docs.adyen.com/account/getting-paid#payout-frequency). Depending on the currencies and banks involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.   Possible values: * **first**: same day. * **urgent**: the next day. * **normal**: between 1 and 3 days. | [optional] 
**transfer_instrument_id** | **str** | The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the bank account. | 
**verification_status** | **str** | The status of the verification process for the bank account.  Possible values: * **valid**: the verification was successful. * **pending**: the verification is in progress. * **invalid**: the information provided is not complete. * **rejected**:  there are reasons to refuse working with this entity. | [optional] 

## Example

```python
from openapi_client.models.payout_settings import PayoutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutSettings from a JSON string
payout_settings_instance = PayoutSettings.from_json(json)
# print the JSON string representation of the object
print PayoutSettings.to_json()

# convert the object into a dict
payout_settings_dict = payout_settings_instance.to_dict()
# create an instance of PayoutSettings from a dict
payout_settings_form_dict = payout_settings.from_dict(payout_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


