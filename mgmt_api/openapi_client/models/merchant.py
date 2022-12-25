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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.data_center import DataCenter
from openapi_client.models.merchant_links import MerchantLinks

class Merchant(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[MerchantLinks] = Field(None, alias="_links")
    capture_delay: Optional[StrictStr] = Field(None, alias="captureDelay", description="The [capture delay](https://docs.adyen.com/online-payments/capture#capture-delay) set for the merchant account.  Possible values: * **Immediate** * **Manual** * Number of days from **1** to **29**")
    company_id: Optional[StrictStr] = Field(None, alias="companyId", description="The unique identifier of the company account this merchant belongs to")
    data_centers: Optional[List[DataCenter]] = Field(None, alias="dataCenters", description="List of available data centers.  Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers.")
    default_shopper_interaction: Optional[StrictStr] = Field(None, alias="defaultShopperInteraction", description="The default [`shopperInteraction`](https://docs.adyen.com/api-explorer/#/CheckoutService/v68/post/payments__reqParam_shopperInteraction) value used when processing payments through this merchant account.")
    description: Optional[StrictStr] = Field(None, description="Your description for the merchant account, maximum 300 characters")
    id: Optional[StrictStr] = Field(None, description="The unique identifier of the merchant account.")
    merchant_city: Optional[StrictStr] = Field(None, alias="merchantCity", description="The city where the legal entity of this merchant account is registered.")
    name: Optional[StrictStr] = Field(None, description="The name of the legal entity associated with the merchant account.")
    pricing_plan: Optional[StrictStr] = Field(None, alias="pricingPlan", description="Only applies to merchant accounts managed by Adyen's partners. The name of the pricing plan assigned to the merchant account.")
    primary_settlement_currency: Optional[StrictStr] = Field(None, alias="primarySettlementCurrency", description="The currency of the country where the legal entity of this merchant account is registered. Format: [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, a legal entity based in the United States has USD as the primary settlement currency.")
    reference: Optional[StrictStr] = Field(None, description="Reference of the merchant account.")
    shop_web_address: Optional[StrictStr] = Field(None, alias="shopWebAddress", description="The URL for the ecommerce website used with this merchant account.")
    status: Optional[StrictStr] = Field(None, description="The status of the merchant account.  Possible values:  * **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments. * **Active**: Users can access the merchant account in the Customer Area. If the company account is also **Active**, then payment processing and payouts are enabled. * **InactiveWithModifications**: Users can access the merchant account in the Customer Area. You cannot process new payments but you can still modify payments, for example issue refunds. You can still receive payouts. * **Inactive**: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled. * **Closed**: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled.")
    __properties = ["_links", "captureDelay", "companyId", "dataCenters", "defaultShopperInteraction", "description", "id", "merchantCity", "name", "pricingPlan", "primarySettlementCurrency", "reference", "shopWebAddress", "status"]

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
    def from_json(cls, json_str: str) -> Merchant:
        """Create an instance of Merchant from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_centers (list)
        _items = []
        if self.data_centers:
            for _item in self.data_centers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataCenters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Merchant:
        """Create an instance of Merchant from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Merchant.parse_obj(obj)

        _obj = Merchant.parse_obj({
            "links": MerchantLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "capture_delay": obj.get("captureDelay"),
            "company_id": obj.get("companyId"),
            "data_centers": [DataCenter.from_dict(_item) for _item in obj.get("dataCenters")] if obj.get("dataCenters") is not None else None,
            "default_shopper_interaction": obj.get("defaultShopperInteraction"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "merchant_city": obj.get("merchantCity"),
            "name": obj.get("name"),
            "pricing_plan": obj.get("pricingPlan"),
            "primary_settlement_currency": obj.get("primarySettlementCurrency"),
            "reference": obj.get("reference"),
            "shop_web_address": obj.get("shopWebAddress"),
            "status": obj.get("status")
        })
        return _obj

