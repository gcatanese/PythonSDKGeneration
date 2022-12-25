# UpdateCompanyApiCredentialRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the API credential is enabled. | [optional] 
**allowed_origins** | **List[str]** | The new list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential. | [optional] 
**associated_merchant_accounts** | **List[str]** | List of merchant accounts that the API credential has access to. | [optional] 
**description** | **str** | Description of the API credential. | [optional] 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) of the API credential. | [optional] 

## Example

```python
from openapi_client.models.update_company_api_credential_request import UpdateCompanyApiCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCompanyApiCredentialRequest from a JSON string
update_company_api_credential_request_instance = UpdateCompanyApiCredentialRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCompanyApiCredentialRequest.to_json()

# convert the object into a dict
update_company_api_credential_request_dict = update_company_api_credential_request_instance.to_dict()
# create an instance of UpdateCompanyApiCredentialRequest from a dict
update_company_api_credential_request_form_dict = update_company_api_credential_request.from_dict(update_company_api_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


