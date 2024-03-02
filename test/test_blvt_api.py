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
from binance_spot.api.blvt_api import BLVTApi  # noqa: E501
from binance_spot.rest import ApiException


class TestBLVTApi(unittest.TestCase):
    """BLVTApi unit test stubs"""

    def setUp(self):
        self.api = BLVTApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_blvt_redeem_post(self):
        """Test case for sapi_v1_blvt_redeem_post

        Redeem BLVT (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_blvt_redeem_record_get(self):
        """Test case for sapi_v1_blvt_redeem_record_get

        Redemption Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_blvt_subscribe_post(self):
        """Test case for sapi_v1_blvt_subscribe_post

        Subscribe BLVT (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_blvt_subscribe_record_get(self):
        """Test case for sapi_v1_blvt_subscribe_record_get

        Query Subscription Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_blvt_token_info_get(self):
        """Test case for sapi_v1_blvt_token_info_get

        BLVT Info (MARKET_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_blvt_user_limit_get(self):
        """Test case for sapi_v1_blvt_user_limit_get

        BLVT User Limit Info (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()