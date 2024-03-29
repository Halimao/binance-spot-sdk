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

class Ticker(object):
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
        'price_change': 'str',
        'price_change_percent': 'str',
        'prev_close_price': 'str',
        'last_price': 'str',
        'bid_price': 'str',
        'bid_qty': 'str',
        'ask_price': 'str',
        'ask_qty': 'str',
        'open_price': 'str',
        'high_price': 'str',
        'low_price': 'str',
        'volume': 'str',
        'quote_volume': 'str',
        'open_time': 'int',
        'close_time': 'int',
        'first_id': 'int',
        'last_id': 'int',
        'count': 'int'
    }

    attribute_map = {
        'symbol': 'symbol',
        'price_change': 'priceChange',
        'price_change_percent': 'priceChangePercent',
        'prev_close_price': 'prevClosePrice',
        'last_price': 'lastPrice',
        'bid_price': 'bidPrice',
        'bid_qty': 'bidQty',
        'ask_price': 'askPrice',
        'ask_qty': 'askQty',
        'open_price': 'openPrice',
        'high_price': 'highPrice',
        'low_price': 'lowPrice',
        'volume': 'volume',
        'quote_volume': 'quoteVolume',
        'open_time': 'openTime',
        'close_time': 'closeTime',
        'first_id': 'firstId',
        'last_id': 'lastId',
        'count': 'count'
    }

    def __init__(self, symbol=None, price_change=None, price_change_percent=None, prev_close_price=None, last_price=None, bid_price=None, bid_qty=None, ask_price=None, ask_qty=None, open_price=None, high_price=None, low_price=None, volume=None, quote_volume=None, open_time=None, close_time=None, first_id=None, last_id=None, count=None):  # noqa: E501
        """Ticker - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._price_change = None
        self._price_change_percent = None
        self._prev_close_price = None
        self._last_price = None
        self._bid_price = None
        self._bid_qty = None
        self._ask_price = None
        self._ask_qty = None
        self._open_price = None
        self._high_price = None
        self._low_price = None
        self._volume = None
        self._quote_volume = None
        self._open_time = None
        self._close_time = None
        self._first_id = None
        self._last_id = None
        self._count = None
        self.discriminator = None
        self.symbol = symbol
        self.price_change = price_change
        self.price_change_percent = price_change_percent
        self.prev_close_price = prev_close_price
        self.last_price = last_price
        self.bid_price = bid_price
        self.bid_qty = bid_qty
        self.ask_price = ask_price
        self.ask_qty = ask_qty
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.volume = volume
        self.quote_volume = quote_volume
        self.open_time = open_time
        self.close_time = close_time
        self.first_id = first_id
        self.last_id = last_id
        self.count = count

    @property
    def symbol(self):
        """Gets the symbol of this Ticker.  # noqa: E501


        :return: The symbol of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Ticker.


        :param symbol: The symbol of this Ticker.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def price_change(self):
        """Gets the price_change of this Ticker.  # noqa: E501


        :return: The price_change of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._price_change

    @price_change.setter
    def price_change(self, price_change):
        """Sets the price_change of this Ticker.


        :param price_change: The price_change of this Ticker.  # noqa: E501
        :type: str
        """
        if price_change is None:
            raise ValueError("Invalid value for `price_change`, must not be `None`")  # noqa: E501

        self._price_change = price_change

    @property
    def price_change_percent(self):
        """Gets the price_change_percent of this Ticker.  # noqa: E501


        :return: The price_change_percent of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._price_change_percent

    @price_change_percent.setter
    def price_change_percent(self, price_change_percent):
        """Sets the price_change_percent of this Ticker.


        :param price_change_percent: The price_change_percent of this Ticker.  # noqa: E501
        :type: str
        """
        if price_change_percent is None:
            raise ValueError("Invalid value for `price_change_percent`, must not be `None`")  # noqa: E501

        self._price_change_percent = price_change_percent

    @property
    def prev_close_price(self):
        """Gets the prev_close_price of this Ticker.  # noqa: E501


        :return: The prev_close_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._prev_close_price

    @prev_close_price.setter
    def prev_close_price(self, prev_close_price):
        """Sets the prev_close_price of this Ticker.


        :param prev_close_price: The prev_close_price of this Ticker.  # noqa: E501
        :type: str
        """
        if prev_close_price is None:
            raise ValueError("Invalid value for `prev_close_price`, must not be `None`")  # noqa: E501

        self._prev_close_price = prev_close_price

    @property
    def last_price(self):
        """Gets the last_price of this Ticker.  # noqa: E501


        :return: The last_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this Ticker.


        :param last_price: The last_price of this Ticker.  # noqa: E501
        :type: str
        """
        if last_price is None:
            raise ValueError("Invalid value for `last_price`, must not be `None`")  # noqa: E501

        self._last_price = last_price

    @property
    def bid_price(self):
        """Gets the bid_price of this Ticker.  # noqa: E501


        :return: The bid_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._bid_price

    @bid_price.setter
    def bid_price(self, bid_price):
        """Sets the bid_price of this Ticker.


        :param bid_price: The bid_price of this Ticker.  # noqa: E501
        :type: str
        """
        if bid_price is None:
            raise ValueError("Invalid value for `bid_price`, must not be `None`")  # noqa: E501

        self._bid_price = bid_price

    @property
    def bid_qty(self):
        """Gets the bid_qty of this Ticker.  # noqa: E501


        :return: The bid_qty of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._bid_qty

    @bid_qty.setter
    def bid_qty(self, bid_qty):
        """Sets the bid_qty of this Ticker.


        :param bid_qty: The bid_qty of this Ticker.  # noqa: E501
        :type: str
        """
        if bid_qty is None:
            raise ValueError("Invalid value for `bid_qty`, must not be `None`")  # noqa: E501

        self._bid_qty = bid_qty

    @property
    def ask_price(self):
        """Gets the ask_price of this Ticker.  # noqa: E501


        :return: The ask_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._ask_price

    @ask_price.setter
    def ask_price(self, ask_price):
        """Sets the ask_price of this Ticker.


        :param ask_price: The ask_price of this Ticker.  # noqa: E501
        :type: str
        """
        if ask_price is None:
            raise ValueError("Invalid value for `ask_price`, must not be `None`")  # noqa: E501

        self._ask_price = ask_price

    @property
    def ask_qty(self):
        """Gets the ask_qty of this Ticker.  # noqa: E501


        :return: The ask_qty of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._ask_qty

    @ask_qty.setter
    def ask_qty(self, ask_qty):
        """Sets the ask_qty of this Ticker.


        :param ask_qty: The ask_qty of this Ticker.  # noqa: E501
        :type: str
        """
        if ask_qty is None:
            raise ValueError("Invalid value for `ask_qty`, must not be `None`")  # noqa: E501

        self._ask_qty = ask_qty

    @property
    def open_price(self):
        """Gets the open_price of this Ticker.  # noqa: E501


        :return: The open_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._open_price

    @open_price.setter
    def open_price(self, open_price):
        """Sets the open_price of this Ticker.


        :param open_price: The open_price of this Ticker.  # noqa: E501
        :type: str
        """
        if open_price is None:
            raise ValueError("Invalid value for `open_price`, must not be `None`")  # noqa: E501

        self._open_price = open_price

    @property
    def high_price(self):
        """Gets the high_price of this Ticker.  # noqa: E501


        :return: The high_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._high_price

    @high_price.setter
    def high_price(self, high_price):
        """Sets the high_price of this Ticker.


        :param high_price: The high_price of this Ticker.  # noqa: E501
        :type: str
        """
        if high_price is None:
            raise ValueError("Invalid value for `high_price`, must not be `None`")  # noqa: E501

        self._high_price = high_price

    @property
    def low_price(self):
        """Gets the low_price of this Ticker.  # noqa: E501


        :return: The low_price of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._low_price

    @low_price.setter
    def low_price(self, low_price):
        """Sets the low_price of this Ticker.


        :param low_price: The low_price of this Ticker.  # noqa: E501
        :type: str
        """
        if low_price is None:
            raise ValueError("Invalid value for `low_price`, must not be `None`")  # noqa: E501

        self._low_price = low_price

    @property
    def volume(self):
        """Gets the volume of this Ticker.  # noqa: E501


        :return: The volume of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Ticker.


        :param volume: The volume of this Ticker.  # noqa: E501
        :type: str
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    @property
    def quote_volume(self):
        """Gets the quote_volume of this Ticker.  # noqa: E501


        :return: The quote_volume of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._quote_volume

    @quote_volume.setter
    def quote_volume(self, quote_volume):
        """Sets the quote_volume of this Ticker.


        :param quote_volume: The quote_volume of this Ticker.  # noqa: E501
        :type: str
        """
        if quote_volume is None:
            raise ValueError("Invalid value for `quote_volume`, must not be `None`")  # noqa: E501

        self._quote_volume = quote_volume

    @property
    def open_time(self):
        """Gets the open_time of this Ticker.  # noqa: E501


        :return: The open_time of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._open_time

    @open_time.setter
    def open_time(self, open_time):
        """Sets the open_time of this Ticker.


        :param open_time: The open_time of this Ticker.  # noqa: E501
        :type: int
        """
        if open_time is None:
            raise ValueError("Invalid value for `open_time`, must not be `None`")  # noqa: E501

        self._open_time = open_time

    @property
    def close_time(self):
        """Gets the close_time of this Ticker.  # noqa: E501


        :return: The close_time of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this Ticker.


        :param close_time: The close_time of this Ticker.  # noqa: E501
        :type: int
        """
        if close_time is None:
            raise ValueError("Invalid value for `close_time`, must not be `None`")  # noqa: E501

        self._close_time = close_time

    @property
    def first_id(self):
        """Gets the first_id of this Ticker.  # noqa: E501


        :return: The first_id of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._first_id

    @first_id.setter
    def first_id(self, first_id):
        """Sets the first_id of this Ticker.


        :param first_id: The first_id of this Ticker.  # noqa: E501
        :type: int
        """
        if first_id is None:
            raise ValueError("Invalid value for `first_id`, must not be `None`")  # noqa: E501

        self._first_id = first_id

    @property
    def last_id(self):
        """Gets the last_id of this Ticker.  # noqa: E501


        :return: The last_id of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._last_id

    @last_id.setter
    def last_id(self, last_id):
        """Sets the last_id of this Ticker.


        :param last_id: The last_id of this Ticker.  # noqa: E501
        :type: int
        """
        if last_id is None:
            raise ValueError("Invalid value for `last_id`, must not be `None`")  # noqa: E501

        self._last_id = last_id

    @property
    def count(self):
        """Gets the count of this Ticker.  # noqa: E501


        :return: The count of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Ticker.


        :param count: The count of this Ticker.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

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
        if issubclass(Ticker, dict):
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
        if not isinstance(other, Ticker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
