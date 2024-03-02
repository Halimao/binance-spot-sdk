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

class InlineResponse20028Rows(object):
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
        'avg_price': 'str',
        'executed_qty': 'str',
        'order_id': 'int',
        'price': 'str',
        'qty': 'str',
        'side': 'str',
        'symbol': 'str',
        'time_in_force': 'str',
        'is_isolated': 'bool',
        'updated_time': 'int'
    }

    attribute_map = {
        'avg_price': 'avgPrice',
        'executed_qty': 'executedQty',
        'order_id': 'orderId',
        'price': 'price',
        'qty': 'qty',
        'side': 'side',
        'symbol': 'symbol',
        'time_in_force': 'timeInForce',
        'is_isolated': 'isIsolated',
        'updated_time': 'updatedTime'
    }

    def __init__(self, avg_price=None, executed_qty=None, order_id=None, price=None, qty=None, side=None, symbol=None, time_in_force=None, is_isolated=None, updated_time=None):  # noqa: E501
        """InlineResponse20028Rows - a model defined in Swagger"""  # noqa: E501
        self._avg_price = None
        self._executed_qty = None
        self._order_id = None
        self._price = None
        self._qty = None
        self._side = None
        self._symbol = None
        self._time_in_force = None
        self._is_isolated = None
        self._updated_time = None
        self.discriminator = None
        self.avg_price = avg_price
        self.executed_qty = executed_qty
        self.order_id = order_id
        self.price = price
        self.qty = qty
        self.side = side
        self.symbol = symbol
        self.time_in_force = time_in_force
        self.is_isolated = is_isolated
        self.updated_time = updated_time

    @property
    def avg_price(self):
        """Gets the avg_price of this InlineResponse20028Rows.  # noqa: E501


        :return: The avg_price of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._avg_price

    @avg_price.setter
    def avg_price(self, avg_price):
        """Sets the avg_price of this InlineResponse20028Rows.


        :param avg_price: The avg_price of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if avg_price is None:
            raise ValueError("Invalid value for `avg_price`, must not be `None`")  # noqa: E501

        self._avg_price = avg_price

    @property
    def executed_qty(self):
        """Gets the executed_qty of this InlineResponse20028Rows.  # noqa: E501


        :return: The executed_qty of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._executed_qty

    @executed_qty.setter
    def executed_qty(self, executed_qty):
        """Sets the executed_qty of this InlineResponse20028Rows.


        :param executed_qty: The executed_qty of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if executed_qty is None:
            raise ValueError("Invalid value for `executed_qty`, must not be `None`")  # noqa: E501

        self._executed_qty = executed_qty

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse20028Rows.  # noqa: E501


        :return: The order_id of this InlineResponse20028Rows.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse20028Rows.


        :param order_id: The order_id of this InlineResponse20028Rows.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def price(self):
        """Gets the price of this InlineResponse20028Rows.  # noqa: E501


        :return: The price of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse20028Rows.


        :param price: The price of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this InlineResponse20028Rows.  # noqa: E501


        :return: The qty of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this InlineResponse20028Rows.


        :param qty: The qty of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def side(self):
        """Gets the side of this InlineResponse20028Rows.  # noqa: E501


        :return: The side of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this InlineResponse20028Rows.


        :param side: The side of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse20028Rows.  # noqa: E501


        :return: The symbol of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse20028Rows.


        :param symbol: The symbol of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def time_in_force(self):
        """Gets the time_in_force of this InlineResponse20028Rows.  # noqa: E501


        :return: The time_in_force of this InlineResponse20028Rows.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this InlineResponse20028Rows.


        :param time_in_force: The time_in_force of this InlineResponse20028Rows.  # noqa: E501
        :type: str
        """
        if time_in_force is None:
            raise ValueError("Invalid value for `time_in_force`, must not be `None`")  # noqa: E501

        self._time_in_force = time_in_force

    @property
    def is_isolated(self):
        """Gets the is_isolated of this InlineResponse20028Rows.  # noqa: E501


        :return: The is_isolated of this InlineResponse20028Rows.  # noqa: E501
        :rtype: bool
        """
        return self._is_isolated

    @is_isolated.setter
    def is_isolated(self, is_isolated):
        """Sets the is_isolated of this InlineResponse20028Rows.


        :param is_isolated: The is_isolated of this InlineResponse20028Rows.  # noqa: E501
        :type: bool
        """
        if is_isolated is None:
            raise ValueError("Invalid value for `is_isolated`, must not be `None`")  # noqa: E501

        self._is_isolated = is_isolated

    @property
    def updated_time(self):
        """Gets the updated_time of this InlineResponse20028Rows.  # noqa: E501


        :return: The updated_time of this InlineResponse20028Rows.  # noqa: E501
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this InlineResponse20028Rows.


        :param updated_time: The updated_time of this InlineResponse20028Rows.  # noqa: E501
        :type: int
        """
        if updated_time is None:
            raise ValueError("Invalid value for `updated_time`, must not be `None`")  # noqa: E501

        self._updated_time = updated_time

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
        if issubclass(InlineResponse20028Rows, dict):
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
        if not isinstance(other, InlineResponse20028Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other