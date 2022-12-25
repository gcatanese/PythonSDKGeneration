# AndroidApp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description that was provided when uploading the app. The description is not shown on the terminal. | [optional] 
**id** | **str** | The unique identifier of the app. | 
**label** | **str** | The app name that is shown on the terminal. | [optional] 
**package_name** | **str** | The package name of the app. | [optional] 
**status** | **str** | The status of the app. Possible values:  * &#x60;processing&#x60;: The app is being signed and converted to a format that the terminal can handle. * &#x60;error&#x60;: Something went wrong. Check that the app matches the [requirements](https://docs.adyen.com/point-of-sale/android-terminals/app-requirements). * &#x60;invalid&#x60;: There is something wrong with the APK file of the app. * &#x60;ready&#x60;: The app has been signed and converted. * &#x60;archived&#x60;: The app is no longer available. | 
**version_code** | **int** | The internal version number of the app. | [optional] 
**version_name** | **str** | The app version number that is shown on the terminal. | [optional] 

## Example

```python
from openapi_client.models.android_app import AndroidApp

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidApp from a JSON string
android_app_instance = AndroidApp.from_json(json)
# print the JSON string representation of the object
print AndroidApp.to_json()

# convert the object into a dict
android_app_dict = android_app_instance.to_dict()
# create an instance of AndroidApp from a dict
android_app_form_dict = android_app.from_dict(android_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


