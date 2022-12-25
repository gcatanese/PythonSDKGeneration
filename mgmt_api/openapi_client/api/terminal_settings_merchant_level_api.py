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

from pydantic import Field, StrictStr

from typing import Optional

from openapi_client.models.logo import Logo
from openapi_client.models.terminal_settings import TerminalSettings

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TerminalSettingsMerchantLevelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_merchants_merchant_id_terminal_logos(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], model : Annotated[Optional[StrictStr], Field(description="The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.")] = None, **kwargs) -> Logo:  # noqa: E501
        """Get the terminal logo  # noqa: E501

        Returns the logo that is configured for a specific payment terminal model at the merchant account identified in the path. You must specify the terminal model as a query parameter.  The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchants_merchant_id_terminal_logos(merchant_id, model, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
        :type model: str
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
        :rtype: Logo
        """
        kwargs['_return_http_data_only'] = True
        return self.get_merchants_merchant_id_terminal_logos_with_http_info(merchant_id, model, **kwargs)  # noqa: E501

    @validate_arguments
    def get_merchants_merchant_id_terminal_logos_with_http_info(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], model : Annotated[Optional[StrictStr], Field(description="The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.")] = None, **kwargs):  # noqa: E501
        """Get the terminal logo  # noqa: E501

        Returns the logo that is configured for a specific payment terminal model at the merchant account identified in the path. You must specify the terminal model as a query parameter.  The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchants_merchant_id_terminal_logos_with_http_info(merchant_id, model, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param model: The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
        :type model: str
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
        :rtype: tuple(Logo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id',
            'model'
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
                    " to method get_merchants_merchant_id_terminal_logos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchantId'] = _params['merchant_id']

        # process the query parameters
        _query_params = []
        if _params.get('model') is not None:  # noqa: E501
            _query_params.append(('model', _params['model']))

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
            '200': "Logo",
            '204': None,
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/merchants/{merchantId}/terminalLogos', 'GET',
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
    def get_merchants_merchant_id_terminal_settings(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], **kwargs) -> TerminalSettings:  # noqa: E501
        """Get terminal settings  # noqa: E501

        Returns the payment terminal settings that are configured for the merchant account identified in the path. These settings apply to all terminals under the merchant account unless different values are configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchants_merchant_id_terminal_settings(merchant_id, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
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
        :rtype: TerminalSettings
        """
        kwargs['_return_http_data_only'] = True
        return self.get_merchants_merchant_id_terminal_settings_with_http_info(merchant_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_merchants_merchant_id_terminal_settings_with_http_info(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], **kwargs):  # noqa: E501
        """Get terminal settings  # noqa: E501

        Returns the payment terminal settings that are configured for the merchant account identified in the path. These settings apply to all terminals under the merchant account unless different values are configured at a lower level (store or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_merchants_merchant_id_terminal_settings_with_http_info(merchant_id, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
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
        :rtype: tuple(TerminalSettings, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id'
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
                    " to method get_merchants_merchant_id_terminal_settings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchantId'] = _params['merchant_id']

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
            '200': "TerminalSettings",
            '204': None,
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/merchants/{merchantId}/terminalSettings', 'GET',
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
    def patch_merchants_merchant_id_terminal_logos(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], model : Annotated[Optional[StrictStr], Field(description="The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.")] = None, logo : Optional[Logo] = None, **kwargs) -> Logo:  # noqa: E501
        """Update the terminal logo  # noqa: E501

        Updates the logo for a specific payment terminal model at the merchant account identified in the path. You must specify the terminal model as a query parameter. You can update the logo for only one terminal model at a time.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the company account, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_merchants_merchant_id_terminal_logos(merchant_id, model, logo, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
        :type model: str
        :param logo:
        :type logo: Logo
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
        :rtype: Logo
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_merchants_merchant_id_terminal_logos_with_http_info(merchant_id, model, logo, **kwargs)  # noqa: E501

    @validate_arguments
    def patch_merchants_merchant_id_terminal_logos_with_http_info(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], model : Annotated[Optional[StrictStr], Field(description="The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.")] = None, logo : Optional[Logo] = None, **kwargs):  # noqa: E501
        """Update the terminal logo  # noqa: E501

        Updates the logo for a specific payment terminal model at the merchant account identified in the path. You must specify the terminal model as a query parameter. You can update the logo for only one terminal model at a time.  This logo applies to all terminals of the specified model under the merchant account, unless a different logo is configured at a lower level (store or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the company account, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_merchants_merchant_id_terminal_logos_with_http_info(merchant_id, model, logo, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param model: The terminal model. Allowed values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
        :type model: str
        :param logo:
        :type logo: Logo
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
        :rtype: tuple(Logo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id',
            'model',
            'logo'
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
                    " to method patch_merchants_merchant_id_terminal_logos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchantId'] = _params['merchant_id']

        # process the query parameters
        _query_params = []
        if _params.get('model') is not None:  # noqa: E501
            _query_params.append(('model', _params['model']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['logo']:
            _body_params = _params['logo']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        _response_types_map = {
            '200': "Logo",
            '204': None,
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/merchants/{merchantId}/terminalLogos', 'PATCH',
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
    def patch_merchants_merchant_id_terminal_settings(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], terminal_settings : Optional[TerminalSettings] = None, **kwargs) -> TerminalSettings:  # noqa: E501
        """Update terminal settings  # noqa: E501

        Updates payment terminal settings for the merchant account identified in the path. These settings apply to all terminals under the merchant account, unless different values are configured at a lower level (store or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_merchants_merchant_id_terminal_settings(merchant_id, terminal_settings, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param terminal_settings:
        :type terminal_settings: TerminalSettings
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
        :rtype: TerminalSettings
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_merchants_merchant_id_terminal_settings_with_http_info(merchant_id, terminal_settings, **kwargs)  # noqa: E501

    @validate_arguments
    def patch_merchants_merchant_id_terminal_settings_with_http_info(self, merchant_id : Annotated[StrictStr, Field(..., description="The unique identifier of the merchant account.")], terminal_settings : Optional[TerminalSettings] = None, **kwargs):  # noqa: E501
        """Update terminal settings  # noqa: E501

        Updates payment terminal settings for the merchant account identified in the path. These settings apply to all terminals under the merchant account, unless different values are configured at a lower level (store or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don't want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_merchants_merchant_id_terminal_settings_with_http_info(merchant_id, terminal_settings, async_req=True)
        >>> result = thread.get()

        :param merchant_id: The unique identifier of the merchant account. (required)
        :type merchant_id: str
        :param terminal_settings:
        :type terminal_settings: TerminalSettings
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
        :rtype: tuple(TerminalSettings, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'merchant_id',
            'terminal_settings'
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
                    " to method patch_merchants_merchant_id_terminal_settings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['merchant_id']:
            _path_params['merchantId'] = _params['merchant_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['terminal_settings']:
            _body_params = _params['terminal_settings']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'BasicAuth']  # noqa: E501

        _response_types_map = {
            '200': "TerminalSettings",
            '204': None,
            '400': "RestServiceError",
            '401': "RestServiceError",
            '403': "RestServiceError",
            '422': "RestServiceError",
            '500': "RestServiceError",
        }

        return self.api_client.call_api(
            '/merchants/{merchantId}/terminalSettings', 'PATCH',
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
