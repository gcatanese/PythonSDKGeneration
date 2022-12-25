# ApplePayInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The list of merchant domains. Maximum: 99 domains per request.  For more information, see [Apple Pay documentation](https://docs.adyen.com/payment-methods/apple-pay/web-drop-in?tab&#x3D;adyen-certificate-live_1#going-live). | 

## Example

```python
from openapi_client.models.apple_pay_info import ApplePayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApplePayInfo from a JSON string
apple_pay_info_instance = ApplePayInfo.from_json(json)
# print the JSON string representation of the object
print ApplePayInfo.to_json()

# convert the object into a dict
apple_pay_info_dict = apple_pay_info_instance.to_dict()
# create an instance of ApplePayInfo from a dict
apple_pay_info_form_dict = apple_pay_info.from_dict(apple_pay_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


