# UpdateStoreRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**UpdatableAddress**](UpdatableAddress.md) |  | [optional] 
**business_line_ids** | **List[str]** | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businesslines__resParam_id) that the store is associated with. | [optional] 
**description** | **str** | The description of the store. | [optional] 
**external_reference_id** | **str** | When using the Zip payment method: The location ID that Zip has assigned to your store. | [optional] 
**split_configuration** | [**StoreSplitConfiguration**](StoreSplitConfiguration.md) |  | [optional] 
**status** | **str** | The status of the store. Possible values are:  - **active**: This value is assigned automatically when a store is created.  - **inactive**: The maximum [transaction limits and number of Store-and-Forward transactions](https://docs.adyen.com/point-of-sale/determine-account-structure/configure-features#payment-features) for the store are set to 0. This blocks new transactions, but captures are still possible. - **closed**: The terminals of the store are reassigned to the merchant inventory, so they can&#39;t process payments.  You can change the status from **active** to **inactive**, and from **inactive** to **active** or **closed**.  Once **closed**, a store can&#39;t be reopened. | [optional] 

## Example

```python
from openapi_client.models.update_store_request import UpdateStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStoreRequest from a JSON string
update_store_request_instance = UpdateStoreRequest.from_json(json)
# print the JSON string representation of the object
print UpdateStoreRequest.to_json()

# convert the object into a dict
update_store_request_dict = update_store_request_instance.to_dict()
# create an instance of UpdateStoreRequest from a dict
update_store_request_form_dict = update_store_request.from_dict(update_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


