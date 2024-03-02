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

class MyTrade(object):
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
        'id': 'int',
        'order_id': 'int',
        'order_list_id': 'int',
        'price': 'str',
        'qty': 'str',
        'quote_qty': 'str',
        'commission': 'str',
        'commission_asset': 'str',
        'time': 'int',
        'is_buyer': 'bool',
        'is_maker': 'bool',
        'is_best_match': 'bool'
    }

    attribute_map = {
        'symbol': 'symbol',
        'id': 'id',
        'order_id': 'orderId',
        'order_list_id': 'orderListId',
        'price': 'price',
        'qty': 'qty',
        'quote_qty': 'quoteQty',
        'commission': 'commission',
        'commission_asset': 'commissionAsset',
        'time': 'time',
        'is_buyer': 'isBuyer',
        'is_maker': 'isMaker',
        'is_best_match': 'isBestMatch'
    }

    def __init__(self, symbol=None, id=None, order_id=None, order_list_id=None, price=None, qty=None, quote_qty=None, commission=None, commission_asset=None, time=None, is_buyer=None, is_maker=None, is_best_match=None):  # noqa: E501
        """MyTrade - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._id = None
        self._order_id = None
        self._order_list_id = None
        self._price = None
        self._qty = None
        self._quote_qty = None
        self._commission = None
        self._commission_asset = None
        self._time = None
        self._is_buyer = None
        self._is_maker = None
        self._is_best_match = None
        self.discriminator = None
        self.symbol = symbol
        self.id = id
        self.order_id = order_id
        self.order_list_id = order_list_id
        self.price = price
        self.qty = qty
        self.quote_qty = quote_qty
        self.commission = commission
        self.commission_asset = commission_asset
        self.time = time
        self.is_buyer = is_buyer
        self.is_maker = is_maker
        self.is_best_match = is_best_match

    @property
    def symbol(self):
        """Gets the symbol of this MyTrade.  # noqa: E501


        :return: The symbol of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this MyTrade.


        :param symbol: The symbol of this MyTrade.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def id(self):
        """Gets the id of this MyTrade.  # noqa: E501

        Trade id  # noqa: E501

        :return: The id of this MyTrade.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MyTrade.

        Trade id  # noqa: E501

        :param id: The id of this MyTrade.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this MyTrade.  # noqa: E501


        :return: The order_id of this MyTrade.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MyTrade.


        :param order_id: The order_id of this MyTrade.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_list_id(self):
        """Gets the order_list_id of this MyTrade.  # noqa: E501


        :return: The order_list_id of this MyTrade.  # noqa: E501
        :rtype: int
        """
        return self._order_list_id

    @order_list_id.setter
    def order_list_id(self, order_list_id):
        """Sets the order_list_id of this MyTrade.


        :param order_list_id: The order_list_id of this MyTrade.  # noqa: E501
        :type: int
        """
        if order_list_id is None:
            raise ValueError("Invalid value for `order_list_id`, must not be `None`")  # noqa: E501

        self._order_list_id = order_list_id

    @property
    def price(self):
        """Gets the price of this MyTrade.  # noqa: E501

        Price  # noqa: E501

        :return: The price of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MyTrade.

        Price  # noqa: E501

        :param price: The price of this MyTrade.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this MyTrade.  # noqa: E501

        Amount of base asset  # noqa: E501

        :return: The qty of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this MyTrade.

        Amount of base asset  # noqa: E501

        :param qty: The qty of this MyTrade.  # noqa: E501
        :type: str
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def quote_qty(self):
        """Gets the quote_qty of this MyTrade.  # noqa: E501

        Amount of quote asset  # noqa: E501

        :return: The quote_qty of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._quote_qty

    @quote_qty.setter
    def quote_qty(self, quote_qty):
        """Sets the quote_qty of this MyTrade.

        Amount of quote asset  # noqa: E501

        :param quote_qty: The quote_qty of this MyTrade.  # noqa: E501
        :type: str
        """
        if quote_qty is None:
            raise ValueError("Invalid value for `quote_qty`, must not be `None`")  # noqa: E501

        self._quote_qty = quote_qty

    @property
    def commission(self):
        """Gets the commission of this MyTrade.  # noqa: E501


        :return: The commission of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this MyTrade.


        :param commission: The commission of this MyTrade.  # noqa: E501
        :type: str
        """
        if commission is None:
            raise ValueError("Invalid value for `commission`, must not be `None`")  # noqa: E501

        self._commission = commission

    @property
    def commission_asset(self):
        """Gets the commission_asset of this MyTrade.  # noqa: E501


        :return: The commission_asset of this MyTrade.  # noqa: E501
        :rtype: str
        """
        return self._commission_asset

    @commission_asset.setter
    def commission_asset(self, commission_asset):
        """Sets the commission_asset of this MyTrade.


        :param commission_asset: The commission_asset of this MyTrade.  # noqa: E501
        :type: str
        """
        if commission_asset is None:
            raise ValueError("Invalid value for `commission_asset`, must not be `None`")  # noqa: E501

        self._commission_asset = commission_asset

    @property
    def time(self):
        """Gets the time of this MyTrade.  # noqa: E501

        Trade timestamp  # noqa: E501

        :return: The time of this MyTrade.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MyTrade.

        Trade timestamp  # noqa: E501

        :param time: The time of this MyTrade.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def is_buyer(self):
        """Gets the is_buyer of this MyTrade.  # noqa: E501


        :return: The is_buyer of this MyTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_buyer

    @is_buyer.setter
    def is_buyer(self, is_buyer):
        """Sets the is_buyer of this MyTrade.


        :param is_buyer: The is_buyer of this MyTrade.  # noqa: E501
        :type: bool
        """
        if is_buyer is None:
            raise ValueError("Invalid value for `is_buyer`, must not be `None`")  # noqa: E501

        self._is_buyer = is_buyer

    @property
    def is_maker(self):
        """Gets the is_maker of this MyTrade.  # noqa: E501


        :return: The is_maker of this MyTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_maker

    @is_maker.setter
    def is_maker(self, is_maker):
        """Sets the is_maker of this MyTrade.


        :param is_maker: The is_maker of this MyTrade.  # noqa: E501
        :type: bool
        """
        if is_maker is None:
            raise ValueError("Invalid value for `is_maker`, must not be `None`")  # noqa: E501

        self._is_maker = is_maker

    @property
    def is_best_match(self):
        """Gets the is_best_match of this MyTrade.  # noqa: E501


        :return: The is_best_match of this MyTrade.  # noqa: E501
        :rtype: bool
        """
        return self._is_best_match

    @is_best_match.setter
    def is_best_match(self, is_best_match):
        """Sets the is_best_match of this MyTrade.


        :param is_best_match: The is_best_match of this MyTrade.  # noqa: E501
        :type: bool
        """
        if is_best_match is None:
            raise ValueError("Invalid value for `is_best_match`, must not be `None`")  # noqa: E501

        self._is_best_match = is_best_match

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
        if issubclass(MyTrade, dict):
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
        if not isinstance(other, MyTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other