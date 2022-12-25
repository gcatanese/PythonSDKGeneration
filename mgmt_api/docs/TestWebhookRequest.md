# TestWebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification** | [**CustomNotification**](CustomNotification.md) |  | [optional] 
**types** | **List[str]** | List of event codes for which to send test notifications. Only the webhook types below are supported.   Possible values if webhook &#x60;type&#x60;: **standard**:  * **AUTHORISATION** * **CHARGEBACK_REVERSED** * **ORDER_CLOSED** * **ORDER_OPENED** * **PAIDOUT_REVERSED** * **PAYOUT_THIRDPARTY** * **REFUNDED_REVERSED** * **REFUND_WITH_DATA** * **REPORT_AVAILABLE** * **CUSTOM** - set your custom notification fields in the [&#x60;notification&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_notification) object.  Possible values if webhook &#x60;type&#x60;: **banktransfer-notification**:  * **PENDING**  Possible values if webhook &#x60;type&#x60;: **report-notification**:  * **REPORT_AVAILABLE**  Possible values if webhook &#x60;type&#x60;: **ideal-notification**:  * **AUTHORISATION**  Possible values if webhook &#x60;type&#x60;: **pending-notification**:  * **PENDING**  | [optional] 

## Example

```python
from openapi_client.models.test_webhook_request import TestWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestWebhookRequest from a JSON string
test_webhook_request_instance = TestWebhookRequest.from_json(json)
# print the JSON string representation of the object
print TestWebhookRequest.to_json()

# convert the object into a dict
test_webhook_request_dict = test_webhook_request_instance.to_dict()
# create an instance of TestWebhookRequest from a dict
test_webhook_request_form_dict = test_webhook_request.from_dict(test_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


