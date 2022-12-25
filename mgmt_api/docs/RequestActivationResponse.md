# RequestActivationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The unique identifier of the company account. | [optional] 
**merchant_id** | **str** | The unique identifier of the merchant account you requested to activate. | [optional] 

## Example

```python
from openapi_client.models.request_activation_response import RequestActivationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestActivationResponse from a JSON string
request_activation_response_instance = RequestActivationResponse.from_json(json)
# print the JSON string representation of the object
print RequestActivationResponse.to_json()

# convert the object into a dict
request_activation_response_dict = request_activation_response_instance.to_dict()
# create an instance of RequestActivationResponse from a dict
request_activation_response_form_dict = request_activation_response.from_dict(request_activation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


