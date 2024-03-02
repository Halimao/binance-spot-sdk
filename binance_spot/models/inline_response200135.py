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

class InlineResponse200135(object):
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
        'project': 'str',
        'amount': 'str',
        'lock_period': 'str',
        'deliver_date': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'position_id': 'positionId',
        'time': 'time',
        'asset': 'asset',
        'project': 'project',
        'amount': 'amount',
        'lock_period': 'lockPeriod',
        'deliver_date': 'deliverDate',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, position_id=None, time=None, asset=None, project=None, amount=None, lock_period=None, deliver_date=None, type=None, status=None):  # noqa: E501
        """InlineResponse200135 - a model defined in Swagger"""  # noqa: E501
        self._position_id = None
        self._time = None
        self._asset = None
        self._project = None
        self._amount = None
        self._lock_period = None
        self._deliver_date = None
        self._type = None
        self._status = None
        self.discriminator = None
        self.position_id = position_id
        self.time = time
        self.asset = asset
        self.project = project
        self.amount = amount
        self.lock_period = lock_period
        self.deliver_date = deliver_date
        self.type = type
        self.status = status

    @property
    def position_id(self):
        """Gets the position_id of this InlineResponse200135.  # noqa: E501


        :return: The position_id of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this InlineResponse200135.


        :param position_id: The position_id of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if position_id is None:
            raise ValueError("Invalid value for `position_id`, must not be `None`")  # noqa: E501

        self._position_id = position_id

    @property
    def time(self):
        """Gets the time of this InlineResponse200135.  # noqa: E501


        :return: The time of this InlineResponse200135.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse200135.


        :param time: The time of this InlineResponse200135.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200135.  # noqa: E501


        :return: The asset of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200135.


        :param asset: The asset of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def project(self):
        """Gets the project of this InlineResponse200135.  # noqa: E501


        :return: The project of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InlineResponse200135.


        :param project: The project of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200135.  # noqa: E501


        :return: The amount of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200135.


        :param amount: The amount of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def lock_period(self):
        """Gets the lock_period of this InlineResponse200135.  # noqa: E501


        :return: The lock_period of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._lock_period

    @lock_period.setter
    def lock_period(self, lock_period):
        """Sets the lock_period of this InlineResponse200135.


        :param lock_period: The lock_period of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if lock_period is None:
            raise ValueError("Invalid value for `lock_period`, must not be `None`")  # noqa: E501

        self._lock_period = lock_period

    @property
    def deliver_date(self):
        """Gets the deliver_date of this InlineResponse200135.  # noqa: E501


        :return: The deliver_date of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._deliver_date

    @deliver_date.setter
    def deliver_date(self, deliver_date):
        """Sets the deliver_date of this InlineResponse200135.


        :param deliver_date: The deliver_date of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if deliver_date is None:
            raise ValueError("Invalid value for `deliver_date`, must not be `None`")  # noqa: E501

        self._deliver_date = deliver_date

    @property
    def type(self):
        """Gets the type of this InlineResponse200135.  # noqa: E501


        :return: The type of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200135.


        :param type: The type of this InlineResponse200135.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this InlineResponse200135.  # noqa: E501


        :return: The status of this InlineResponse200135.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200135.


        :param status: The status of this InlineResponse200135.  # noqa: E501
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
        if issubclass(InlineResponse200135, dict):
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
        if not isinstance(other, InlineResponse200135):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
