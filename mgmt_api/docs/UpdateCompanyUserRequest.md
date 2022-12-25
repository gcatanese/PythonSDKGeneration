# UpdateCompanyUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_groups** | **List[str]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**active** | **bool** | Indicates whether this user is active. | [optional] 
**associated_merchant_accounts** | **List[str]** | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) to associate the user with. | [optional] 
**email** | **str** | The email address of the user. | [optional] 
**name** | [**Name2**](Name2.md) |  | [optional] 
**roles** | **List[str]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | [optional] 
**time_zone_code** | **str** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | [optional] 

## Example

```python
from openapi_client.models.update_company_user_request import UpdateCompanyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyUserRequest from a JSON string
update_company_user_request_instance = UpdateCompanyUserRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCompanyUserRequest.to_json()

# convert the object into a dict
update_company_user_request_dict = update_company_user_request_instance.to_dict()
# create an instance of UpdateCompanyUserRequest from a dict
update_company_user_request_form_dict = update_company_user_request.from_dict(update_company_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


