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

class InlineResponse200224(object):
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
        'from_asset': 'str',
        'to_asset': 'str',
        'from_asset_min_amount': 'str',
        'from_asset_max_amount': 'str',
        'to_asset_min_amount': 'str',
        'to_asset_max_amount': 'str'
    }

    attribute_map = {
        'from_asset': 'fromAsset',
        'to_asset': 'toAsset',
        'from_asset_min_amount': 'fromAssetMinAmount',
        'from_asset_max_amount': 'fromAssetMaxAmount',
        'to_asset_min_amount': 'toAssetMinAmount',
        'to_asset_max_amount': 'toAssetMaxAmount'
    }

    def __init__(self, from_asset=None, to_asset=None, from_asset_min_amount=None, from_asset_max_amount=None, to_asset_min_amount=None, to_asset_max_amount=None):  # noqa: E501
        """InlineResponse200224 - a model defined in Swagger"""  # noqa: E501
        self._from_asset = None
        self._to_asset = None
        self._from_asset_min_amount = None
        self._from_asset_max_amount = None
        self._to_asset_min_amount = None
        self._to_asset_max_amount = None
        self.discriminator = None
        self.from_asset = from_asset
        self.to_asset = to_asset
        self.from_asset_min_amount = from_asset_min_amount
        self.from_asset_max_amount = from_asset_max_amount
        self.to_asset_min_amount = to_asset_min_amount
        self.to_asset_max_amount = to_asset_max_amount

    @property
    def from_asset(self):
        """Gets the from_asset of this InlineResponse200224.  # noqa: E501


        :return: The from_asset of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._from_asset

    @from_asset.setter
    def from_asset(self, from_asset):
        """Sets the from_asset of this InlineResponse200224.


        :param from_asset: The from_asset of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if from_asset is None:
            raise ValueError("Invalid value for `from_asset`, must not be `None`")  # noqa: E501

        self._from_asset = from_asset

    @property
    def to_asset(self):
        """Gets the to_asset of this InlineResponse200224.  # noqa: E501


        :return: The to_asset of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._to_asset

    @to_asset.setter
    def to_asset(self, to_asset):
        """Sets the to_asset of this InlineResponse200224.


        :param to_asset: The to_asset of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if to_asset is None:
            raise ValueError("Invalid value for `to_asset`, must not be `None`")  # noqa: E501

        self._to_asset = to_asset

    @property
    def from_asset_min_amount(self):
        """Gets the from_asset_min_amount of this InlineResponse200224.  # noqa: E501


        :return: The from_asset_min_amount of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._from_asset_min_amount

    @from_asset_min_amount.setter
    def from_asset_min_amount(self, from_asset_min_amount):
        """Sets the from_asset_min_amount of this InlineResponse200224.


        :param from_asset_min_amount: The from_asset_min_amount of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if from_asset_min_amount is None:
            raise ValueError("Invalid value for `from_asset_min_amount`, must not be `None`")  # noqa: E501

        self._from_asset_min_amount = from_asset_min_amount

    @property
    def from_asset_max_amount(self):
        """Gets the from_asset_max_amount of this InlineResponse200224.  # noqa: E501


        :return: The from_asset_max_amount of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._from_asset_max_amount

    @from_asset_max_amount.setter
    def from_asset_max_amount(self, from_asset_max_amount):
        """Sets the from_asset_max_amount of this InlineResponse200224.


        :param from_asset_max_amount: The from_asset_max_amount of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if from_asset_max_amount is None:
            raise ValueError("Invalid value for `from_asset_max_amount`, must not be `None`")  # noqa: E501

        self._from_asset_max_amount = from_asset_max_amount

    @property
    def to_asset_min_amount(self):
        """Gets the to_asset_min_amount of this InlineResponse200224.  # noqa: E501


        :return: The to_asset_min_amount of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_min_amount

    @to_asset_min_amount.setter
    def to_asset_min_amount(self, to_asset_min_amount):
        """Sets the to_asset_min_amount of this InlineResponse200224.


        :param to_asset_min_amount: The to_asset_min_amount of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if to_asset_min_amount is None:
            raise ValueError("Invalid value for `to_asset_min_amount`, must not be `None`")  # noqa: E501

        self._to_asset_min_amount = to_asset_min_amount

    @property
    def to_asset_max_amount(self):
        """Gets the to_asset_max_amount of this InlineResponse200224.  # noqa: E501


        :return: The to_asset_max_amount of this InlineResponse200224.  # noqa: E501
        :rtype: str
        """
        return self._to_asset_max_amount

    @to_asset_max_amount.setter
    def to_asset_max_amount(self, to_asset_max_amount):
        """Sets the to_asset_max_amount of this InlineResponse200224.


        :param to_asset_max_amount: The to_asset_max_amount of this InlineResponse200224.  # noqa: E501
        :type: str
        """
        if to_asset_max_amount is None:
            raise ValueError("Invalid value for `to_asset_max_amount`, must not be `None`")  # noqa: E501

        self._to_asset_max_amount = to_asset_max_amount

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
        if issubclass(InlineResponse200224, dict):
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
        if not isinstance(other, InlineResponse200224):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
