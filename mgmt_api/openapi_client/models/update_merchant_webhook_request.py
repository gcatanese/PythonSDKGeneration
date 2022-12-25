# coding: utf-8

"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator
from openapi_client.models.additional_settings import AdditionalSettings

class UpdateMerchantWebhookRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    accepts_expired_certificate: Optional[StrictBool] = Field(None, alias="acceptsExpiredCertificate", description="Indicates if expired SSL certificates are accepted. Default value: **false**.")
    accepts_self_signed_certificate: Optional[StrictBool] = Field(None, alias="acceptsSelfSignedCertificate", description="Indicates if self-signed SSL certificates are accepted. Default value: **false**.")
    accepts_untrusted_root_certificate: Optional[StrictBool] = Field(None, alias="acceptsUntrustedRootCertificate", description="Indicates if untrusted SSL certificates are accepted. Default value: **false**.")
    active: StrictBool = Field(..., description="Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account.")
    additional_settings: Optional[AdditionalSettings] = Field(None, alias="additionalSettings")
    communication_format: StrictStr = Field(..., alias="communicationFormat", description="Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json** ")
    description: Optional[StrictStr] = Field(None, description="Your description for this webhook configuration.")
    network_type: Optional[StrictStr] = Field(None, alias="networkType", description="Network type for Terminal API notification webhooks. Possible values: * **public** * **local**  Default Value: **public**.")
    password: Optional[StrictStr] = Field(None, description="Password to access the webhook URL.")
    populate_soap_action_header: Optional[StrictBool] = Field(None, alias="populateSoapActionHeader", description="Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if `communicationFormat`: **soap**.")
    ssl_version: Optional[StrictStr] = Field(None, alias="sslVersion", description="SSL version to access the public webhook URL specified in the `url` field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use `sslVersion`: **TLSv1.2**.")
    url: StrictStr = Field(..., description="Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**.")
    username: Optional[constr(strict=True, max_length=255)] = Field(None, description="Username to access the webhook URL.")
    __properties = ["acceptsExpiredCertificate", "acceptsSelfSignedCertificate", "acceptsUntrustedRootCertificate", "active", "additionalSettings", "communicationFormat", "description", "networkType", "password", "populateSoapActionHeader", "sslVersion", "url", "username"]

    @validator('communication_format')
    def communication_format_validate_enum(cls, v):
        if v not in ('HTTP', 'JSON', 'SOAP'):
            raise ValueError("must validate the enum values ('HTTP', 'JSON', 'SOAP')")
        return v

    @validator('network_type')
    def network_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('LOCAL', 'PUBLIC'):
            raise ValueError("must validate the enum values ('LOCAL', 'PUBLIC')")
        return v

    @validator('ssl_version')
    def ssl_version_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HTTP', 'SSL', 'SSLV3', 'SSL_INSECURE_CIPHERS', 'TLS', 'TLSV1', 'TLSV1_1', 'TLSV1_2', 'TLSV1_3', 'TLSV1_INSECURE_CIPHERS'):
            raise ValueError("must validate the enum values ('HTTP', 'SSL', 'SSLV3', 'SSL_INSECURE_CIPHERS', 'TLS', 'TLSV1', 'TLSV1_1', 'TLSV1_2', 'TLSV1_3', 'TLSV1_INSECURE_CIPHERS')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateMerchantWebhookRequest:
        """Create an instance of UpdateMerchantWebhookRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of additional_settings
        if self.additional_settings:
            _dict['additionalSettings'] = self.additional_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateMerchantWebhookRequest:
        """Create an instance of UpdateMerchantWebhookRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateMerchantWebhookRequest.parse_obj(obj)

        _obj = UpdateMerchantWebhookRequest.parse_obj({
            "accepts_expired_certificate": obj.get("acceptsExpiredCertificate"),
            "accepts_self_signed_certificate": obj.get("acceptsSelfSignedCertificate"),
            "accepts_untrusted_root_certificate": obj.get("acceptsUntrustedRootCertificate"),
            "active": obj.get("active"),
            "additional_settings": AdditionalSettings.from_dict(obj.get("additionalSettings")) if obj.get("additionalSettings") is not None else None,
            "communication_format": obj.get("communicationFormat"),
            "description": obj.get("description"),
            "network_type": obj.get("networkType"),
            "password": obj.get("password"),
            "populate_soap_action_header": obj.get("populateSoapActionHeader"),
            "ssl_version": obj.get("sslVersion"),
            "url": obj.get("url"),
            "username": obj.get("username")
        })
        return _obj

