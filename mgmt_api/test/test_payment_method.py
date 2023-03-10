# coding: utf-8

"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.payment_method import PaymentMethod  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentMethod(unittest.TestCase):
    """PaymentMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentMethod`
        """
        model = openapi_client.models.payment_method.PaymentMethod()  # noqa: E501
        if include_optional :
            return PaymentMethod(
                allowed = True, 
                apple_pay = openapi_client.models.apple_pay_info.ApplePayInfo(
                    domains = [
                        ''
                        ], ), 
                bcmc = openapi_client.models.bcmc_info.BcmcInfo(
                    enable_bcmc_mobile = True, ), 
                business_line_id = '', 
                cartes_bancaires = openapi_client.models.cartes_bancaires_info.CartesBancairesInfo(
                    siret = '', ), 
                countries = [
                    ''
                    ], 
                currencies = [
                    ''
                    ], 
                enabled = True, 
                giro_pay = openapi_client.models.giro_pay_info.GiroPayInfo(
                    support_email = '', ), 
                google_pay = openapi_client.models.google_pay_info.GooglePayInfo(
                    merchant_id = '0123456789101112131415', ), 
                id = '', 
                klarna = openapi_client.models.klarna_info.KlarnaInfo(
                    auto_capture = True, 
                    dispute_email = '', 
                    region = 'NA', 
                    support_email = '', ), 
                paypal = openapi_client.models.pay_pal_info.PayPalInfo(
                    direct_capture = True, 
                    payer_id = '0123456789101112', 
                    subject = '', ), 
                shopper_interaction = '', 
                sofort = openapi_client.models.sofort_info.SofortInfo(
                    currency_code = '', 
                    logo = '', ), 
                store_id = '', 
                swish = openapi_client.models.swish_info.SwishInfo(
                    swish_number = '0123456789', ), 
                type = '', 
                verification_status = 'valid'
            )
        else :
            return PaymentMethod(
                id = '',
        )
        """

    def testPaymentMethod(self):
        """Test PaymentMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
