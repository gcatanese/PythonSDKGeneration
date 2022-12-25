# CompanyLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_credentials** | [**LinksElement**](LinksElement.md) |  | [optional] 
**var_self** | [**LinksElement**](LinksElement.md) |  | 
**users** | [**LinksElement**](LinksElement.md) |  | [optional] 
**webhooks** | [**LinksElement**](LinksElement.md) |  | [optional] 

## Example

```python
from openapi_client.models.company_links import CompanyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyLinks from a JSON string
company_links_instance = CompanyLinks.from_json(json)
# print the JSON string representation of the object
print CompanyLinks.to_json()

# convert the object into a dict
company_links_dict = company_links_instance.to_dict()
# create an instance of CompanyLinks from a dict
company_links_form_dict = company_links.from_dict(company_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


