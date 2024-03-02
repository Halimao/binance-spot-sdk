# coding: utf-8

"""
    Binance Public Spot API

    OpenAPI Specifications for the Binance Public Spot API  API documents:   - [https://github.com/binance/binance-spot-api-docs](https://github.com/binance/binance-spot-api-docs)   - [https://binance-docs.github.io/apidocs/spot/en](https://binance-docs.github.io/apidocs/spot/en)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import binance_spot
from binance_spot.api.market_api import MarketApi  # noqa: E501
from binance_spot.rest import ApiException


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self):
        self.api = MarketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v3_agg_trades_get(self):
        """Test case for api_v3_agg_trades_get

        Compressed/Aggregate Trades List  # noqa: E501
        """
        pass

    def test_api_v3_avg_price_get(self):
        """Test case for api_v3_avg_price_get

        Current Average Price  # noqa: E501
        """
        pass

    def test_api_v3_depth_get(self):
        """Test case for api_v3_depth_get

        Order Book  # noqa: E501
        """
        pass

    def test_api_v3_exchange_info_get(self):
        """Test case for api_v3_exchange_info_get

        Exchange Information  # noqa: E501
        """
        pass

    def test_api_v3_historical_trades_get(self):
        """Test case for api_v3_historical_trades_get

        Old Trade Lookup  # noqa: E501
        """
        pass

    def test_api_v3_klines_get(self):
        """Test case for api_v3_klines_get

        Kline/Candlestick Data  # noqa: E501
        """
        pass

    def test_api_v3_ping_get(self):
        """Test case for api_v3_ping_get

        Test Connectivity  # noqa: E501
        """
        pass

    def test_api_v3_ticker24hr_get(self):
        """Test case for api_v3_ticker24hr_get

        24hr Ticker Price Change Statistics  # noqa: E501
        """
        pass

    def test_api_v3_ticker_book_ticker_get(self):
        """Test case for api_v3_ticker_book_ticker_get

        Symbol Order Book Ticker  # noqa: E501
        """
        pass

    def test_api_v3_ticker_get(self):
        """Test case for api_v3_ticker_get

        Rolling window price change statistics  # noqa: E501
        """
        pass

    def test_api_v3_ticker_price_get(self):
        """Test case for api_v3_ticker_price_get

        Symbol Price Ticker  # noqa: E501
        """
        pass

    def test_api_v3_time_get(self):
        """Test case for api_v3_time_get

        Check Server Time  # noqa: E501
        """
        pass

    def test_api_v3_trades_get(self):
        """Test case for api_v3_trades_get

        Recent Trades List  # noqa: E501
        """
        pass

    def test_api_v3_ui_klines_get(self):
        """Test case for api_v3_ui_klines_get

        UIKlines  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()