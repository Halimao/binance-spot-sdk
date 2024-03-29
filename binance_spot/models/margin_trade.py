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

class MarginTrade(object):
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
        'commission': 'str',
        'commission_asset': 'str',
        'id': 'int',
        'is_best_match': 'bool',
        'is_buyer': 'bool',
        'is_maker': 'bool',
        'order_id': 'int',
        'price': 'str',
        'qty': 'str',
        'symbol': 'str',
        'is_isolated': 'bool',
        'time': 'int'
    }

    attribute_map = {
        'commission': 'commission',
        'commission_asset': 'commissionAsset',
        'id': 'id',
        'is_best_match': 'isBestMatch',
        'is_buyer': 'isBuyer',
        'is_maker': 'isMaker',
        'order_id': 'orderId',
        'price': 'price',
        'qty': 'qty',
        'symbol': 'symbol',
        'is_isolated': 'isIsolated',
        'time': 'time'
    }

    def __init__(self, commission=None, commission_asset=None, id=None, is_best_match=None, is_buyer=None, is_maker=None, order_id=None, price=None, qty=None, symbol=None, is_isolated=None, time=None):  # noqa: E501
        """MarginTrade - a model defined in Swagger"""  # noqa: E501
        self._commission = None
        self._commission_asset = None
        self._id = None
        self._is_best_match = None
        self._is_buyer = None
        self._is_maker = None
        self._order_id = None
        self._price = None
        self._qty = None
        self._symbol = None
        self._is_isolated = None
        self._time = None
        self.discriminator = None
        self.commission = commission
        self.commission_asset = commission_asset
        self.id = id
        self.is_best_match = is_best_match
        self.is_buyer = is_buyer
        self.is_maker = is_maker
        self.order_id = order_id
        self.price = price
        self.qty = qty
        self.symbol = symbol
        self.is_isolated = is_isolated
        self.time = time

    @property
    def commission(self):
        """Gets the commission of this MarginTrade.  # noqa: E501


        :return: The commission of this MarginTrade.  # noqa: E501
        :rtype: str
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this MarginTrade.


        :param commission: The commission of this MarginTrade.  # noqa: E501
        :type: str
        """
        if commission is None:
            raise ValueError("Invalid value for `commission`, must not be `None`")  # noqa: E501

        self._commission = commission

    @property
    def commission_asset(self):
        """Gets the commission_asset of this MarginTrade.  # noqa: E501


        :return: The commission_asset of this MarginTrade.  # noqa: E501
        :rtype: str
        """
        return self._commission_asset

    @commission_asset.setter
    def commission_asset(self, commission_asset):
        """Sets the commission_asset of this MarginTrade.


        :param commission_asset: The commission_asset of this MarginTrade.  # noqa: E501
        :type: str
        """
        if commission_asset is None:
            raise ValueError("Invalid value for `commission_asset`, must not be `None`")  # noqa: E501

        self._commission_asset = commission_asset

    @property
    def id(self):
        """Gets the id of this MarginTrade.  # noqa: E501


        :return: The id of this MarginTrade.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarginTrade.


        :param id: The id of this MarginTrade.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_best_match(self):
        """Gets the is_best_match of this MarginTrade.  # noqa: E501


        :return: The is_best_match of this MarginTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_best_match

    @is_best_match.setter
    def is_best_match(self, is_best_match):
        """Sets the is_best_match of this MarginTrade.


        :param is_best_match: The is_best_match of this MarginTrade.  # noqa: E501
        :type: bool
        """
        if is_best_match is None:
            raise ValueError("Invalid value for `is_best_match`, must not be `None`")  # noqa: E501

        self._is_best_match = is_best_match

    @property
    def is_buyer(self):
        """Gets the is_buyer of this MarginTrade.  # noqa: E501


        :return: The is_buyer of this MarginTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_buyer

    @is_buyer.setter
    def is_buyer(self, is_buyer):
        """Sets the is_buyer of this MarginTrade.


        :param is_buyer: The is_buyer of this MarginTrade.  # noqa: E501
        :type: bool
        """
        if is_buyer is None:
            raise ValueError("Invalid value for `is_buyer`, must not be `None`")  # noqa: E501

        self._is_buyer = is_buyer

    @property
    def is_maker(self):
        """Gets the is_maker of this MarginTrade.  # noqa: E501


        :return: The is_maker of this MarginTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_maker

    @is_maker.setter
    def is_maker(self, is_maker):
        """Sets the is_maker of this MarginTrade.


        :param is_maker: The is_maker of this MarginTrade.  # noqa: E501
        :type: bool
        """
        if is_maker is None:
            raise ValueError("Invalid value for `is_maker`, must not be `None`")  # noqa: E501

        self._is_maker = is_maker

    @property
    def order_id(self):
        """Gets the order_id of this MarginTrade.  # noqa: E501


        :return: The order_id of this MarginTrade.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MarginTrade.


        :param order_id: The order_id of this MarginTrade.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def price(self):
        """Gets the price of this MarginTrade.  # noqa: E501


        :return: The price of this MarginTrade.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MarginTrade.


        :param price: The price of this MarginTrade.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this MarginTrade.  # noqa: E501


        :return: The qty of this MarginTrade.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this MarginTrade.


        :param qty: The qty of this MarginTrade.  # noqa: E501
        :type: str
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def symbol(self):
        """Gets the symbol of this MarginTrade.  # noqa: E501


        :return: The symbol of this MarginTrade.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this MarginTrade.


        :param symbol: The symbol of this MarginTrade.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def is_isolated(self):
        """Gets the is_isolated of this MarginTrade.  # noqa: E501


        :return: The is_isolated of this MarginTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_isolated

    @is_isolated.setter
    def is_isolated(self, is_isolated):
        """Sets the is_isolated of this MarginTrade.


        :param is_isolated: The is_isolated of this MarginTrade.  # noqa: E501
        :type: bool
        """
        if is_isolated is None:
            raise ValueError("Invalid value for `is_isolated`, must not be `None`")  # noqa: E501

        self._is_isolated = is_isolated

    @property
    def time(self):
        """Gets the time of this MarginTrade.  # noqa: E501


        :return: The time of this MarginTrade.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MarginTrade.


        :param time: The time of this MarginTrade.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(MarginTrade, dict):
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
        if not isinstance(other, MarginTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
