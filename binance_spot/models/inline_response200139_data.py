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

class InlineResponse200139Data(object):
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
        'worker_name': 'str',
        'type': 'str',
        'hashrate_datas': 'list[InlineResponse200139HashrateDatas]'
    }

    attribute_map = {
        'worker_name': 'workerName',
        'type': 'type',
        'hashrate_datas': 'hashrateDatas'
    }

    def __init__(self, worker_name=None, type=None, hashrate_datas=None):  # noqa: E501
        """InlineResponse200139Data - a model defined in Swagger"""  # noqa: E501
        self._worker_name = None
        self._type = None
        self._hashrate_datas = None
        self.discriminator = None
        self.worker_name = worker_name
        self.type = type
        self.hashrate_datas = hashrate_datas

    @property
    def worker_name(self):
        """Gets the worker_name of this InlineResponse200139Data.  # noqa: E501

        Mining Account name  # noqa: E501

        :return: The worker_name of this InlineResponse200139Data.  # noqa: E501
        :rtype: str
        """
        return self._worker_name

    @worker_name.setter
    def worker_name(self, worker_name):
        """Sets the worker_name of this InlineResponse200139Data.

        Mining Account name  # noqa: E501

        :param worker_name: The worker_name of this InlineResponse200139Data.  # noqa: E501
        :type: str
        """
        if worker_name is None:
            raise ValueError("Invalid value for `worker_name`, must not be `None`")  # noqa: E501

        self._worker_name = worker_name

    @property
    def type(self):
        """Gets the type of this InlineResponse200139Data.  # noqa: E501

        Type of hourly hashrate  # noqa: E501

        :return: The type of this InlineResponse200139Data.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200139Data.

        Type of hourly hashrate  # noqa: E501

        :param type: The type of this InlineResponse200139Data.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def hashrate_datas(self):
        """Gets the hashrate_datas of this InlineResponse200139Data.  # noqa: E501


        :return: The hashrate_datas of this InlineResponse200139Data.  # noqa: E501
        :rtype: list[InlineResponse200139HashrateDatas]
        """
        return self._hashrate_datas

    @hashrate_datas.setter
    def hashrate_datas(self, hashrate_datas):
        """Sets the hashrate_datas of this InlineResponse200139Data.


        :param hashrate_datas: The hashrate_datas of this InlineResponse200139Data.  # noqa: E501
        :type: list[InlineResponse200139HashrateDatas]
        """
        if hashrate_datas is None:
            raise ValueError("Invalid value for `hashrate_datas`, must not be `None`")  # noqa: E501

        self._hashrate_datas = hashrate_datas

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
        if issubclass(InlineResponse200139Data, dict):
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
        if not isinstance(other, InlineResponse200139Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
