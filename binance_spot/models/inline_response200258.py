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

class InlineResponse200258(object):
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
        'purchase_id': 'int',
        'success': 'bool'
    }

    attribute_map = {
        'purchase_id': 'purchaseId',
        'success': 'success'
    }

    def __init__(self, purchase_id=None, success=None):  # noqa: E501
        """InlineResponse200258 - a model defined in Swagger"""  # noqa: E501
        self._purchase_id = None
        self._success = None
        self.discriminator = None
        self.purchase_id = purchase_id
        self.success = success

    @property
    def purchase_id(self):
        """Gets the purchase_id of this InlineResponse200258.  # noqa: E501


        :return: The purchase_id of this InlineResponse200258.  # noqa: E501
        :rtype: int
        """
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, purchase_id):
        """Sets the purchase_id of this InlineResponse200258.


        :param purchase_id: The purchase_id of this InlineResponse200258.  # noqa: E501
        :type: int
        """
        if purchase_id is None:
            raise ValueError("Invalid value for `purchase_id`, must not be `None`")  # noqa: E501

        self._purchase_id = purchase_id

    @property
    def success(self):
        """Gets the success of this InlineResponse200258.  # noqa: E501


        :return: The success of this InlineResponse200258.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse200258.


        :param success: The success of this InlineResponse200258.  # noqa: E501
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
        if issubclass(InlineResponse200258, dict):
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
        if not isinstance(other, InlineResponse200258):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
