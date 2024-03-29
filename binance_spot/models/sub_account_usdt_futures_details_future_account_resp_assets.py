# coding: utf-8

"""
    Binance Public Spot API

    OpenAPI Specifications for the Binance Public Spot API  API documents:   - [https://github.com/binance/binance-spot-api-docs](https://github.com/binance/binance-spot-api-docs)   - [https://binance-docs.github.io/apidocs/spot/en](https://binance-docs.github.io/apidocs/spot/en)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SubAccountUSDTFuturesDetailsFutureAccountRespAssets(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'asset': 'str',
        'initial_margin': 'str',
        'maintenance_margin': 'str',
        'margin_balance': 'str',
        'max_withdraw_amount': 'str',
        'open_order_initial_margin': 'str',
        'position_initial_margin': 'str',
        'unrealized_profit': 'str',
        'wallet_balance': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'initial_margin': 'initialMargin',
        'maintenance_margin': 'maintenanceMargin',
        'margin_balance': 'marginBalance',
        'max_withdraw_amount': 'maxWithdrawAmount',
        'open_order_initial_margin': 'openOrderInitialMargin',
        'position_initial_margin': 'positionInitialMargin',
        'unrealized_profit': 'unrealizedProfit',
        'wallet_balance': 'walletBalance'
    }

    def __init__(self, asset=None, initial_margin=None, maintenance_margin=None, margin_balance=None, max_withdraw_amount=None, open_order_initial_margin=None, position_initial_margin=None, unrealized_profit=None, wallet_balance=None):  # noqa: E501
        """SubAccountUSDTFuturesDetailsFutureAccountRespAssets - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._initial_margin = None
        self._maintenance_margin = None
        self._margin_balance = None
        self._max_withdraw_amount = None
        self._open_order_initial_margin = None
        self._position_initial_margin = None
        self._unrealized_profit = None
        self._wallet_balance = None
        self.discriminator = None
        self.asset = asset
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin
        self.margin_balance = margin_balance
        self.max_withdraw_amount = max_withdraw_amount
        self.open_order_initial_margin = open_order_initial_margin
        self.position_initial_margin = position_initial_margin
        self.unrealized_profit = unrealized_profit
        self.wallet_balance = wallet_balance

    @property
    def asset(self):
        """Gets the asset of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The asset of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param asset: The asset of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def initial_margin(self):
        """Gets the initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._initial_margin

    @initial_margin.setter
    def initial_margin(self, initial_margin):
        """Sets the initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param initial_margin: The initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if initial_margin is None:
            raise ValueError("Invalid value for `initial_margin`, must not be `None`")  # noqa: E501

        self._initial_margin = initial_margin

    @property
    def maintenance_margin(self):
        """Gets the maintenance_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The maintenance_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_margin

    @maintenance_margin.setter
    def maintenance_margin(self, maintenance_margin):
        """Sets the maintenance_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param maintenance_margin: The maintenance_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if maintenance_margin is None:
            raise ValueError("Invalid value for `maintenance_margin`, must not be `None`")  # noqa: E501

        self._maintenance_margin = maintenance_margin

    @property
    def margin_balance(self):
        """Gets the margin_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The margin_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._margin_balance

    @margin_balance.setter
    def margin_balance(self, margin_balance):
        """Sets the margin_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param margin_balance: The margin_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if margin_balance is None:
            raise ValueError("Invalid value for `margin_balance`, must not be `None`")  # noqa: E501

        self._margin_balance = margin_balance

    @property
    def max_withdraw_amount(self):
        """Gets the max_withdraw_amount of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The max_withdraw_amount of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._max_withdraw_amount

    @max_withdraw_amount.setter
    def max_withdraw_amount(self, max_withdraw_amount):
        """Sets the max_withdraw_amount of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param max_withdraw_amount: The max_withdraw_amount of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if max_withdraw_amount is None:
            raise ValueError("Invalid value for `max_withdraw_amount`, must not be `None`")  # noqa: E501

        self._max_withdraw_amount = max_withdraw_amount

    @property
    def open_order_initial_margin(self):
        """Gets the open_order_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The open_order_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._open_order_initial_margin

    @open_order_initial_margin.setter
    def open_order_initial_margin(self, open_order_initial_margin):
        """Sets the open_order_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param open_order_initial_margin: The open_order_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if open_order_initial_margin is None:
            raise ValueError("Invalid value for `open_order_initial_margin`, must not be `None`")  # noqa: E501

        self._open_order_initial_margin = open_order_initial_margin

    @property
    def position_initial_margin(self):
        """Gets the position_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The position_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._position_initial_margin

    @position_initial_margin.setter
    def position_initial_margin(self, position_initial_margin):
        """Sets the position_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param position_initial_margin: The position_initial_margin of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if position_initial_margin is None:
            raise ValueError("Invalid value for `position_initial_margin`, must not be `None`")  # noqa: E501

        self._position_initial_margin = position_initial_margin

    @property
    def unrealized_profit(self):
        """Gets the unrealized_profit of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The unrealized_profit of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._unrealized_profit

    @unrealized_profit.setter
    def unrealized_profit(self, unrealized_profit):
        """Sets the unrealized_profit of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param unrealized_profit: The unrealized_profit of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if unrealized_profit is None:
            raise ValueError("Invalid value for `unrealized_profit`, must not be `None`")  # noqa: E501

        self._unrealized_profit = unrealized_profit

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501


        :return: The wallet_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :rtype: str
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.


        :param wallet_balance: The wallet_balance of this SubAccountUSDTFuturesDetailsFutureAccountRespAssets.  # noqa: E501
        :type: str
        """
        if wallet_balance is None:
            raise ValueError("Invalid value for `wallet_balance`, must not be `None`")  # noqa: E501

        self._wallet_balance = wallet_balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SubAccountUSDTFuturesDetailsFutureAccountRespAssets, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubAccountUSDTFuturesDetailsFutureAccountRespAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
