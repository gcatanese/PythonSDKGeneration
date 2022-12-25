# OfflineProcessing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chip_floor_limit** | **int** | The maximum offline transaction amount for chip cards, in the processing currency and specified in [minor units](https://docs.adyen.com/development-resources/currency-codes). | [optional] 
**offline_swipe_limits** | [**List[MinorUnitsMonetaryValue]**](MinorUnitsMonetaryValue.md) | The maximum offline transaction amount for swiped cards, in the specified currency. | [optional] 

## Example

```python
from openapi_client.models.offline_processing import OfflineProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineProcessing from a JSON string
offline_processing_instance = OfflineProcessing.from_json(json)
# print the JSON string representation of the object
print OfflineProcessing.to_json()

# convert the object into a dict
offline_processing_dict = offline_processing_instance.to_dict()
# create an instance of OfflineProcessing from a dict
offline_processing_form_dict = offline_processing.from_dict(offline_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


