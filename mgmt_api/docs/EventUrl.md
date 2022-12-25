# EventUrl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_local_urls** | [**List[Url]**](Url.md) | One or more local URLs to send event notifications to when using Terminal API. | [optional] 
**event_public_urls** | [**List[Url]**](Url.md) | One or more public URLs to send event notifications to when using Terminal API. | [optional] 

## Example

```python
from openapi_client.models.event_url import EventUrl

# TODO update the JSON string below
json = "{}"
# create an instance of EventUrl from a JSON string
event_url_instance = EventUrl.from_json(json)
# print the JSON string representation of the object
print EventUrl.to_json()

# convert the object into a dict
event_url_dict = event_url_instance.to_dict()
# create an instance of EventUrl from a dict
event_url_form_dict = event_url.from_dict(event_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


