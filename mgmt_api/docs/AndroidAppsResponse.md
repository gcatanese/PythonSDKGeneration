# AndroidAppsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AndroidApp]**](AndroidApp.md) | Apps uploaded for Android payment terminals. | [optional] 

## Example

```python
from openapi_client.models.android_apps_response import AndroidAppsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidAppsResponse from a JSON string
android_apps_response_instance = AndroidAppsResponse.from_json(json)
# print the JSON string representation of the object
print AndroidAppsResponse.to_json()

# convert the object into a dict
android_apps_response_dict = android_apps_response_instance.to_dict()
# create an instance of AndroidAppsResponse from a dict
android_apps_response_form_dict = android_apps_response.from_dict(android_apps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


