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
from openapi_client.models.terminal_orders_response import TerminalOrdersResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestTerminalOrdersResponse(unittest.TestCase):
    """TerminalOrdersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TerminalOrdersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TerminalOrdersResponse`
        """
        model = openapi_client.models.terminal_orders_response.TerminalOrdersResponse()  # noqa: E501
        if include_optional :
            return TerminalOrdersResponse(
                data = [
                    openapi_client.models.terminal_order.TerminalOrder(
                        billing_entity = openapi_client.models.billing_entity.BillingEntity(
                            address = openapi_client.models.address.Address(
                                city = '', 
                                company_name = '', 
                                country = '', 
                                postal_code = '', 
                                state_or_province = '', 
                                street_address = '', 
                                street_address2 = '', ), 
                            email = '', 
                            id = '', 
                            name = '', 
                            tax_id = '', ), 
                        customer_order_reference = '', 
                        id = '', 
                        items = [
                            openapi_client.models.order_item.OrderItem(
                                id = '', 
                                name = '', 
                                quantity = 56, )
                            ], 
                        order_date = '', 
                        shipping_location = openapi_client.models.shipping_location.ShippingLocation(
                            contact = openapi_client.models.contact.Contact(
                                email = '', 
                                first_name = '', 
                                infix = '', 
                                last_name = '', 
                                phone_number = '', ), 
                            id = '', 
                            name = '', ), 
                        status = '', 
                        tracking_url = '', )
                    ]
            )
        else :
            return TerminalOrdersResponse(
        )
        """

    def testTerminalOrdersResponse(self):
        """Test TerminalOrdersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
