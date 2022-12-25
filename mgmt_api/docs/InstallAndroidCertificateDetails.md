# InstallAndroidCertificateDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** | The unique identifier of the certificate to be installed. | [optional] 
**type** | **str** | Type of terminal action: Install an Android certificate. | [optional] [default to 'InstallAndroidCertificate']

## Example

```python
from openapi_client.models.install_android_certificate_details import InstallAndroidCertificateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InstallAndroidCertificateDetails from a JSON string
install_android_certificate_details_instance = InstallAndroidCertificateDetails.from_json(json)
# print the JSON string representation of the object
print InstallAndroidCertificateDetails.to_json()

# convert the object into a dict
install_android_certificate_details_dict = install_android_certificate_details_instance.to_dict()
# create an instance of InstallAndroidCertificateDetails from a dict
install_android_certificate_details_form_dict = install_android_certificate_details.from_dict(install_android_certificate_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


