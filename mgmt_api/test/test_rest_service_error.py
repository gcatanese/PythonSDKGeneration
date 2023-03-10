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
from openapi_client.models.rest_service_error import RestServiceError  # noqa: E501
from openapi_client.rest import ApiException

class TestRestServiceError(unittest.TestCase):
    """RestServiceError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RestServiceError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestServiceError`
        """
        model = openapi_client.models.rest_service_error.RestServiceError()  # noqa: E501
        if include_optional :
            return RestServiceError(
                detail = '', 
                error_code = '', 
                instance = '', 
                invalid_fields = [
                    openapi_client.models.invalid_field.InvalidField(
                        message = '', 
                        name = '', 
                        value = '', )
                    ], 
                request_id = '', 
                response = openapi_client.models.json_object.JSONObject(
                    paths = [
                        openapi_client.models.json_path.JSONPath(
                            content = [
                                ''
                                ], )
                        ], 
                    root_path = openapi_client.models.json_path.JSONPath(), ), 
                status = 56, 
                title = '', 
                type = ''
            )
        else :
            return RestServiceError(
                detail = '',
                error_code = '',
                status = 56,
                title = '',
                type = '',
        )
        """

    def testRestServiceError(self):
        """Test RestServiceError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
