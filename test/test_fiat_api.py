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
from binance_spot.api.fiat_api import FiatApi  # noqa: E501
from binance_spot.rest import ApiException


class TestFiatApi(unittest.TestCase):
    """FiatApi unit test stubs"""

    def setUp(self):
        self.api = FiatApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_fiat_orders_get(self):
        """Test case for sapi_v1_fiat_orders_get

        Fiat Deposit/Withdraw History (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_fiat_payments_get(self):
        """Test case for sapi_v1_fiat_payments_get

        Fiat Payments History (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
