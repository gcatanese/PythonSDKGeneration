# CreateMerchantUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_groups** | **List[str]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**email** | **str** | The email address of the user. | 
**name** | [**Name**](Name.md) |  | 
**roles** | **List[str]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | [optional] 
**time_zone_code** | **str** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | [optional] 
**username** | **str** | The username for this user. Allowed length: 255 alphanumeric characters. | 

## Example

```python
from openapi_client.models.create_merchant_user_request import CreateMerchantUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantUserRequest from a JSON string
create_merchant_user_request_instance = CreateMerchantUserRequest.from_json(json)
# print the JSON string representation of the object
print CreateMerchantUserRequest.to_json()

# convert the object into a dict
create_merchant_user_request_dict = create_merchant_user_request_instance.to_dict()
# create an instance of CreateMerchantUserRequest from a dict
create_merchant_user_request_form_dict = create_merchant_user_request.from_dict(create_merchant_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


