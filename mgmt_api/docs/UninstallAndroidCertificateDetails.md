# UninstallAndroidCertificateDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** | The unique identifier of the certificate to be uninstalled. | [optional] 
**type** | **str** | Type of terminal action: Uninstall an Android certificate. | [optional] [default to 'UninstallAndroidCertificate']

## Example

```python
from openapi_client.models.uninstall_android_certificate_details import UninstallAndroidCertificateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallAndroidCertificateDetails from a JSON string
uninstall_android_certificate_details_instance = UninstallAndroidCertificateDetails.from_json(json)
# print the JSON string representation of the object
print UninstallAndroidCertificateDetails.to_json()

# convert the object into a dict
uninstall_android_certificate_details_dict = uninstall_android_certificate_details_instance.to_dict()
# create an instance of UninstallAndroidCertificateDetails from a dict
uninstall_android_certificate_details_form_dict = uninstall_android_certificate_details.from_dict(uninstall_android_certificate_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


