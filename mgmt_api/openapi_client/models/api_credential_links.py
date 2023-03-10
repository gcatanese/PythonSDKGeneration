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
from pydantic import BaseModel, Field
from openapi_client.models.links_element import LinksElement

class ApiCredentialLinks(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    allowed_origins: Optional[LinksElement] = Field(None, alias="allowedOrigins")
    company: Optional[LinksElement] = None
    generate_api_key: Optional[LinksElement] = Field(None, alias="generateApiKey")
    generate_client_key: Optional[LinksElement] = Field(None, alias="generateClientKey")
    merchant: Optional[LinksElement] = None
    var_self: LinksElement = Field(..., alias="self")
    __properties = ["allowedOrigins", "company", "generateApiKey", "generateClientKey", "merchant", "self"]

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
    def from_json(cls, json_str: str) -> ApiCredentialLinks:
        """Create an instance of ApiCredentialLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of allowed_origins
        if self.allowed_origins:
            _dict['allowedOrigins'] = self.allowed_origins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_api_key
        if self.generate_api_key:
            _dict['generateApiKey'] = self.generate_api_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generate_client_key
        if self.generate_client_key:
            _dict['generateClientKey'] = self.generate_client_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict['merchant'] = self.merchant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiCredentialLinks:
        """Create an instance of ApiCredentialLinks from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiCredentialLinks.parse_obj(obj)

        _obj = ApiCredentialLinks.parse_obj({
            "allowed_origins": LinksElement.from_dict(obj.get("allowedOrigins")) if obj.get("allowedOrigins") is not None else None,
            "company": LinksElement.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "generate_api_key": LinksElement.from_dict(obj.get("generateApiKey")) if obj.get("generateApiKey") is not None else None,
            "generate_client_key": LinksElement.from_dict(obj.get("generateClientKey")) if obj.get("generateClientKey") is not None else None,
            "merchant": LinksElement.from_dict(obj.get("merchant")) if obj.get("merchant") is not None else None,
            "var_self": LinksElement.from_dict(obj.get("self")) if obj.get("self") is not None else None
        })
        return _obj

