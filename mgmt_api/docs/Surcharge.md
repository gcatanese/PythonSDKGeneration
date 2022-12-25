# Surcharge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_confirmation** | **bool** | Show the surcharge details on the terminal, so the shopper can confirm. | [optional] 
**configurations** | [**List[Configuration]**](Configuration.md) | Surcharge fees or percentages for specific payment methods, funding sources (credit or debit), and currencies. | [optional] 

## Example

```python
from openapi_client.models.surcharge import Surcharge

# TODO update the JSON string below
json = "{}"
# create an instance of Surcharge from a JSON string
surcharge_instance = Surcharge.from_json(json)
# print the JSON string representation of the object
print Surcharge.to_json()

# convert the object into a dict
surcharge_dict = surcharge_instance.to_dict()
# create an instance of Surcharge from a dict
surcharge_form_dict = surcharge.from_dict(surcharge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


