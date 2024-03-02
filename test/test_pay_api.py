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
from binance_spot.api.pay_api import PayApi  # noqa: E501
from binance_spot.rest import ApiException


class TestPayApi(unittest.TestCase):
    """PayApi unit test stubs"""

    def setUp(self):
        self.api = PayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_pay_transactions_get(self):
        """Test case for sapi_v1_pay_transactions_get

        Get Pay Trade History (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()