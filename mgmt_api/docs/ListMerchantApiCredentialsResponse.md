# ListMerchantApiCredentialsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**data** | [**List[ApiCredential]**](ApiCredential.md) | The list of API credentials. | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 

## Example

```python
from openapi_client.models.list_merchant_api_credentials_response import ListMerchantApiCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMerchantApiCredentialsResponse from a JSON string
list_merchant_api_credentials_response_instance = ListMerchantApiCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print ListMerchantApiCredentialsResponse.to_json()

# convert the object into a dict
list_merchant_api_credentials_response_dict = list_merchant_api_credentials_response_instance.to_dict()
# create an instance of ListMerchantApiCredentialsResponse from a dict
list_merchant_api_credentials_response_form_dict = list_merchant_api_credentials_response.from_dict(list_merchant_api_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


