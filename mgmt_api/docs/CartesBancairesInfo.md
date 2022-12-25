# CartesBancairesInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siret** | **str** | Cartes Bancaires SIRET. Format: 14 digits. | 

## Example

```python
from openapi_client.models.cartes_bancaires_info import CartesBancairesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CartesBancairesInfo from a JSON string
cartes_bancaires_info_instance = CartesBancairesInfo.from_json(json)
# print the JSON string representation of the object
print CartesBancairesInfo.to_json()

# convert the object into a dict
cartes_bancaires_info_dict = cartes_bancaires_info_instance.to_dict()
# create an instance of CartesBancairesInfo from a dict
cartes_bancaires_info_form_dict = cartes_bancaires_info.from_dict(cartes_bancaires_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


