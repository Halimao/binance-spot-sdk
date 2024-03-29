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

class Sapiv1bswapliquidityShare(object):
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
        'share_amount': 'float',
        'share_percentage': 'float',
        'asset': 'Sapiv1bswapliquidityShareAsset'
    }

    attribute_map = {
        'share_amount': 'shareAmount',
        'share_percentage': 'sharePercentage',
        'asset': 'asset'
    }

    def __init__(self, share_amount=None, share_percentage=None, asset=None):  # noqa: E501
        """Sapiv1bswapliquidityShare - a model defined in Swagger"""  # noqa: E501
        self._share_amount = None
        self._share_percentage = None
        self._asset = None
        self.discriminator = None
        self.share_amount = share_amount
        self.share_percentage = share_percentage
        self.asset = asset

    @property
    def share_amount(self):
        """Gets the share_amount of this Sapiv1bswapliquidityShare.  # noqa: E501


        :return: The share_amount of this Sapiv1bswapliquidityShare.  # noqa: E501
        :rtype: float
        """
        return self._share_amount

    @share_amount.setter
    def share_amount(self, share_amount):
        """Sets the share_amount of this Sapiv1bswapliquidityShare.


        :param share_amount: The share_amount of this Sapiv1bswapliquidityShare.  # noqa: E501
        :type: float
        """
        if share_amount is None:
            raise ValueError("Invalid value for `share_amount`, must not be `None`")  # noqa: E501

        self._share_amount = share_amount

    @property
    def share_percentage(self):
        """Gets the share_percentage of this Sapiv1bswapliquidityShare.  # noqa: E501


        :return: The share_percentage of this Sapiv1bswapliquidityShare.  # noqa: E501
        :rtype: float
        """
        return self._share_percentage

    @share_percentage.setter
    def share_percentage(self, share_percentage):
        """Sets the share_percentage of this Sapiv1bswapliquidityShare.


        :param share_percentage: The share_percentage of this Sapiv1bswapliquidityShare.  # noqa: E501
        :type: float
        """
        if share_percentage is None:
            raise ValueError("Invalid value for `share_percentage`, must not be `None`")  # noqa: E501

        self._share_percentage = share_percentage

    @property
    def asset(self):
        """Gets the asset of this Sapiv1bswapliquidityShare.  # noqa: E501


        :return: The asset of this Sapiv1bswapliquidityShare.  # noqa: E501
        :rtype: Sapiv1bswapliquidityShareAsset
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this Sapiv1bswapliquidityShare.


        :param asset: The asset of this Sapiv1bswapliquidityShare.  # noqa: E501
        :type: Sapiv1bswapliquidityShareAsset
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

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
        if issubclass(Sapiv1bswapliquidityShare, dict):
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
        if not isinstance(other, Sapiv1bswapliquidityShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
