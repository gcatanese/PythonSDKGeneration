# ReleaseUpdateDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of terminal action: Update Release. | [optional] [default to 'ReleaseUpdate']
**update_at_first_maintenance_call** | **bool** | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. | [optional] 

## Example

```python
from openapi_client.models.release_update_details import ReleaseUpdateDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseUpdateDetails from a JSON string
release_update_details_instance = ReleaseUpdateDetails.from_json(json)
# print the JSON string representation of the object
print ReleaseUpdateDetails.to_json()

# convert the object into a dict
release_update_details_dict = release_update_details_instance.to_dict()
# create an instance of ReleaseUpdateDetails from a dict
release_update_details_form_dict = release_update_details.from_dict(release_update_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


