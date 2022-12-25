# BcmcInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_bcmc_mobile** | **bool** | Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled. | [optional] 

## Example

```python
from openapi_client.models.bcmc_info import BcmcInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BcmcInfo from a JSON string
bcmc_info_instance = BcmcInfo.from_json(json)
# print the JSON string representation of the object
print BcmcInfo.to_json()

# convert the object into a dict
bcmc_info_dict = bcmc_info_instance.to_dict()
# create an instance of BcmcInfo from a dict
bcmc_info_form_dict = bcmc_info.from_dict(bcmc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


