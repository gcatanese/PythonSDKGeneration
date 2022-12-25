# UpdateMerchantApiCredentialRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the API credential is enabled. | [optional] 
**allowed_origins** | **List[str]** | The new list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential. | [optional] 
**description** | **str** | Description of the API credential. | [optional] 
**roles** | **List[str]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. | [optional] 

## Example

```python
from openapi_client.models.update_merchant_api_credential_request import UpdateMerchantApiCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMerchantApiCredentialRequest from a JSON string
update_merchant_api_credential_request_instance = UpdateMerchantApiCredentialRequest.from_json(json)
# print the JSON string representation of the object
print UpdateMerchantApiCredentialRequest.to_json()

# convert the object into a dict
update_merchant_api_credential_request_dict = update_merchant_api_credential_request_instance.to_dict()
# create an instance of UpdateMerchantApiCredentialRequest from a dict
update_merchant_api_credential_request_form_dict = update_merchant_api_credential_request.from_dict(update_merchant_api_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


