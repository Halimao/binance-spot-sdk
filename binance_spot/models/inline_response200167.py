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

class InlineResponse200167(object):
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
        'interest': 'str',
        'interest_accrued_time': 'int',
        'interest_rate': 'str',
        'principal': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'interest': 'interest',
        'interest_accrued_time': 'interestAccruedTime',
        'interest_rate': 'interestRate',
        'principal': 'principal'
    }

    def __init__(self, asset=None, interest=None, interest_accrued_time=None, interest_rate=None, principal=None):  # noqa: E501
        """InlineResponse200167 - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._interest = None
        self._interest_accrued_time = None
        self._interest_rate = None
        self._principal = None
        self.discriminator = None
        self.asset = asset
        self.interest = interest
        self.interest_accrued_time = interest_accrued_time
        self.interest_rate = interest_rate
        self.principal = principal

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200167.  # noqa: E501


        :return: The asset of this InlineResponse200167.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200167.


        :param asset: The asset of this InlineResponse200167.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def interest(self):
        """Gets the interest of this InlineResponse200167.  # noqa: E501


        :return: The interest of this InlineResponse200167.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this InlineResponse200167.


        :param interest: The interest of this InlineResponse200167.  # noqa: E501
        :type: str
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def interest_accrued_time(self):
        """Gets the interest_accrued_time of this InlineResponse200167.  # noqa: E501


        :return: The interest_accrued_time of this InlineResponse200167.  # noqa: E501
        :rtype: int
        """
        return self._interest_accrued_time

    @interest_accrued_time.setter
    def interest_accrued_time(self, interest_accrued_time):
        """Sets the interest_accrued_time of this InlineResponse200167.


        :param interest_accrued_time: The interest_accrued_time of this InlineResponse200167.  # noqa: E501
        :type: int
        """
        if interest_accrued_time is None:
            raise ValueError("Invalid value for `interest_accrued_time`, must not be `None`")  # noqa: E501

        self._interest_accrued_time = interest_accrued_time

    @property
    def interest_rate(self):
        """Gets the interest_rate of this InlineResponse200167.  # noqa: E501


        :return: The interest_rate of this InlineResponse200167.  # noqa: E501
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this InlineResponse200167.


        :param interest_rate: The interest_rate of this InlineResponse200167.  # noqa: E501
        :type: str
        """
        if interest_rate is None:
            raise ValueError("Invalid value for `interest_rate`, must not be `None`")  # noqa: E501

        self._interest_rate = interest_rate

    @property
    def principal(self):
        """Gets the principal of this InlineResponse200167.  # noqa: E501


        :return: The principal of this InlineResponse200167.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this InlineResponse200167.


        :param principal: The principal of this InlineResponse200167.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

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
        if issubclass(InlineResponse200167, dict):
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
        if not isinstance(other, InlineResponse200167):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
