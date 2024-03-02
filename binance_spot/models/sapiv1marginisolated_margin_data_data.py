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

class Sapiv1marginisolatedMarginDataData(object):
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
        'coin': 'str',
        'daily_interest': 'str',
        'borrow_limit': 'str'
    }

    attribute_map = {
        'coin': 'coin',
        'daily_interest': 'dailyInterest',
        'borrow_limit': 'borrowLimit'
    }

    def __init__(self, coin=None, daily_interest=None, borrow_limit=None):  # noqa: E501
        """Sapiv1marginisolatedMarginDataData - a model defined in Swagger"""  # noqa: E501
        self._coin = None
        self._daily_interest = None
        self._borrow_limit = None
        self.discriminator = None
        if coin is not None:
            self.coin = coin
        if daily_interest is not None:
            self.daily_interest = daily_interest
        if borrow_limit is not None:
            self.borrow_limit = borrow_limit

    @property
    def coin(self):
        """Gets the coin of this Sapiv1marginisolatedMarginDataData.  # noqa: E501


        :return: The coin of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this Sapiv1marginisolatedMarginDataData.


        :param coin: The coin of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :type: str
        """

        self._coin = coin

    @property
    def daily_interest(self):
        """Gets the daily_interest of this Sapiv1marginisolatedMarginDataData.  # noqa: E501


        :return: The daily_interest of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :rtype: str
        """
        return self._daily_interest

    @daily_interest.setter
    def daily_interest(self, daily_interest):
        """Sets the daily_interest of this Sapiv1marginisolatedMarginDataData.


        :param daily_interest: The daily_interest of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :type: str
        """

        self._daily_interest = daily_interest

    @property
    def borrow_limit(self):
        """Gets the borrow_limit of this Sapiv1marginisolatedMarginDataData.  # noqa: E501


        :return: The borrow_limit of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :rtype: str
        """
        return self._borrow_limit

    @borrow_limit.setter
    def borrow_limit(self, borrow_limit):
        """Sets the borrow_limit of this Sapiv1marginisolatedMarginDataData.


        :param borrow_limit: The borrow_limit of this Sapiv1marginisolatedMarginDataData.  # noqa: E501
        :type: str
        """

        self._borrow_limit = borrow_limit

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
        if issubclass(Sapiv1marginisolatedMarginDataData, dict):
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
        if not isinstance(other, Sapiv1marginisolatedMarginDataData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other