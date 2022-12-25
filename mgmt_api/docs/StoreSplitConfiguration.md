# StoreSplitConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_account_id** | **str** | The [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id) linked to the account holder. | [optional] 
**split_configuration_id** | **str** | The UUID of the [split configuration](https://docs.adyen.com/marketplaces-and-platforms/classic/split-configuration-for-stores) from the Customer Area. | [optional] 

## Example

```python
from openapi_client.models.store_split_configuration import StoreSplitConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StoreSplitConfiguration from a JSON string
store_split_configuration_instance = StoreSplitConfiguration.from_json(json)
# print the JSON string representation of the object
print StoreSplitConfiguration.to_json()

# convert the object into a dict
store_split_configuration_dict = store_split_configuration_instance.to_dict()
# create an instance of StoreSplitConfiguration from a dict
store_split_configuration_form_dict = store_split_configuration.from_dict(store_split_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


