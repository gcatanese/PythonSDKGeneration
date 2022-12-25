# DataCenter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_prefix** | **str** | The unique [live URL prefix](https://docs.adyen.com/development-resources/live-endpoints#live-url-prefix) for your live endpoint. Each data center has its own live URL prefix.  This field is empty for requests made in the test environment. | [optional] 
**name** | **str** | The name assigned to a data center, for example **EU** for the European data center. Possible values are:  * **default**: the European data center. This value is always returned in the test environment.  * **AU** * **EU** * **US** | [optional] 

## Example

```python
from openapi_client.models.data_center import DataCenter

# TODO update the JSON string below
json = "{}"
# create an instance of DataCenter from a JSON string
data_center_instance = DataCenter.from_json(json)
# print the JSON string representation of the object
print DataCenter.to_json()

# convert the object into a dict
data_center_dict = data_center_instance.to_dict()
# create an instance of DataCenter from a dict
data_center_form_dict = data_center.from_dict(data_center_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


