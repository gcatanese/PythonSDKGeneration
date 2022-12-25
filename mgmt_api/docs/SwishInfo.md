# SwishInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swish_number** | **str** | Swish number. Format: 10 digits without spaces. For example, **1231111111**. | 

## Example

```python
from openapi_client.models.swish_info import SwishInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SwishInfo from a JSON string
swish_info_instance = SwishInfo.from_json(json)
# print the JSON string representation of the object
print SwishInfo.to_json()

# convert the object into a dict
swish_info_dict = swish_info_instance.to_dict()
# create an instance of SwishInfo from a dict
swish_info_form_dict = swish_info.from_dict(swish_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


