# ListMerchantResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**data** | [**List[Merchant]**](Merchant.md) | The list of merchant accounts. | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 

## Example

```python
from openapi_client.models.list_merchant_response import ListMerchantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMerchantResponse from a JSON string
list_merchant_response_instance = ListMerchantResponse.from_json(json)
# print the JSON string representation of the object
print ListMerchantResponse.to_json()

# convert the object into a dict
list_merchant_response_dict = list_merchant_response_instance.to_dict()
# create an instance of ListMerchantResponse from a dict
list_merchant_response_form_dict = list_merchant_response.from_dict(list_merchant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


