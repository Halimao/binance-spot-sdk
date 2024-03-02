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

class SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList(object):
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
        'email': 'str',
        'total_initial_margin': 'str',
        'total_maintenance_margin': 'str',
        'total_margin_balance': 'str',
        'total_open_order_initial_margin': 'str',
        'total_position_initial_margin': 'str',
        'total_unrealized_profit': 'str',
        'total_wallet_balance': 'str',
        'asset': 'str'
    }

    attribute_map = {
        'email': 'email',
        'total_initial_margin': 'totalInitialMargin',
        'total_maintenance_margin': 'totalMaintenanceMargin',
        'total_margin_balance': 'totalMarginBalance',
        'total_open_order_initial_margin': 'totalOpenOrderInitialMargin',
        'total_position_initial_margin': 'totalPositionInitialMargin',
        'total_unrealized_profit': 'totalUnrealizedProfit',
        'total_wallet_balance': 'totalWalletBalance',
        'asset': 'asset'
    }

    def __init__(self, email=None, total_initial_margin=None, total_maintenance_margin=None, total_margin_balance=None, total_open_order_initial_margin=None, total_position_initial_margin=None, total_unrealized_profit=None, total_wallet_balance=None, asset=None):  # noqa: E501
        """SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._total_initial_margin = None
        self._total_maintenance_margin = None
        self._total_margin_balance = None
        self._total_open_order_initial_margin = None
        self._total_position_initial_margin = None
        self._total_unrealized_profit = None
        self._total_wallet_balance = None
        self._asset = None
        self.discriminator = None
        self.email = email
        self.total_initial_margin = total_initial_margin
        self.total_maintenance_margin = total_maintenance_margin
        self.total_margin_balance = total_margin_balance
        self.total_open_order_initial_margin = total_open_order_initial_margin
        self.total_position_initial_margin = total_position_initial_margin
        self.total_unrealized_profit = total_unrealized_profit
        self.total_wallet_balance = total_wallet_balance
        self.asset = asset

    @property
    def email(self):
        """Gets the email of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The email of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param email: The email of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def total_initial_margin(self):
        """Gets the total_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_initial_margin

    @total_initial_margin.setter
    def total_initial_margin(self, total_initial_margin):
        """Sets the total_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_initial_margin: The total_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_initial_margin is None:
            raise ValueError("Invalid value for `total_initial_margin`, must not be `None`")  # noqa: E501

        self._total_initial_margin = total_initial_margin

    @property
    def total_maintenance_margin(self):
        """Gets the total_maintenance_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_maintenance_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_maintenance_margin

    @total_maintenance_margin.setter
    def total_maintenance_margin(self, total_maintenance_margin):
        """Sets the total_maintenance_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_maintenance_margin: The total_maintenance_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_maintenance_margin is None:
            raise ValueError("Invalid value for `total_maintenance_margin`, must not be `None`")  # noqa: E501

        self._total_maintenance_margin = total_maintenance_margin

    @property
    def total_margin_balance(self):
        """Gets the total_margin_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_margin_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_margin_balance

    @total_margin_balance.setter
    def total_margin_balance(self, total_margin_balance):
        """Sets the total_margin_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_margin_balance: The total_margin_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_margin_balance is None:
            raise ValueError("Invalid value for `total_margin_balance`, must not be `None`")  # noqa: E501

        self._total_margin_balance = total_margin_balance

    @property
    def total_open_order_initial_margin(self):
        """Gets the total_open_order_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_open_order_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_open_order_initial_margin

    @total_open_order_initial_margin.setter
    def total_open_order_initial_margin(self, total_open_order_initial_margin):
        """Sets the total_open_order_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_open_order_initial_margin: The total_open_order_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_open_order_initial_margin is None:
            raise ValueError("Invalid value for `total_open_order_initial_margin`, must not be `None`")  # noqa: E501

        self._total_open_order_initial_margin = total_open_order_initial_margin

    @property
    def total_position_initial_margin(self):
        """Gets the total_position_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_position_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_position_initial_margin

    @total_position_initial_margin.setter
    def total_position_initial_margin(self, total_position_initial_margin):
        """Sets the total_position_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_position_initial_margin: The total_position_initial_margin of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_position_initial_margin is None:
            raise ValueError("Invalid value for `total_position_initial_margin`, must not be `None`")  # noqa: E501

        self._total_position_initial_margin = total_position_initial_margin

    @property
    def total_unrealized_profit(self):
        """Gets the total_unrealized_profit of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_unrealized_profit of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_unrealized_profit

    @total_unrealized_profit.setter
    def total_unrealized_profit(self, total_unrealized_profit):
        """Sets the total_unrealized_profit of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_unrealized_profit: The total_unrealized_profit of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_unrealized_profit is None:
            raise ValueError("Invalid value for `total_unrealized_profit`, must not be `None`")  # noqa: E501

        self._total_unrealized_profit = total_unrealized_profit

    @property
    def total_wallet_balance(self):
        """Gets the total_wallet_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501


        :return: The total_wallet_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._total_wallet_balance

    @total_wallet_balance.setter
    def total_wallet_balance(self, total_wallet_balance):
        """Sets the total_wallet_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.


        :param total_wallet_balance: The total_wallet_balance of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if total_wallet_balance is None:
            raise ValueError("Invalid value for `total_wallet_balance`, must not be `None`")  # noqa: E501

        self._total_wallet_balance = total_wallet_balance

    @property
    def asset(self):
        """Gets the asset of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501

        The sum of BUSD and USDT  # noqa: E501

        :return: The asset of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.

        The sum of BUSD and USDT  # noqa: E501

        :param asset: The asset of this SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

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
        if issubclass(SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList, dict):
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
        if not isinstance(other, SubAccountUSDTFuturesSummaryFutureAccountSummaryRespSubAccountList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
