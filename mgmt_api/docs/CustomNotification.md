# CustomNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount2**](Amount2.md) |  | [optional] 
**event_code** | **str** | The event that caused the notification to be sent.Currently supported values: * **AUTHORISATION** * **CANCELLATION** * **REFUND** * **CAPTURE** * **DEACTIVATE_RECURRING** * **REPORT_AVAILABLE** * **CHARGEBACK** * **REQUEST_FOR_INFORMATION** * **NOTIFICATION_OF_CHARGEBACK** * **NOTIFICATIONTEST** * **ORDER_OPENED** * **ORDER_CLOSED** * **CHARGEBACK_REVERSED** * **REFUNDED_REVERSED** * **REFUND_WITH_DATA** | [optional] 
**event_date** | **datetime** | The time of the event. Format: [ISO 8601](http://www.w3.org/TR/NOTE-datetime), YYYY-MM-DDThh:mm:ssTZD. | [optional] 
**merchant_reference** | **str** | Your reference for the custom test notification. | [optional] 
**payment_method** | **str** | The payment method for the payment that the notification is about. Possible values: * **amex** * **visa** * **mc** * **maestro** * **bcmc** * **paypal**  * **sms**  * **bankTransfer_NL** * **bankTransfer_DE** * **bankTransfer_BE** * **ideal** * **elv** * **sepadirectdebit**  | [optional] 
**reason** | **str** | A descripton of what caused the notification. | [optional] 
**success** | **bool** | The outcome of the event which the notification is about. Set to either **true** or **false**.  | [optional] 

## Example

```python
from openapi_client.models.custom_notification import CustomNotification

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotification from a JSON string
custom_notification_instance = CustomNotification.from_json(json)
# print the JSON string representation of the object
print CustomNotification.to_json()

# convert the object into a dict
custom_notification_dict = custom_notification_instance.to_dict()
# create an instance of CustomNotification from a dict
custom_notification_form_dict = custom_notification.from_dict(custom_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


