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

class InlineResponse200221Rows(object):
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
        'flexible_interest_rate': 'str',
        'flexible_min_limit': 'str',
        'flexible_max_limit': 'str'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'flexible_interest_rate': 'flexibleInterestRate',
        'flexible_min_limit': 'flexibleMinLimit',
        'flexible_max_limit': 'flexibleMaxLimit'
    }

    def __init__(self, loan_coin=None, flexible_interest_rate=None, flexible_min_limit=None, flexible_max_limit=None):  # noqa: E501
        """InlineResponse200221Rows - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._flexible_interest_rate = None
        self._flexible_min_limit = None
        self._flexible_max_limit = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.flexible_interest_rate = flexible_interest_rate
        self.flexible_min_limit = flexible_min_limit
        self.flexible_max_limit = flexible_max_limit

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200221Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200221Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200221Rows.


        :param loan_coin: The loan_coin of this InlineResponse200221Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def flexible_interest_rate(self):
        """Gets the flexible_interest_rate of this InlineResponse200221Rows.  # noqa: E501


        :return: The flexible_interest_rate of this InlineResponse200221Rows.  # noqa: E501
        :rtype: str
        """
        return self._flexible_interest_rate

    @flexible_interest_rate.setter
    def flexible_interest_rate(self, flexible_interest_rate):
        """Sets the flexible_interest_rate of this InlineResponse200221Rows.


        :param flexible_interest_rate: The flexible_interest_rate of this InlineResponse200221Rows.  # noqa: E501
        :type: str
        """
        if flexible_interest_rate is None:
            raise ValueError("Invalid value for `flexible_interest_rate`, must not be `None`")  # noqa: E501

        self._flexible_interest_rate = flexible_interest_rate

    @property
    def flexible_min_limit(self):
        """Gets the flexible_min_limit of this InlineResponse200221Rows.  # noqa: E501


        :return: The flexible_min_limit of this InlineResponse200221Rows.  # noqa: E501
        :rtype: str
        """
        return self._flexible_min_limit

    @flexible_min_limit.setter
    def flexible_min_limit(self, flexible_min_limit):
        """Sets the flexible_min_limit of this InlineResponse200221Rows.


        :param flexible_min_limit: The flexible_min_limit of this InlineResponse200221Rows.  # noqa: E501
        :type: str
        """
        if flexible_min_limit is None:
            raise ValueError("Invalid value for `flexible_min_limit`, must not be `None`")  # noqa: E501

        self._flexible_min_limit = flexible_min_limit

    @property
    def flexible_max_limit(self):
        """Gets the flexible_max_limit of this InlineResponse200221Rows.  # noqa: E501


        :return: The flexible_max_limit of this InlineResponse200221Rows.  # noqa: E501
        :rtype: str
        """
        return self._flexible_max_limit

    @flexible_max_limit.setter
    def flexible_max_limit(self, flexible_max_limit):
        """Sets the flexible_max_limit of this InlineResponse200221Rows.


        :param flexible_max_limit: The flexible_max_limit of this InlineResponse200221Rows.  # noqa: E501
        :type: str
        """
        if flexible_max_limit is None:
            raise ValueError("Invalid value for `flexible_max_limit`, must not be `None`")  # noqa: E501

        self._flexible_max_limit = flexible_max_limit

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
        if issubclass(InlineResponse200221Rows, dict):
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
        if not isinstance(other, InlineResponse200221Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other