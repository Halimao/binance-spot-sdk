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

class InlineResponse200209Rows(object):
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
        'loan_coin': 'str',
        'collateral_coin': 'str',
        'direction': 'str',
        'amount': 'str',
        'pre_ltv': 'str',
        'after_ltv': 'str',
        'adjust_time': 'int',
        'order_id': 'int'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'collateral_coin': 'collateralCoin',
        'direction': 'direction',
        'amount': 'amount',
        'pre_ltv': 'preLTV',
        'after_ltv': 'afterLTV',
        'adjust_time': 'adjustTime',
        'order_id': 'orderId'
    }

    def __init__(self, loan_coin=None, collateral_coin=None, direction=None, amount=None, pre_ltv=None, after_ltv=None, adjust_time=None, order_id=None):  # noqa: E501
        """InlineResponse200209Rows - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._collateral_coin = None
        self._direction = None
        self._amount = None
        self._pre_ltv = None
        self._after_ltv = None
        self._adjust_time = None
        self._order_id = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.collateral_coin = collateral_coin
        self.direction = direction
        self.amount = amount
        self.pre_ltv = pre_ltv
        self.after_ltv = after_ltv
        self.adjust_time = adjust_time
        self.order_id = order_id

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200209Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200209Rows.


        :param loan_coin: The loan_coin of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200209Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200209Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def direction(self):
        """Gets the direction of this InlineResponse200209Rows.  # noqa: E501


        :return: The direction of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this InlineResponse200209Rows.


        :param direction: The direction of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200209Rows.  # noqa: E501


        :return: The amount of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200209Rows.


        :param amount: The amount of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def pre_ltv(self):
        """Gets the pre_ltv of this InlineResponse200209Rows.  # noqa: E501


        :return: The pre_ltv of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._pre_ltv

    @pre_ltv.setter
    def pre_ltv(self, pre_ltv):
        """Sets the pre_ltv of this InlineResponse200209Rows.


        :param pre_ltv: The pre_ltv of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if pre_ltv is None:
            raise ValueError("Invalid value for `pre_ltv`, must not be `None`")  # noqa: E501

        self._pre_ltv = pre_ltv

    @property
    def after_ltv(self):
        """Gets the after_ltv of this InlineResponse200209Rows.  # noqa: E501


        :return: The after_ltv of this InlineResponse200209Rows.  # noqa: E501
        :rtype: str
        """
        return self._after_ltv

    @after_ltv.setter
    def after_ltv(self, after_ltv):
        """Sets the after_ltv of this InlineResponse200209Rows.


        :param after_ltv: The after_ltv of this InlineResponse200209Rows.  # noqa: E501
        :type: str
        """
        if after_ltv is None:
            raise ValueError("Invalid value for `after_ltv`, must not be `None`")  # noqa: E501

        self._after_ltv = after_ltv

    @property
    def adjust_time(self):
        """Gets the adjust_time of this InlineResponse200209Rows.  # noqa: E501


        :return: The adjust_time of this InlineResponse200209Rows.  # noqa: E501
        :rtype: int
        """
        return self._adjust_time

    @adjust_time.setter
    def adjust_time(self, adjust_time):
        """Sets the adjust_time of this InlineResponse200209Rows.


        :param adjust_time: The adjust_time of this InlineResponse200209Rows.  # noqa: E501
        :type: int
        """
        if adjust_time is None:
            raise ValueError("Invalid value for `adjust_time`, must not be `None`")  # noqa: E501

        self._adjust_time = adjust_time

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse200209Rows.  # noqa: E501


        :return: The order_id of this InlineResponse200209Rows.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse200209Rows.


        :param order_id: The order_id of this InlineResponse200209Rows.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if issubclass(InlineResponse200209Rows, dict):
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
        if not isinstance(other, InlineResponse200209Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other