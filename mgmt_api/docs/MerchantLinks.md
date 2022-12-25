# MerchantLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_credentials** | [**LinksElement**](LinksElement.md) |  | [optional] 
**var_self** | [**LinksElement**](LinksElement.md) |  | 
**users** | [**LinksElement**](LinksElement.md) |  | [optional] 
**webhooks** | [**LinksElement**](LinksElement.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_links import MerchantLinks

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantLinks from a JSON string
merchant_links_instance = MerchantLinks.from_json(json)
# print the JSON string representation of the object
print MerchantLinks.to_json()

# convert the object into a dict
merchant_links_dict = merchant_links_instance.to_dict()
# create an instance of MerchantLinks from a dict
merchant_links_form_dict = merchant_links.from_dict(merchant_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


