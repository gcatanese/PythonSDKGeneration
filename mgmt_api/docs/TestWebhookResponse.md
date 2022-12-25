# TestWebhookResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TestOutput]**](TestOutput.md) | List with test results. Each test webhook we send has a list element with the result. | [optional] 

## Example

```python
from openapi_client.models.test_webhook_response import TestWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestWebhookResponse from a JSON string
test_webhook_response_instance = TestWebhookResponse.from_json(json)
# print the JSON string representation of the object
print TestWebhookResponse.to_json()

# convert the object into a dict
test_webhook_response_dict = test_webhook_response_instance.to_dict()
# create an instance of TestWebhookResponse from a dict
test_webhook_response_form_dict = test_webhook_response.from_dict(test_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


