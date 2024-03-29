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

class InlineResponse20064DataTriggerCondition(object):
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
        'gcr': 'int',
        'ifer': 'int',
        'ufr': 'int'
    }

    attribute_map = {
        'gcr': 'GCR',
        'ifer': 'IFER',
        'ufr': 'UFR'
    }

    def __init__(self, gcr=None, ifer=None, ufr=None):  # noqa: E501
        """InlineResponse20064DataTriggerCondition - a model defined in Swagger"""  # noqa: E501
        self._gcr = None
        self._ifer = None
        self._ufr = None
        self.discriminator = None
        self.gcr = gcr
        self.ifer = ifer
        self.ufr = ufr

    @property
    def gcr(self):
        """Gets the gcr of this InlineResponse20064DataTriggerCondition.  # noqa: E501

        Number of GTC orders  # noqa: E501

        :return: The gcr of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :rtype: int
        """
        return self._gcr

    @gcr.setter
    def gcr(self, gcr):
        """Sets the gcr of this InlineResponse20064DataTriggerCondition.

        Number of GTC orders  # noqa: E501

        :param gcr: The gcr of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :type: int
        """
        if gcr is None:
            raise ValueError("Invalid value for `gcr`, must not be `None`")  # noqa: E501

        self._gcr = gcr

    @property
    def ifer(self):
        """Gets the ifer of this InlineResponse20064DataTriggerCondition.  # noqa: E501

        Number of FOK/IOC orders  # noqa: E501

        :return: The ifer of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :rtype: int
        """
        return self._ifer

    @ifer.setter
    def ifer(self, ifer):
        """Sets the ifer of this InlineResponse20064DataTriggerCondition.

        Number of FOK/IOC orders  # noqa: E501

        :param ifer: The ifer of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :type: int
        """
        if ifer is None:
            raise ValueError("Invalid value for `ifer`, must not be `None`")  # noqa: E501

        self._ifer = ifer

    @property
    def ufr(self):
        """Gets the ufr of this InlineResponse20064DataTriggerCondition.  # noqa: E501

        Number of orders  # noqa: E501

        :return: The ufr of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :rtype: int
        """
        return self._ufr

    @ufr.setter
    def ufr(self, ufr):
        """Sets the ufr of this InlineResponse20064DataTriggerCondition.

        Number of orders  # noqa: E501

        :param ufr: The ufr of this InlineResponse20064DataTriggerCondition.  # noqa: E501
        :type: int
        """
        if ufr is None:
            raise ValueError("Invalid value for `ufr`, must not be `None`")  # noqa: E501

        self._ufr = ufr

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
        if issubclass(InlineResponse20064DataTriggerCondition, dict):
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
        if not isinstance(other, InlineResponse20064DataTriggerCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
