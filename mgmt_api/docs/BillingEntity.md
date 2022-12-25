# BillingEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** | The email address of the billing entity. | [optional] 
**id** | **str** | The unique identifier of the billing entity, for use as &#x60;billingEntityId&#x60; when creating an order. | [optional] 
**name** | **str** | The unique name of the billing entity. | [optional] 
**tax_id** | **str** | The tax number of the billing entity. | [optional] 

## Example

```python
from openapi_client.models.billing_entity import BillingEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BillingEntity from a JSON string
billing_entity_instance = BillingEntity.from_json(json)
# print the JSON string representation of the object
print BillingEntity.to_json()

# convert the object into a dict
billing_entity_dict = billing_entity_instance.to_dict()
# create an instance of BillingEntity from a dict
billing_entity_form_dict = billing_entity.from_dict(billing_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


