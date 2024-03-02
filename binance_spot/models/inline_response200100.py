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

class InlineResponse200100(object):
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
        'entry_price': 'str',
        'leverage': 'str',
        'max_notional': 'str',
        'liquidation_price': 'str',
        'mark_price': 'str',
        'position_amount': 'str',
        'symbol': 'str',
        'unrealized_profit': 'str'
    }

    attribute_map = {
        'entry_price': 'entryPrice',
        'leverage': 'leverage',
        'max_notional': 'maxNotional',
        'liquidation_price': 'liquidationPrice',
        'mark_price': 'markPrice',
        'position_amount': 'positionAmount',
        'symbol': 'symbol',
        'unrealized_profit': 'unrealizedProfit'
    }

    def __init__(self, entry_price=None, leverage=None, max_notional=None, liquidation_price=None, mark_price=None, position_amount=None, symbol=None, unrealized_profit=None):  # noqa: E501
        """InlineResponse200100 - a model defined in Swagger"""  # noqa: E501
        self._entry_price = None
        self._leverage = None
        self._max_notional = None
        self._liquidation_price = None
        self._mark_price = None
        self._position_amount = None
        self._symbol = None
        self._unrealized_profit = None
        self.discriminator = None
        self.entry_price = entry_price
        self.leverage = leverage
        self.max_notional = max_notional
        self.liquidation_price = liquidation_price
        self.mark_price = mark_price
        self.position_amount = position_amount
        self.symbol = symbol
        self.unrealized_profit = unrealized_profit

    @property
    def entry_price(self):
        """Gets the entry_price of this InlineResponse200100.  # noqa: E501


        :return: The entry_price of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._entry_price

    @entry_price.setter
    def entry_price(self, entry_price):
        """Sets the entry_price of this InlineResponse200100.


        :param entry_price: The entry_price of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if entry_price is None:
            raise ValueError("Invalid value for `entry_price`, must not be `None`")  # noqa: E501

        self._entry_price = entry_price

    @property
    def leverage(self):
        """Gets the leverage of this InlineResponse200100.  # noqa: E501

        current initial leverage  # noqa: E501

        :return: The leverage of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this InlineResponse200100.

        current initial leverage  # noqa: E501

        :param leverage: The leverage of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if leverage is None:
            raise ValueError("Invalid value for `leverage`, must not be `None`")  # noqa: E501

        self._leverage = leverage

    @property
    def max_notional(self):
        """Gets the max_notional of this InlineResponse200100.  # noqa: E501

        notional value limit of current initial leverage  # noqa: E501

        :return: The max_notional of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._max_notional

    @max_notional.setter
    def max_notional(self, max_notional):
        """Sets the max_notional of this InlineResponse200100.

        notional value limit of current initial leverage  # noqa: E501

        :param max_notional: The max_notional of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if max_notional is None:
            raise ValueError("Invalid value for `max_notional`, must not be `None`")  # noqa: E501

        self._max_notional = max_notional

    @property
    def liquidation_price(self):
        """Gets the liquidation_price of this InlineResponse200100.  # noqa: E501


        :return: The liquidation_price of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._liquidation_price

    @liquidation_price.setter
    def liquidation_price(self, liquidation_price):
        """Sets the liquidation_price of this InlineResponse200100.


        :param liquidation_price: The liquidation_price of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if liquidation_price is None:
            raise ValueError("Invalid value for `liquidation_price`, must not be `None`")  # noqa: E501

        self._liquidation_price = liquidation_price

    @property
    def mark_price(self):
        """Gets the mark_price of this InlineResponse200100.  # noqa: E501


        :return: The mark_price of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._mark_price

    @mark_price.setter
    def mark_price(self, mark_price):
        """Sets the mark_price of this InlineResponse200100.


        :param mark_price: The mark_price of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if mark_price is None:
            raise ValueError("Invalid value for `mark_price`, must not be `None`")  # noqa: E501

        self._mark_price = mark_price

    @property
    def position_amount(self):
        """Gets the position_amount of this InlineResponse200100.  # noqa: E501


        :return: The position_amount of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._position_amount

    @position_amount.setter
    def position_amount(self, position_amount):
        """Sets the position_amount of this InlineResponse200100.


        :param position_amount: The position_amount of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if position_amount is None:
            raise ValueError("Invalid value for `position_amount`, must not be `None`")  # noqa: E501

        self._position_amount = position_amount

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse200100.  # noqa: E501


        :return: The symbol of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse200100.


        :param symbol: The symbol of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def unrealized_profit(self):
        """Gets the unrealized_profit of this InlineResponse200100.  # noqa: E501


        :return: The unrealized_profit of this InlineResponse200100.  # noqa: E501
        :rtype: str
        """
        return self._unrealized_profit

    @unrealized_profit.setter
    def unrealized_profit(self, unrealized_profit):
        """Sets the unrealized_profit of this InlineResponse200100.


        :param unrealized_profit: The unrealized_profit of this InlineResponse200100.  # noqa: E501
        :type: str
        """
        if unrealized_profit is None:
            raise ValueError("Invalid value for `unrealized_profit`, must not be `None`")  # noqa: E501

        self._unrealized_profit = unrealized_profit

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
        if issubclass(InlineResponse200100, dict):
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
        if not isinstance(other, InlineResponse200100):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
