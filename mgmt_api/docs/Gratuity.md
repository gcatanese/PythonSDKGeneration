# Gratuity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_custom_amount** | **bool** | Indicates whether one of the predefined tipping options is to let the shopper enter a custom tip. If **true**, only three of the other options defined in &#x60;predefinedTipEntries&#x60; are shown. | [optional] 
**currency** | **str** | The currency that the tipping settings apply to. | [optional] 
**predefined_tip_entries** | **List[str]** | Tipping options the shopper can choose from if &#x60;usePredefinedTipEntries&#x60; is **true**. The maximum number of predefined options is four, or three plus the option to enter a custom tip. The options can be a mix of:  - A percentage of the transaction amount. Example: **5%** - A tip amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). Example: **500** for a EUR 5 tip. | [optional] 
**use_predefined_tip_entries** | **bool** | Indicates whether the terminal shows a prompt to enter a tip (**false**), or predefined tipping options to choose from (**true**). | [optional] 

## Example

```python
from openapi_client.models.gratuity import Gratuity

# TODO update the JSON string below
json = "{}"
# create an instance of Gratuity from a JSON string
gratuity_instance = Gratuity.from_json(json)
# print the JSON string representation of the object
print Gratuity.to_json()

# convert the object into a dict
gratuity_dict = gratuity_instance.to_dict()
# create an instance of Gratuity from a dict
gratuity_form_dict = gratuity.from_dict(gratuity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


