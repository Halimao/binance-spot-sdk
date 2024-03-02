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

class InlineResponse200245(object):
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
        'plan_id': 'int',
        'next_execution_date_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'plan_id': 'planId',
        'next_execution_date_time': 'nextExecutionDateTime',
        'status': 'status'
    }

    def __init__(self, plan_id=None, next_execution_date_time=None, status=None):  # noqa: E501
        """InlineResponse200245 - a model defined in Swagger"""  # noqa: E501
        self._plan_id = None
        self._next_execution_date_time = None
        self._status = None
        self.discriminator = None
        self.plan_id = plan_id
        self.next_execution_date_time = next_execution_date_time
        self.status = status

    @property
    def plan_id(self):
        """Gets the plan_id of this InlineResponse200245.  # noqa: E501


        :return: The plan_id of this InlineResponse200245.  # noqa: E501
        :rtype: int
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this InlineResponse200245.


        :param plan_id: The plan_id of this InlineResponse200245.  # noqa: E501
        :type: int
        """
        if plan_id is None:
            raise ValueError("Invalid value for `plan_id`, must not be `None`")  # noqa: E501

        self._plan_id = plan_id

    @property
    def next_execution_date_time(self):
        """Gets the next_execution_date_time of this InlineResponse200245.  # noqa: E501


        :return: The next_execution_date_time of this InlineResponse200245.  # noqa: E501
        :rtype: int
        """
        return self._next_execution_date_time

    @next_execution_date_time.setter
    def next_execution_date_time(self, next_execution_date_time):
        """Sets the next_execution_date_time of this InlineResponse200245.


        :param next_execution_date_time: The next_execution_date_time of this InlineResponse200245.  # noqa: E501
        :type: int
        """
        if next_execution_date_time is None:
            raise ValueError("Invalid value for `next_execution_date_time`, must not be `None`")  # noqa: E501

        self._next_execution_date_time = next_execution_date_time

    @property
    def status(self):
        """Gets the status of this InlineResponse200245.  # noqa: E501


        :return: The status of this InlineResponse200245.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200245.


        :param status: The status of this InlineResponse200245.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(InlineResponse200245, dict):
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
        if not isinstance(other, InlineResponse200245):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other