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

class InlineResponse200219(object):
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
        'adjustment_amount': 'str',
        'current_ltv': 'str',
        'status': 'str'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'collateral_coin': 'collateralCoin',
        'direction': 'direction',
        'adjustment_amount': 'adjustmentAmount',
        'current_ltv': 'currentLTV',
        'status': 'status'
    }

    def __init__(self, loan_coin=None, collateral_coin=None, direction=None, adjustment_amount=None, current_ltv=None, status=None):  # noqa: E501
        """InlineResponse200219 - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._collateral_coin = None
        self._direction = None
        self._adjustment_amount = None
        self._current_ltv = None
        self._status = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.collateral_coin = collateral_coin
        self.direction = direction
        self.adjustment_amount = adjustment_amount
        self.current_ltv = current_ltv
        self.status = status

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200219.  # noqa: E501


        :return: The loan_coin of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200219.


        :param loan_coin: The loan_coin of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200219.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200219.


        :param collateral_coin: The collateral_coin of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def direction(self):
        """Gets the direction of this InlineResponse200219.  # noqa: E501


        :return: The direction of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this InlineResponse200219.


        :param direction: The direction of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def adjustment_amount(self):
        """Gets the adjustment_amount of this InlineResponse200219.  # noqa: E501


        :return: The adjustment_amount of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._adjustment_amount

    @adjustment_amount.setter
    def adjustment_amount(self, adjustment_amount):
        """Sets the adjustment_amount of this InlineResponse200219.


        :param adjustment_amount: The adjustment_amount of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if adjustment_amount is None:
            raise ValueError("Invalid value for `adjustment_amount`, must not be `None`")  # noqa: E501

        self._adjustment_amount = adjustment_amount

    @property
    def current_ltv(self):
        """Gets the current_ltv of this InlineResponse200219.  # noqa: E501


        :return: The current_ltv of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._current_ltv

    @current_ltv.setter
    def current_ltv(self, current_ltv):
        """Sets the current_ltv of this InlineResponse200219.


        :param current_ltv: The current_ltv of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if current_ltv is None:
            raise ValueError("Invalid value for `current_ltv`, must not be `None`")  # noqa: E501

        self._current_ltv = current_ltv

    @property
    def status(self):
        """Gets the status of this InlineResponse200219.  # noqa: E501


        :return: The status of this InlineResponse200219.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200219.


        :param status: The status of this InlineResponse200219.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(InlineResponse200219, dict):
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
        if not isinstance(other, InlineResponse200219):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other