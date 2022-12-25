# ApiCredentialLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | [**LinksElement**](LinksElement.md) |  | [optional] 
**company** | [**LinksElement**](LinksElement.md) |  | [optional] 
**generate_api_key** | [**LinksElement**](LinksElement.md) |  | [optional] 
**generate_client_key** | [**LinksElement**](LinksElement.md) |  | [optional] 
**merchant** | [**LinksElement**](LinksElement.md) |  | [optional] 
**var_self** | [**LinksElement**](LinksElement.md) |  | 

## Example

```python
from openapi_client.models.api_credential_links import ApiCredentialLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCredentialLinks from a JSON string
api_credential_links_instance = ApiCredentialLinks.from_json(json)
# print the JSON string representation of the object
print ApiCredentialLinks.to_json()

# convert the object into a dict
api_credential_links_dict = api_credential_links_instance.to_dict()
# create an instance of ApiCredentialLinks from a dict
api_credential_links_form_dict = api_credential_links.from_dict(api_credential_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


