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

class BookTicker(object):
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
        'symbol': 'str',
        'bid_price': 'str',
        'bid_qty': 'str',
        'ask_price': 'str',
        'ask_qty': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'bid_price': 'bidPrice',
        'bid_qty': 'bidQty',
        'ask_price': 'askPrice',
        'ask_qty': 'askQty'
    }

    def __init__(self, symbol=None, bid_price=None, bid_qty=None, ask_price=None, ask_qty=None):  # noqa: E501
        """BookTicker - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._bid_price = None
        self._bid_qty = None
        self._ask_price = None
        self._ask_qty = None
        self.discriminator = None
        self.symbol = symbol
        self.bid_price = bid_price
        self.bid_qty = bid_qty
        self.ask_price = ask_price
        self.ask_qty = ask_qty

    @property
    def symbol(self):
        """Gets the symbol of this BookTicker.  # noqa: E501


        :return: The symbol of this BookTicker.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this BookTicker.


        :param symbol: The symbol of this BookTicker.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def bid_price(self):
        """Gets the bid_price of this BookTicker.  # noqa: E501


        :return: The bid_price of this BookTicker.  # noqa: E501
        :rtype: str
        """
        return self._bid_price

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this BookTicker.


        :param bid_price: The bid_price of this BookTicker.  # noqa: E501
        :type: str
        """
        if bid_price is None:
            raise ValueError("Invalid value for `bid_price`, must not be `None`")  # noqa: E501

        self._bid_price = bid_price

    @property
    def bid_qty(self):
        """Gets the bid_qty of this BookTicker.  # noqa: E501


        :return: The bid_qty of this BookTicker.  # noqa: E501
        :rtype: str
        """
        return self._bid_qty

    @bid_qty.setter
    def bid_qty(self, bid_qty):
        """Sets the bid_qty of this BookTicker.


        :param bid_qty: The bid_qty of this BookTicker.  # noqa: E501
        :type: str
        """
        if bid_qty is None:
            raise ValueError("Invalid value for `bid_qty`, must not be `None`")  # noqa: E501

        self._bid_qty = bid_qty

    @property
    def ask_price(self):
        """Gets the ask_price of this BookTicker.  # noqa: E501


        :return: The ask_price of this BookTicker.  # noqa: E501
        :rtype: str
        """
        return self._ask_price

    @ask_price.setter
    def ask_price(self, ask_price):
        """Sets the ask_price of this BookTicker.


        :param ask_price: The ask_price of this BookTicker.  # noqa: E501
        :type: str
        """
        if ask_price is None:
            raise ValueError("Invalid value for `ask_price`, must not be `None`")  # noqa: E501

        self._ask_price = ask_price

    @property
    def ask_qty(self):
        """Gets the ask_qty of this BookTicker.  # noqa: E501


        :return: The ask_qty of this BookTicker.  # noqa: E501
        :rtype: str
        """
        return self._ask_qty

    @ask_qty.setter
    def ask_qty(self, ask_qty):
        """Sets the ask_qty of this BookTicker.


        :param ask_qty: The ask_qty of this BookTicker.  # noqa: E501
        :type: str
        """
        if ask_qty is None:
            raise ValueError("Invalid value for `ask_qty`, must not be `None`")  # noqa: E501

        self._ask_qty = ask_qty

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
        if issubclass(BookTicker, dict):
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
        if not isinstance(other, BookTicker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
