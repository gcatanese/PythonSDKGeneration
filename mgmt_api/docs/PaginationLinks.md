# PaginationLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**LinksElement**](LinksElement.md) |  | 
**last** | [**LinksElement**](LinksElement.md) |  | 
**next** | [**LinksElement**](LinksElement.md) |  | [optional] 
**prev** | [**LinksElement**](LinksElement.md) |  | [optional] 
**var_self** | [**LinksElement**](LinksElement.md) |  | 

## Example

```python
from openapi_client.models.pagination_links import PaginationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinks from a JSON string
pagination_links_instance = PaginationLinks.from_json(json)
# print the JSON string representation of the object
print PaginationLinks.to_json()

# convert the object into a dict
pagination_links_dict = pagination_links_instance.to_dict()
# create an instance of PaginationLinks from a dict
pagination_links_form_dict = pagination_links.from_dict(pagination_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


