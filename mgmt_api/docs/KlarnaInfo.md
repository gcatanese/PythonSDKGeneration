# KlarnaInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_capture** | **bool** | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). Default value: **false**. | [optional] 
**dispute_email** | **str** | The email address for disputes. | 
**region** | **str** | The region of operation. For example, **NA**, **EU**, **CH**, **AU**. | 
**support_email** | **str** | The email address of merchant support. | 

## Example

```python
from openapi_client.models.klarna_info import KlarnaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KlarnaInfo from a JSON string
klarna_info_instance = KlarnaInfo.from_json(json)
# print the JSON string representation of the object
print KlarnaInfo.to_json()

# convert the object into a dict
klarna_info_dict = klarna_info_instance.to_dict()
# create an instance of KlarnaInfo from a dict
klarna_info_form_dict = klarna_info.from_dict(klarna_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


