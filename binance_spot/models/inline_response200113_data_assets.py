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

class InlineResponse200113DataAssets(object):
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
        'margin_balance': 'float',
        'wallet_balance': 'float'
    }

    attribute_map = {
        'asset': 'asset',
        'margin_balance': 'marginBalance',
        'wallet_balance': 'walletBalance'
    }

    def __init__(self, asset=None, margin_balance=None, wallet_balance=None):  # noqa: E501
        """InlineResponse200113DataAssets - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._margin_balance = None
        self._wallet_balance = None
        self.discriminator = None
        self.asset = asset
        self.margin_balance = margin_balance
        self.wallet_balance = wallet_balance

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200113DataAssets.  # noqa: E501


        :return: The asset of this InlineResponse200113DataAssets.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200113DataAssets.


        :param asset: The asset of this InlineResponse200113DataAssets.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def margin_balance(self):
        """Gets the margin_balance of this InlineResponse200113DataAssets.  # noqa: E501


        :return: The margin_balance of this InlineResponse200113DataAssets.  # noqa: E501
        :rtype: float
        """
        return self._margin_balance

    @margin_balance.setter
    def margin_balance(self, margin_balance):
        """Sets the margin_balance of this InlineResponse200113DataAssets.


        :param margin_balance: The margin_balance of this InlineResponse200113DataAssets.  # noqa: E501
        :type: float
        """
        if margin_balance is None:
            raise ValueError("Invalid value for `margin_balance`, must not be `None`")  # noqa: E501

        self._margin_balance = margin_balance

    @property
    def wallet_balance(self):
        """Gets the wallet_balance of this InlineResponse200113DataAssets.  # noqa: E501


        :return: The wallet_balance of this InlineResponse200113DataAssets.  # noqa: E501
        :rtype: float
        """
        return self._wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wallet_balance):
        """Sets the wallet_balance of this InlineResponse200113DataAssets.


        :param wallet_balance: The wallet_balance of this InlineResponse200113DataAssets.  # noqa: E501
        :type: float
        """
        if wallet_balance is None:
            raise ValueError("Invalid value for `wallet_balance`, must not be `None`")  # noqa: E501

        self._wallet_balance = wallet_balance

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
        if issubclass(InlineResponse200113DataAssets, dict):
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
        if not isinstance(other, InlineResponse200113DataAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
