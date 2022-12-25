# MeApiCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApiCredentialLinks**](ApiCredentialLinks.md) |  | [optional] 
**active** | **bool** | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. | 
**allowed_ip_addresses** | **List[str]** | List of IP addresses from which your client can make requests.  If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, you get a security error. | 
**allowed_origins** | [**List[AllowedOrigin]**](AllowedOrigin.md) | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. | [optional] 
**associated_merchant_accounts** | **List[str]** | List of merchant accounts that the API credential has explicit access to.   If the credential has access to a company, this implies access to all merchant accounts and no merchants for that company will be included. | [optional] 
**client_key** | **str** | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. | 
**company_name** | **str** | Name of the company linked to the API credential. | [optional] 
**description** | **str** | Description of the API credential. | [optional] 
**id** | **str** | Unique identifier of the API credential. | 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. | 
**username** | **str** | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. | 

## Example

```python
from openapi_client.models.me_api_credential import MeApiCredential

# TODO update the JSON string below
json = "{}"
# create an instance of MeApiCredential from a JSON string
me_api_credential_instance = MeApiCredential.from_json(json)
# print the JSON string representation of the object
print MeApiCredential.to_json()

# convert the object into a dict
me_api_credential_dict = me_api_credential_instance.to_dict()
# create an instance of MeApiCredential from a dict
me_api_credential_form_dict = me_api_credential.from_dict(me_api_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


