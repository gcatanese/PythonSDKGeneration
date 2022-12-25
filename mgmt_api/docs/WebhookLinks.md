# WebhookLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**LinksElement**](LinksElement.md) |  | [optional] 
**generate_hmac** | [**LinksElement**](LinksElement.md) |  | 
**merchant** | [**LinksElement**](LinksElement.md) |  | [optional] 
**var_self** | [**LinksElement**](LinksElement.md) |  | 
**test_webhook** | [**LinksElement**](LinksElement.md) |  | 

## Example

```python
from openapi_client.models.webhook_links import WebhookLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLinks from a JSON string
webhook_links_instance = WebhookLinks.from_json(json)
# print the JSON string representation of the object
print WebhookLinks.to_json()

# convert the object into a dict
webhook_links_dict = webhook_links_instance.to_dict()
# create an instance of WebhookLinks from a dict
webhook_links_form_dict = webhook_links.from_dict(webhook_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


