# UninstallAndroidAppDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The unique identifier of the app to be uninstalled. | [optional] 
**type** | **str** | Type of terminal action: Uninstall an Android app. | [optional] [default to 'UninstallAndroidApp']

## Example

```python
from openapi_client.models.uninstall_android_app_details import UninstallAndroidAppDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallAndroidAppDetails from a JSON string
uninstall_android_app_details_instance = UninstallAndroidAppDetails.from_json(json)
# print the JSON string representation of the object
print UninstallAndroidAppDetails.to_json()

# convert the object into a dict
uninstall_android_app_details_dict = uninstall_android_app_details_instance.to_dict()
# create an instance of UninstallAndroidAppDetails from a dict
uninstall_android_app_details_form_dict = uninstall_android_app_details.from_dict(uninstall_android_app_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


