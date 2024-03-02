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

class InlineResponse200249AssetAllocation(object):
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
        'target_asset': 'str',
        'allocation': 'str'
    }

    attribute_map = {
        'target_asset': 'targetAsset',
        'allocation': 'allocation'
    }

    def __init__(self, target_asset=None, allocation=None):  # noqa: E501
        """InlineResponse200249AssetAllocation - a model defined in Swagger"""  # noqa: E501
        self._target_asset = None
        self._allocation = None
        self.discriminator = None
        self.target_asset = target_asset
        self.allocation = allocation

    @property
    def target_asset(self):
        """Gets the target_asset of this InlineResponse200249AssetAllocation.  # noqa: E501


        :return: The target_asset of this InlineResponse200249AssetAllocation.  # noqa: E501
        :rtype: str
        """
        return self._target_asset

    @target_asset.setter
    def target_asset(self, target_asset):
        """Sets the target_asset of this InlineResponse200249AssetAllocation.


        :param target_asset: The target_asset of this InlineResponse200249AssetAllocation.  # noqa: E501
        :type: str
        """
        if target_asset is None:
            raise ValueError("Invalid value for `target_asset`, must not be `None`")  # noqa: E501

        self._target_asset = target_asset

    @property
    def allocation(self):
        """Gets the allocation of this InlineResponse200249AssetAllocation.  # noqa: E501


        :return: The allocation of this InlineResponse200249AssetAllocation.  # noqa: E501
        :rtype: str
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this InlineResponse200249AssetAllocation.


        :param allocation: The allocation of this InlineResponse200249AssetAllocation.  # noqa: E501
        :type: str
        """
        if allocation is None:
            raise ValueError("Invalid value for `allocation`, must not be `None`")  # noqa: E501

        self._allocation = allocation

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
        if issubclass(InlineResponse200249AssetAllocation, dict):
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
        if not isinstance(other, InlineResponse200249AssetAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other