# WifiProfiles


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[Profile]**](Profile.md) | List of remote Wi-Fi profiles | [optional] 
**settings** | [**Settings**](Settings.md) |  | [optional] 

## Example

```python
from openapi_client.models.wifi_profiles import WifiProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of WifiProfiles from a JSON string
wifi_profiles_instance = WifiProfiles.from_json(json)
# print the JSON string representation of the object
print WifiProfiles.to_json()

# convert the object into a dict
wifi_profiles_dict = wifi_profiles_instance.to_dict()
# create an instance of WifiProfiles from a dict
wifi_profiles_form_dict = wifi_profiles.from_dict(wifi_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


