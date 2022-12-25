# TerminalSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardholder_receipt** | [**CardholderReceipt**](CardholderReceipt.md) |  | [optional] 
**connectivity** | [**Connectivity**](Connectivity.md) |  | [optional] 
**gratuities** | [**List[Gratuity]**](Gratuity.md) | Settings for tipping with or without predefined options to choose from. The maximum number of predefined options is four, or three plus the option to enter a custom tip. | [optional] 
**hardware** | [**Hardware**](Hardware.md) |  | [optional] 
**nexo** | [**Nexo**](Nexo.md) |  | [optional] 
**offline_processing** | [**OfflineProcessing**](OfflineProcessing.md) |  | [optional] 
**opi** | [**Opi**](Opi.md) |  | [optional] 
**receipt_options** | [**ReceiptOptions**](ReceiptOptions.md) |  | [optional] 
**receipt_printing** | [**ReceiptPrinting**](ReceiptPrinting.md) |  | [optional] 
**signature** | [**Signature**](Signature.md) |  | [optional] 
**surcharge** | [**Surcharge**](Surcharge.md) |  | [optional] 
**timeouts** | [**Timeouts**](Timeouts.md) |  | [optional] 
**wifi_profiles** | [**WifiProfiles**](WifiProfiles.md) |  | [optional] 

## Example

```python
from openapi_client.models.terminal_settings import TerminalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalSettings from a JSON string
terminal_settings_instance = TerminalSettings.from_json(json)
# print the JSON string representation of the object
print TerminalSettings.to_json()

# convert the object into a dict
terminal_settings_dict = terminal_settings_instance.to_dict()
# create an instance of TerminalSettings from a dict
terminal_settings_form_dict = terminal_settings.from_dict(terminal_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


