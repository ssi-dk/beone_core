"""
    Bio API

    REST API for controlling bioinformatic calculations  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from web.src.services.bio_api.openapi.api_client import ApiClient, Endpoint as _Endpoint
from web.src.services.bio_api.openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from web.src.services.bio_api.openapi.model.common_post_response import CommonPOSTResponse
from web.src.services.bio_api.openapi.model.hc_tree_calc_get_response import HCTreeCalcGETResponse
from web.src.services.bio_api.openapi.model.hc_tree_calc_request import HCTreeCalcRequest
from web.src.services.bio_api.openapi.model.http_validation_error import HTTPValidationError
from web.src.services.bio_api.openapi.model.message import Message


class TreesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __hc_tree_from_dmx_job_v1_trees_post(
            self,
            hc_tree_calc_request,
            **kwargs
        ):
            """Hc Tree From Dmx Job  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.hc_tree_from_dmx_job_v1_trees_post(hc_tree_calc_request, async_req=True)
            >>> result = thread.get()

            Args:
                hc_tree_calc_request (HCTreeCalcRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CommonPOSTResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['hc_tree_calc_request'] = \
                hc_tree_calc_request
            return self.call_with_http_info(**kwargs)

        self.hc_tree_from_dmx_job_v1_trees_post = _Endpoint(
            settings={
                'response_type': (CommonPOSTResponse,),
                'auth': [],
                'endpoint_path': '/v1/trees',
                'operation_id': 'hc_tree_from_dmx_job_v1_trees_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'hc_tree_calc_request',
                ],
                'required': [
                    'hc_tree_calc_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'hc_tree_calc_request':
                        (HCTreeCalcRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'hc_tree_calc_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__hc_tree_from_dmx_job_v1_trees_post
        )

        def __hc_tree_result_v1_trees_tc_id_get(
            self,
            tc_id,
            **kwargs
        ):
            """Hc Tree Result  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.hc_tree_result_v1_trees_tc_id_get(tc_id, async_req=True)
            >>> result = thread.get()

            Args:
                tc_id (str):

            Keyword Args:
                level (str): [optional] if omitted the server will use the default value of "full"
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                HCTreeCalcGETResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['tc_id'] = \
                tc_id
            return self.call_with_http_info(**kwargs)

        self.hc_tree_result_v1_trees_tc_id_get = _Endpoint(
            settings={
                'response_type': (HCTreeCalcGETResponse,),
                'auth': [],
                'endpoint_path': '/v1/trees/{tc_id}',
                'operation_id': 'hc_tree_result_v1_trees_tc_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tc_id',
                    'level',
                ],
                'required': [
                    'tc_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tc_id':
                        (str,),
                    'level':
                        (str,),
                },
                'attribute_map': {
                    'tc_id': 'tc_id',
                    'level': 'level',
                },
                'location_map': {
                    'tc_id': 'path',
                    'level': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__hc_tree_result_v1_trees_tc_id_get
        )
