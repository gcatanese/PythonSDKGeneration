# AndroidCertificatesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AndroidCertificate]**](AndroidCertificate.md) | Uploaded Android certificates for Android payment terminals. | [optional] 

## Example

```python
from openapi_client.models.android_certificates_response import AndroidCertificatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidCertificatesResponse from a JSON string
android_certificates_response_instance = AndroidCertificatesResponse.from_json(json)
# print the JSON string representation of the object
print AndroidCertificatesResponse.to_json()

# convert the object into a dict
android_certificates_response_dict = android_certificates_response_instance.to_dict()
# create an instance of AndroidCertificatesResponse from a dict
android_certificates_response_form_dict = android_certificates_response.from_dict(android_certificates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


