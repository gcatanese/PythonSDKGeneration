# Settings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**band** | **str** | The preferred Wi-Fi Band, for use if the terminals support multiple bands. Possible values: All, 2.4GHz, 5GHz. | [optional] 
**roaming** | **bool** | Indicates whether roaming is enabled on the terminals. | [optional] 
**timeout** | **int** | The connection time-out in seconds. Minimum value: 0 | [optional] 

## Example

```python
from openapi_client.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print Settings.to_json()

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_form_dict = settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


