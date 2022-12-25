# TestCompanyWebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_ids** | **List[str]** | List of &#x60;merchantId&#x60; values for which test webhooks will be sent. The list can have a maximum of 20 &#x60;merchantId&#x60; values.  If not specified, we send sample notifications to all the merchant accounts that the webhook is configured for. If this is more than 20 merchant accounts, use this list to specify a subset of the merchant accounts for which to send test notifications. | [optional] 
**notification** | [**CustomNotification**](CustomNotification.md) |  | [optional] 
**types** | **List[str]** | List of event codes for which to send test notifications. Only the webhook types below are supported.   Possible values if webhook &#x60;type&#x60;: **standard**:  * **AUTHORISATION** * **CHARGEBACK_REVERSED** * **ORDER_CLOSED** * **ORDER_OPENED** * **PAIDOUT_REVERSED** * **PAYOUT_THIRDPARTY** * **REFUNDED_REVERSED** * **REFUND_WITH_DATA** * **REPORT_AVAILABLE** * **CUSTOM** - set your custom notification fields in the [&#x60;notification&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_notification) object.  Possible values if webhook &#x60;type&#x60;: **banktransfer-notification**:  * **PENDING**  Possible values if webhook &#x60;type&#x60;: **report-notification**:  * **REPORT_AVAILABLE**  Possible values if webhook &#x60;type&#x60;: **ideal-notification**:  * **AUTHORISATION**  Possible values if webhook &#x60;type&#x60;: **pending-notification**:  * **PENDING**  | [optional] 

## Example

```python
from openapi_client.models.test_company_webhook_request import TestCompanyWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestCompanyWebhookRequest from a JSON string
test_company_webhook_request_instance = TestCompanyWebhookRequest.from_json(json)
# print the JSON string representation of the object
print TestCompanyWebhookRequest.to_json()

# convert the object into a dict
test_company_webhook_request_dict = test_company_webhook_request_instance.to_dict()
# create an instance of TestCompanyWebhookRequest from a dict
test_company_webhook_request_form_dict = test_company_webhook_request.from_dict(test_company_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


