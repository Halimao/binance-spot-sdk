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
from binance_spot.api.gift_card_api import GiftCardApi  # noqa: E501
from binance_spot.rest import ApiException


class TestGiftCardApi(unittest.TestCase):
    """GiftCardApi unit test stubs"""

    def setUp(self):
        self.api = GiftCardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_giftcard_buy_code_post(self):
        """Test case for sapi_v1_giftcard_buy_code_post

        Buy a Binance Code (TRADE)  # noqa: E501
        """
        pass

    def test_sapi_v1_giftcard_buy_code_token_limit_get(self):
        """Test case for sapi_v1_giftcard_buy_code_token_limit_get

        Fetch Token Limit (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_giftcard_create_code_post(self):
        """Test case for sapi_v1_giftcard_create_code_post

        Create a Binance Code (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_giftcard_cryptography_rsa_public_key_get(self):
        """Test case for sapi_v1_giftcard_cryptography_rsa_public_key_get

        Fetch RSA Public Key (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_giftcard_redeem_code_post(self):
        """Test case for sapi_v1_giftcard_redeem_code_post

        Redeem a Binance Code (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_giftcard_verify_get(self):
        """Test case for sapi_v1_giftcard_verify_get

        Verify a Binance Code (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
