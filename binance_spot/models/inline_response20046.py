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

class InlineResponse20046(object):
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
        'asset': 'str',
        'interest': 'str',
        'principal': 'str',
        'liability_asset': 'str',
        'liability_qty': 'float'
    }

    attribute_map = {
        'asset': 'asset',
        'interest': 'interest',
        'principal': 'principal',
        'liability_asset': 'liabilityAsset',
        'liability_qty': 'liabilityQty'
    }

    def __init__(self, asset=None, interest=None, principal=None, liability_asset=None, liability_qty=None):  # noqa: E501
        """InlineResponse20046 - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._interest = None
        self._principal = None
        self._liability_asset = None
        self._liability_qty = None
        self.discriminator = None
        self.asset = asset
        self.interest = interest
        self.principal = principal
        self.liability_asset = liability_asset
        self.liability_qty = liability_qty

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20046.  # noqa: E501


        :return: The asset of this InlineResponse20046.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20046.


        :param asset: The asset of this InlineResponse20046.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def interest(self):
        """Gets the interest of this InlineResponse20046.  # noqa: E501


        :return: The interest of this InlineResponse20046.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this InlineResponse20046.


        :param interest: The interest of this InlineResponse20046.  # noqa: E501
        :type: str
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def principal(self):
        """Gets the principal of this InlineResponse20046.  # noqa: E501


        :return: The principal of this InlineResponse20046.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this InlineResponse20046.


        :param principal: The principal of this InlineResponse20046.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def liability_asset(self):
        """Gets the liability_asset of this InlineResponse20046.  # noqa: E501


        :return: The liability_asset of this InlineResponse20046.  # noqa: E501
        :rtype: str
        """
        return self._liability_asset

    @liability_asset.setter
    def liability_asset(self, liability_asset):
        """Sets the liability_asset of this InlineResponse20046.


        :param liability_asset: The liability_asset of this InlineResponse20046.  # noqa: E501
        :type: str
        """
        if liability_asset is None:
            raise ValueError("Invalid value for `liability_asset`, must not be `None`")  # noqa: E501

        self._liability_asset = liability_asset

    @property
    def liability_qty(self):
        """Gets the liability_qty of this InlineResponse20046.  # noqa: E501


        :return: The liability_qty of this InlineResponse20046.  # noqa: E501
        :rtype: float
        """
        return self._liability_qty

    @liability_qty.setter
    def liability_qty(self, liability_qty):
        """Sets the liability_qty of this InlineResponse20046.


        :param liability_qty: The liability_qty of this InlineResponse20046.  # noqa: E501
        :type: float
        """
        if liability_qty is None:
            raise ValueError("Invalid value for `liability_qty`, must not be `None`")  # noqa: E501

        self._liability_qty = liability_qty

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
        if issubclass(InlineResponse20046, dict):
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
        if not isinstance(other, InlineResponse20046):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
