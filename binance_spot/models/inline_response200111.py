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

class InlineResponse200111(object):
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
        'code': 'int',
        'msg': 'str',
        'snapshot_vos': 'list[InlineResponse200111SnapshotVos]'
    }

    attribute_map = {
        'code': 'code',
        'msg': 'msg',
        'snapshot_vos': 'snapshotVos'
    }

    def __init__(self, code=None, msg=None, snapshot_vos=None):  # noqa: E501
        """InlineResponse200111 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._msg = None
        self._snapshot_vos = None
        self.discriminator = None
        self.code = code
        self.msg = msg
        self.snapshot_vos = snapshot_vos

    @property
    def code(self):
        """Gets the code of this InlineResponse200111.  # noqa: E501


        :return: The code of this InlineResponse200111.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse200111.


        :param code: The code of this InlineResponse200111.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def msg(self):
        """Gets the msg of this InlineResponse200111.  # noqa: E501


        :return: The msg of this InlineResponse200111.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this InlineResponse200111.


        :param msg: The msg of this InlineResponse200111.  # noqa: E501
        :type: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

    @property
    def snapshot_vos(self):
        """Gets the snapshot_vos of this InlineResponse200111.  # noqa: E501


        :return: The snapshot_vos of this InlineResponse200111.  # noqa: E501
        :rtype: list[InlineResponse200111SnapshotVos]
        """
        return self._snapshot_vos

    @snapshot_vos.setter
    def snapshot_vos(self, snapshot_vos):
        """Sets the snapshot_vos of this InlineResponse200111.


        :param snapshot_vos: The snapshot_vos of this InlineResponse200111.  # noqa: E501
        :type: list[InlineResponse200111SnapshotVos]
        """
        if snapshot_vos is None:
            raise ValueError("Invalid value for `snapshot_vos`, must not be `None`")  # noqa: E501

        self._snapshot_vos = snapshot_vos

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
        if issubclass(InlineResponse200111, dict):
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
        if not isinstance(other, InlineResponse200111):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
