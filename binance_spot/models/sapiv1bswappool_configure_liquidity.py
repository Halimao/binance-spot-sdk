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

class Sapiv1bswappoolConfigureLiquidity(object):
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
        'constant_a': 'int',
        'min_redeem_share': 'float',
        'slippage_tolerance': 'float'
    }

    attribute_map = {
        'constant_a': 'constantA',
        'min_redeem_share': 'minRedeemShare',
        'slippage_tolerance': 'slippageTolerance'
    }

    def __init__(self, constant_a=None, min_redeem_share=None, slippage_tolerance=None):  # noqa: E501
        """Sapiv1bswappoolConfigureLiquidity - a model defined in Swagger"""  # noqa: E501
        self._constant_a = None
        self._min_redeem_share = None
        self._slippage_tolerance = None
        self.discriminator = None
        self.constant_a = constant_a
        self.min_redeem_share = min_redeem_share
        self.slippage_tolerance = slippage_tolerance

    @property
    def constant_a(self):
        """Gets the constant_a of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501

        \"NA\" if pool is an innovation pool  # noqa: E501

        :return: The constant_a of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :rtype: int
        """
        return self._constant_a

    @constant_a.setter
    def constant_a(self, constant_a):
        """Sets the constant_a of this Sapiv1bswappoolConfigureLiquidity.

        \"NA\" if pool is an innovation pool  # noqa: E501

        :param constant_a: The constant_a of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :type: int
        """
        if constant_a is None:
            raise ValueError("Invalid value for `constant_a`, must not be `None`")  # noqa: E501

        self._constant_a = constant_a

    @property
    def min_redeem_share(self):
        """Gets the min_redeem_share of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501


        :return: The min_redeem_share of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :rtype: float
        """
        return self._min_redeem_share

    @min_redeem_share.setter
    def min_redeem_share(self, min_redeem_share):
        """Sets the min_redeem_share of this Sapiv1bswappoolConfigureLiquidity.


        :param min_redeem_share: The min_redeem_share of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :type: float
        """
        if min_redeem_share is None:
            raise ValueError("Invalid value for `min_redeem_share`, must not be `None`")  # noqa: E501

        self._min_redeem_share = min_redeem_share

    @property
    def slippage_tolerance(self):
        """Gets the slippage_tolerance of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501

        The swap proceeds only when the slippage is within the set range  # noqa: E501

        :return: The slippage_tolerance of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :rtype: float
        """
        return self._slippage_tolerance

    @slippage_tolerance.setter
    def slippage_tolerance(self, slippage_tolerance):
        """Sets the slippage_tolerance of this Sapiv1bswappoolConfigureLiquidity.

        The swap proceeds only when the slippage is within the set range  # noqa: E501

        :param slippage_tolerance: The slippage_tolerance of this Sapiv1bswappoolConfigureLiquidity.  # noqa: E501
        :type: float
        """
        if slippage_tolerance is None:
            raise ValueError("Invalid value for `slippage_tolerance`, must not be `None`")  # noqa: E501

        self._slippage_tolerance = slippage_tolerance

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
        if issubclass(Sapiv1bswappoolConfigureLiquidity, dict):
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
        if not isinstance(other, Sapiv1bswappoolConfigureLiquidity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
