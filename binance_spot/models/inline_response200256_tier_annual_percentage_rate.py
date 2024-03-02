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

class InlineResponse200256TierAnnualPercentageRate(object):
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
        '_0_5_btc': 'float',
        '_5_10_btc': 'float'
    }

    attribute_map = {
        '_0_5_btc': '0-5BTC',
        '_5_10_btc': '5-10BTC'
    }

    def __init__(self, _0_5_btc=None, _5_10_btc=None):  # noqa: E501
        """InlineResponse200256TierAnnualPercentageRate - a model defined in Swagger"""  # noqa: E501
        self.__0_5_btc = None
        self.__5_10_btc = None
        self.discriminator = None
        self._0_5_btc = _0_5_btc
        self._5_10_btc = _5_10_btc

    @property
    def _0_5_btc(self):
        """Gets the _0_5_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501


        :return: The _0_5_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501
        :rtype: float
        """
        return self.__0_5_btc

    @_0_5_btc.setter
    def _0_5_btc(self, _0_5_btc):
        """Sets the _0_5_btc of this InlineResponse200256TierAnnualPercentageRate.


        :param _0_5_btc: The _0_5_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501
        :type: float
        """
        if _0_5_btc is None:
            raise ValueError("Invalid value for `_0_5_btc`, must not be `None`")  # noqa: E501

        self.__0_5_btc = _0_5_btc

    @property
    def _5_10_btc(self):
        """Gets the _5_10_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501


        :return: The _5_10_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501
        :rtype: float
        """
        return self.__5_10_btc

    @_5_10_btc.setter
    def _5_10_btc(self, _5_10_btc):
        """Sets the _5_10_btc of this InlineResponse200256TierAnnualPercentageRate.


        :param _5_10_btc: The _5_10_btc of this InlineResponse200256TierAnnualPercentageRate.  # noqa: E501
        :type: float
        """
        if _5_10_btc is None:
            raise ValueError("Invalid value for `_5_10_btc`, must not be `None`")  # noqa: E501

        self.__5_10_btc = _5_10_btc

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
        if issubclass(InlineResponse200256TierAnnualPercentageRate, dict):
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
        if not isinstance(other, InlineResponse200256TierAnnualPercentageRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
