# Connectivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simcard_status** | **str** | Indicates the status of the SIM card in the payment terminal. Can be updated and received only at terminal level, and only for models that support cellular connectivity.  Possible values: * **ACTIVATED**: the SIM card is activated. Cellular connectivity may still need to be enabled on the terminal itself, in the **Network** settings. * **INVENTORY**: the SIM card is not activated. The terminal can&#39;t use cellular connectivity. | [optional] 

## Example

```python
from openapi_client.models.connectivity import Connectivity

# TODO update the JSON string below
json = "{}"
# create an instance of Connectivity from a JSON string
connectivity_instance = Connectivity.from_json(json)
# print the JSON string representation of the object
print Connectivity.to_json()

# convert the object into a dict
connectivity_dict = connectivity_instance.to_dict()
# create an instance of Connectivity from a dict
connectivity_form_dict = connectivity.from_dict(connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


