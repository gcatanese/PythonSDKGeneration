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

class UpdateCompanyApiCredentialRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    active: Optional[StrictBool] = Field(None, description="Indicates if the API credential is enabled.")
    allowed_origins: Optional[List[StrictStr]] = Field(None, alias="allowedOrigins", description="The new list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential.")
    associated_merchant_accounts: Optional[List[StrictStr]] = Field(None, alias="associatedMerchantAccounts", description="List of merchant accounts that the API credential has access to.")
    description: Optional[StrictStr] = Field(None, description="Description of the API credential.")
    roles: Optional[List[StrictStr]] = Field(None, description="List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) of the API credential.")
    __properties = ["active", "allowedOrigins", "associatedMerchantAccounts", "description", "roles"]

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
    def from_json(cls, json_str: str) -> UpdateCompanyApiCredentialRequest:
        """Create an instance of UpdateCompanyApiCredentialRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCompanyApiCredentialRequest:
        """Create an instance of UpdateCompanyApiCredentialRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateCompanyApiCredentialRequest.parse_obj(obj)

        _obj = UpdateCompanyApiCredentialRequest.parse_obj({
            "active": obj.get("active"),
            "allowed_origins": obj.get("allowedOrigins"),
            "associated_merchant_accounts": obj.get("associatedMerchantAccounts"),
            "description": obj.get("description"),
            "roles": obj.get("roles")
        })
        return _obj

