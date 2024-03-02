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
from binance_spot.api.staking_api import StakingApi  # noqa: E501
from binance_spot.rest import ApiException


class TestStakingApi(unittest.TestCase):
    """StakingApi unit test stubs"""

    def setUp(self):
        self.api = StakingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_staking_personal_left_quota_get(self):
        """Test case for sapi_v1_staking_personal_left_quota_get

        Get Personal Left Quota of Staking Product (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_position_get(self):
        """Test case for sapi_v1_staking_position_get

        Get Staking Product Position (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_product_list_get(self):
        """Test case for sapi_v1_staking_product_list_get

        Get Staking Product List (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_purchase_post(self):
        """Test case for sapi_v1_staking_purchase_post

        Purchase Staking Product (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_redeem_post(self):
        """Test case for sapi_v1_staking_redeem_post

        Redeem Staking Product (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_set_auto_staking_post(self):
        """Test case for sapi_v1_staking_set_auto_staking_post

        Set Auto Staking (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_staking_staking_record_get(self):
        """Test case for sapi_v1_staking_staking_record_get

        Get Staking History (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
