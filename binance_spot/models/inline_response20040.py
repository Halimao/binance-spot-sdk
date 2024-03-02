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

class InlineResponse20040(object):
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
        'vip_level': 'int',
        'coin': 'str',
        'transfer_in': 'bool',
        'borrowable': 'bool',
        'daily_interest': 'str',
        'yearly_interest': 'str',
        'borrow_limit': 'str',
        'marginable_pairs': 'list[str]'
    }

    attribute_map = {
        'vip_level': 'vipLevel',
        'coin': 'coin',
        'transfer_in': 'transferIn',
        'borrowable': 'borrowable',
        'daily_interest': 'dailyInterest',
        'yearly_interest': 'yearlyInterest',
        'borrow_limit': 'borrowLimit',
        'marginable_pairs': 'marginablePairs'
    }

    def __init__(self, vip_level=None, coin=None, transfer_in=None, borrowable=None, daily_interest=None, yearly_interest=None, borrow_limit=None, marginable_pairs=None):  # noqa: E501
        """InlineResponse20040 - a model defined in Swagger"""  # noqa: E501
        self._vip_level = None
        self._coin = None
        self._transfer_in = None
        self._borrowable = None
        self._daily_interest = None
        self._yearly_interest = None
        self._borrow_limit = None
        self._marginable_pairs = None
        self.discriminator = None
        self.vip_level = vip_level
        self.coin = coin
        self.transfer_in = transfer_in
        self.borrowable = borrowable
        self.daily_interest = daily_interest
        self.yearly_interest = yearly_interest
        self.borrow_limit = borrow_limit
        self.marginable_pairs = marginable_pairs

    @property
    def vip_level(self):
        """Gets the vip_level of this InlineResponse20040.  # noqa: E501


        :return: The vip_level of this InlineResponse20040.  # noqa: E501
        :rtype: int
        """
        return self._vip_level

    @vip_level.setter
    def vip_level(self, vip_level):
        """Sets the vip_level of this InlineResponse20040.


        :param vip_level: The vip_level of this InlineResponse20040.  # noqa: E501
        :type: int
        """
        if vip_level is None:
            raise ValueError("Invalid value for `vip_level`, must not be `None`")  # noqa: E501

        self._vip_level = vip_level

    @property
    def coin(self):
        """Gets the coin of this InlineResponse20040.  # noqa: E501


        :return: The coin of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this InlineResponse20040.


        :param coin: The coin of this InlineResponse20040.  # noqa: E501
        :type: str
        """
        if coin is None:
            raise ValueError("Invalid value for `coin`, must not be `None`")  # noqa: E501

        self._coin = coin

    @property
    def transfer_in(self):
        """Gets the transfer_in of this InlineResponse20040.  # noqa: E501


        :return: The transfer_in of this InlineResponse20040.  # noqa: E501
        :rtype: bool
        """
        return self._transfer_in

    @transfer_in.setter
    def transfer_in(self, transfer_in):
        """Sets the transfer_in of this InlineResponse20040.


        :param transfer_in: The transfer_in of this InlineResponse20040.  # noqa: E501
        :type: bool
        """
        if transfer_in is None:
            raise ValueError("Invalid value for `transfer_in`, must not be `None`")  # noqa: E501

        self._transfer_in = transfer_in

    @property
    def borrowable(self):
        """Gets the borrowable of this InlineResponse20040.  # noqa: E501


        :return: The borrowable of this InlineResponse20040.  # noqa: E501
        :rtype: bool
        """
        return self._borrowable

    @borrowable.setter
    def borrowable(self, borrowable):
        """Sets the borrowable of this InlineResponse20040.


        :param borrowable: The borrowable of this InlineResponse20040.  # noqa: E501
        :type: bool
        """
        if borrowable is None:
            raise ValueError("Invalid value for `borrowable`, must not be `None`")  # noqa: E501

        self._borrowable = borrowable

    @property
    def daily_interest(self):
        """Gets the daily_interest of this InlineResponse20040.  # noqa: E501


        :return: The daily_interest of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._daily_interest

    @daily_interest.setter
    def daily_interest(self, daily_interest):
        """Sets the daily_interest of this InlineResponse20040.


        :param daily_interest: The daily_interest of this InlineResponse20040.  # noqa: E501
        :type: str
        """
        if daily_interest is None:
            raise ValueError("Invalid value for `daily_interest`, must not be `None`")  # noqa: E501

        self._daily_interest = daily_interest

    @property
    def yearly_interest(self):
        """Gets the yearly_interest of this InlineResponse20040.  # noqa: E501


        :return: The yearly_interest of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._yearly_interest

    @yearly_interest.setter
    def yearly_interest(self, yearly_interest):
        """Sets the yearly_interest of this InlineResponse20040.


        :param yearly_interest: The yearly_interest of this InlineResponse20040.  # noqa: E501
        :type: str
        """
        if yearly_interest is None:
            raise ValueError("Invalid value for `yearly_interest`, must not be `None`")  # noqa: E501

        self._yearly_interest = yearly_interest

    @property
    def borrow_limit(self):
        """Gets the borrow_limit of this InlineResponse20040.  # noqa: E501


        :return: The borrow_limit of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._borrow_limit

    @borrow_limit.setter
    def borrow_limit(self, borrow_limit):
        """Sets the borrow_limit of this InlineResponse20040.


        :param borrow_limit: The borrow_limit of this InlineResponse20040.  # noqa: E501
        :type: str
        """
        if borrow_limit is None:
            raise ValueError("Invalid value for `borrow_limit`, must not be `None`")  # noqa: E501

        self._borrow_limit = borrow_limit

    @property
    def marginable_pairs(self):
        """Gets the marginable_pairs of this InlineResponse20040.  # noqa: E501


        :return: The marginable_pairs of this InlineResponse20040.  # noqa: E501
        :rtype: list[str]
        """
        return self._marginable_pairs

    @marginable_pairs.setter
    def marginable_pairs(self, marginable_pairs):
        """Sets the marginable_pairs of this InlineResponse20040.


        :param marginable_pairs: The marginable_pairs of this InlineResponse20040.  # noqa: E501
        :type: list[str]
        """
        if marginable_pairs is None:
            raise ValueError("Invalid value for `marginable_pairs`, must not be `None`")  # noqa: E501

        self._marginable_pairs = marginable_pairs

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
        if issubclass(InlineResponse20040, dict):
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
        if not isinstance(other, InlineResponse20040):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
