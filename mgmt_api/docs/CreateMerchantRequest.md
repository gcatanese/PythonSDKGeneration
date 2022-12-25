# CreateMerchantRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_line_id** | **str** | The unique identifier of the [business line](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines). Required for an Adyen for Platforms Manage integration. | [optional] 
**company_id** | **str** | The unique identifier of the company account. | 
**description** | **str** | Your description for the merchant account, maximum 300 characters. | [optional] 
**legal_entity_id** | **str** | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities). Required for an Adyen for Platforms Manage integration. | [optional] 
**pricing_plan** | **str** | Sets the pricing plan for the merchant account. Required for an Adyen for Platforms Manage integration. Your Adyen contact will provide the values that you can use. | [optional] 
**reference** | **str** | Your reference for the merchant account. To make this reference the unique identifier of the merchant account, your Adyen contact can set up a template on your company account. The template can have 6 to 255 characters with upper- and lower-case letters, underscores, and numbers. When your company account has a template, then the &#x60;reference&#x60; is required and must be unique within the company account. | [optional] 

## Example

```python
from openapi_client.models.create_merchant_request import CreateMerchantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantRequest from a JSON string
create_merchant_request_instance = CreateMerchantRequest.from_json(json)
# print the JSON string representation of the object
print CreateMerchantRequest.to_json()

# convert the object into a dict
create_merchant_request_dict = create_merchant_request_instance.to_dict()
# create an instance of CreateMerchantRequest from a dict
create_merchant_request_form_dict = create_merchant_request.from_dict(create_merchant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


