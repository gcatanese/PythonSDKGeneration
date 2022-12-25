# TestOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Unique identifier of the merchant account that the notification is about. | [optional] 
**output** | **str** | The response your server returned for the test webhook.  Your server must respond with **[accepted]** for the test webhook to be successful (&#x60;data.status&#x60;: **success**). Find out more about [accepting notifications](https://docs.adyen.com/development-resources/webhooks#accept-notifications)  You can use the value of this field together with the [&#x60;responseCode&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-responseCode) value to troubleshoot unsuccessful test webhooks. | [optional] 
**request_sent** | **str** | The [body of the notification webhook](https://docs.adyen.com/development-resources/webhooks/understand-notifications#notification-structure) that was sent to your server. | [optional] 
**response_code** | **str** | The HTTP response code for your server&#39;s response to the test webhook.  You can use the value of this field together with the the [&#x60;output&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-output) field value to troubleshoot failed test webhooks. | [optional] 
**response_time** | **str** | The time between sending the test webhook and receiving the response from your server. You can use it as an indication of how long your server takes to process a webhook notification. Measured in milliseconds, for example **304 ms**. | [optional] 
**status** | **str** | The status of the test request. Possible values are: * **success**, if &#x60;data.output&#x60;: **[accepted]** and &#x60;data.responseCode&#x60;: **200**. * **failed**, in all other cases.  You can use the value of the [&#x60;output&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-output) field together with the [&#x60;responseCode&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-responseCode) value to troubleshoot failed test webhooks. | 

## Example

```python
from openapi_client.models.test_output import TestOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TestOutput from a JSON string
test_output_instance = TestOutput.from_json(json)
# print the JSON string representation of the object
print TestOutput.to_json()

# convert the object into a dict
test_output_dict = test_output_instance.to_dict()
# create an instance of TestOutput from a dict
test_output_form_dict = test_output.from_dict(test_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


