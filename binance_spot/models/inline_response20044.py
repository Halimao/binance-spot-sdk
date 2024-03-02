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

class InlineResponse20044(object):
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
        'total': 'int',
        'user_asset_dribblets': 'list[InlineResponse20044UserAssetDribblets]'
    }

    attribute_map = {
        'total': 'total',
        'user_asset_dribblets': 'userAssetDribblets'
    }

    def __init__(self, total=None, user_asset_dribblets=None):  # noqa: E501
        """InlineResponse20044 - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._user_asset_dribblets = None
        self.discriminator = None
        self.total = total
        self.user_asset_dribblets = user_asset_dribblets

    @property
    def total(self):
        """Gets the total of this InlineResponse20044.  # noqa: E501


        :return: The total of this InlineResponse20044.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse20044.


        :param total: The total of this InlineResponse20044.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def user_asset_dribblets(self):
        """Gets the user_asset_dribblets of this InlineResponse20044.  # noqa: E501


        :return: The user_asset_dribblets of this InlineResponse20044.  # noqa: E501
        :rtype: list[InlineResponse20044UserAssetDribblets]
        """
        return self._user_asset_dribblets

    @user_asset_dribblets.setter
    def user_asset_dribblets(self, user_asset_dribblets):
        """Sets the user_asset_dribblets of this InlineResponse20044.


        :param user_asset_dribblets: The user_asset_dribblets of this InlineResponse20044.  # noqa: E501
        :type: list[InlineResponse20044UserAssetDribblets]
        """
        if user_asset_dribblets is None:
            raise ValueError("Invalid value for `user_asset_dribblets`, must not be `None`")  # noqa: E501

        self._user_asset_dribblets = user_asset_dribblets

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
        if issubclass(InlineResponse20044, dict):
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
        if not isinstance(other, InlineResponse20044):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
