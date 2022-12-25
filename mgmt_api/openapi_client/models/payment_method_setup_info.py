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
from openapi_client.models.apple_pay_info import ApplePayInfo
from openapi_client.models.bcmc_info import BcmcInfo
from openapi_client.models.cartes_bancaires_info import CartesBancairesInfo
from openapi_client.models.giro_pay_info import GiroPayInfo
from openapi_client.models.google_pay_info import GooglePayInfo
from openapi_client.models.klarna_info import KlarnaInfo
from openapi_client.models.pay_pal_info import PayPalInfo
from openapi_client.models.sofort_info import SofortInfo
from openapi_client.models.swish_info import SwishInfo

class PaymentMethodSetupInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    apple_pay: Optional[ApplePayInfo] = Field(None, alias="applePay")
    bcmc: Optional[BcmcInfo] = None
    business_line_id: Optional[StrictStr] = Field(None, alias="businessLineId", description="The unique identifier of the business line.")
    cartes_bancaires: Optional[CartesBancairesInfo] = Field(None, alias="cartesBancaires")
    countries: Optional[List[StrictStr]] = Field(None, description="The list of countries where a payment method is available. By default, all countries supported by the payment method.")
    currencies: Optional[List[StrictStr]] = Field(None, description="The list of currencies that a payment method supports. By default, all currencies supported by the payment method.")
    giro_pay: Optional[GiroPayInfo] = Field(None, alias="giroPay")
    google_pay: Optional[GooglePayInfo] = Field(None, alias="googlePay")
    klarna: Optional[KlarnaInfo] = None
    paypal: Optional[PayPalInfo] = None
    shopper_interaction: Optional[StrictStr] = Field(None, alias="shopperInteraction", description="The sales channel. Required if the merchant account does not have a sales channel. When you provide this field, it overrides the default sales channel set on the merchant account.  Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**. ")
    sofort: Optional[SofortInfo] = None
    store_id: Optional[StrictStr] = Field(None, alias="storeId", description="The ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/post/stores__resParam_id), if any.")
    swish: Optional[SwishInfo] = None
    type: StrictStr = Field(..., description="Payment method [variant](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).")
    __properties = ["applePay", "bcmc", "businessLineId", "cartesBancaires", "countries", "currencies", "giroPay", "googlePay", "klarna", "paypal", "shopperInteraction", "sofort", "storeId", "swish", "type"]

    @validator('shopper_interaction')
    def shopper_interaction_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('eCommerce', 'pos', 'moto', 'contAuth'):
            raise ValueError("must validate the enum values ('eCommerce', 'pos', 'moto', 'contAuth')")
        return v

    @validator('type')
    def type_validate_enum(cls, v):
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
    def from_json(cls, json_str: str) -> PaymentMethodSetupInfo:
        """Create an instance of PaymentMethodSetupInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of apple_pay
        if self.apple_pay:
            _dict['applePay'] = self.apple_pay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bcmc
        if self.bcmc:
            _dict['bcmc'] = self.bcmc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cartes_bancaires
        if self.cartes_bancaires:
            _dict['cartesBancaires'] = self.cartes_bancaires.to_dict()
        # override the default output from pydantic by calling `to_dict()` of giro_pay
        if self.giro_pay:
            _dict['giroPay'] = self.giro_pay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_pay
        if self.google_pay:
            _dict['googlePay'] = self.google_pay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of klarna
        if self.klarna:
            _dict['klarna'] = self.klarna.to_dict()
        # override the default output from pydantic by calling `to_dict()` of paypal
        if self.paypal:
            _dict['paypal'] = self.paypal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sofort
        if self.sofort:
            _dict['sofort'] = self.sofort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of swish
        if self.swish:
            _dict['swish'] = self.swish.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodSetupInfo:
        """Create an instance of PaymentMethodSetupInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentMethodSetupInfo.parse_obj(obj)

        _obj = PaymentMethodSetupInfo.parse_obj({
            "apple_pay": ApplePayInfo.from_dict(obj.get("applePay")) if obj.get("applePay") is not None else None,
            "bcmc": BcmcInfo.from_dict(obj.get("bcmc")) if obj.get("bcmc") is not None else None,
            "business_line_id": obj.get("businessLineId"),
            "cartes_bancaires": CartesBancairesInfo.from_dict(obj.get("cartesBancaires")) if obj.get("cartesBancaires") is not None else None,
            "countries": obj.get("countries"),
            "currencies": obj.get("currencies"),
            "giro_pay": GiroPayInfo.from_dict(obj.get("giroPay")) if obj.get("giroPay") is not None else None,
            "google_pay": GooglePayInfo.from_dict(obj.get("googlePay")) if obj.get("googlePay") is not None else None,
            "klarna": KlarnaInfo.from_dict(obj.get("klarna")) if obj.get("klarna") is not None else None,
            "paypal": PayPalInfo.from_dict(obj.get("paypal")) if obj.get("paypal") is not None else None,
            "shopper_interaction": obj.get("shopperInteraction"),
            "sofort": SofortInfo.from_dict(obj.get("sofort")) if obj.get("sofort") is not None else None,
            "store_id": obj.get("storeId"),
            "swish": SwishInfo.from_dict(obj.get("swish")) if obj.get("swish") is not None else None,
            "type": obj.get("type")
        })
        return _obj

