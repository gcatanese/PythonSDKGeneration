# SofortInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Sofort currency code. For example, **EUR**. | 
**logo** | **str** | Sofort logo. Format: Base64-encoded string. | 

## Example

```python
from openapi_client.models.sofort_info import SofortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SofortInfo from a JSON string
sofort_info_instance = SofortInfo.from_json(json)
# print the JSON string representation of the object
print SofortInfo.to_json()

# convert the object into a dict
sofort_info_dict = sofort_info_instance.to_dict()
# create an instance of SofortInfo from a dict
sofort_info_form_dict = sofort_info.from_dict(sofort_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


