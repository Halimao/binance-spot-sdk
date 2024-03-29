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

class InlineResponse20064DataIndicators(object):
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
        'btcusdt': 'list[InlineResponse20064DataIndicatorsBTCUSDT]'
    }

    attribute_map = {
        'btcusdt': 'BTCUSDT'
    }

    def __init__(self, btcusdt=None):  # noqa: E501
        """InlineResponse20064DataIndicators - a model defined in Swagger"""  # noqa: E501
        self._btcusdt = None
        self.discriminator = None
        self.btcusdt = btcusdt

    @property
    def btcusdt(self):
        """Gets the btcusdt of this InlineResponse20064DataIndicators.  # noqa: E501


        :return: The btcusdt of this InlineResponse20064DataIndicators.  # noqa: E501
        :rtype: list[InlineResponse20064DataIndicatorsBTCUSDT]
        """
        return self._btcusdt

    @btcusdt.setter
    def btcusdt(self, btcusdt):
        """Sets the btcusdt of this InlineResponse20064DataIndicators.


        :param btcusdt: The btcusdt of this InlineResponse20064DataIndicators.  # noqa: E501
        :type: list[InlineResponse20064DataIndicatorsBTCUSDT]
        """
        if btcusdt is None:
            raise ValueError("Invalid value for `btcusdt`, must not be `None`")  # noqa: E501

        self._btcusdt = btcusdt

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
        if issubclass(InlineResponse20064DataIndicators, dict):
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
        if not isinstance(other, InlineResponse20064DataIndicators):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
