# Company


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**CompanyLinks**](CompanyLinks.md) |  | [optional] 
**data_centers** | [**List[DataCenter]**](DataCenter.md) | List of available data centers.  Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. | [optional] 
**description** | **str** | Your description for the company account, maximum 300 characters | [optional] 
**id** | **str** | The unique identifier of the company account. | [optional] 
**name** | **str** | The legal or trading name of the company. | [optional] 
**reference** | **str** | Your reference to the account | [optional] 
**status** | **str** | The status of the company account.  Possible values:  * **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account. * **Inactive**: Users can log in. Payment processing and payouts are disabled. * **Closed**: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. | [optional] 

## Example

```python
from openapi_client.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print Company.to_json()

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_form_dict = company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


