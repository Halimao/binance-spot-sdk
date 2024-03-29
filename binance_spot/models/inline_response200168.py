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

class InlineResponse200168(object):
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
        'asset': 'str',
        'asset_index_price': 'str',
        'time': 'int'
    }

    attribute_map = {
        'asset': 'asset',
        'asset_index_price': 'assetIndexPrice',
        'time': 'time'
    }

    def __init__(self, asset=None, asset_index_price=None, time=None):  # noqa: E501
        """InlineResponse200168 - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._asset_index_price = None
        self._time = None
        self.discriminator = None
        self.asset = asset
        self.asset_index_price = asset_index_price
        self.time = time

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200168.  # noqa: E501


        :return: The asset of this InlineResponse200168.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200168.


        :param asset: The asset of this InlineResponse200168.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def asset_index_price(self):
        """Gets the asset_index_price of this InlineResponse200168.  # noqa: E501


        :return: The asset_index_price of this InlineResponse200168.  # noqa: E501
        :rtype: str
        """
        return self._asset_index_price

    @asset_index_price.setter
    def asset_index_price(self, asset_index_price):
        """Sets the asset_index_price of this InlineResponse200168.


        :param asset_index_price: The asset_index_price of this InlineResponse200168.  # noqa: E501
        :type: str
        """
        if asset_index_price is None:
            raise ValueError("Invalid value for `asset_index_price`, must not be `None`")  # noqa: E501

        self._asset_index_price = asset_index_price

    @property
    def time(self):
        """Gets the time of this InlineResponse200168.  # noqa: E501


        :return: The time of this InlineResponse200168.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse200168.


        :param time: The time of this InlineResponse200168.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(InlineResponse200168, dict):
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
        if not isinstance(other, InlineResponse200168):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
