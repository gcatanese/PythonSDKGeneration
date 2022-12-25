# Webhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhookLinks**](WebhookLinks.md) |  | [optional] 
**accepts_expired_certificate** | **bool** | Indicates if expired SSL certificates are accepted. Default value: **false**. | [optional] 
**accepts_self_signed_certificate** | **bool** | Indicates if self-signed SSL certificates are accepted. Default value: **false**. | [optional] 
**accepts_untrusted_root_certificate** | **bool** | Indicates if untrusted SSL certificates are accepted. Default value: **false**. | [optional] 
**account_reference** | **str** | Reference to the account the webook is set on. | [optional] 
**active** | **bool** | Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account. | 
**additional_settings** | [**AdditionalSettingsResponse**](AdditionalSettingsResponse.md) |  | [optional] 
**certificate_alias** | **str** | The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias. | [optional] 
**communication_format** | **str** | Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**  | 
**description** | **str** | Your description for this webhook configuration. | [optional] 
**filter_merchant_account_type** | **str** | Shows how merchant accounts are included in company-level webhooks. Possible values: * **includeAccounts** * **excludeAccounts** * **allAccounts**: Includes all merchant accounts, and does not require specifying &#x60;filterMerchantAccounts&#x60;. | [optional] 
**filter_merchant_accounts** | **List[str]** | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for &#x60;filterMerchantAccountType&#x60;.  Required if &#x60;filterMerchantAccountType&#x60; is either: * **includeAccounts** * **excludeAccounts**  Not needed for &#x60;filterMerchantAccountType&#x60;: **allAccounts**. | [optional] 
**has_error** | **bool** | Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookid}/test). | [optional] 
**has_password** | **bool** | Indicates if the webhook is password protected. | [optional] 
**hmac_key_check_value** | **str** | The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook. | [optional] 
**id** | **str** | Unique identifier for this webhook. | [optional] 
**network_type** | **str** | Network type for Terminal API details webhooks. | [optional] 
**populate_soap_action_header** | **bool** | Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if &#x60;communicationFormat&#x60;: **soap**. | [optional] 
**ssl_version** | **str** | SSL version to access the public webhook URL specified in the &#x60;url&#x60; field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use &#x60;sslVersion&#x60;: **TLSv1.2**. | [optional] 
**type** | **str** | The type of webhook. Possible values are:  - **standard** - **account-settings-notification** - **banktransfer-notification** - **boletobancario-notification** - **directdebit-notification** - **pending-notification** - **ideal-notification** - **ideal-pending-notification** - **report-notification** - **terminal-api-notification**  Find out more about [standard notification webhooks](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes) and [other types of notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#other-notifications). | 
**url** | **str** | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. | 
**username** | **str** | Username to access the webhook URL. | [optional] 

## Example

```python
from openapi_client.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print Webhook.to_json()

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_form_dict = webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


