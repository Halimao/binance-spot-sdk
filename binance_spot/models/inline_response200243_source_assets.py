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

class InlineResponse200243SourceAssets(object):
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
        'source_asset': 'str',
        'asset_min_amount': 'str',
        'asset_max_amount': 'str',
        'scale': 'str',
        'flexible_amount': 'str'
    }

    attribute_map = {
        'source_asset': 'sourceAsset',
        'asset_min_amount': 'assetMinAmount',
        'asset_max_amount': 'assetMaxAmount',
        'scale': 'scale',
        'flexible_amount': 'flexibleAmount'
    }

    def __init__(self, source_asset=None, asset_min_amount=None, asset_max_amount=None, scale=None, flexible_amount=None):  # noqa: E501
        """InlineResponse200243SourceAssets - a model defined in Swagger"""  # noqa: E501
        self._source_asset = None
        self._asset_min_amount = None
        self._asset_max_amount = None
        self._scale = None
        self._flexible_amount = None
        self.discriminator = None
        self.source_asset = source_asset
        self.asset_min_amount = asset_min_amount
        self.asset_max_amount = asset_max_amount
        self.scale = scale
        self.flexible_amount = flexible_amount

    @property
    def source_asset(self):
        """Gets the source_asset of this InlineResponse200243SourceAssets.  # noqa: E501


        :return: The source_asset of this InlineResponse200243SourceAssets.  # noqa: E501
        :rtype: str
        """
        return self._source_asset

    @source_asset.setter
    def source_asset(self, source_asset):
        """Sets the source_asset of this InlineResponse200243SourceAssets.


        :param source_asset: The source_asset of this InlineResponse200243SourceAssets.  # noqa: E501
        :type: str
        """
        if source_asset is None:
            raise ValueError("Invalid value for `source_asset`, must not be `None`")  # noqa: E501

        self._source_asset = source_asset

    @property
    def asset_min_amount(self):
        """Gets the asset_min_amount of this InlineResponse200243SourceAssets.  # noqa: E501


        :return: The asset_min_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :rtype: str
        """
        return self._asset_min_amount

    @asset_min_amount.setter
    def asset_min_amount(self, asset_min_amount):
        """Sets the asset_min_amount of this InlineResponse200243SourceAssets.


        :param asset_min_amount: The asset_min_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :type: str
        """
        if asset_min_amount is None:
            raise ValueError("Invalid value for `asset_min_amount`, must not be `None`")  # noqa: E501

        self._asset_min_amount = asset_min_amount

    @property
    def asset_max_amount(self):
        """Gets the asset_max_amount of this InlineResponse200243SourceAssets.  # noqa: E501


        :return: The asset_max_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :rtype: str
        """
        return self._asset_max_amount

    @asset_max_amount.setter
    def asset_max_amount(self, asset_max_amount):
        """Sets the asset_max_amount of this InlineResponse200243SourceAssets.


        :param asset_max_amount: The asset_max_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :type: str
        """
        if asset_max_amount is None:
            raise ValueError("Invalid value for `asset_max_amount`, must not be `None`")  # noqa: E501

        self._asset_max_amount = asset_max_amount

    @property
    def scale(self):
        """Gets the scale of this InlineResponse200243SourceAssets.  # noqa: E501


        :return: The scale of this InlineResponse200243SourceAssets.  # noqa: E501
        :rtype: str
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this InlineResponse200243SourceAssets.


        :param scale: The scale of this InlineResponse200243SourceAssets.  # noqa: E501
        :type: str
        """
        if scale is None:
            raise ValueError("Invalid value for `scale`, must not be `None`")  # noqa: E501

        self._scale = scale

    @property
    def flexible_amount(self):
        """Gets the flexible_amount of this InlineResponse200243SourceAssets.  # noqa: E501


        :return: The flexible_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :rtype: str
        """
        return self._flexible_amount

    @flexible_amount.setter
    def flexible_amount(self, flexible_amount):
        """Sets the flexible_amount of this InlineResponse200243SourceAssets.


        :param flexible_amount: The flexible_amount of this InlineResponse200243SourceAssets.  # noqa: E501
        :type: str
        """
        if flexible_amount is None:
            raise ValueError("Invalid value for `flexible_amount`, must not be `None`")  # noqa: E501

        self._flexible_amount = flexible_amount

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
        if issubclass(InlineResponse200243SourceAssets, dict):
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
        if not isinstance(other, InlineResponse200243SourceAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
