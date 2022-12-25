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

import openapi_client
from openapi_client.api.allowed_origins_merchant_level_api import AllowedOriginsMerchantLevelApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAllowedOriginsMerchantLevelApi(unittest.TestCase):
    """AllowedOriginsMerchantLevelApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.allowed_origins_merchant_level_api.AllowedOriginsMerchantLevelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(self):
        """Test case for delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

        Delete an allowed origin  # noqa: E501
        """
        pass

    def test_get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(self):
        """Test case for get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

        Get a list of allowed origins  # noqa: E501
        """
        pass

    def test_get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(self):
        """Test case for get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

        Get an allowed origin  # noqa: E501
        """
        pass

    def test_post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(self):
        """Test case for post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

        Create an allowed origin  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()