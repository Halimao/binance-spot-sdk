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

class OrderDetails(object):
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
        'order_id': 'int',
        'order_list_id': 'int',
        'client_order_id': 'str',
        'price': 'str',
        'orig_qty': 'str',
        'executed_qty': 'str',
        'cummulative_quote_qty': 'str',
        'status': 'str',
        'time_in_force': 'str',
        'type': 'str',
        'side': 'str',
        'stop_price': 'str',
        'iceberg_qty': 'str',
        'time': 'int',
        'update_time': 'int',
        'is_working': 'bool',
        'working_time': 'int',
        'orig_quote_order_qty': 'str',
        'self_trade_prevention_mode': 'str',
        'prevented_match_id': 'int',
        'prevented_quantity': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'order_id': 'orderId',
        'order_list_id': 'orderListId',
        'client_order_id': 'clientOrderId',
        'price': 'price',
        'orig_qty': 'origQty',
        'executed_qty': 'executedQty',
        'cummulative_quote_qty': 'cummulativeQuoteQty',
        'status': 'status',
        'time_in_force': 'timeInForce',
        'type': 'type',
        'side': 'side',
        'stop_price': 'stopPrice',
        'iceberg_qty': 'icebergQty',
        'time': 'time',
        'update_time': 'updateTime',
        'is_working': 'isWorking',
        'working_time': 'workingTime',
        'orig_quote_order_qty': 'origQuoteOrderQty',
        'self_trade_prevention_mode': 'selfTradePreventionMode',
        'prevented_match_id': 'preventedMatchId',
        'prevented_quantity': 'preventedQuantity'
    }

    def __init__(self, symbol=None, order_id=None, order_list_id=None, client_order_id=None, price=None, orig_qty=None, executed_qty=None, cummulative_quote_qty=None, status=None, time_in_force=None, type=None, side=None, stop_price=None, iceberg_qty=None, time=None, update_time=None, is_working=None, working_time=None, orig_quote_order_qty=None, self_trade_prevention_mode=None, prevented_match_id=None, prevented_quantity=None):  # noqa: E501
        """OrderDetails - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._order_id = None
        self._order_list_id = None
        self._client_order_id = None
        self._price = None
        self._orig_qty = None
        self._executed_qty = None
        self._cummulative_quote_qty = None
        self._status = None
        self._time_in_force = None
        self._type = None
        self._side = None
        self._stop_price = None
        self._iceberg_qty = None
        self._time = None
        self._update_time = None
        self._is_working = None
        self._working_time = None
        self._orig_quote_order_qty = None
        self._self_trade_prevention_mode = None
        self._prevented_match_id = None
        self._prevented_quantity = None
        self.discriminator = None
        self.symbol = symbol
        self.order_id = order_id
        self.order_list_id = order_list_id
        self.client_order_id = client_order_id
        self.price = price
        self.orig_qty = orig_qty
        self.executed_qty = executed_qty
        self.cummulative_quote_qty = cummulative_quote_qty
        self.status = status
        self.time_in_force = time_in_force
        self.type = type
        self.side = side
        self.stop_price = stop_price
        self.iceberg_qty = iceberg_qty
        self.time = time
        self.update_time = update_time
        self.is_working = is_working
        self.working_time = working_time
        self.orig_quote_order_qty = orig_quote_order_qty
        self.self_trade_prevention_mode = self_trade_prevention_mode
        if prevented_match_id is not None:
            self.prevented_match_id = prevented_match_id
        if prevented_quantity is not None:
            self.prevented_quantity = prevented_quantity

    @property
    def symbol(self):
        """Gets the symbol of this OrderDetails.  # noqa: E501


        :return: The symbol of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this OrderDetails.


        :param symbol: The symbol of this OrderDetails.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def order_id(self):
        """Gets the order_id of this OrderDetails.  # noqa: E501


        :return: The order_id of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderDetails.


        :param order_id: The order_id of this OrderDetails.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_list_id(self):
        """Gets the order_list_id of this OrderDetails.  # noqa: E501

        Unless OCO, value will be -1  # noqa: E501

        :return: The order_list_id of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._order_list_id

    @order_list_id.setter
    def order_list_id(self, order_list_id):
        """Sets the order_list_id of this OrderDetails.

        Unless OCO, value will be -1  # noqa: E501

        :param order_list_id: The order_list_id of this OrderDetails.  # noqa: E501
        :type: int
        """
        if order_list_id is None:
            raise ValueError("Invalid value for `order_list_id`, must not be `None`")  # noqa: E501

        self._order_list_id = order_list_id

    @property
    def client_order_id(self):
        """Gets the client_order_id of this OrderDetails.  # noqa: E501


        :return: The client_order_id of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this OrderDetails.


        :param client_order_id: The client_order_id of this OrderDetails.  # noqa: E501
        :type: str
        """
        if client_order_id is None:
            raise ValueError("Invalid value for `client_order_id`, must not be `None`")  # noqa: E501

        self._client_order_id = client_order_id

    @property
    def price(self):
        """Gets the price of this OrderDetails.  # noqa: E501


        :return: The price of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderDetails.


        :param price: The price of this OrderDetails.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def orig_qty(self):
        """Gets the orig_qty of this OrderDetails.  # noqa: E501


        :return: The orig_qty of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._orig_qty

    @orig_qty.setter
    def orig_qty(self, orig_qty):
        """Sets the orig_qty of this OrderDetails.


        :param orig_qty: The orig_qty of this OrderDetails.  # noqa: E501
        :type: str
        """
        if orig_qty is None:
            raise ValueError("Invalid value for `orig_qty`, must not be `None`")  # noqa: E501

        self._orig_qty = orig_qty

    @property
    def executed_qty(self):
        """Gets the executed_qty of this OrderDetails.  # noqa: E501


        :return: The executed_qty of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._executed_qty

    @executed_qty.setter
    def executed_qty(self, executed_qty):
        """Sets the executed_qty of this OrderDetails.


        :param executed_qty: The executed_qty of this OrderDetails.  # noqa: E501
        :type: str
        """
        if executed_qty is None:
            raise ValueError("Invalid value for `executed_qty`, must not be `None`")  # noqa: E501

        self._executed_qty = executed_qty

    @property
    def cummulative_quote_qty(self):
        """Gets the cummulative_quote_qty of this OrderDetails.  # noqa: E501


        :return: The cummulative_quote_qty of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._cummulative_quote_qty

    @cummulative_quote_qty.setter
    def cummulative_quote_qty(self, cummulative_quote_qty):
        """Sets the cummulative_quote_qty of this OrderDetails.


        :param cummulative_quote_qty: The cummulative_quote_qty of this OrderDetails.  # noqa: E501
        :type: str
        """
        if cummulative_quote_qty is None:
            raise ValueError("Invalid value for `cummulative_quote_qty`, must not be `None`")  # noqa: E501

        self._cummulative_quote_qty = cummulative_quote_qty

    @property
    def status(self):
        """Gets the status of this OrderDetails.  # noqa: E501


        :return: The status of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderDetails.


        :param status: The status of this OrderDetails.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def time_in_force(self):
        """Gets the time_in_force of this OrderDetails.  # noqa: E501


        :return: The time_in_force of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this OrderDetails.


        :param time_in_force: The time_in_force of this OrderDetails.  # noqa: E501
        :type: str
        """
        if time_in_force is None:
            raise ValueError("Invalid value for `time_in_force`, must not be `None`")  # noqa: E501

        self._time_in_force = time_in_force

    @property
    def type(self):
        """Gets the type of this OrderDetails.  # noqa: E501


        :return: The type of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrderDetails.


        :param type: The type of this OrderDetails.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def side(self):
        """Gets the side of this OrderDetails.  # noqa: E501


        :return: The side of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderDetails.


        :param side: The side of this OrderDetails.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def stop_price(self):
        """Gets the stop_price of this OrderDetails.  # noqa: E501


        :return: The stop_price of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this OrderDetails.


        :param stop_price: The stop_price of this OrderDetails.  # noqa: E501
        :type: str
        """
        if stop_price is None:
            raise ValueError("Invalid value for `stop_price`, must not be `None`")  # noqa: E501

        self._stop_price = stop_price

    @property
    def iceberg_qty(self):
        """Gets the iceberg_qty of this OrderDetails.  # noqa: E501


        :return: The iceberg_qty of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._iceberg_qty

    @iceberg_qty.setter
    def iceberg_qty(self, iceberg_qty):
        """Sets the iceberg_qty of this OrderDetails.


        :param iceberg_qty: The iceberg_qty of this OrderDetails.  # noqa: E501
        :type: str
        """
        if iceberg_qty is None:
            raise ValueError("Invalid value for `iceberg_qty`, must not be `None`")  # noqa: E501

        self._iceberg_qty = iceberg_qty

    @property
    def time(self):
        """Gets the time of this OrderDetails.  # noqa: E501


        :return: The time of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OrderDetails.


        :param time: The time of this OrderDetails.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def update_time(self):
        """Gets the update_time of this OrderDetails.  # noqa: E501


        :return: The update_time of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this OrderDetails.


        :param update_time: The update_time of this OrderDetails.  # noqa: E501
        :type: int
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def is_working(self):
        """Gets the is_working of this OrderDetails.  # noqa: E501


        :return: The is_working of this OrderDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_working

    @is_working.setter
    def is_working(self, is_working):
        """Sets the is_working of this OrderDetails.


        :param is_working: The is_working of this OrderDetails.  # noqa: E501
        :type: bool
        """
        if is_working is None:
            raise ValueError("Invalid value for `is_working`, must not be `None`")  # noqa: E501

        self._is_working = is_working

    @property
    def working_time(self):
        """Gets the working_time of this OrderDetails.  # noqa: E501


        :return: The working_time of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._working_time

    @working_time.setter
    def working_time(self, working_time):
        """Sets the working_time of this OrderDetails.


        :param working_time: The working_time of this OrderDetails.  # noqa: E501
        :type: int
        """
        if working_time is None:
            raise ValueError("Invalid value for `working_time`, must not be `None`")  # noqa: E501

        self._working_time = working_time

    @property
    def orig_quote_order_qty(self):
        """Gets the orig_quote_order_qty of this OrderDetails.  # noqa: E501


        :return: The orig_quote_order_qty of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._orig_quote_order_qty

    @orig_quote_order_qty.setter
    def orig_quote_order_qty(self, orig_quote_order_qty):
        """Sets the orig_quote_order_qty of this OrderDetails.


        :param orig_quote_order_qty: The orig_quote_order_qty of this OrderDetails.  # noqa: E501
        :type: str
        """
        if orig_quote_order_qty is None:
            raise ValueError("Invalid value for `orig_quote_order_qty`, must not be `None`")  # noqa: E501

        self._orig_quote_order_qty = orig_quote_order_qty

    @property
    def self_trade_prevention_mode(self):
        """Gets the self_trade_prevention_mode of this OrderDetails.  # noqa: E501


        :return: The self_trade_prevention_mode of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._self_trade_prevention_mode

    @self_trade_prevention_mode.setter
    def self_trade_prevention_mode(self, self_trade_prevention_mode):
        """Sets the self_trade_prevention_mode of this OrderDetails.


        :param self_trade_prevention_mode: The self_trade_prevention_mode of this OrderDetails.  # noqa: E501
        :type: str
        """
        if self_trade_prevention_mode is None:
            raise ValueError("Invalid value for `self_trade_prevention_mode`, must not be `None`")  # noqa: E501

        self._self_trade_prevention_mode = self_trade_prevention_mode

    @property
    def prevented_match_id(self):
        """Gets the prevented_match_id of this OrderDetails.  # noqa: E501


        :return: The prevented_match_id of this OrderDetails.  # noqa: E501
        :rtype: int
        """
        return self._prevented_match_id

    @prevented_match_id.setter
    def prevented_match_id(self, prevented_match_id):
        """Sets the prevented_match_id of this OrderDetails.


        :param prevented_match_id: The prevented_match_id of this OrderDetails.  # noqa: E501
        :type: int
        """

        self._prevented_match_id = prevented_match_id

    @property
    def prevented_quantity(self):
        """Gets the prevented_quantity of this OrderDetails.  # noqa: E501


        :return: The prevented_quantity of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._prevented_quantity

    @prevented_quantity.setter
    def prevented_quantity(self, prevented_quantity):
        """Sets the prevented_quantity of this OrderDetails.


        :param prevented_quantity: The prevented_quantity of this OrderDetails.  # noqa: E501
        :type: str
        """

        self._prevented_quantity = prevented_quantity

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
        if issubclass(OrderDetails, dict):
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
        if not isinstance(other, OrderDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
