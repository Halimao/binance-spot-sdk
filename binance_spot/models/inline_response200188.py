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

class InlineResponse200188(object):
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
        'total_unclaimed_rewards': 'InlineResponse200188TotalUnclaimedRewards',
        'details': 'InlineResponse200188Details'
    }

    attribute_map = {
        'total_unclaimed_rewards': 'totalUnclaimedRewards',
        'details': 'details'
    }

    def __init__(self, total_unclaimed_rewards=None, details=None):  # noqa: E501
        """InlineResponse200188 - a model defined in Swagger"""  # noqa: E501
        self._total_unclaimed_rewards = None
        self._details = None
        self.discriminator = None
        self.total_unclaimed_rewards = total_unclaimed_rewards
        self.details = details

    @property
    def total_unclaimed_rewards(self):
        """Gets the total_unclaimed_rewards of this InlineResponse200188.  # noqa: E501


        :return: The total_unclaimed_rewards of this InlineResponse200188.  # noqa: E501
        :rtype: InlineResponse200188TotalUnclaimedRewards
        """
        return self._total_unclaimed_rewards

    @total_unclaimed_rewards.setter
    def total_unclaimed_rewards(self, total_unclaimed_rewards):
        """Sets the total_unclaimed_rewards of this InlineResponse200188.


        :param total_unclaimed_rewards: The total_unclaimed_rewards of this InlineResponse200188.  # noqa: E501
        :type: InlineResponse200188TotalUnclaimedRewards
        """
        if total_unclaimed_rewards is None:
            raise ValueError("Invalid value for `total_unclaimed_rewards`, must not be `None`")  # noqa: E501

        self._total_unclaimed_rewards = total_unclaimed_rewards

    @property
    def details(self):
        """Gets the details of this InlineResponse200188.  # noqa: E501


        :return: The details of this InlineResponse200188.  # noqa: E501
        :rtype: InlineResponse200188Details
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this InlineResponse200188.


        :param details: The details of this InlineResponse200188.  # noqa: E501
        :type: InlineResponse200188Details
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

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
        if issubclass(InlineResponse200188, dict):
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
        if not isinstance(other, InlineResponse200188):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
