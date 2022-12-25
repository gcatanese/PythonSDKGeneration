# CreateCompanyUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_groups** | **List[str]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**associated_merchant_accounts** | **List[str]** | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) associated with this user. | [optional] 
**email** | **str** | The email address of the user. | 
**name** | [**Name**](Name.md) |  | 
**roles** | **List[str]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | [optional] 
**time_zone_code** | **str** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | [optional] 
**username** | **str** | The username for this user. Allowed length: 255 alphanumeric characters. | 

## Example

```python
from openapi_client.models.create_company_user_request import CreateCompanyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyUserRequest from a JSON string
create_company_user_request_instance = CreateCompanyUserRequest.from_json(json)
# print the JSON string representation of the object
print CreateCompanyUserRequest.to_json()

# convert the object into a dict
create_company_user_request_dict = create_company_user_request_instance.to_dict()
# create an instance of CreateCompanyUserRequest from a dict
create_company_user_request_form_dict = create_company_user_request.from_dict(create_company_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


