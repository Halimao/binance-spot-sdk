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

class InlineResponse20086SpotSubUserAssetBtcVoList(object):
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
        'email': 'str',
        'total_asset': 'str'
    }

    attribute_map = {
        'email': 'email',
        'total_asset': 'totalAsset'
    }

    def __init__(self, email=None, total_asset=None):  # noqa: E501
        """InlineResponse20086SpotSubUserAssetBtcVoList - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._total_asset = None
        self.discriminator = None
        self.email = email
        self.total_asset = total_asset

    @property
    def email(self):
        """Gets the email of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501


        :return: The email of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20086SpotSubUserAssetBtcVoList.


        :param email: The email of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def total_asset(self):
        """Gets the total_asset of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501


        :return: The total_asset of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501
        :rtype: str
        """
        return self._total_asset

    @total_asset.setter
    def total_asset(self, total_asset):
        """Sets the total_asset of this InlineResponse20086SpotSubUserAssetBtcVoList.


        :param total_asset: The total_asset of this InlineResponse20086SpotSubUserAssetBtcVoList.  # noqa: E501
        :type: str
        """
        if total_asset is None:
            raise ValueError("Invalid value for `total_asset`, must not be `None`")  # noqa: E501

        self._total_asset = total_asset

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
        if issubclass(InlineResponse20086SpotSubUserAssetBtcVoList, dict):
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
        if not isinstance(other, InlineResponse20086SpotSubUserAssetBtcVoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
