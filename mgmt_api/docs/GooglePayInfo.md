# GooglePayInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | GooglePay Merchant ID. Character length and limitations: 16 alphanumeric characters or 20 numeric characters. | 

## Example

```python
from openapi_client.models.google_pay_info import GooglePayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePayInfo from a JSON string
google_pay_info_instance = GooglePayInfo.from_json(json)
# print the JSON string representation of the object
print GooglePayInfo.to_json()

# convert the object into a dict
google_pay_info_dict = google_pay_info_instance.to_dict()
# create an instance of GooglePayInfo from a dict
google_pay_info_form_dict = google_pay_info.from_dict(google_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


