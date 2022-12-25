# ListCompanyUsersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**data** | [**List[CompanyUser]**](CompanyUser.md) | The list of users. | [optional] 
**items_total** | **int** | Total number of items. | 
**pages_total** | **int** | Total number of pages. | 

## Example

```python
from openapi_client.models.list_company_users_response import ListCompanyUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompanyUsersResponse from a JSON string
list_company_users_response_instance = ListCompanyUsersResponse.from_json(json)
# print the JSON string representation of the object
print ListCompanyUsersResponse.to_json()

# convert the object into a dict
list_company_users_response_dict = list_company_users_response_instance.to_dict()
# create an instance of ListCompanyUsersResponse from a dict
list_company_users_response_form_dict = list_company_users_response.from_dict(list_company_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


