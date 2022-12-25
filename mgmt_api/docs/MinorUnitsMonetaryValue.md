# MinorUnitsMonetaryValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The transaction amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). | [optional] 
**currency_code** | **str** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). | [optional] 

## Example

```python
from openapi_client.models.minor_units_monetary_value import MinorUnitsMonetaryValue

# TODO update the JSON string below
json = "{}"
# create an instance of MinorUnitsMonetaryValue from a JSON string
minor_units_monetary_value_instance = MinorUnitsMonetaryValue.from_json(json)
# print the JSON string representation of the object
print MinorUnitsMonetaryValue.to_json()

# convert the object into a dict
minor_units_monetary_value_dict = minor_units_monetary_value_instance.to_dict()
# create an instance of MinorUnitsMonetaryValue from a dict
minor_units_monetary_value_form_dict = minor_units_monetary_value.from_dict(minor_units_monetary_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


