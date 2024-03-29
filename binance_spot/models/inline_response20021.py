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

class InlineResponse20021(object):
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
        'asset_full_name': 'str',
        'asset_name': 'str',
        'is_borrowable': 'bool',
        'is_mortgageable': 'bool',
        'user_min_borrow': 'str',
        'user_min_repay': 'str'
    }

    attribute_map = {
        'asset_full_name': 'assetFullName',
        'asset_name': 'assetName',
        'is_borrowable': 'isBorrowable',
        'is_mortgageable': 'isMortgageable',
        'user_min_borrow': 'userMinBorrow',
        'user_min_repay': 'userMinRepay'
    }

    def __init__(self, asset_full_name=None, asset_name=None, is_borrowable=None, is_mortgageable=None, user_min_borrow=None, user_min_repay=None):  # noqa: E501
        """InlineResponse20021 - a model defined in Swagger"""  # noqa: E501
        self._asset_full_name = None
        self._asset_name = None
        self._is_borrowable = None
        self._is_mortgageable = None
        self._user_min_borrow = None
        self._user_min_repay = None
        self.discriminator = None
        self.asset_full_name = asset_full_name
        self.asset_name = asset_name
        self.is_borrowable = is_borrowable
        self.is_mortgageable = is_mortgageable
        self.user_min_borrow = user_min_borrow
        self.user_min_repay = user_min_repay

    @property
    def asset_full_name(self):
        """Gets the asset_full_name of this InlineResponse20021.  # noqa: E501


        :return: The asset_full_name of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._asset_full_name

    @asset_full_name.setter
    def asset_full_name(self, asset_full_name):
        """Sets the asset_full_name of this InlineResponse20021.


        :param asset_full_name: The asset_full_name of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if asset_full_name is None:
            raise ValueError("Invalid value for `asset_full_name`, must not be `None`")  # noqa: E501

        self._asset_full_name = asset_full_name

    @property
    def asset_name(self):
        """Gets the asset_name of this InlineResponse20021.  # noqa: E501


        :return: The asset_name of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this InlineResponse20021.


        :param asset_name: The asset_name of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if asset_name is None:
            raise ValueError("Invalid value for `asset_name`, must not be `None`")  # noqa: E501

        self._asset_name = asset_name

    @property
    def is_borrowable(self):
        """Gets the is_borrowable of this InlineResponse20021.  # noqa: E501


        :return: The is_borrowable of this InlineResponse20021.  # noqa: E501
        :rtype: bool
        """
        return self._is_borrowable

    @is_borrowable.setter
    def is_borrowable(self, is_borrowable):
        """Sets the is_borrowable of this InlineResponse20021.


        :param is_borrowable: The is_borrowable of this InlineResponse20021.  # noqa: E501
        :type: bool
        """
        if is_borrowable is None:
            raise ValueError("Invalid value for `is_borrowable`, must not be `None`")  # noqa: E501

        self._is_borrowable = is_borrowable

    @property
    def is_mortgageable(self):
        """Gets the is_mortgageable of this InlineResponse20021.  # noqa: E501


        :return: The is_mortgageable of this InlineResponse20021.  # noqa: E501
        :rtype: bool
        """
        return self._is_mortgageable

    @is_mortgageable.setter
    def is_mortgageable(self, is_mortgageable):
        """Sets the is_mortgageable of this InlineResponse20021.


        :param is_mortgageable: The is_mortgageable of this InlineResponse20021.  # noqa: E501
        :type: bool
        """
        if is_mortgageable is None:
            raise ValueError("Invalid value for `is_mortgageable`, must not be `None`")  # noqa: E501

        self._is_mortgageable = is_mortgageable

    @property
    def user_min_borrow(self):
        """Gets the user_min_borrow of this InlineResponse20021.  # noqa: E501


        :return: The user_min_borrow of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._user_min_borrow

    @user_min_borrow.setter
    def user_min_borrow(self, user_min_borrow):
        """Sets the user_min_borrow of this InlineResponse20021.


        :param user_min_borrow: The user_min_borrow of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if user_min_borrow is None:
            raise ValueError("Invalid value for `user_min_borrow`, must not be `None`")  # noqa: E501

        self._user_min_borrow = user_min_borrow

    @property
    def user_min_repay(self):
        """Gets the user_min_repay of this InlineResponse20021.  # noqa: E501


        :return: The user_min_repay of this InlineResponse20021.  # noqa: E501
        :rtype: str
        """
        return self._user_min_repay

    @user_min_repay.setter
    def user_min_repay(self, user_min_repay):
        """Sets the user_min_repay of this InlineResponse20021.


        :param user_min_repay: The user_min_repay of this InlineResponse20021.  # noqa: E501
        :type: str
        """
        if user_min_repay is None:
            raise ValueError("Invalid value for `user_min_repay`, must not be `None`")  # noqa: E501

        self._user_min_repay = user_min_repay

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
        if issubclass(InlineResponse20021, dict):
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
        if not isinstance(other, InlineResponse20021):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
