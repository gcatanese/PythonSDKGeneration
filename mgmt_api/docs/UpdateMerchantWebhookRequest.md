# UpdateMerchantWebhookRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepts_expired_certificate** | **bool** | Indicates if expired SSL certificates are accepted. Default value: **false**. | [optional] 
**accepts_self_signed_certificate** | **bool** | Indicates if self-signed SSL certificates are accepted. Default value: **false**. | [optional] 
**accepts_untrusted_root_certificate** | **bool** | Indicates if untrusted SSL certificates are accepted. Default value: **false**. | [optional] 
**active** | **bool** | Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account. | 
**additional_settings** | [**AdditionalSettings**](AdditionalSettings.md) |  | [optional] 
**communication_format** | **str** | Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**  | 
**description** | **str** | Your description for this webhook configuration. | [optional] 
**network_type** | **str** | Network type for Terminal API notification webhooks. Possible values: * **public** * **local**  Default Value: **public**. | [optional] 
**password** | **str** | Password to access the webhook URL. | [optional] 
**populate_soap_action_header** | **bool** | Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if &#x60;communicationFormat&#x60;: **soap**. | [optional] 
**ssl_version** | **str** | SSL version to access the public webhook URL specified in the &#x60;url&#x60; field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use &#x60;sslVersion&#x60;: **TLSv1.2**. | [optional] 
**url** | **str** | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. | 
**username** | **str** | Username to access the webhook URL. | [optional] 

## Example

```python
from openapi_client.models.update_merchant_webhook_request import UpdateMerchantWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMerchantWebhookRequest from a JSON string
update_merchant_webhook_request_instance = UpdateMerchantWebhookRequest.from_json(json)
# print the JSON string representation of the object
print UpdateMerchantWebhookRequest.to_json()

# convert the object into a dict
update_merchant_webhook_request_dict = update_merchant_webhook_request_instance.to_dict()
# create an instance of UpdateMerchantWebhookRequest from a dict
update_merchant_webhook_request_form_dict = update_merchant_webhook_request.from_dict(update_merchant_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


