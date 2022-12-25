# BillingEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillingEntity]**](BillingEntity.md) | List of legal entities that can be used for the billing of orders. | [optional] 

## Example

```python
from openapi_client.models.billing_entities_response import BillingEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingEntitiesResponse from a JSON string
billing_entities_response_instance = BillingEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print BillingEntitiesResponse.to_json()

# convert the object into a dict
billing_entities_response_dict = billing_entities_response_instance.to_dict()
# create an instance of BillingEntitiesResponse from a dict
billing_entities_response_form_dict = billing_entities_response.from_dict(billing_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


