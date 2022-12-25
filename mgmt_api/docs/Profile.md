# Profile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | The type of Wi-Fi network. Possible values: **wpa-psk**, **wpa2-psk**, **wpa-eap**, **wpa2-eap**. | 
**auto_wifi** | **bool** | Indicates whether to automatically select the best authentication method available. Does not work on older terminal models. | [optional] 
**bss_type** | **str** | Use **infra** for infrastructure-based networks. This applies to most networks. Use **adhoc** only if the communication is p2p-based between base stations. | 
**channel** | **int** | The channel number of the Wi-Fi network. The recommended setting is **0** for automatic channel selection. | [optional] 
**default_profile** | **bool** | Indicates whether this is your preferred wireless network. If **true**, the terminal will try connecting to this network first. | [optional] 
**eap** | **str** | For &#x60;authType&#x60; **wpa-eap** or **wpa2-eap**. Possible values: **tls**, **peap**, **leap**, **fast** | [optional] 
**eap_ca_cert** | [**File**](File.md) |  | [optional] 
**eap_client_cert** | [**File**](File.md) |  | [optional] 
**eap_client_key** | [**File**](File.md) |  | [optional] 
**eap_client_pwd** | **str** | For &#x60;eap&#x60; **tls**. The password of the RSA key file, if that file is password-protected. | [optional] 
**eap_identity** | **str** | For &#x60;authType&#x60; **wpa-eap** or **wpa2-eap**. The EAP-PEAP username from your MS-CHAP account. Must match the configuration of your RADIUS server. | [optional] 
**eap_intermediate_cert** | [**File**](File.md) |  | [optional] 
**eap_pwd** | **str** | For &#x60;eap&#x60; **peap**. The EAP-PEAP password from your MS-CHAP account. Must match the configuration of your RADIUS server. | [optional] 
**hidden_ssid** | **bool** | Indicates if the network doesn&#39;t broadcast its SSID. Mandatory for Android terminals, because these terminals rely on this setting to be able to connect to any network. | [optional] 
**name** | **str** | Your name for the Wi-Fi profile. | [optional] 
**psk** | **str** | For &#x60;authType&#x60; **wpa-psk or **wpa2-psk**. The password to the wireless network. | [optional] 
**ssid** | **str** | The name of the wireless network. | 
**wsec** | **str** | The type of encryption. Possible values: **auto**, **ccmp** (recommended), **tkip** | 

## Example

```python
from openapi_client.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print Profile.to_json()

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_form_dict = profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


