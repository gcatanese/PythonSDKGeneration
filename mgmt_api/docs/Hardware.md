# Hardware


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_maximum_back_light** | **int** | The brightness of the display when the terminal is being used, expressed as a percentage. | [optional] 

## Example

```python
from openapi_client.models.hardware import Hardware

# TODO update the JSON string below
json = "{}"
# create an instance of Hardware from a JSON string
hardware_instance = Hardware.from_json(json)
# print the JSON string representation of the object
print Hardware.to_json()

# convert the object into a dict
hardware_dict = hardware_instance.to_dict()
# create an instance of Hardware from a dict
hardware_form_dict = hardware.from_dict(hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


