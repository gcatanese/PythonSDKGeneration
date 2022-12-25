# Signature


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_signature_on_screen** | **bool** | If &#x60;skipSignature&#x60; is false, indicates whether the shopper should provide a signature on the display (**true**) or on the merchant receipt (**false**). | [optional] 
**device_name** | **str** | Name that identifies the terminal. | [optional] 
**skip_signature** | **bool** | Skip asking for a signature. This is possible because all global card schemes (American Express, Diners, Discover, JCB, MasterCard, VISA, and UnionPay) regard a signature as optional. | [optional] 

## Example

```python
from openapi_client.models.signature import Signature

# TODO update the JSON string below
json = "{}"
# create an instance of Signature from a JSON string
signature_instance = Signature.from_json(json)
# print the JSON string representation of the object
print Signature.to_json()

# convert the object into a dict
signature_dict = signature_instance.to_dict()
# create an instance of Signature from a dict
signature_form_dict = signature.from_dict(signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


