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

class InlineResponse200239(object):
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
        'code': 'str',
        'message': 'str',
        'data': 'InlineResponse200239Data',
        'success': 'bool'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data',
        'success': 'success'
    }

    def __init__(self, code=None, message=None, data=None, success=None):  # noqa: E501
        """InlineResponse200239 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._data = None
        self._success = None
        self.discriminator = None
        self.code = code
        self.message = message
        self.data = data
        self.success = success

    @property
    def code(self):
        """Gets the code of this InlineResponse200239.  # noqa: E501


        :return: The code of this InlineResponse200239.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse200239.


        :param code: The code of this InlineResponse200239.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponse200239.  # noqa: E501


        :return: The message of this InlineResponse200239.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse200239.


        :param message: The message of this InlineResponse200239.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def data(self):
        """Gets the data of this InlineResponse200239.  # noqa: E501


        :return: The data of this InlineResponse200239.  # noqa: E501
        :rtype: InlineResponse200239Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse200239.


        :param data: The data of this InlineResponse200239.  # noqa: E501
        :type: InlineResponse200239Data
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def success(self):
        """Gets the success of this InlineResponse200239.  # noqa: E501


        :return: The success of this InlineResponse200239.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse200239.


        :param success: The success of this InlineResponse200239.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

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
        if issubclass(InlineResponse200239, dict):
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
        if not isinstance(other, InlineResponse200239):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
