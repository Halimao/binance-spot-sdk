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

class InlineResponse20074(object):
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
        'free': 'str',
        'locked': 'str',
        'freeze': 'str',
        'withdrawing': 'str',
        'ipoable': 'str',
        'btc_valuation': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'free': 'free',
        'locked': 'locked',
        'freeze': 'freeze',
        'withdrawing': 'withdrawing',
        'ipoable': 'ipoable',
        'btc_valuation': 'btcValuation'
    }

    def __init__(self, asset=None, free=None, locked=None, freeze=None, withdrawing=None, ipoable=None, btc_valuation=None):  # noqa: E501
        """InlineResponse20074 - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._free = None
        self._locked = None
        self._freeze = None
        self._withdrawing = None
        self._ipoable = None
        self._btc_valuation = None
        self.discriminator = None
        self.asset = asset
        self.free = free
        self.locked = locked
        self.freeze = freeze
        self.withdrawing = withdrawing
        self.ipoable = ipoable
        self.btc_valuation = btc_valuation

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20074.  # noqa: E501


        :return: The asset of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20074.


        :param asset: The asset of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def free(self):
        """Gets the free of this InlineResponse20074.  # noqa: E501


        :return: The free of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this InlineResponse20074.


        :param free: The free of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if free is None:
            raise ValueError("Invalid value for `free`, must not be `None`")  # noqa: E501

        self._free = free

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20074.  # noqa: E501


        :return: The locked of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20074.


        :param locked: The locked of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if locked is None:
            raise ValueError("Invalid value for `locked`, must not be `None`")  # noqa: E501

        self._locked = locked

    @property
    def freeze(self):
        """Gets the freeze of this InlineResponse20074.  # noqa: E501


        :return: The freeze of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._freeze

    @freeze.setter
    def freeze(self, freeze):
        """Sets the freeze of this InlineResponse20074.


        :param freeze: The freeze of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if freeze is None:
            raise ValueError("Invalid value for `freeze`, must not be `None`")  # noqa: E501

        self._freeze = freeze

    @property
    def withdrawing(self):
        """Gets the withdrawing of this InlineResponse20074.  # noqa: E501


        :return: The withdrawing of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._withdrawing

    @withdrawing.setter
    def withdrawing(self, withdrawing):
        """Sets the withdrawing of this InlineResponse20074.


        :param withdrawing: The withdrawing of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if withdrawing is None:
            raise ValueError("Invalid value for `withdrawing`, must not be `None`")  # noqa: E501

        self._withdrawing = withdrawing

    @property
    def ipoable(self):
        """Gets the ipoable of this InlineResponse20074.  # noqa: E501


        :return: The ipoable of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._ipoable

    @ipoable.setter
    def ipoable(self, ipoable):
        """Sets the ipoable of this InlineResponse20074.


        :param ipoable: The ipoable of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if ipoable is None:
            raise ValueError("Invalid value for `ipoable`, must not be `None`")  # noqa: E501

        self._ipoable = ipoable

    @property
    def btc_valuation(self):
        """Gets the btc_valuation of this InlineResponse20074.  # noqa: E501


        :return: The btc_valuation of this InlineResponse20074.  # noqa: E501
        :rtype: str
        """
        return self._btc_valuation

    @btc_valuation.setter
    def btc_valuation(self, btc_valuation):
        """Sets the btc_valuation of this InlineResponse20074.


        :param btc_valuation: The btc_valuation of this InlineResponse20074.  # noqa: E501
        :type: str
        """
        if btc_valuation is None:
            raise ValueError("Invalid value for `btc_valuation`, must not be `None`")  # noqa: E501

        self._btc_valuation = btc_valuation

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
        if issubclass(InlineResponse20074, dict):
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
        if not isinstance(other, InlineResponse20074):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
