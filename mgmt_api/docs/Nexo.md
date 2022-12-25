# Nexo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_urls** | [**EventUrl**](EventUrl.md) |  | [optional] 
**nexo_event_urls** | **List[str]** | @deprecated One or more URLs to send event messages to when using Terminal API. | [optional] 

## Example

```python
from openapi_client.models.nexo import Nexo

# TODO update the JSON string below
json = "{}"
# create an instance of Nexo from a JSON string
nexo_instance = Nexo.from_json(json)
# print the JSON string representation of the object
print Nexo.to_json()

# convert the object into a dict
nexo_dict = nexo_instance.to_dict()
# create an instance of Nexo from a dict
nexo_form_dict = nexo.from_dict(nexo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


