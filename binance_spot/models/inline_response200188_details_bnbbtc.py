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

class InlineResponse200188DetailsBNBBTC(object):
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
        'bnb': 'float'
    }

    attribute_map = {
        'bnb': 'BNB'
    }

    def __init__(self, bnb=None):  # noqa: E501
        """InlineResponse200188DetailsBNBBTC - a model defined in Swagger"""  # noqa: E501
        self._bnb = None
        self.discriminator = None
        self.bnb = bnb

    @property
    def bnb(self):
        """Gets the bnb of this InlineResponse200188DetailsBNBBTC.  # noqa: E501


        :return: The bnb of this InlineResponse200188DetailsBNBBTC.  # noqa: E501
        :rtype: float
        """
        return self._bnb

    @bnb.setter
    def bnb(self, bnb):
        """Sets the bnb of this InlineResponse200188DetailsBNBBTC.


        :param bnb: The bnb of this InlineResponse200188DetailsBNBBTC.  # noqa: E501
        :type: float
        """
        if bnb is None:
            raise ValueError("Invalid value for `bnb`, must not be `None`")  # noqa: E501

        self._bnb = bnb

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
        if issubclass(InlineResponse200188DetailsBNBBTC, dict):
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
        if not isinstance(other, InlineResponse200188DetailsBNBBTC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
