# coding: utf-8

"""
    Binance Public Spot API

    OpenAPI Specifications for the Binance Public Spot API  API documents:   - [https://github.com/binance/binance-spot-api-docs](https://github.com/binance/binance-spot-api-docs)   - [https://binance-docs.github.io/apidocs/spot/en](https://binance-docs.github.io/apidocs/spot/en)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from binance_spot.api_client import ApiClient


class FuturesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sapi_v1_futures_hist_data_link_get(self, symbol, data_type, timestamp, signature, **kwargs):  # noqa: E501
        """Get Future TickLevel Orderbook Historical Data Download Link (USER_DATA)  # noqa: E501

        Weight(IP): 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_hist_data_link_get(symbol, data_type, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: (required)
        :param str data_type: (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int start_time: UTC timestamp in ms
        :param int end_time: UTC timestamp in ms
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200152
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sapi_v1_futures_hist_data_link_get_with_http_info(symbol, data_type, timestamp, signature, **kwargs)  # noqa: E501
        else:
            (data) = self.sapi_v1_futures_hist_data_link_get_with_http_info(symbol, data_type, timestamp, signature, **kwargs)  # noqa: E501
            return data

    def sapi_v1_futures_hist_data_link_get_with_http_info(self, symbol, data_type, timestamp, signature, **kwargs):  # noqa: E501
        """Get Future TickLevel Orderbook Historical Data Download Link (USER_DATA)  # noqa: E501

        Weight(IP): 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_hist_data_link_get_with_http_info(symbol, data_type, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: (required)
        :param str data_type: (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int start_time: UTC timestamp in ms
        :param int end_time: UTC timestamp in ms
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200152
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'data_type', 'timestamp', 'signature', 'start_time', 'end_time', 'recv_window']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sapi_v1_futures_hist_data_link_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `sapi_v1_futures_hist_data_link_get`")  # noqa: E501
        # verify the required parameter 'data_type' is set
        if ('data_type' not in params or
                params['data_type'] is None):
            raise ValueError("Missing the required parameter `data_type` when calling `sapi_v1_futures_hist_data_link_get`")  # noqa: E501
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in params or
                params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `sapi_v1_futures_hist_data_link_get`")  # noqa: E501
        # verify the required parameter 'signature' is set
        if ('signature' not in params or
                params['signature'] is None):
            raise ValueError("Missing the required parameter `signature` when calling `sapi_v1_futures_hist_data_link_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'symbol' in params:
            query_params.append(('symbol', params['symbol']))  # noqa: E501
        if 'data_type' in params:
            query_params.append(('dataType', params['data_type']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'recv_window' in params:
            query_params.append(('recvWindow', params['recv_window']))  # noqa: E501
        if 'timestamp' in params:
            query_params.append(('timestamp', params['timestamp']))  # noqa: E501
        if 'signature' in params:
            query_params.append(('signature', params['signature']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sapi/v1/futures/histDataLink', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200152',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sapi_v1_futures_transfer_get(self, asset, start_time, timestamp, signature, **kwargs):  # noqa: E501
        """Get Future Account Transaction History List (USER_DATA)  # noqa: E501

        Weight(IP): 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_transfer_get(asset, start_time, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: (required)
        :param int start_time: UTC timestamp in ms (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int end_time: UTC timestamp in ms
        :param int current: Current querying page. Start from 1. Default:1
        :param int size: Default:10 Max:100
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200150
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sapi_v1_futures_transfer_get_with_http_info(asset, start_time, timestamp, signature, **kwargs)  # noqa: E501
        else:
            (data) = self.sapi_v1_futures_transfer_get_with_http_info(asset, start_time, timestamp, signature, **kwargs)  # noqa: E501
            return data

    def sapi_v1_futures_transfer_get_with_http_info(self, asset, start_time, timestamp, signature, **kwargs):  # noqa: E501
        """Get Future Account Transaction History List (USER_DATA)  # noqa: E501

        Weight(IP): 10  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_transfer_get_with_http_info(asset, start_time, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: (required)
        :param int start_time: UTC timestamp in ms (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int end_time: UTC timestamp in ms
        :param int current: Current querying page. Start from 1. Default:1
        :param int size: Default:10 Max:100
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200150
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset', 'start_time', 'timestamp', 'signature', 'end_time', 'current', 'size', 'recv_window']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sapi_v1_futures_transfer_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset' is set
        if ('asset' not in params or
                params['asset'] is None):
            raise ValueError("Missing the required parameter `asset` when calling `sapi_v1_futures_transfer_get`")  # noqa: E501
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params or
                params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `sapi_v1_futures_transfer_get`")  # noqa: E501
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in params or
                params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `sapi_v1_futures_transfer_get`")  # noqa: E501
        # verify the required parameter 'signature' is set
        if ('signature' not in params or
                params['signature'] is None):
            raise ValueError("Missing the required parameter `signature` when calling `sapi_v1_futures_transfer_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset' in params:
            query_params.append(('asset', params['asset']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'current' in params:
            query_params.append(('current', params['current']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'recv_window' in params:
            query_params.append(('recvWindow', params['recv_window']))  # noqa: E501
        if 'timestamp' in params:
            query_params.append(('timestamp', params['timestamp']))  # noqa: E501
        if 'signature' in params:
            query_params.append(('signature', params['signature']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sapi/v1/futures/transfer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200150',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sapi_v1_futures_transfer_post(self, asset, amount, type, timestamp, signature, **kwargs):  # noqa: E501
        """New Future Account Transfer (USER_DATA)  # noqa: E501

        Execute transfer between spot account and futures account.  Weight(IP): 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_transfer_post(asset, amount, type, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: (required)
        :param float amount: (required)
        :param int type: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures account to spot account. (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200151
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sapi_v1_futures_transfer_post_with_http_info(asset, amount, type, timestamp, signature, **kwargs)  # noqa: E501
        else:
            (data) = self.sapi_v1_futures_transfer_post_with_http_info(asset, amount, type, timestamp, signature, **kwargs)  # noqa: E501
            return data

    def sapi_v1_futures_transfer_post_with_http_info(self, asset, amount, type, timestamp, signature, **kwargs):  # noqa: E501
        """New Future Account Transfer (USER_DATA)  # noqa: E501

        Execute transfer between spot account and futures account.  Weight(IP): 1  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sapi_v1_futures_transfer_post_with_http_info(asset, amount, type, timestamp, signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset: (required)
        :param float amount: (required)
        :param int type: 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures account to spot account. (required)
        :param int timestamp: UTC timestamp in ms (required)
        :param str signature: Signature (required)
        :param int recv_window: The value cannot be greater than 60000
        :return: InlineResponse200151
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset', 'amount', 'type', 'timestamp', 'signature', 'recv_window']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sapi_v1_futures_transfer_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset' is set
        if ('asset' not in params or
                params['asset'] is None):
            raise ValueError("Missing the required parameter `asset` when calling `sapi_v1_futures_transfer_post`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if ('amount' not in params or
                params['amount'] is None):
            raise ValueError("Missing the required parameter `amount` when calling `sapi_v1_futures_transfer_post`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `sapi_v1_futures_transfer_post`")  # noqa: E501
        # verify the required parameter 'timestamp' is set
        if ('timestamp' not in params or
                params['timestamp'] is None):
            raise ValueError("Missing the required parameter `timestamp` when calling `sapi_v1_futures_transfer_post`")  # noqa: E501
        # verify the required parameter 'signature' is set
        if ('signature' not in params or
                params['signature'] is None):
            raise ValueError("Missing the required parameter `signature` when calling `sapi_v1_futures_transfer_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset' in params:
            query_params.append(('asset', params['asset']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'recv_window' in params:
            query_params.append(('recvWindow', params['recv_window']))  # noqa: E501
        if 'timestamp' in params:
            query_params.append(('timestamp', params['timestamp']))  # noqa: E501
        if 'signature' in params:
            query_params.append(('signature', params['signature']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sapi/v1/futures/transfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200151',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)