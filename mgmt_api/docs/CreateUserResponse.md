# CreateUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | [optional] 
**account_groups** | **List[str]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**active** | **bool** | Indicates whether this user is active. | [optional] 
**email** | **str** | The email address of the user. | 
**id** | **str** | The unique identifier of the user. | 
**name** | [**Name**](Name.md) |  | [optional] 
**roles** | **List[str]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | 
**time_zone_code** | **str** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | 
**username** | **str** | The username for this user. | 

## Example

```python
from openapi_client.models.create_user_response import CreateUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserResponse from a JSON string
create_user_response_instance = CreateUserResponse.from_json(json)
# print the JSON string representation of the object
print CreateUserResponse.to_json()

# convert the object into a dict
create_user_response_dict = create_user_response_instance.to_dict()
# create an instance of CreateUserResponse from a dict
create_user_response_form_dict = create_user_response.from_dict(create_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


