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

class InlineResponse200110(object):
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
        'name': 'str',
        'total_balance': 'str',
        'available_balance': 'str',
        'in_order': 'str',
        'btc_value': 'str'
    }

    attribute_map = {
        'coin': 'coin',
        'name': 'name',
        'total_balance': 'totalBalance',
        'available_balance': 'availableBalance',
        'in_order': 'inOrder',
        'btc_value': 'btcValue'
    }

    def __init__(self, coin=None, name=None, total_balance=None, available_balance=None, in_order=None, btc_value=None):  # noqa: E501
        """InlineResponse200110 - a model defined in Swagger"""  # noqa: E501
        self._coin = None
        self._name = None
        self._total_balance = None
        self._available_balance = None
        self._in_order = None
        self._btc_value = None
        self.discriminator = None
        self.coin = coin
        self.name = name
        self.total_balance = total_balance
        self.available_balance = available_balance
        self.in_order = in_order
        self.btc_value = btc_value

    @property
    def coin(self):
        """Gets the coin of this InlineResponse200110.  # noqa: E501


        :return: The coin of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this InlineResponse200110.


        :param coin: The coin of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if coin is None:
            raise ValueError("Invalid value for `coin`, must not be `None`")  # noqa: E501

        self._coin = coin

    @property
    def name(self):
        """Gets the name of this InlineResponse200110.  # noqa: E501


        :return: The name of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200110.


        :param name: The name of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def total_balance(self):
        """Gets the total_balance of this InlineResponse200110.  # noqa: E501


        :return: The total_balance of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._total_balance

    @total_balance.setter
    def total_balance(self, total_balance):
        """Sets the total_balance of this InlineResponse200110.


        :param total_balance: The total_balance of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if total_balance is None:
            raise ValueError("Invalid value for `total_balance`, must not be `None`")  # noqa: E501

        self._total_balance = total_balance

    @property
    def available_balance(self):
        """Gets the available_balance of this InlineResponse200110.  # noqa: E501


        :return: The available_balance of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this InlineResponse200110.


        :param available_balance: The available_balance of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if available_balance is None:
            raise ValueError("Invalid value for `available_balance`, must not be `None`")  # noqa: E501

        self._available_balance = available_balance

    @property
    def in_order(self):
        """Gets the in_order of this InlineResponse200110.  # noqa: E501


        :return: The in_order of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._in_order

    @in_order.setter
    def in_order(self, in_order):
        """Sets the in_order of this InlineResponse200110.


        :param in_order: The in_order of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if in_order is None:
            raise ValueError("Invalid value for `in_order`, must not be `None`")  # noqa: E501

        self._in_order = in_order

    @property
    def btc_value(self):
        """Gets the btc_value of this InlineResponse200110.  # noqa: E501


        :return: The btc_value of this InlineResponse200110.  # noqa: E501
        :rtype: str
        """
        return self._btc_value

    @btc_value.setter
    def btc_value(self, btc_value):
        """Sets the btc_value of this InlineResponse200110.


        :param btc_value: The btc_value of this InlineResponse200110.  # noqa: E501
        :type: str
        """
        if btc_value is None:
            raise ValueError("Invalid value for `btc_value`, must not be `None`")  # noqa: E501

        self._btc_value = btc_value

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
        if issubclass(InlineResponse200110, dict):
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
        if not isinstance(other, InlineResponse200110):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
