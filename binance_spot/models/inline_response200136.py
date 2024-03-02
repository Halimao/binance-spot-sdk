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

class InlineResponse200136(object):
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
        'left_personal_quota': 'str'
    }

    attribute_map = {
        'left_personal_quota': 'leftPersonalQuota'
    }

    def __init__(self, left_personal_quota=None):  # noqa: E501
        """InlineResponse200136 - a model defined in Swagger"""  # noqa: E501
        self._left_personal_quota = None
        self.discriminator = None
        self.left_personal_quota = left_personal_quota

    @property
    def left_personal_quota(self):
        """Gets the left_personal_quota of this InlineResponse200136.  # noqa: E501


        :return: The left_personal_quota of this InlineResponse200136.  # noqa: E501
        :rtype: str
        """
        return self._left_personal_quota

    @left_personal_quota.setter
    def left_personal_quota(self, left_personal_quota):
        """Sets the left_personal_quota of this InlineResponse200136.


        :param left_personal_quota: The left_personal_quota of this InlineResponse200136.  # noqa: E501
        :type: str
        """
        if left_personal_quota is None:
            raise ValueError("Invalid value for `left_personal_quota`, must not be `None`")  # noqa: E501

        self._left_personal_quota = left_personal_quota

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
        if issubclass(InlineResponse200136, dict):
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
        if not isinstance(other, InlineResponse200136):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
