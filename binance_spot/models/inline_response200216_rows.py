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

class InlineResponse200216Rows(object):
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
        'initial_loan_amount': 'str',
        'collateral_coin': 'str',
        'initial_collateral_amount': 'str',
        'borrow_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'initial_loan_amount': 'initialLoanAmount',
        'collateral_coin': 'collateralCoin',
        'initial_collateral_amount': 'initialCollateralAmount',
        'borrow_time': 'borrowTime',
        'status': 'status'
    }

    def __init__(self, loan_coin=None, initial_loan_amount=None, collateral_coin=None, initial_collateral_amount=None, borrow_time=None, status=None):  # noqa: E501
        """InlineResponse200216Rows - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._initial_loan_amount = None
        self._collateral_coin = None
        self._initial_collateral_amount = None
        self._borrow_time = None
        self._status = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.initial_loan_amount = initial_loan_amount
        self.collateral_coin = collateral_coin
        self.initial_collateral_amount = initial_collateral_amount
        self.borrow_time = borrow_time
        self.status = status

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200216Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200216Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200216Rows.


        :param loan_coin: The loan_coin of this InlineResponse200216Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def initial_loan_amount(self):
        """Gets the initial_loan_amount of this InlineResponse200216Rows.  # noqa: E501


        :return: The initial_loan_amount of this InlineResponse200216Rows.  # noqa: E501
        :rtype: str
        """
        return self._initial_loan_amount

    @initial_loan_amount.setter
    def initial_loan_amount(self, initial_loan_amount):
        """Sets the initial_loan_amount of this InlineResponse200216Rows.


        :param initial_loan_amount: The initial_loan_amount of this InlineResponse200216Rows.  # noqa: E501
        :type: str
        """
        if initial_loan_amount is None:
            raise ValueError("Invalid value for `initial_loan_amount`, must not be `None`")  # noqa: E501

        self._initial_loan_amount = initial_loan_amount

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200216Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200216Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200216Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200216Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def initial_collateral_amount(self):
        """Gets the initial_collateral_amount of this InlineResponse200216Rows.  # noqa: E501


        :return: The initial_collateral_amount of this InlineResponse200216Rows.  # noqa: E501
        :rtype: str
        """
        return self._initial_collateral_amount

    @initial_collateral_amount.setter
    def initial_collateral_amount(self, initial_collateral_amount):
        """Sets the initial_collateral_amount of this InlineResponse200216Rows.


        :param initial_collateral_amount: The initial_collateral_amount of this InlineResponse200216Rows.  # noqa: E501
        :type: str
        """
        if initial_collateral_amount is None:
            raise ValueError("Invalid value for `initial_collateral_amount`, must not be `None`")  # noqa: E501

        self._initial_collateral_amount = initial_collateral_amount

    @property
    def borrow_time(self):
        """Gets the borrow_time of this InlineResponse200216Rows.  # noqa: E501


        :return: The borrow_time of this InlineResponse200216Rows.  # noqa: E501
        :rtype: int
        """
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, borrow_time):
        """Sets the borrow_time of this InlineResponse200216Rows.


        :param borrow_time: The borrow_time of this InlineResponse200216Rows.  # noqa: E501
        :type: int
        """
        if borrow_time is None:
            raise ValueError("Invalid value for `borrow_time`, must not be `None`")  # noqa: E501

        self._borrow_time = borrow_time

    @property
    def status(self):
        """Gets the status of this InlineResponse200216Rows.  # noqa: E501


        :return: The status of this InlineResponse200216Rows.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200216Rows.


        :param status: The status of this InlineResponse200216Rows.  # noqa: E501
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
        if issubclass(InlineResponse200216Rows, dict):
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
        if not isinstance(other, InlineResponse200216Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
