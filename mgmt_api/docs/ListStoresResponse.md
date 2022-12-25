# ListStoresResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**data** | [**List[Store]**](Store.md) | List of stores | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 

## Example

```python
from openapi_client.models.list_stores_response import ListStoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListStoresResponse from a JSON string
list_stores_response_instance = ListStoresResponse.from_json(json)
# print the JSON string representation of the object
print ListStoresResponse.to_json()

# convert the object into a dict
list_stores_response_dict = list_stores_response_instance.to_dict()
# create an instance of ListStoresResponse from a dict
list_stores_response_form_dict = list_stores_response.from_dict(list_stores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


