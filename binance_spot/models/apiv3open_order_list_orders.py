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

class Apiv3openOrderListOrders(object):
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
        'client_order_id': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'order_id': 'orderId',
        'client_order_id': 'clientOrderId'
    }

    def __init__(self, symbol=None, order_id=None, client_order_id=None):  # noqa: E501
        """Apiv3openOrderListOrders - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._order_id = None
        self._client_order_id = None
        self.discriminator = None
        self.symbol = symbol
        self.order_id = order_id
        self.client_order_id = client_order_id

    @property
    def symbol(self):
        """Gets the symbol of this Apiv3openOrderListOrders.  # noqa: E501


        :return: The symbol of this Apiv3openOrderListOrders.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Apiv3openOrderListOrders.


        :param symbol: The symbol of this Apiv3openOrderListOrders.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def order_id(self):
        """Gets the order_id of this Apiv3openOrderListOrders.  # noqa: E501


        :return: The order_id of this Apiv3openOrderListOrders.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Apiv3openOrderListOrders.


        :param order_id: The order_id of this Apiv3openOrderListOrders.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def client_order_id(self):
        """Gets the client_order_id of this Apiv3openOrderListOrders.  # noqa: E501


        :return: The client_order_id of this Apiv3openOrderListOrders.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this Apiv3openOrderListOrders.


        :param client_order_id: The client_order_id of this Apiv3openOrderListOrders.  # noqa: E501
        :type: str
        """
        if client_order_id is None:
            raise ValueError("Invalid value for `client_order_id`, must not be `None`")  # noqa: E501

        self._client_order_id = client_order_id

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
        if issubclass(Apiv3openOrderListOrders, dict):
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
        if not isinstance(other, Apiv3openOrderListOrders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
