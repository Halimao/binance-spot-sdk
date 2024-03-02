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

class InlineResponse200232(object):
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
        'list': 'list[InlineResponse200232List]'
    }

    attribute_map = {
        'total': 'total',
        'list': 'list'
    }

    def __init__(self, total=None, list=None):  # noqa: E501
        """InlineResponse200232 - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._list = None
        self.discriminator = None
        self.total = total
        self.list = list

    @property
    def total(self):
        """Gets the total of this InlineResponse200232.  # noqa: E501


        :return: The total of this InlineResponse200232.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse200232.


        :param total: The total of this InlineResponse200232.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def list(self):
        """Gets the list of this InlineResponse200232.  # noqa: E501


        :return: The list of this InlineResponse200232.  # noqa: E501
        :rtype: list[InlineResponse200232List]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InlineResponse200232.


        :param list: The list of this InlineResponse200232.  # noqa: E501
        :type: list[InlineResponse200232List]
        """
        if list is None:
            raise ValueError("Invalid value for `list`, must not be `None`")  # noqa: E501

        self._list = list

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
        if issubclass(InlineResponse200232, dict):
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
        if not isinstance(other, InlineResponse200232):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other