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
from binance_spot.api.simple_earn_api import SimpleEarnApi  # noqa: E501
from binance_spot.rest import ApiException


class TestSimpleEarnApi(unittest.TestCase):
    """SimpleEarnApi unit test stubs"""

    def setUp(self):
        self.api = SimpleEarnApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_simple_earn_account_get(self):
        """Test case for sapi_v1_simple_earn_account_get

        Simple Account (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_history_collateral_record_get(self):
        """Test case for sapi_v1_simple_earn_flexible_history_collateral_record_get

        Get Collateral Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_history_rate_history_get(self):
        """Test case for sapi_v1_simple_earn_flexible_history_rate_history_get

        Get Rate History (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_history_redemption_record_get(self):
        """Test case for sapi_v1_simple_earn_flexible_history_redemption_record_get

        Get Flexible Redemption Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_history_rewards_record_get(self):
        """Test case for sapi_v1_simple_earn_flexible_history_rewards_record_get

        Get Flexible Rewards History (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_history_subscription_record_get(self):
        """Test case for sapi_v1_simple_earn_flexible_history_subscription_record_get

        Get Flexible Subscription Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_list_get(self):
        """Test case for sapi_v1_simple_earn_flexible_list_get

        Get Simple Earn Flexible Product List (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_personal_left_quota_get(self):
        """Test case for sapi_v1_simple_earn_flexible_personal_left_quota_get

        Get Flexible Personal Left Quota (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_position_get(self):
        """Test case for sapi_v1_simple_earn_flexible_position_get

        Get Flexible Product Position (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_redeem_post(self):
        """Test case for sapi_v1_simple_earn_flexible_redeem_post

        Redeem Flexible Product (TRADE)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_set_auto_subscribe_post(self):
        """Test case for sapi_v1_simple_earn_flexible_set_auto_subscribe_post

        Set Flexible Auto Subscribe (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_subscribe_post(self):
        """Test case for sapi_v1_simple_earn_flexible_subscribe_post

        Subscribe Flexible Product (TRADE)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_flexible_subscription_preview_get(self):
        """Test case for sapi_v1_simple_earn_flexible_subscription_preview_get

        Get Flexible Subscription Preview (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_history_redemption_record_get(self):
        """Test case for sapi_v1_simple_earn_locked_history_redemption_record_get

        Get Locked Redemption Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_history_rewards_record_get(self):
        """Test case for sapi_v1_simple_earn_locked_history_rewards_record_get

        Get Locked Rewards History (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_history_subscription_record_get(self):
        """Test case for sapi_v1_simple_earn_locked_history_subscription_record_get

        Get Locked Subscription Record (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_list_get(self):
        """Test case for sapi_v1_simple_earn_locked_list_get

        Get Simple Earn Locked Product List (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_personal_left_quota_get(self):
        """Test case for sapi_v1_simple_earn_locked_personal_left_quota_get

        Get Locked Personal Left Quota (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_position_get(self):
        """Test case for sapi_v1_simple_earn_locked_position_get

        Get Locked Product Position (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_redeem_post(self):
        """Test case for sapi_v1_simple_earn_locked_redeem_post

        Redeem Locked Product (TRADE)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_set_auto_subscribe_post(self):
        """Test case for sapi_v1_simple_earn_locked_set_auto_subscribe_post

        Set Locked Auto Subscribe (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_subscribe_post(self):
        """Test case for sapi_v1_simple_earn_locked_subscribe_post

        Subscribe Locked Product (TRADE)  # noqa: E501
        """
        pass

    def test_sapi_v1_simple_earn_locked_subscription_preview_get(self):
        """Test case for sapi_v1_simple_earn_locked_subscription_preview_get

        Get Locked Subscription Preview (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
