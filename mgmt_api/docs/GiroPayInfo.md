# GiroPayInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support_email** | **str** | The email address of merchant support. | 

## Example

```python
from openapi_client.models.giro_pay_info import GiroPayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GiroPayInfo from a JSON string
giro_pay_info_instance = GiroPayInfo.from_json(json)
# print the JSON string representation of the object
print GiroPayInfo.to_json()

# convert the object into a dict
giro_pay_info_dict = giro_pay_info_instance.to_dict()
# create an instance of GiroPayInfo from a dict
giro_pay_info_form_dict = giro_pay_info.from_dict(giro_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


