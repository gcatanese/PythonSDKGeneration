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
from openapi_client.api.terminal_actions_company_level_api import TerminalActionsCompanyLevelApi  # noqa: E501
from openapi_client.rest import ApiException


class TestTerminalActionsCompanyLevelApi(unittest.TestCase):
    """TerminalActionsCompanyLevelApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.terminal_actions_company_level_api.TerminalActionsCompanyLevelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_companies_company_id_android_apps(self):
        """Test case for get_companies_company_id_android_apps

        Get a list of Android apps  # noqa: E501
        """
        pass

    def test_get_companies_company_id_android_certificates(self):
        """Test case for get_companies_company_id_android_certificates

        Get a list of Android certificates  # noqa: E501
        """
        pass

    def test_get_companies_company_id_terminal_actions(self):
        """Test case for get_companies_company_id_terminal_actions

        Get a list of terminal actions  # noqa: E501
        """
        pass

    def test_get_companies_company_id_terminal_actions_action_id(self):
        """Test case for get_companies_company_id_terminal_actions_action_id

        Get terminal action  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
