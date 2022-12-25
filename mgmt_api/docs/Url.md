# Url


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password for authentication of the event notifications. | [optional] 
**url** | **str** | The URL in the format: http(s)://domain.com. | [optional] 
**username** | **str** | The username for authentication of the event notifications. | [optional] 

## Example

```python
from openapi_client.models.url import Url

# TODO update the JSON string below
json = "{}"
# create an instance of Url from a JSON string
url_instance = Url.from_json(json)
# print the JSON string representation of the object
print Url.to_json()

# convert the object into a dict
url_dict = url_instance.to_dict()
# create an instance of Url from a dict
url_form_dict = url.from_dict(url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


