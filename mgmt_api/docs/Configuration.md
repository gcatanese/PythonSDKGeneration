# Configuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | Payment method, like **eftpos_australia** or **mc**. See the [possible values](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).  | 
**currencies** | [**List[Currency]**](Currency.md) | Currency, and surcharge percentage or amount. | 
**sources** | **List[str]** | Funding source. Possible values: * **Credit** * **Debit** | [optional] 

## Example

```python
from openapi_client.models.configuration import Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of Configuration from a JSON string
configuration_instance = Configuration.from_json(json)
# print the JSON string representation of the object
print Configuration.to_json()

# convert the object into a dict
configuration_dict = configuration_instance.to_dict()
# create an instance of Configuration from a dict
configuration_form_dict = configuration.from_dict(configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


