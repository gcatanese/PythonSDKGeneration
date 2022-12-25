# AndroidCertificate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description that was provided when uploading the certificate. | [optional] 
**extension** | **str** | The file format of the certificate, as indicated by the file extension. For example, **.cert** or **.pem**. | [optional] 
**id** | **str** | The unique identifier of the certificate. | 
**name** | **str** | The file name of the certificate. For example, **mycert**. | [optional] 
**not_after** | **datetime** | The date when the certificate stops to be valid. | [optional] 
**not_before** | **datetime** | The date when the certificate starts to be valid. | [optional] 
**status** | **str** | The status of the certificate. | [optional] 

## Example

```python
from openapi_client.models.android_certificate import AndroidCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidCertificate from a JSON string
android_certificate_instance = AndroidCertificate.from_json(json)
# print the JSON string representation of the object
print AndroidCertificate.to_json()

# convert the object into a dict
android_certificate_dict = android_certificate_instance.to_dict()
# create an instance of AndroidCertificate from a dict
android_certificate_form_dict = android_certificate.from_dict(android_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


