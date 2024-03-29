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

class InlineResponse200122(object):
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
        'status': 'str',
        'ip_list': 'list[str]',
        'update_time': 'int',
        'api_key': 'str'
    }

    attribute_map = {
        'status': 'status',
        'ip_list': 'ipList',
        'update_time': 'updateTime',
        'api_key': 'apiKey'
    }

    def __init__(self, status=None, ip_list=None, update_time=None, api_key=None):  # noqa: E501
        """InlineResponse200122 - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._ip_list = None
        self._update_time = None
        self._api_key = None
        self.discriminator = None
        self.status = status
        self.ip_list = ip_list
        self.update_time = update_time
        self.api_key = api_key

    @property
    def status(self):
        """Gets the status of this InlineResponse200122.  # noqa: E501


        :return: The status of this InlineResponse200122.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200122.


        :param status: The status of this InlineResponse200122.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def ip_list(self):
        """Gets the ip_list of this InlineResponse200122.  # noqa: E501


        :return: The ip_list of this InlineResponse200122.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this InlineResponse200122.


        :param ip_list: The ip_list of this InlineResponse200122.  # noqa: E501
        :type: list[str]
        """
        if ip_list is None:
            raise ValueError("Invalid value for `ip_list`, must not be `None`")  # noqa: E501

        self._ip_list = ip_list

    @property
    def update_time(self):
        """Gets the update_time of this InlineResponse200122.  # noqa: E501


        :return: The update_time of this InlineResponse200122.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this InlineResponse200122.


        :param update_time: The update_time of this InlineResponse200122.  # noqa: E501
        :type: int
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def api_key(self):
        """Gets the api_key of this InlineResponse200122.  # noqa: E501


        :return: The api_key of this InlineResponse200122.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this InlineResponse200122.


        :param api_key: The api_key of this InlineResponse200122.  # noqa: E501
        :type: str
        """
        if api_key is None:
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

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
        if issubclass(InlineResponse200122, dict):
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
        if not isinstance(other, InlineResponse200122):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
