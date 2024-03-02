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

class InlineResponse200197Rows(object):
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
        'flexible_daily_interest_rate': 'str',
        'flexible_yearly_interest_rate': 'str',
        '_30d_daily_interest_rate': 'str',
        '_30d_yearly_interest_rate': 'str',
        '_60d_daily_interest_rate': 'str',
        '_60d_yearly_interest_rate': 'str',
        'min_limit': 'str',
        'max_limit': 'str',
        'vip_level': 'int'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'flexible_daily_interest_rate': '_flexibleDailyInterestRate',
        'flexible_yearly_interest_rate': '_flexibleYearlyInterestRate',
        '_30d_daily_interest_rate': '_30dDailyInterestRate',
        '_30d_yearly_interest_rate': '_30dYearlyInterestRate',
        '_60d_daily_interest_rate': '_60dDailyInterestRate',
        '_60d_yearly_interest_rate': '_60dYearlyInterestRate',
        'min_limit': 'minLimit',
        'max_limit': 'maxLimit',
        'vip_level': 'vipLevel'
    }

    def __init__(self, loan_coin=None, flexible_daily_interest_rate=None, flexible_yearly_interest_rate=None, _30d_daily_interest_rate=None, _30d_yearly_interest_rate=None, _60d_daily_interest_rate=None, _60d_yearly_interest_rate=None, min_limit=None, max_limit=None, vip_level=None):  # noqa: E501
        """InlineResponse200197Rows - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._flexible_daily_interest_rate = None
        self._flexible_yearly_interest_rate = None
        self.__30d_daily_interest_rate = None
        self.__30d_yearly_interest_rate = None
        self.__60d_daily_interest_rate = None
        self.__60d_yearly_interest_rate = None
        self._min_limit = None
        self._max_limit = None
        self._vip_level = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.flexible_daily_interest_rate = flexible_daily_interest_rate
        self.flexible_yearly_interest_rate = flexible_yearly_interest_rate
        self._30d_daily_interest_rate = _30d_daily_interest_rate
        self._30d_yearly_interest_rate = _30d_yearly_interest_rate
        self._60d_daily_interest_rate = _60d_daily_interest_rate
        self._60d_yearly_interest_rate = _60d_yearly_interest_rate
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.vip_level = vip_level

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200197Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200197Rows.


        :param loan_coin: The loan_coin of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def flexible_daily_interest_rate(self):
        """Gets the flexible_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The flexible_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self._flexible_daily_interest_rate

    @flexible_daily_interest_rate.setter
    def flexible_daily_interest_rate(self, flexible_daily_interest_rate):
        """Sets the flexible_daily_interest_rate of this InlineResponse200197Rows.


        :param flexible_daily_interest_rate: The flexible_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if flexible_daily_interest_rate is None:
            raise ValueError("Invalid value for `flexible_daily_interest_rate`, must not be `None`")  # noqa: E501

        self._flexible_daily_interest_rate = flexible_daily_interest_rate

    @property
    def flexible_yearly_interest_rate(self):
        """Gets the flexible_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The flexible_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self._flexible_yearly_interest_rate

    @flexible_yearly_interest_rate.setter
    def flexible_yearly_interest_rate(self, flexible_yearly_interest_rate):
        """Sets the flexible_yearly_interest_rate of this InlineResponse200197Rows.


        :param flexible_yearly_interest_rate: The flexible_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if flexible_yearly_interest_rate is None:
            raise ValueError("Invalid value for `flexible_yearly_interest_rate`, must not be `None`")  # noqa: E501

        self._flexible_yearly_interest_rate = flexible_yearly_interest_rate

    @property
    def _30d_daily_interest_rate(self):
        """Gets the _30d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The _30d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self.__30d_daily_interest_rate

    @_30d_daily_interest_rate.setter
    def _30d_daily_interest_rate(self, _30d_daily_interest_rate):
        """Sets the _30d_daily_interest_rate of this InlineResponse200197Rows.


        :param _30d_daily_interest_rate: The _30d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if _30d_daily_interest_rate is None:
            raise ValueError("Invalid value for `_30d_daily_interest_rate`, must not be `None`")  # noqa: E501

        self.__30d_daily_interest_rate = _30d_daily_interest_rate

    @property
    def _30d_yearly_interest_rate(self):
        """Gets the _30d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The _30d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self.__30d_yearly_interest_rate

    @_30d_yearly_interest_rate.setter
    def _30d_yearly_interest_rate(self, _30d_yearly_interest_rate):
        """Sets the _30d_yearly_interest_rate of this InlineResponse200197Rows.


        :param _30d_yearly_interest_rate: The _30d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if _30d_yearly_interest_rate is None:
            raise ValueError("Invalid value for `_30d_yearly_interest_rate`, must not be `None`")  # noqa: E501

        self.__30d_yearly_interest_rate = _30d_yearly_interest_rate

    @property
    def _60d_daily_interest_rate(self):
        """Gets the _60d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The _60d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self.__60d_daily_interest_rate

    @_60d_daily_interest_rate.setter
    def _60d_daily_interest_rate(self, _60d_daily_interest_rate):
        """Sets the _60d_daily_interest_rate of this InlineResponse200197Rows.


        :param _60d_daily_interest_rate: The _60d_daily_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if _60d_daily_interest_rate is None:
            raise ValueError("Invalid value for `_60d_daily_interest_rate`, must not be `None`")  # noqa: E501

        self.__60d_daily_interest_rate = _60d_daily_interest_rate

    @property
    def _60d_yearly_interest_rate(self):
        """Gets the _60d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501


        :return: The _60d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self.__60d_yearly_interest_rate

    @_60d_yearly_interest_rate.setter
    def _60d_yearly_interest_rate(self, _60d_yearly_interest_rate):
        """Sets the _60d_yearly_interest_rate of this InlineResponse200197Rows.


        :param _60d_yearly_interest_rate: The _60d_yearly_interest_rate of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if _60d_yearly_interest_rate is None:
            raise ValueError("Invalid value for `_60d_yearly_interest_rate`, must not be `None`")  # noqa: E501

        self.__60d_yearly_interest_rate = _60d_yearly_interest_rate

    @property
    def min_limit(self):
        """Gets the min_limit of this InlineResponse200197Rows.  # noqa: E501


        :return: The min_limit of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self._min_limit

    @min_limit.setter
    def min_limit(self, min_limit):
        """Sets the min_limit of this InlineResponse200197Rows.


        :param min_limit: The min_limit of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if min_limit is None:
            raise ValueError("Invalid value for `min_limit`, must not be `None`")  # noqa: E501

        self._min_limit = min_limit

    @property
    def max_limit(self):
        """Gets the max_limit of this InlineResponse200197Rows.  # noqa: E501


        :return: The max_limit of this InlineResponse200197Rows.  # noqa: E501
        :rtype: str
        """
        return self._max_limit

    @max_limit.setter
    def max_limit(self, max_limit):
        """Sets the max_limit of this InlineResponse200197Rows.


        :param max_limit: The max_limit of this InlineResponse200197Rows.  # noqa: E501
        :type: str
        """
        if max_limit is None:
            raise ValueError("Invalid value for `max_limit`, must not be `None`")  # noqa: E501

        self._max_limit = max_limit

    @property
    def vip_level(self):
        """Gets the vip_level of this InlineResponse200197Rows.  # noqa: E501


        :return: The vip_level of this InlineResponse200197Rows.  # noqa: E501
        :rtype: int
        """
        return self._vip_level

    @vip_level.setter
    def vip_level(self, vip_level):
        """Sets the vip_level of this InlineResponse200197Rows.


        :param vip_level: The vip_level of this InlineResponse200197Rows.  # noqa: E501
        :type: int
        """
        if vip_level is None:
            raise ValueError("Invalid value for `vip_level`, must not be `None`")  # noqa: E501

        self._vip_level = vip_level

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
        if issubclass(InlineResponse200197Rows, dict):
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
        if not isinstance(other, InlineResponse200197Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
