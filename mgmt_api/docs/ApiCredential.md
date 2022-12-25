# ApiCredential


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApiCredentialLinks**](ApiCredentialLinks.md) |  | [optional] 
**active** | **bool** | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. | 
**allowed_ip_addresses** | **List[str]** | List of IP addresses from which your client can make requests.  If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, you get a security error. | 
**allowed_origins** | [**List[AllowedOrigin]**](AllowedOrigin.md) | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. | [optional] 
**client_key** | **str** | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. | 
**description** | **str** | Description of the API credential. | [optional] 
**id** | **str** | Unique identifier of the API credential. | 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. | 
**username** | **str** | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. | 

## Example

```python
from openapi_client.models.api_credential import ApiCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCredential from a JSON string
api_credential_instance = ApiCredential.from_json(json)
# print the JSON string representation of the object
print ApiCredential.to_json()

# convert the object into a dict
api_credential_dict = api_credential_instance.to_dict()
# create an instance of ApiCredential from a dict
api_credential_form_dict = api_credential.from_dict(api_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


