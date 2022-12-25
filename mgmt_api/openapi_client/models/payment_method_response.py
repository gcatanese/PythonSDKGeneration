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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from openapi_client.models.pagination_links import PaginationLinks
from openapi_client.models.payment_method import PaymentMethod

class PaymentMethodResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[PaginationLinks] = Field(None, alias="_links")
    data: Optional[List[PaymentMethod]] = Field(None, description="Payment methods details.")
    items_total: StrictInt = Field(..., alias="itemsTotal", description="Total number of items.")
    pages_total: StrictInt = Field(..., alias="pagesTotal", description="Total number of pages.")
    types_with_errors: Optional[List[StrictStr]] = Field(None, alias="typesWithErrors", description="Payment method types with errors.")
    __properties = ["_links", "data", "itemsTotal", "pagesTotal", "typesWithErrors"]

    @validator('types_with_errors')
    def types_with_errors_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('alipay', 'amex', 'applepay', 'bcmc', 'blik', 'cartebancaire', 'cup', 'diners', 'directEbanking', 'directdebit_GB', 'discover', 'ebanking_FI', 'eftpos_australia', 'girocard', 'giropay', 'googlepay', 'ideal', 'interac_card', 'jcb', 'klarna', 'klarna_account', 'klarna_paynow', 'maestro', 'mbway', 'mc', 'mobilepay', 'multibanco', 'paypal', 'payshop', 'swish', 'trustly', 'visa', 'wechatpay', 'wechatpay_pos'):
            raise ValueError("must validate the enum values ('alipay', 'amex', 'applepay', 'bcmc', 'blik', 'cartebancaire', 'cup', 'diners', 'directEbanking', 'directdebit_GB', 'discover', 'ebanking_FI', 'eftpos_australia', 'girocard', 'giropay', 'googlepay', 'ideal', 'interac_card', 'jcb', 'klarna', 'klarna_account', 'klarna_paynow', 'maestro', 'mbway', 'mc', 'mobilepay', 'multibanco', 'paypal', 'payshop', 'swish', 'trustly', 'visa', 'wechatpay', 'wechatpay_pos')")
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
    def from_json(cls, json_str: str) -> PaymentMethodResponse:
        """Create an instance of PaymentMethodResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodResponse:
        """Create an instance of PaymentMethodResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentMethodResponse.parse_obj(obj)

        _obj = PaymentMethodResponse.parse_obj({
            "links": PaginationLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "data": [PaymentMethod.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "items_total": obj.get("itemsTotal"),
            "pages_total": obj.get("pagesTotal"),
            "types_with_errors": obj.get("typesWithErrors")
        })
        return _obj
