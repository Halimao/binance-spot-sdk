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

class Sapiv1stakingproductListDetail(object):
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
        'reward_asset': 'str',
        'duration': 'int',
        'renewable': 'bool',
        'apy': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'reward_asset': 'rewardAsset',
        'duration': 'duration',
        'renewable': 'renewable',
        'apy': 'apy'
    }

    def __init__(self, asset=None, reward_asset=None, duration=None, renewable=None, apy=None):  # noqa: E501
        """Sapiv1stakingproductListDetail - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._reward_asset = None
        self._duration = None
        self._renewable = None
        self._apy = None
        self.discriminator = None
        self.asset = asset
        self.reward_asset = reward_asset
        self.duration = duration
        self.renewable = renewable
        self.apy = apy

    @property
    def asset(self):
        """Gets the asset of this Sapiv1stakingproductListDetail.  # noqa: E501


        :return: The asset of this Sapiv1stakingproductListDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this Sapiv1stakingproductListDetail.


        :param asset: The asset of this Sapiv1stakingproductListDetail.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def reward_asset(self):
        """Gets the reward_asset of this Sapiv1stakingproductListDetail.  # noqa: E501


        :return: The reward_asset of this Sapiv1stakingproductListDetail.  # noqa: E501
        :rtype: str
        """
        return self._reward_asset

    @reward_asset.setter
    def reward_asset(self, reward_asset):
        """Sets the reward_asset of this Sapiv1stakingproductListDetail.


        :param reward_asset: The reward_asset of this Sapiv1stakingproductListDetail.  # noqa: E501
        :type: str
        """
        if reward_asset is None:
            raise ValueError("Invalid value for `reward_asset`, must not be `None`")  # noqa: E501

        self._reward_asset = reward_asset

    @property
    def duration(self):
        """Gets the duration of this Sapiv1stakingproductListDetail.  # noqa: E501


        :return: The duration of this Sapiv1stakingproductListDetail.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Sapiv1stakingproductListDetail.


        :param duration: The duration of this Sapiv1stakingproductListDetail.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def renewable(self):
        """Gets the renewable of this Sapiv1stakingproductListDetail.  # noqa: E501


        :return: The renewable of this Sapiv1stakingproductListDetail.  # noqa: E501
        :rtype: bool
        """
        return self._renewable

    @renewable.setter
    def renewable(self, renewable):
        """Sets the renewable of this Sapiv1stakingproductListDetail.


        :param renewable: The renewable of this Sapiv1stakingproductListDetail.  # noqa: E501
        :type: bool
        """
        if renewable is None:
            raise ValueError("Invalid value for `renewable`, must not be `None`")  # noqa: E501

        self._renewable = renewable

    @property
    def apy(self):
        """Gets the apy of this Sapiv1stakingproductListDetail.  # noqa: E501


        :return: The apy of this Sapiv1stakingproductListDetail.  # noqa: E501
        :rtype: str
        """
        return self._apy

    @apy.setter
    def apy(self, apy):
        """Sets the apy of this Sapiv1stakingproductListDetail.


        :param apy: The apy of this Sapiv1stakingproductListDetail.  # noqa: E501
        :type: str
        """
        if apy is None:
            raise ValueError("Invalid value for `apy`, must not be `None`")  # noqa: E501

        self._apy = apy

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
        if issubclass(Sapiv1stakingproductListDetail, dict):
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
        if not isinstance(other, Sapiv1stakingproductListDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other