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

class InlineResponse200143DataConfigDetails(object):
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
        'config_id': 'int',
        'pool_username': 'str',
        'to_pool_username': 'str',
        'algo_name': 'str',
        'hash_rate': 'int',
        'start_day': 'int',
        'end_day': 'int',
        'status': 'int'
    }

    attribute_map = {
        'config_id': 'configId',
        'pool_username': 'poolUsername',
        'to_pool_username': 'toPoolUsername',
        'algo_name': 'algoName',
        'hash_rate': 'hashRate',
        'start_day': 'startDay',
        'end_day': 'endDay',
        'status': 'status'
    }

    def __init__(self, config_id=None, pool_username=None, to_pool_username=None, algo_name=None, hash_rate=None, start_day=None, end_day=None, status=None):  # noqa: E501
        """InlineResponse200143DataConfigDetails - a model defined in Swagger"""  # noqa: E501
        self._config_id = None
        self._pool_username = None
        self._to_pool_username = None
        self._algo_name = None
        self._hash_rate = None
        self._start_day = None
        self._end_day = None
        self._status = None
        self.discriminator = None
        self.config_id = config_id
        self.pool_username = pool_username
        self.to_pool_username = to_pool_username
        self.algo_name = algo_name
        self.hash_rate = hash_rate
        self.start_day = start_day
        self.end_day = end_day
        self.status = status

    @property
    def config_id(self):
        """Gets the config_id of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Mining ID  # noqa: E501

        :return: The config_id of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: int
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this InlineResponse200143DataConfigDetails.

        Mining ID  # noqa: E501

        :param config_id: The config_id of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: int
        """
        if config_id is None:
            raise ValueError("Invalid value for `config_id`, must not be `None`")  # noqa: E501

        self._config_id = config_id

    @property
    def pool_username(self):
        """Gets the pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Transfer out of subaccount  # noqa: E501

        :return: The pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: str
        """
        return self._pool_username

    @pool_username.setter
    def pool_username(self, pool_username):
        """Sets the pool_username of this InlineResponse200143DataConfigDetails.

        Transfer out of subaccount  # noqa: E501

        :param pool_username: The pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: str
        """
        if pool_username is None:
            raise ValueError("Invalid value for `pool_username`, must not be `None`")  # noqa: E501

        self._pool_username = pool_username

    @property
    def to_pool_username(self):
        """Gets the to_pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Transfer into subaccount  # noqa: E501

        :return: The to_pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: str
        """
        return self._to_pool_username

    @to_pool_username.setter
    def to_pool_username(self, to_pool_username):
        """Sets the to_pool_username of this InlineResponse200143DataConfigDetails.

        Transfer into subaccount  # noqa: E501

        :param to_pool_username: The to_pool_username of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: str
        """
        if to_pool_username is None:
            raise ValueError("Invalid value for `to_pool_username`, must not be `None`")  # noqa: E501

        self._to_pool_username = to_pool_username

    @property
    def algo_name(self):
        """Gets the algo_name of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Transfer algorithm  # noqa: E501

        :return: The algo_name of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: str
        """
        return self._algo_name

    @algo_name.setter
    def algo_name(self, algo_name):
        """Sets the algo_name of this InlineResponse200143DataConfigDetails.

        Transfer algorithm  # noqa: E501

        :param algo_name: The algo_name of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: str
        """
        if algo_name is None:
            raise ValueError("Invalid value for `algo_name`, must not be `None`")  # noqa: E501

        self._algo_name = algo_name

    @property
    def hash_rate(self):
        """Gets the hash_rate of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Transferred Hashrate quantity  # noqa: E501

        :return: The hash_rate of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: int
        """
        return self._hash_rate

    @hash_rate.setter
    def hash_rate(self, hash_rate):
        """Sets the hash_rate of this InlineResponse200143DataConfigDetails.

        Transferred Hashrate quantity  # noqa: E501

        :param hash_rate: The hash_rate of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: int
        """
        if hash_rate is None:
            raise ValueError("Invalid value for `hash_rate`, must not be `None`")  # noqa: E501

        self._hash_rate = hash_rate

    @property
    def start_day(self):
        """Gets the start_day of this InlineResponse200143DataConfigDetails.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_day of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: int
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        """Sets the start_day of this InlineResponse200143DataConfigDetails.

        Start date  # noqa: E501

        :param start_day: The start_day of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: int
        """
        if start_day is None:
            raise ValueError("Invalid value for `start_day`, must not be `None`")  # noqa: E501

        self._start_day = start_day

    @property
    def end_day(self):
        """Gets the end_day of this InlineResponse200143DataConfigDetails.  # noqa: E501

        End date  # noqa: E501

        :return: The end_day of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: int
        """
        return self._end_day

    @end_day.setter
    def end_day(self, end_day):
        """Sets the end_day of this InlineResponse200143DataConfigDetails.

        End date  # noqa: E501

        :param end_day: The end_day of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: int
        """
        if end_day is None:
            raise ValueError("Invalid value for `end_day`, must not be `None`")  # noqa: E501

        self._end_day = end_day

    @property
    def status(self):
        """Gets the status of this InlineResponse200143DataConfigDetails.  # noqa: E501

        0 Processing, 1：Cancelled, 2：Terminated   # noqa: E501

        :return: The status of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200143DataConfigDetails.

        0 Processing, 1：Cancelled, 2：Terminated   # noqa: E501

        :param status: The status of this InlineResponse200143DataConfigDetails.  # noqa: E501
        :type: int
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
        if issubclass(InlineResponse200143DataConfigDetails, dict):
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
        if not isinstance(other, InlineResponse200143DataConfigDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
