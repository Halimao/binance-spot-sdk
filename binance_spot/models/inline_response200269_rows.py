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

class InlineResponse200269Rows(object):
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
        'position_id': 'str',
        'time': 'int',
        'asset': 'str',
        'lock_period': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'position_id': 'positionId',
        'time': 'time',
        'asset': 'asset',
        'lock_period': 'lockPeriod',
        'amount': 'amount'
    }

    def __init__(self, position_id=None, time=None, asset=None, lock_period=None, amount=None):  # noqa: E501
        """InlineResponse200269Rows - a model defined in Swagger"""  # noqa: E501
        self._position_id = None
        self._time = None
        self._asset = None
        self._lock_period = None
        self._amount = None
        self.discriminator = None
        self.position_id = position_id
        self.time = time
        self.asset = asset
        self.lock_period = lock_period
        self.amount = amount

    @property
    def position_id(self):
        """Gets the position_id of this InlineResponse200269Rows.  # noqa: E501


        :return: The position_id of this InlineResponse200269Rows.  # noqa: E501
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this InlineResponse200269Rows.


        :param position_id: The position_id of this InlineResponse200269Rows.  # noqa: E501
        :type: str
        """
        if position_id is None:
            raise ValueError("Invalid value for `position_id`, must not be `None`")  # noqa: E501

        self._position_id = position_id

    @property
    def time(self):
        """Gets the time of this InlineResponse200269Rows.  # noqa: E501


        :return: The time of this InlineResponse200269Rows.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse200269Rows.


        :param time: The time of this InlineResponse200269Rows.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200269Rows.  # noqa: E501


        :return: The asset of this InlineResponse200269Rows.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200269Rows.


        :param asset: The asset of this InlineResponse200269Rows.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def lock_period(self):
        """Gets the lock_period of this InlineResponse200269Rows.  # noqa: E501


        :return: The lock_period of this InlineResponse200269Rows.  # noqa: E501
        :rtype: str
        """
        return self._lock_period

    @lock_period.setter
    def lock_period(self, lock_period):
        """Sets the lock_period of this InlineResponse200269Rows.


        :param lock_period: The lock_period of this InlineResponse200269Rows.  # noqa: E501
        :type: str
        """
        if lock_period is None:
            raise ValueError("Invalid value for `lock_period`, must not be `None`")  # noqa: E501

        self._lock_period = lock_period

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200269Rows.  # noqa: E501


        :return: The amount of this InlineResponse200269Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200269Rows.


        :param amount: The amount of this InlineResponse200269Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(InlineResponse200269Rows, dict):
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
        if not isinstance(other, InlineResponse200269Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other