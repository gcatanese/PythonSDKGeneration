# ListWebhooksResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**account_reference** | **str** | Reference to the account. | [optional] 
**data** | [**List[Webhook]**](Webhook.md) | The list of webhooks configured for this account. | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 

## Example

```python
from openapi_client.models.list_webhooks_response import ListWebhooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhooksResponse from a JSON string
list_webhooks_response_instance = ListWebhooksResponse.from_json(json)
# print the JSON string representation of the object
print ListWebhooksResponse.to_json()

# convert the object into a dict
list_webhooks_response_dict = list_webhooks_response_instance.to_dict()
# create an instance of ListWebhooksResponse from a dict
list_webhooks_response_form_dict = list_webhooks_response.from_dict(list_webhooks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


