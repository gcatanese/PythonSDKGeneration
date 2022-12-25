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
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.address2 import Address2
from openapi_client.models.links import Links
from openapi_client.models.store_split_configuration import StoreSplitConfiguration

class Store(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[Links] = Field(None, alias="_links")
    address: Optional[Address2] = None
    business_line_ids: Optional[List[StrictStr]] = Field(None, alias="businessLineIds", description="The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businesslines__resParam_id) that the store is associated with.  If not specified, the business line of the merchant account is used. Required when there are multiple business lines under the merchant account.")
    description: Optional[StrictStr] = Field(None, description="The description of the store.")
    external_reference_id: Optional[StrictStr] = Field(None, alias="externalReferenceId", description="When using the Zip payment method: The location ID that Zip has assigned to your store.")
    id: Optional[StrictStr] = Field(None, description="The unique identifier of the store. This value is generated by Adyen.")
    merchant_id: Optional[StrictStr] = Field(None, alias="merchantId", description="The unique identifier of the merchant account that the store belongs to.")
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber", description="The phone number of the store, including '+' and country code.")
    reference: Optional[StrictStr] = Field(None, description="A reference to recognize the store by. Also known as the store code.  Allowed characters: Lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and underscore (_)")
    shopper_statement: Optional[StrictStr] = Field(None, alias="shopperStatement", description="The store name shown on the shopper's bank or credit card statement and on the shopper receipt.")
    split_configuration: Optional[StoreSplitConfiguration] = Field(None, alias="splitConfiguration")
    status: Optional[StrictStr] = Field(None, description="The status of the store. Possible values are:  - **active**. This value is assigned automatically when a store is created.  - **inactive**. The terminals under the store are blocked from accepting new transactions, but capturing outstanding transactions is still possible. - **closed**. This status is irreversible. The terminals under the store are reassigned to the merchant inventory.")
    __properties = ["_links", "address", "businessLineIds", "description", "externalReferenceId", "id", "merchantId", "phoneNumber", "reference", "shopperStatement", "splitConfiguration", "status"]

    @validator('status')
    def status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('active', 'closed', 'inactive'):
            raise ValueError("must validate the enum values ('active', 'closed', 'inactive')")
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
    def from_json(cls, json_str: str) -> Store:
        """Create an instance of Store from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of split_configuration
        if self.split_configuration:
            _dict['splitConfiguration'] = self.split_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Store:
        """Create an instance of Store from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Store.parse_obj(obj)

        _obj = Store.parse_obj({
            "links": Links.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "address": Address2.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "business_line_ids": obj.get("businessLineIds"),
            "description": obj.get("description"),
            "external_reference_id": obj.get("externalReferenceId"),
            "id": obj.get("id"),
            "merchant_id": obj.get("merchantId"),
            "phone_number": obj.get("phoneNumber"),
            "reference": obj.get("reference"),
            "shopper_statement": obj.get("shopperStatement"),
            "split_configuration": StoreSplitConfiguration.from_dict(obj.get("splitConfiguration")) if obj.get("splitConfiguration") is not None else None,
            "status": obj.get("status")
        })
        return _obj

