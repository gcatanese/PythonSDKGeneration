# coding: utf-8

"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from openapi_client.models.company import Company
from openapi_client.models.list_company_response import ListCompanyResponse
from openapi_client.models.list_merchant_response import ListMerchantResponse

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AccountCompanyLevelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_companies(self, page_number : Annotated[Optional[StrictInt], Field(description="The number of the page to fetch.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of items to have on a page, maximum 100. The default is 10 items on a page.")] = None, **kwargs) -> ListCompanyResponse:  # noqa: E501
        """Get a list of company accounts  # noqa: E501

        Returns the list of company accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies(page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param page_number: The number of the page to fetch.
        :type page_number: int
        :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListCompanyResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_companies_with_http_info(page_number, page_size, **kwargs)  # noqa: E501

    @validate_arguments
    def get_companies_with_http_info(self, page_number : Annotated[Optional[StrictInt], Field(description="The number of the page to fetch.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of items to have on a page, maximum 100. The default is 10 items on a page.")] = None, **kwargs):  # noqa: E501
        """Get a list of company accounts  # noqa: E501

        Returns the list of company accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies_with_http_info(page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param page_number: The number of the page to fetch.
        :type page_number: int
        :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListCompanyResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page_number',
            'page_size'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_companies" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('pageNumber', _params['page_number']))
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        _response_types_map = {
            '200': "ListCompanyResponse",
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/companies', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_companies_company_id(self, company_id : Annotated[StrictStr, Field(..., description="The unique identifier of the company account.")], **kwargs) -> Company:  # noqa: E501
        """Get a company account  # noqa: E501

        Returns the company account specified in the path. Your API credential must have access to the company account.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies_company_id(company_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The unique identifier of the company account. (required)
        :type company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Company
        """
        kwargs['_return_http_data_only'] = True
        return self.get_companies_company_id_with_http_info(company_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_companies_company_id_with_http_info(self, company_id : Annotated[StrictStr, Field(..., description="The unique identifier of the company account.")], **kwargs):  # noqa: E501
        """Get a company account  # noqa: E501

        Returns the company account specified in the path. Your API credential must have access to the company account.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies_company_id_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The unique identifier of the company account. (required)
        :type company_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Company, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'company_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_companies_company_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['company_id']:
            _path_params['companyId'] = _params['company_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        _response_types_map = {
            '200': "Company",
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/companies/{companyId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_companies_company_id_merchants(self, company_id : Annotated[StrictStr, Field(..., description="The unique identifier of the company account.")], page_number : Annotated[Optional[StrictInt], Field(description="The number of the page to fetch.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of items to have on a page, maximum 100. The default is 10 items on a page.")] = None, **kwargs) -> ListMerchantResponse:  # noqa: E501
        """Get a list of merchant accounts  # noqa: E501

        Returns the list of merchant accounts under the company account specified in the path. The list only includes merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies_company_id_merchants(company_id, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param company_id: The unique identifier of the company account. (required)
        :type company_id: str
        :param page_number: The number of the page to fetch.
        :type page_number: int
        :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListMerchantResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_companies_company_id_merchants_with_http_info(company_id, page_number, page_size, **kwargs)  # noqa: E501

    @validate_arguments
    def get_companies_company_id_merchants_with_http_info(self, company_id : Annotated[StrictStr, Field(..., description="The unique identifier of the company account.")], page_number : Annotated[Optional[StrictInt], Field(description="The number of the page to fetch.")] = None, page_size : Annotated[Optional[StrictInt], Field(description="The number of items to have on a page, maximum 100. The default is 10 items on a page.")] = None, **kwargs):  # noqa: E501
        """Get a list of merchant accounts  # noqa: E501

        Returns the list of merchant accounts under the company account specified in the path. The list only includes merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_companies_company_id_merchants_with_http_info(company_id, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param company_id: The unique identifier of the company account. (required)
        :type company_id: str
        :param page_number: The number of the page to fetch.
        :type page_number: int
        :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListMerchantResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'company_id',
            'page_number',
            'page_size'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_companies_company_id_merchants" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['company_id']:
            _path_params['companyId'] = _params['company_id']

        # process the query parameters
        _query_params = []
        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('pageNumber', _params['page_number']))
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        _response_types_map = {
            '200': "ListMerchantResponse",
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/companies/{companyId}/merchants', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
