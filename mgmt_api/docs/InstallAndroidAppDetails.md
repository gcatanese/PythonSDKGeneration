# InstallAndroidAppDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The unique identifier of the app to be installed. | [optional] 
**type** | **str** | Type of terminal action: Install an Android app. | [optional] [default to 'InstallAndroidApp']

## Example

```python
from openapi_client.models.install_android_app_details import InstallAndroidAppDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InstallAndroidAppDetails from a JSON string
install_android_app_details_instance = InstallAndroidAppDetails.from_json(json)
# print the JSON string representation of the object
print InstallAndroidAppDetails.to_json()

# convert the object into a dict
install_android_app_details_dict = install_android_app_details_instance.to_dict()
# create an instance of InstallAndroidAppDetails from a dict
install_android_app_details_form_dict = install_android_app_details.from_dict(install_android_app_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


