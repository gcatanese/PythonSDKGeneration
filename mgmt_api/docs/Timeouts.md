# Timeouts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_active_to_sleep** | **int** | Indicates the number of seconds of inactivity after which the terminal display goes into sleep mode. | [optional] 

## Example

```python
from openapi_client.models.timeouts import Timeouts

# TODO update the JSON string below
json = "{}"
# create an instance of Timeouts from a JSON string
timeouts_instance = Timeouts.from_json(json)
# print the JSON string representation of the object
print Timeouts.to_json()

# convert the object into a dict
timeouts_dict = timeouts_instance.to_dict()
# create an instance of Timeouts from a dict
timeouts_form_dict = timeouts.from_dict(timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


