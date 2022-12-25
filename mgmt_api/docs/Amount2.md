# Amount2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). | 
**value** | **int** | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). | 

## Example

```python
from openapi_client.models.amount2 import Amount2

# TODO update the JSON string below
json = "{}"
# create an instance of Amount2 from a JSON string
amount2_instance = Amount2.from_json(json)
# print the JSON string representation of the object
print Amount2.to_json()

# convert the object into a dict
amount2_dict = amount2_instance.to_dict()
# create an instance of Amount2 from a dict
amount2_form_dict = amount2.from_dict(amount2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


