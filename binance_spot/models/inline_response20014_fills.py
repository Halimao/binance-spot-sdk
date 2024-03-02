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

class InlineResponse20014Fills(object):
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
        'match_type': 'str',
        'price': 'str',
        'qty': 'str',
        'commission': 'str',
        'commission_asset': 'str',
        'trade_id': 'int',
        'alloc_id': 'int'
    }

    attribute_map = {
        'match_type': 'matchType',
        'price': 'price',
        'qty': 'qty',
        'commission': 'commission',
        'commission_asset': 'commissionAsset',
        'trade_id': 'tradeId',
        'alloc_id': 'allocId'
    }

    def __init__(self, match_type=None, price=None, qty=None, commission=None, commission_asset=None, trade_id=None, alloc_id=None):  # noqa: E501
        """InlineResponse20014Fills - a model defined in Swagger"""  # noqa: E501
        self._match_type = None
        self._price = None
        self._qty = None
        self._commission = None
        self._commission_asset = None
        self._trade_id = None
        self._alloc_id = None
        self.discriminator = None
        self.match_type = match_type
        self.price = price
        self.qty = qty
        self.commission = commission
        self.commission_asset = commission_asset
        self.trade_id = trade_id
        self.alloc_id = alloc_id

    @property
    def match_type(self):
        """Gets the match_type of this InlineResponse20014Fills.  # noqa: E501


        :return: The match_type of this InlineResponse20014Fills.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this InlineResponse20014Fills.


        :param match_type: The match_type of this InlineResponse20014Fills.  # noqa: E501
        :type: str
        """
        if match_type is None:
            raise ValueError("Invalid value for `match_type`, must not be `None`")  # noqa: E501

        self._match_type = match_type

    @property
    def price(self):
        """Gets the price of this InlineResponse20014Fills.  # noqa: E501


        :return: The price of this InlineResponse20014Fills.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse20014Fills.


        :param price: The price of this InlineResponse20014Fills.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this InlineResponse20014Fills.  # noqa: E501


        :return: The qty of this InlineResponse20014Fills.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this InlineResponse20014Fills.


        :param qty: The qty of this InlineResponse20014Fills.  # noqa: E501
        :type: str
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")  # noqa: E501

        self._qty = qty

    @property
    def commission(self):
        """Gets the commission of this InlineResponse20014Fills.  # noqa: E501


        :return: The commission of this InlineResponse20014Fills.  # noqa: E501
        :rtype: str
        """
        return self._commission

    @commission.setter
    def commission(self, commission):
        """Sets the commission of this InlineResponse20014Fills.


        :param commission: The commission of this InlineResponse20014Fills.  # noqa: E501
        :type: str
        """
        if commission is None:
            raise ValueError("Invalid value for `commission`, must not be `None`")  # noqa: E501

        self._commission = commission

    @property
    def commission_asset(self):
        """Gets the commission_asset of this InlineResponse20014Fills.  # noqa: E501


        :return: The commission_asset of this InlineResponse20014Fills.  # noqa: E501
        :rtype: str
        """
        return self._commission_asset

    @commission_asset.setter
    def commission_asset(self, commission_asset):
        """Sets the commission_asset of this InlineResponse20014Fills.


        :param commission_asset: The commission_asset of this InlineResponse20014Fills.  # noqa: E501
        :type: str
        """
        if commission_asset is None:
            raise ValueError("Invalid value for `commission_asset`, must not be `None`")  # noqa: E501

        self._commission_asset = commission_asset

    @property
    def trade_id(self):
        """Gets the trade_id of this InlineResponse20014Fills.  # noqa: E501


        :return: The trade_id of this InlineResponse20014Fills.  # noqa: E501
        :rtype: int
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this InlineResponse20014Fills.


        :param trade_id: The trade_id of this InlineResponse20014Fills.  # noqa: E501
        :type: int
        """
        if trade_id is None:
            raise ValueError("Invalid value for `trade_id`, must not be `None`")  # noqa: E501

        self._trade_id = trade_id

    @property
    def alloc_id(self):
        """Gets the alloc_id of this InlineResponse20014Fills.  # noqa: E501


        :return: The alloc_id of this InlineResponse20014Fills.  # noqa: E501
        :rtype: int
        """
        return self._alloc_id

    @alloc_id.setter
    def alloc_id(self, alloc_id):
        """Sets the alloc_id of this InlineResponse20014Fills.


        :param alloc_id: The alloc_id of this InlineResponse20014Fills.  # noqa: E501
        :type: int
        """
        if alloc_id is None:
            raise ValueError("Invalid value for `alloc_id`, must not be `None`")  # noqa: E501

        self._alloc_id = alloc_id

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
        if issubclass(InlineResponse20014Fills, dict):
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
        if not isinstance(other, InlineResponse20014Fills):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other