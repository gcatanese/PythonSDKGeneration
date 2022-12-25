# PayPalInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_capture** | **bool** | Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the [capture](https://docs.adyen.com/online-payments/capture) settings of your merchant account. Default value: **true**. | [optional] 
**payer_id** | **str** | PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters. | 
**subject** | **str** | Your business email address. | 

## Example

```python
from openapi_client.models.pay_pal_info import PayPalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayPalInfo from a JSON string
pay_pal_info_instance = PayPalInfo.from_json(json)
# print the JSON string representation of the object
print PayPalInfo.to_json()

# convert the object into a dict
pay_pal_info_dict = pay_pal_info_instance.to_dict()
# create an instance of PayPalInfo from a dict
pay_pal_info_form_dict = pay_pal_info.from_dict(pay_pal_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


