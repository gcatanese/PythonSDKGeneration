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


from typing import List, Optional
from pydantic import BaseModel, Field
from openapi_client.models.profile import Profile
from openapi_client.models.settings import Settings

class WifiProfiles(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    profiles: Optional[List[Profile]] = Field(None, description="List of remote Wi-Fi profiles")
    settings: Optional[Settings] = None
    __properties = ["profiles", "settings"]

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
    def from_json(cls, json_str: str) -> WifiProfiles:
        """Create an instance of WifiProfiles from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in profiles (list)
        _items = []
        if self.profiles:
            for _item in self.profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['profiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WifiProfiles:
        """Create an instance of WifiProfiles from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WifiProfiles.parse_obj(obj)

        _obj = WifiProfiles.parse_obj({
            "profiles": [Profile.from_dict(_item) for _item in obj.get("profiles")] if obj.get("profiles") is not None else None,
            "settings": Settings.from_dict(obj.get("settings")) if obj.get("settings") is not None else None
        })
        return _obj

