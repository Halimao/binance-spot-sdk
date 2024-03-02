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

class Sapiv1margincrossMarginCollateralRatioCollaterals(object):
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
        'min_usd_value': 'str',
        'max_usd_value': 'str',
        'discount_rate': 'str'
    }

    attribute_map = {
        'min_usd_value': 'minUsdValue',
        'max_usd_value': 'maxUsdValue',
        'discount_rate': 'discountRate'
    }

    def __init__(self, min_usd_value=None, max_usd_value=None, discount_rate=None):  # noqa: E501
        """Sapiv1margincrossMarginCollateralRatioCollaterals - a model defined in Swagger"""  # noqa: E501
        self._min_usd_value = None
        self._max_usd_value = None
        self._discount_rate = None
        self.discriminator = None
        self.min_usd_value = min_usd_value
        self.max_usd_value = max_usd_value
        self.discount_rate = discount_rate

    @property
    def min_usd_value(self):
        """Gets the min_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501


        :return: The min_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :rtype: str
        """
        return self._min_usd_value

    @min_usd_value.setter
    def min_usd_value(self, min_usd_value):
        """Sets the min_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.


        :param min_usd_value: The min_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :type: str
        """
        if min_usd_value is None:
            raise ValueError("Invalid value for `min_usd_value`, must not be `None`")  # noqa: E501

        self._min_usd_value = min_usd_value

    @property
    def max_usd_value(self):
        """Gets the max_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501


        :return: The max_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :rtype: str
        """
        return self._max_usd_value

    @max_usd_value.setter
    def max_usd_value(self, max_usd_value):
        """Sets the max_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.


        :param max_usd_value: The max_usd_value of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :type: str
        """
        if max_usd_value is None:
            raise ValueError("Invalid value for `max_usd_value`, must not be `None`")  # noqa: E501

        self._max_usd_value = max_usd_value

    @property
    def discount_rate(self):
        """Gets the discount_rate of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501


        :return: The discount_rate of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :rtype: str
        """
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        """Sets the discount_rate of this Sapiv1margincrossMarginCollateralRatioCollaterals.


        :param discount_rate: The discount_rate of this Sapiv1margincrossMarginCollateralRatioCollaterals.  # noqa: E501
        :type: str
        """
        if discount_rate is None:
            raise ValueError("Invalid value for `discount_rate`, must not be `None`")  # noqa: E501

        self._discount_rate = discount_rate

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
        if issubclass(Sapiv1margincrossMarginCollateralRatioCollaterals, dict):
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
        if not isinstance(other, Sapiv1margincrossMarginCollateralRatioCollaterals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
