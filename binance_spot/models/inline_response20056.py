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

class InlineResponse20056(object):
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
        'status': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'msg': 'msg'
    }

    def __init__(self, status=None, msg=None):  # noqa: E501
        """InlineResponse20056 - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._msg = None
        self.discriminator = None
        self.status = status
        self.msg = msg

    @property
    def status(self):
        """Gets the status of this InlineResponse20056.  # noqa: E501

        0: normal, 1：system maintenance  # noqa: E501

        :return: The status of this InlineResponse20056.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20056.

        0: normal, 1：system maintenance  # noqa: E501

        :param status: The status of this InlineResponse20056.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def msg(self):
        """Gets the msg of this InlineResponse20056.  # noqa: E501

        \"normal\", \"system_maintenance\"  # noqa: E501

        :return: The msg of this InlineResponse20056.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this InlineResponse20056.

        \"normal\", \"system_maintenance\"  # noqa: E501

        :param msg: The msg of this InlineResponse20056.  # noqa: E501
        :type: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

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
        if issubclass(InlineResponse20056, dict):
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
        if not isinstance(other, InlineResponse20056):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
