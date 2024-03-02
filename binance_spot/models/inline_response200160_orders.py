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

class InlineResponse200160Orders(object):
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
        'algo_id': 'int',
        'symbol': 'str',
        'side': 'str',
        'total_qty': 'str',
        'executed_qty': 'str',
        'executed_amt': 'str',
        'avg_price': 'str',
        'client_algo_id': 'str',
        'book_time': 'int',
        'end_time': 'int',
        'algo_status': 'str',
        'algo_type': 'str',
        'urgency': 'str'
    }

    attribute_map = {
        'algo_id': 'algoId',
        'symbol': 'symbol',
        'side': 'side',
        'total_qty': 'totalQty',
        'executed_qty': 'executedQty',
        'executed_amt': 'executedAmt',
        'avg_price': 'avgPrice',
        'client_algo_id': 'clientAlgoId',
        'book_time': 'bookTime',
        'end_time': 'endTime',
        'algo_status': 'algoStatus',
        'algo_type': 'algoType',
        'urgency': 'urgency'
    }

    def __init__(self, algo_id=None, symbol=None, side=None, total_qty=None, executed_qty=None, executed_amt=None, avg_price=None, client_algo_id=None, book_time=None, end_time=None, algo_status=None, algo_type=None, urgency=None):  # noqa: E501
        """InlineResponse200160Orders - a model defined in Swagger"""  # noqa: E501
        self._algo_id = None
        self._symbol = None
        self._side = None
        self._total_qty = None
        self._executed_qty = None
        self._executed_amt = None
        self._avg_price = None
        self._client_algo_id = None
        self._book_time = None
        self._end_time = None
        self._algo_status = None
        self._algo_type = None
        self._urgency = None
        self.discriminator = None
        self.algo_id = algo_id
        self.symbol = symbol
        self.side = side
        self.total_qty = total_qty
        self.executed_qty = executed_qty
        self.executed_amt = executed_amt
        self.avg_price = avg_price
        self.client_algo_id = client_algo_id
        self.book_time = book_time
        self.end_time = end_time
        self.algo_status = algo_status
        self.algo_type = algo_type
        self.urgency = urgency

    @property
    def algo_id(self):
        """Gets the algo_id of this InlineResponse200160Orders.  # noqa: E501


        :return: The algo_id of this InlineResponse200160Orders.  # noqa: E501
        :rtype: int
        """
        return self._algo_id

    @algo_id.setter
    def algo_id(self, algo_id):
        """Sets the algo_id of this InlineResponse200160Orders.


        :param algo_id: The algo_id of this InlineResponse200160Orders.  # noqa: E501
        :type: int
        """
        if algo_id is None:
            raise ValueError("Invalid value for `algo_id`, must not be `None`")  # noqa: E501

        self._algo_id = algo_id

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse200160Orders.  # noqa: E501


        :return: The symbol of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse200160Orders.


        :param symbol: The symbol of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def side(self):
        """Gets the side of this InlineResponse200160Orders.  # noqa: E501


        :return: The side of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this InlineResponse200160Orders.


        :param side: The side of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def total_qty(self):
        """Gets the total_qty of this InlineResponse200160Orders.  # noqa: E501


        :return: The total_qty of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._total_qty

    @total_qty.setter
    def total_qty(self, total_qty):
        """Sets the total_qty of this InlineResponse200160Orders.


        :param total_qty: The total_qty of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if total_qty is None:
            raise ValueError("Invalid value for `total_qty`, must not be `None`")  # noqa: E501

        self._total_qty = total_qty

    @property
    def executed_qty(self):
        """Gets the executed_qty of this InlineResponse200160Orders.  # noqa: E501


        :return: The executed_qty of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._executed_qty

    @executed_qty.setter
    def executed_qty(self, executed_qty):
        """Sets the executed_qty of this InlineResponse200160Orders.


        :param executed_qty: The executed_qty of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if executed_qty is None:
            raise ValueError("Invalid value for `executed_qty`, must not be `None`")  # noqa: E501

        self._executed_qty = executed_qty

    @property
    def executed_amt(self):
        """Gets the executed_amt of this InlineResponse200160Orders.  # noqa: E501


        :return: The executed_amt of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._executed_amt

    @executed_amt.setter
    def executed_amt(self, executed_amt):
        """Sets the executed_amt of this InlineResponse200160Orders.


        :param executed_amt: The executed_amt of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if executed_amt is None:
            raise ValueError("Invalid value for `executed_amt`, must not be `None`")  # noqa: E501

        self._executed_amt = executed_amt

    @property
    def avg_price(self):
        """Gets the avg_price of this InlineResponse200160Orders.  # noqa: E501


        :return: The avg_price of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._avg_price

    @avg_price.setter
    def avg_price(self, avg_price):
        """Sets the avg_price of this InlineResponse200160Orders.


        :param avg_price: The avg_price of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if avg_price is None:
            raise ValueError("Invalid value for `avg_price`, must not be `None`")  # noqa: E501

        self._avg_price = avg_price

    @property
    def client_algo_id(self):
        """Gets the client_algo_id of this InlineResponse200160Orders.  # noqa: E501


        :return: The client_algo_id of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._client_algo_id

    @client_algo_id.setter
    def client_algo_id(self, client_algo_id):
        """Sets the client_algo_id of this InlineResponse200160Orders.


        :param client_algo_id: The client_algo_id of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if client_algo_id is None:
            raise ValueError("Invalid value for `client_algo_id`, must not be `None`")  # noqa: E501

        self._client_algo_id = client_algo_id

    @property
    def book_time(self):
        """Gets the book_time of this InlineResponse200160Orders.  # noqa: E501


        :return: The book_time of this InlineResponse200160Orders.  # noqa: E501
        :rtype: int
        """
        return self._book_time

    @book_time.setter
    def book_time(self, book_time):
        """Sets the book_time of this InlineResponse200160Orders.


        :param book_time: The book_time of this InlineResponse200160Orders.  # noqa: E501
        :type: int
        """
        if book_time is None:
            raise ValueError("Invalid value for `book_time`, must not be `None`")  # noqa: E501

        self._book_time = book_time

    @property
    def end_time(self):
        """Gets the end_time of this InlineResponse200160Orders.  # noqa: E501


        :return: The end_time of this InlineResponse200160Orders.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InlineResponse200160Orders.


        :param end_time: The end_time of this InlineResponse200160Orders.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def algo_status(self):
        """Gets the algo_status of this InlineResponse200160Orders.  # noqa: E501


        :return: The algo_status of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._algo_status

    @algo_status.setter
    def algo_status(self, algo_status):
        """Sets the algo_status of this InlineResponse200160Orders.


        :param algo_status: The algo_status of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if algo_status is None:
            raise ValueError("Invalid value for `algo_status`, must not be `None`")  # noqa: E501

        self._algo_status = algo_status

    @property
    def algo_type(self):
        """Gets the algo_type of this InlineResponse200160Orders.  # noqa: E501


        :return: The algo_type of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._algo_type

    @algo_type.setter
    def algo_type(self, algo_type):
        """Sets the algo_type of this InlineResponse200160Orders.


        :param algo_type: The algo_type of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if algo_type is None:
            raise ValueError("Invalid value for `algo_type`, must not be `None`")  # noqa: E501

        self._algo_type = algo_type

    @property
    def urgency(self):
        """Gets the urgency of this InlineResponse200160Orders.  # noqa: E501


        :return: The urgency of this InlineResponse200160Orders.  # noqa: E501
        :rtype: str
        """
        return self._urgency

    @urgency.setter
    def urgency(self, urgency):
        """Sets the urgency of this InlineResponse200160Orders.


        :param urgency: The urgency of this InlineResponse200160Orders.  # noqa: E501
        :type: str
        """
        if urgency is None:
            raise ValueError("Invalid value for `urgency`, must not be `None`")  # noqa: E501

        self._urgency = urgency

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
        if issubclass(InlineResponse200160Orders, dict):
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
        if not isinstance(other, InlineResponse200160Orders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other