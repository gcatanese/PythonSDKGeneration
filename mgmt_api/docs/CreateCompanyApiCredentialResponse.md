# CreateCompanyApiCredentialResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApiCredentialLinks**](ApiCredentialLinks.md) |  | [optional] 
**active** | **bool** | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. | 
**allowed_ip_addresses** | **List[str]** | List of IP addresses from which your client can make requests.  If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, you get a security error. | 
**allowed_origins** | [**List[AllowedOrigin]**](AllowedOrigin.md) | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. | [optional] 
**api_key** | **str** | The API key for the API credential that was created. | 
**associated_merchant_accounts** | **List[str]** | List of merchant accounts that the API credential has access to. | 
**client_key** | **str** | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. | 
**description** | **str** | Description of the API credential. | [optional] 
**id** | **str** | Unique identifier of the API credential. | 
**password** | **str** | The password for the API credential that was created. | 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. | 
**username** | **str** | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. | 

## Example

```python
from openapi_client.models.create_company_api_credential_response import CreateCompanyApiCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyApiCredentialResponse from a JSON string
create_company_api_credential_response_instance = CreateCompanyApiCredentialResponse.from_json(json)
# print the JSON string representation of the object
print CreateCompanyApiCredentialResponse.to_json()

# convert the object into a dict
create_company_api_credential_response_dict = create_company_api_credential_response_instance.to_dict()
# create an instance of CreateCompanyApiCredentialResponse from a dict
create_company_api_credential_response_form_dict = create_company_api_credential_response.from_dict(create_company_api_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


