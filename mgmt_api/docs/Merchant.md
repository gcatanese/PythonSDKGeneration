# Merchant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**MerchantLinks**](MerchantLinks.md) |  | [optional] 
**capture_delay** | **str** | The [capture delay](https://docs.adyen.com/online-payments/capture#capture-delay) set for the merchant account.  Possible values: * **Immediate** * **Manual** * Number of days from **1** to **29** | [optional] 
**company_id** | **str** | The unique identifier of the company account this merchant belongs to | [optional] 
**data_centers** | [**List[DataCenter]**](DataCenter.md) | List of available data centers.  Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. | [optional] 
**default_shopper_interaction** | **str** | The default [&#x60;shopperInteraction&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/v68/post/payments__reqParam_shopperInteraction) value used when processing payments through this merchant account. | [optional] 
**description** | **str** | Your description for the merchant account, maximum 300 characters | [optional] 
**id** | **str** | The unique identifier of the merchant account. | [optional] 
**merchant_city** | **str** | The city where the legal entity of this merchant account is registered. | [optional] 
**name** | **str** | The name of the legal entity associated with the merchant account. | [optional] 
**pricing_plan** | **str** | Only applies to merchant accounts managed by Adyen&#39;s partners. The name of the pricing plan assigned to the merchant account. | [optional] 
**primary_settlement_currency** | **str** | The currency of the country where the legal entity of this merchant account is registered. Format: [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, a legal entity based in the United States has USD as the primary settlement currency. | [optional] 
**reference** | **str** | Reference of the merchant account. | [optional] 
**shop_web_address** | **str** | The URL for the ecommerce website used with this merchant account. | [optional] 
**status** | **str** | The status of the merchant account.  Possible values:  * **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments. * **Active**: Users can access the merchant account in the Customer Area. If the company account is also **Active**, then payment processing and payouts are enabled. * **InactiveWithModifications**: Users can access the merchant account in the Customer Area. You cannot process new payments but you can still modify payments, for example issue refunds. You can still receive payouts. * **Inactive**: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled. * **Closed**: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. | [optional] 

## Example

```python
from openapi_client.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print Merchant.to_json()

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_form_dict = merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


