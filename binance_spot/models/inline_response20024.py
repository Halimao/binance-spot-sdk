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

class InlineResponse20024(object):
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
        'base': 'str',
        'id': 'int',
        'is_buy_allowed': 'bool',
        'is_margin_trade': 'bool',
        'is_sell_allowed': 'bool',
        'quote': 'str',
        'symbol': 'str'
    }

    attribute_map = {
        'base': 'base',
        'id': 'id',
        'is_buy_allowed': 'isBuyAllowed',
        'is_margin_trade': 'isMarginTrade',
        'is_sell_allowed': 'isSellAllowed',
        'quote': 'quote',
        'symbol': 'symbol'
    }

    def __init__(self, base=None, id=None, is_buy_allowed=None, is_margin_trade=None, is_sell_allowed=None, quote=None, symbol=None):  # noqa: E501
        """InlineResponse20024 - a model defined in Swagger"""  # noqa: E501
        self._base = None
        self._id = None
        self._is_buy_allowed = None
        self._is_margin_trade = None
        self._is_sell_allowed = None
        self._quote = None
        self._symbol = None
        self.discriminator = None
        self.base = base
        self.id = id
        self.is_buy_allowed = is_buy_allowed
        self.is_margin_trade = is_margin_trade
        self.is_sell_allowed = is_sell_allowed
        self.quote = quote
        self.symbol = symbol

    @property
    def base(self):
        """Gets the base of this InlineResponse20024.  # noqa: E501


        :return: The base of this InlineResponse20024.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this InlineResponse20024.


        :param base: The base of this InlineResponse20024.  # noqa: E501
        :type: str
        """
        if base is None:
            raise ValueError("Invalid value for `base`, must not be `None`")  # noqa: E501

        self._base = base

    @property
    def id(self):
        """Gets the id of this InlineResponse20024.  # noqa: E501


        :return: The id of this InlineResponse20024.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20024.


        :param id: The id of this InlineResponse20024.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_buy_allowed(self):
        """Gets the is_buy_allowed of this InlineResponse20024.  # noqa: E501


        :return: The is_buy_allowed of this InlineResponse20024.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy_allowed

    @is_buy_allowed.setter
    def is_buy_allowed(self, is_buy_allowed):
        """Sets the is_buy_allowed of this InlineResponse20024.


        :param is_buy_allowed: The is_buy_allowed of this InlineResponse20024.  # noqa: E501
        :type: bool
        """
        if is_buy_allowed is None:
            raise ValueError("Invalid value for `is_buy_allowed`, must not be `None`")  # noqa: E501

        self._is_buy_allowed = is_buy_allowed

    @property
    def is_margin_trade(self):
        """Gets the is_margin_trade of this InlineResponse20024.  # noqa: E501


        :return: The is_margin_trade of this InlineResponse20024.  # noqa: E501
        :rtype: bool
        """
        return self._is_margin_trade

    @is_margin_trade.setter
    def is_margin_trade(self, is_margin_trade):
        """Sets the is_margin_trade of this InlineResponse20024.


        :param is_margin_trade: The is_margin_trade of this InlineResponse20024.  # noqa: E501
        :type: bool
        """
        if is_margin_trade is None:
            raise ValueError("Invalid value for `is_margin_trade`, must not be `None`")  # noqa: E501

        self._is_margin_trade = is_margin_trade

    @property
    def is_sell_allowed(self):
        """Gets the is_sell_allowed of this InlineResponse20024.  # noqa: E501


        :return: The is_sell_allowed of this InlineResponse20024.  # noqa: E501
        :rtype: bool
        """
        return self._is_sell_allowed

    @is_sell_allowed.setter
    def is_sell_allowed(self, is_sell_allowed):
        """Sets the is_sell_allowed of this InlineResponse20024.


        :param is_sell_allowed: The is_sell_allowed of this InlineResponse20024.  # noqa: E501
        :type: bool
        """
        if is_sell_allowed is None:
            raise ValueError("Invalid value for `is_sell_allowed`, must not be `None`")  # noqa: E501

        self._is_sell_allowed = is_sell_allowed

    @property
    def quote(self):
        """Gets the quote of this InlineResponse20024.  # noqa: E501


        :return: The quote of this InlineResponse20024.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this InlineResponse20024.


        :param quote: The quote of this InlineResponse20024.  # noqa: E501
        :type: str
        """
        if quote is None:
            raise ValueError("Invalid value for `quote`, must not be `None`")  # noqa: E501

        self._quote = quote

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse20024.  # noqa: E501


        :return: The symbol of this InlineResponse20024.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse20024.


        :param symbol: The symbol of this InlineResponse20024.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

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
        if issubclass(InlineResponse20024, dict):
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
        if not isinstance(other, InlineResponse20024):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
