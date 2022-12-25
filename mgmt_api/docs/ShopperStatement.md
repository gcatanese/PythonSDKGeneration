# ShopperStatement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doing_business_as_name** | **str** | The name you want to be shown on the shopper&#39;s bank or credit card statement. Maximum length: 22 characters; can&#39;t be all numbers. | 
**type** | **str** | The type of shopperstatement you want to use: fixed, append or dynamic | [optional] 

## Example

```python
from openapi_client.models.shopper_statement import ShopperStatement

# TODO update the JSON string below
json = "{}"
# create an instance of ShopperStatement from a JSON string
shopper_statement_instance = ShopperStatement.from_json(json)
# print the JSON string representation of the object
print ShopperStatement.to_json()

# convert the object into a dict
shopper_statement_dict = shopper_statement_instance.to_dict()
# create an instance of ShopperStatement from a dict
shopper_statement_form_dict = shopper_statement.from_dict(shopper_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


