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

class InlineResponse200217(object):
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
        'remaining_debt': 'str',
        'remaining_collateral': 'str',
        'full_repayment': 'bool',
        'current_ltv': 'str',
        'repay_status': 'str'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'collateral_coin': 'collateralCoin',
        'remaining_debt': 'remainingDebt',
        'remaining_collateral': 'remainingCollateral',
        'full_repayment': 'fullRepayment',
        'current_ltv': 'currentLTV',
        'repay_status': 'repayStatus'
    }

    def __init__(self, loan_coin=None, collateral_coin=None, remaining_debt=None, remaining_collateral=None, full_repayment=None, current_ltv=None, repay_status=None):  # noqa: E501
        """InlineResponse200217 - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._collateral_coin = None
        self._remaining_debt = None
        self._remaining_collateral = None
        self._full_repayment = None
        self._current_ltv = None
        self._repay_status = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.collateral_coin = collateral_coin
        self.remaining_debt = remaining_debt
        self.remaining_collateral = remaining_collateral
        self.full_repayment = full_repayment
        self.current_ltv = current_ltv
        self.repay_status = repay_status

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200217.  # noqa: E501


        :return: The loan_coin of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200217.


        :param loan_coin: The loan_coin of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200217.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200217.


        :param collateral_coin: The collateral_coin of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def remaining_debt(self):
        """Gets the remaining_debt of this InlineResponse200217.  # noqa: E501


        :return: The remaining_debt of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._remaining_debt

    @remaining_debt.setter
    def remaining_debt(self, remaining_debt):
        """Sets the remaining_debt of this InlineResponse200217.


        :param remaining_debt: The remaining_debt of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if remaining_debt is None:
            raise ValueError("Invalid value for `remaining_debt`, must not be `None`")  # noqa: E501

        self._remaining_debt = remaining_debt

    @property
    def remaining_collateral(self):
        """Gets the remaining_collateral of this InlineResponse200217.  # noqa: E501


        :return: The remaining_collateral of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._remaining_collateral

    @remaining_collateral.setter
    def remaining_collateral(self, remaining_collateral):
        """Sets the remaining_collateral of this InlineResponse200217.


        :param remaining_collateral: The remaining_collateral of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if remaining_collateral is None:
            raise ValueError("Invalid value for `remaining_collateral`, must not be `None`")  # noqa: E501

        self._remaining_collateral = remaining_collateral

    @property
    def full_repayment(self):
        """Gets the full_repayment of this InlineResponse200217.  # noqa: E501


        :return: The full_repayment of this InlineResponse200217.  # noqa: E501
        :rtype: bool
        """
        return self._full_repayment

    @full_repayment.setter
    def full_repayment(self, full_repayment):
        """Sets the full_repayment of this InlineResponse200217.


        :param full_repayment: The full_repayment of this InlineResponse200217.  # noqa: E501
        :type: bool
        """
        if full_repayment is None:
            raise ValueError("Invalid value for `full_repayment`, must not be `None`")  # noqa: E501

        self._full_repayment = full_repayment

    @property
    def current_ltv(self):
        """Gets the current_ltv of this InlineResponse200217.  # noqa: E501


        :return: The current_ltv of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._current_ltv

    @current_ltv.setter
    def current_ltv(self, current_ltv):
        """Sets the current_ltv of this InlineResponse200217.


        :param current_ltv: The current_ltv of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if current_ltv is None:
            raise ValueError("Invalid value for `current_ltv`, must not be `None`")  # noqa: E501

        self._current_ltv = current_ltv

    @property
    def repay_status(self):
        """Gets the repay_status of this InlineResponse200217.  # noqa: E501


        :return: The repay_status of this InlineResponse200217.  # noqa: E501
        :rtype: str
        """
        return self._repay_status

    @repay_status.setter
    def repay_status(self, repay_status):
        """Sets the repay_status of this InlineResponse200217.


        :param repay_status: The repay_status of this InlineResponse200217.  # noqa: E501
        :type: str
        """
        if repay_status is None:
            raise ValueError("Invalid value for `repay_status`, must not be `None`")  # noqa: E501

        self._repay_status = repay_status

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
        if issubclass(InlineResponse200217, dict):
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
        if not isinstance(other, InlineResponse200217):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
