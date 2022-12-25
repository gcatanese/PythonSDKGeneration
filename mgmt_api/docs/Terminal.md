# Terminal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned** | **bool** | The [assignment status](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api) of the terminal. If true, the terminal is assigned. If false, the terminal is in inventory and can&#39;t be boarded. | [optional] 
**bluetooth_ip** | **str** | The Bluetooth IP address of the terminal. | [optional] 
**bluetooth_mac** | **str** | The Bluetooth MAC address of the terminal. | [optional] 
**city** | **str** | The city where the terminal is located. | [optional] 
**company_account** | **str** | The company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account. | [optional] 
**country_code** | **str** | The country code of the country where the terminal is located. | [optional] 
**device_model** | **str** | The model name of the terminal. | [optional] 
**ethernet_ip** | **str** | The ethernet IP address of the terminal. | [optional] 
**ethernet_mac** | **str** | The ethernet MAC address of the terminal. | [optional] 
**firmware_version** | **str** | The software release currently in use on the terminal. | [optional] 
**iccid** | **str** | The integrated circuit card identifier (ICCID) of the SIM card in the terminal. | [optional] 
**id** | **str** | The unique identifier of the terminal. | [optional] 
**last_activity_date_time** | **datetime** | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. | [optional] 
**last_transaction_date_time** | **datetime** | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. | [optional] 
**link_negotiation** | **str** | The Ethernet link negotiation that the terminal uses:  - &#x60;auto&#x60;: Auto-negotiation  - &#x60;100full&#x60;: 100 Mbps full duplex | [optional] 
**serial_number** | **str** | The serial number of the terminal. | [optional] 
**sim_status** | **str** | On a terminal that supports 3G or 4G connectivity, indicates the status of the SIM card in the terminal: ACTIVE or INVENTORY. | [optional] 
**status** | **str** | Indicates when the terminal was last online, whether the terminal is being reassigned, or whether the terminal is turned off. If the terminal was last online more that a week ago, it is also shown as turned off. | [optional] 
**store_status** | **str** | The status of the store that the terminal is assigned to. | [optional] 
**wifi_ip** | **str** | The terminal&#39;s IP address in your Wi-Fi network. | [optional] 
**wifi_mac** | **str** | The terminal&#39;s MAC address in your Wi-Fi network. | [optional] 
**wifi_ssid** | **str** | The SSID of the Wi-Fi network that your terminal is connected to. | [optional] 

## Example

```python
from openapi_client.models.terminal import Terminal

# TODO update the JSON string below
json = "{}"
# create an instance of Terminal from a JSON string
terminal_instance = Terminal.from_json(json)
# print the JSON string representation of the object
print Terminal.to_json()

# convert the object into a dict
terminal_dict = terminal_instance.to_dict()
# create an instance of Terminal from a dict
terminal_form_dict = terminal.from_dict(terminal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


