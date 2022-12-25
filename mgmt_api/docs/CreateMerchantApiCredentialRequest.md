# CreateMerchantApiCredentialRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** | The list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential. | [optional] 
**description** | **str** | Description of the API credential. | [optional] 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. | [optional] 

## Example

```python
from openapi_client.models.create_merchant_api_credential_request import CreateMerchantApiCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantApiCredentialRequest from a JSON string
create_merchant_api_credential_request_instance = CreateMerchantApiCredentialRequest.from_json(json)
# print the JSON string representation of the object
print CreateMerchantApiCredentialRequest.to_json()

# convert the object into a dict
create_merchant_api_credential_request_dict = create_merchant_api_credential_request_instance.to_dict()
# create an instance of CreateMerchantApiCredentialRequest from a dict
create_merchant_api_credential_request_form_dict = create_merchant_api_credential_request.from_dict(create_merchant_api_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


