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
from binance_spot.api.savings_api import SavingsApi  # noqa: E501
from binance_spot.rest import ApiException


class TestSavingsApi(unittest.TestCase):
    """SavingsApi unit test stubs"""

    def setUp(self):
        self.api = SavingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sapi_v1_lending_customized_fixed_purchase_post(self):
        """Test case for sapi_v1_lending_customized_fixed_purchase_post

        Purchase Fixed/Activity Project (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_lending_position_changed_post(self):
        """Test case for sapi_v1_lending_position_changed_post

        Change Fixed/Activity Position to Daily Position (USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_lending_project_list_get(self):
        """Test case for sapi_v1_lending_project_list_get

        Get Fixed/Activity Project List(USER_DATA)  # noqa: E501
        """
        pass

    def test_sapi_v1_lending_project_position_list_get(self):
        """Test case for sapi_v1_lending_project_position_list_get

        Get Fixed/Activity Project Position (USER_DATA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
