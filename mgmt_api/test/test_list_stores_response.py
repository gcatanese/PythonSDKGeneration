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
from openapi_client.models.list_stores_response import ListStoresResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestListStoresResponse(unittest.TestCase):
    """ListStoresResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListStoresResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListStoresResponse`
        """
        model = openapi_client.models.list_stores_response.ListStoresResponse()  # noqa: E501
        if include_optional :
            return ListStoresResponse(
                links = openapi_client.models.pagination_links.PaginationLinks(
                    first = openapi_client.models.links_element.LinksElement(
                        href = '', ), 
                    last = openapi_client.models.links_element.LinksElement(
                        href = '', ), 
                    next = , 
                    prev = , 
                    self = , ), 
                data = [
                    openapi_client.models.store.Store(
                        _links = openapi_client.models.links.Links(
                            self = openapi_client.models.links_element.LinksElement(
                                href = '', ), ), 
                        address = openapi_client.models.address_2.Address-2(
                            city = '', 
                            country = '', 
                            line1 = '', 
                            line2 = '', 
                            line3 = '', 
                            postal_code = '', 
                            state_or_province = '', ), 
                        business_line_ids = [
                            ''
                            ], 
                        description = '', 
                        external_reference_id = '', 
                        id = '', 
                        merchant_id = '', 
                        phone_number = '', 
                        reference = '', 
                        shopper_statement = '', 
                        split_configuration = openapi_client.models.store_split_configuration.StoreSplitConfiguration(
                            balance_account_id = '', 
                            split_configuration_id = '', ), 
                        status = 'active', )
                    ], 
                items_total = 56, 
                pages_total = 56
            )
        else :
            return ListStoresResponse(
                items_total = 56,
                pages_total = 56,
        )
        """

    def testListStoresResponse(self):
        """Test ListStoresResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()