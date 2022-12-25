# StoreCreationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address2**](Address2.md) |  | 
**business_line_ids** | **List[str]** | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businesslines__resParam_id) that the store is associated with. If not specified, the business line of the merchant account is used. Required when there are multiple business lines under the merchant account. | [optional] 
**description** | **str** | Your description of the store. | 
**external_reference_id** | **str** | When using the Zip payment method: The location ID that Zip has assigned to your store. | [optional] 
**phone_number** | **str** | The phone number of the store, including &#39;+&#39; and country code. | 
**reference** | **str** | Your reference to recognize the store by. Also known as the store code.  Allowed characters: Lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and underscore (_). | [optional] 
**shopper_statement** | **str** | The store name to be shown on the shopper&#39;s bank or credit card statement and on the shopper receipt. Maximum length: 22 characters; can&#39;t be all numbers. | 
**split_configuration** | [**StoreSplitConfiguration**](StoreSplitConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_creation_request import StoreCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreationRequest from a JSON string
store_creation_request_instance = StoreCreationRequest.from_json(json)
# print the JSON string representation of the object
print StoreCreationRequest.to_json()

# convert the object into a dict
store_creation_request_dict = store_creation_request_instance.to_dict()
# create an instance of StoreCreationRequest from a dict
store_creation_request_form_dict = store_creation_request.from_dict(store_creation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


