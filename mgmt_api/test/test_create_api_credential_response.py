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
from openapi_client.models.create_api_credential_response import CreateApiCredentialResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestCreateApiCredentialResponse(unittest.TestCase):
    """CreateApiCredentialResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateApiCredentialResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateApiCredentialResponse`
        """
        model = openapi_client.models.create_api_credential_response.CreateApiCredentialResponse()  # noqa: E501
        if include_optional :
            return CreateApiCredentialResponse(
                links = openapi_client.models.api_credential_links.ApiCredentialLinks(
                    allowed_origins = openapi_client.models.links_element.LinksElement(
                        href = '', ), 
                    company = openapi_client.models.links_element.LinksElement(
                        href = '', ), 
                    generate_api_key = , 
                    generate_client_key = , 
                    merchant = , 
                    self = , ), 
                active = True, 
                allowed_ip_addresses = [
                    ''
                    ], 
                allowed_origins = [
                    openapi_client.models.allowed_origin.AllowedOrigin(
                        _links = openapi_client.models.links.Links(
                            self = openapi_client.models.links_element.LinksElement(
                                href = '', ), ), 
                        domain = 'https://adyen.com', 
                        id = '', )
                    ], 
                api_key = '', 
                client_key = '', 
                description = '', 
                id = '', 
                password = '', 
                roles = [
                    ''
                    ], 
                username = ''
            )
        else :
            return CreateApiCredentialResponse(
                active = True,
                allowed_ip_addresses = [
                    ''
                    ],
                api_key = '',
                client_key = '',
                id = '',
                password = '',
                roles = [
                    ''
                    ],
                username = '',
        )
        """

    def testCreateApiCredentialResponse(self):
        """Test CreateApiCredentialResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
