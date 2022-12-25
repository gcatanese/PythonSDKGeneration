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
from openapi_client.models.create_company_webhook_request import CreateCompanyWebhookRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestCreateCompanyWebhookRequest(unittest.TestCase):
    """CreateCompanyWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCompanyWebhookRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCompanyWebhookRequest`
        """
        model = openapi_client.models.create_company_webhook_request.CreateCompanyWebhookRequest()  # noqa: E501
        if include_optional :
            return CreateCompanyWebhookRequest(
                accepts_expired_certificate = True, 
                accepts_self_signed_certificate = True, 
                accepts_untrusted_root_certificate = True, 
                active = True, 
                additional_settings = openapi_client.models.additional_settings.AdditionalSettings(
                    include_event_codes = [
                        ''
                        ], 
                    properties = {
                        'key' : True
                        }, ), 
                communication_format = 'SOAP', 
                description = '', 
                filter_merchant_account_type = 'EXCLUDE_LIST', 
                filter_merchant_accounts = [
                    ''
                    ], 
                network_type = 'LOCAL', 
                password = '', 
                populate_soap_action_header = True, 
                ssl_version = 'TLSv1.2', 
                type = '', 
                url = 'http://www.adyen.com', 
                username = ''
            )
        else :
            return CreateCompanyWebhookRequest(
                active = True,
                communication_format = 'SOAP',
                filter_merchant_account_type = 'EXCLUDE_LIST',
                filter_merchant_accounts = [
                    ''
                    ],
                type = '',
                url = 'http://www.adyen.com',
        )
        """

    def testCreateCompanyWebhookRequest(self):
        """Test CreateCompanyWebhookRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
