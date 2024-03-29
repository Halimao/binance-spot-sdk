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

class InlineResponse200212(object):
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
        'repay_amount': 'str',
        'rate': 'str'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'collateral_coin': 'collateralCoin',
        'repay_amount': 'repayAmount',
        'rate': 'rate'
    }

    def __init__(self, loan_coin=None, collateral_coin=None, repay_amount=None, rate=None):  # noqa: E501
        """InlineResponse200212 - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._collateral_coin = None
        self._repay_amount = None
        self._rate = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.collateral_coin = collateral_coin
        self.repay_amount = repay_amount
        self.rate = rate

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200212.  # noqa: E501


        :return: The loan_coin of this InlineResponse200212.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200212.


        :param loan_coin: The loan_coin of this InlineResponse200212.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200212.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200212.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200212.


        :param collateral_coin: The collateral_coin of this InlineResponse200212.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def repay_amount(self):
        """Gets the repay_amount of this InlineResponse200212.  # noqa: E501


        :return: The repay_amount of this InlineResponse200212.  # noqa: E501
        :rtype: str
        """
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, repay_amount):
        """Sets the repay_amount of this InlineResponse200212.


        :param repay_amount: The repay_amount of this InlineResponse200212.  # noqa: E501
        :type: str
        """
        if repay_amount is None:
            raise ValueError("Invalid value for `repay_amount`, must not be `None`")  # noqa: E501

        self._repay_amount = repay_amount

    @property
    def rate(self):
        """Gets the rate of this InlineResponse200212.  # noqa: E501

        rate of collateral coin/loan coin  # noqa: E501

        :return: The rate of this InlineResponse200212.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this InlineResponse200212.

        rate of collateral coin/loan coin  # noqa: E501

        :param rate: The rate of this InlineResponse200212.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

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
        if issubclass(InlineResponse200212, dict):
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
        if not isinstance(other, InlineResponse200212):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
