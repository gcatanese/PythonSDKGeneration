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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class Gratuity(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    allow_custom_amount: Optional[StrictBool] = Field(None, alias="allowCustomAmount", description="Indicates whether one of the predefined tipping options is to let the shopper enter a custom tip. If **true**, only three of the other options defined in `predefinedTipEntries` are shown.")
    currency: Optional[StrictStr] = Field(None, description="The currency that the tipping settings apply to.")
    predefined_tip_entries: Optional[List[StrictStr]] = Field(None, alias="predefinedTipEntries", description="Tipping options the shopper can choose from if `usePredefinedTipEntries` is **true**. The maximum number of predefined options is four, or three plus the option to enter a custom tip. The options can be a mix of:  - A percentage of the transaction amount. Example: **5%** - A tip amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). Example: **500** for a EUR 5 tip.")
    use_predefined_tip_entries: Optional[StrictBool] = Field(None, alias="usePredefinedTipEntries", description="Indicates whether the terminal shows a prompt to enter a tip (**false**), or predefined tipping options to choose from (**true**).")
    __properties = ["allowCustomAmount", "currency", "predefinedTipEntries", "usePredefinedTipEntries"]

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
    def from_json(cls, json_str: str) -> Gratuity:
        """Create an instance of Gratuity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Gratuity:
        """Create an instance of Gratuity from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Gratuity.parse_obj(obj)

        _obj = Gratuity.parse_obj({
            "allow_custom_amount": obj.get("allowCustomAmount"),
            "currency": obj.get("currency"),
            "predefined_tip_entries": obj.get("predefinedTipEntries"),
            "use_predefined_tip_entries": obj.get("usePredefinedTipEntries")
        })
        return _obj
