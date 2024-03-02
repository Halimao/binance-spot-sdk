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

class InlineResponse200198Rows(object):
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
        'collateral_coin': 'str',
        '_1st_collateral_ratio': 'str',
        '_1st_collateral_range': 'str',
        '_2nd_collateral_ratio': 'str',
        '_2nd_collateral_range': 'str',
        '_3rd_collateral_ratio': 'str',
        '_3rd_collateral_range': 'str',
        '_4th_collateral_ratio': 'str',
        '_4th_collateral_range': 'str'
    }

    attribute_map = {
        'collateral_coin': 'collateralCoin',
        '_1st_collateral_ratio': '_1stCollateralRatio',
        '_1st_collateral_range': '_1stCollateralRange',
        '_2nd_collateral_ratio': '_2ndCollateralRatio',
        '_2nd_collateral_range': '_2ndCollateralRange',
        '_3rd_collateral_ratio': '_3rdCollateralRatio',
        '_3rd_collateral_range': '_3rdCollateralRange',
        '_4th_collateral_ratio': '_4thCollateralRatio',
        '_4th_collateral_range': '_4thCollateralRange'
    }

    def __init__(self, collateral_coin=None, _1st_collateral_ratio=None, _1st_collateral_range=None, _2nd_collateral_ratio=None, _2nd_collateral_range=None, _3rd_collateral_ratio=None, _3rd_collateral_range=None, _4th_collateral_ratio=None, _4th_collateral_range=None):  # noqa: E501
        """InlineResponse200198Rows - a model defined in Swagger"""  # noqa: E501
        self._collateral_coin = None
        self.__1st_collateral_ratio = None
        self.__1st_collateral_range = None
        self.__2nd_collateral_ratio = None
        self.__2nd_collateral_range = None
        self.__3rd_collateral_ratio = None
        self.__3rd_collateral_range = None
        self.__4th_collateral_ratio = None
        self.__4th_collateral_range = None
        self.discriminator = None
        self.collateral_coin = collateral_coin
        self._1st_collateral_ratio = _1st_collateral_ratio
        self._1st_collateral_range = _1st_collateral_range
        self._2nd_collateral_ratio = _2nd_collateral_ratio
        self._2nd_collateral_range = _2nd_collateral_range
        self._3rd_collateral_ratio = _3rd_collateral_ratio
        self._3rd_collateral_range = _3rd_collateral_range
        self._4th_collateral_ratio = _4th_collateral_ratio
        self._4th_collateral_range = _4th_collateral_range

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200198Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200198Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def _1st_collateral_ratio(self):
        """Gets the _1st_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501


        :return: The _1st_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__1st_collateral_ratio

    @_1st_collateral_ratio.setter
    def _1st_collateral_ratio(self, _1st_collateral_ratio):
        """Sets the _1st_collateral_ratio of this InlineResponse200198Rows.


        :param _1st_collateral_ratio: The _1st_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _1st_collateral_ratio is None:
            raise ValueError("Invalid value for `_1st_collateral_ratio`, must not be `None`")  # noqa: E501

        self.__1st_collateral_ratio = _1st_collateral_ratio

    @property
    def _1st_collateral_range(self):
        """Gets the _1st_collateral_range of this InlineResponse200198Rows.  # noqa: E501


        :return: The _1st_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__1st_collateral_range

    @_1st_collateral_range.setter
    def _1st_collateral_range(self, _1st_collateral_range):
        """Sets the _1st_collateral_range of this InlineResponse200198Rows.


        :param _1st_collateral_range: The _1st_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _1st_collateral_range is None:
            raise ValueError("Invalid value for `_1st_collateral_range`, must not be `None`")  # noqa: E501

        self.__1st_collateral_range = _1st_collateral_range

    @property
    def _2nd_collateral_ratio(self):
        """Gets the _2nd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501


        :return: The _2nd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__2nd_collateral_ratio

    @_2nd_collateral_ratio.setter
    def _2nd_collateral_ratio(self, _2nd_collateral_ratio):
        """Sets the _2nd_collateral_ratio of this InlineResponse200198Rows.


        :param _2nd_collateral_ratio: The _2nd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _2nd_collateral_ratio is None:
            raise ValueError("Invalid value for `_2nd_collateral_ratio`, must not be `None`")  # noqa: E501

        self.__2nd_collateral_ratio = _2nd_collateral_ratio

    @property
    def _2nd_collateral_range(self):
        """Gets the _2nd_collateral_range of this InlineResponse200198Rows.  # noqa: E501


        :return: The _2nd_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__2nd_collateral_range

    @_2nd_collateral_range.setter
    def _2nd_collateral_range(self, _2nd_collateral_range):
        """Sets the _2nd_collateral_range of this InlineResponse200198Rows.


        :param _2nd_collateral_range: The _2nd_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _2nd_collateral_range is None:
            raise ValueError("Invalid value for `_2nd_collateral_range`, must not be `None`")  # noqa: E501

        self.__2nd_collateral_range = _2nd_collateral_range

    @property
    def _3rd_collateral_ratio(self):
        """Gets the _3rd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501


        :return: The _3rd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__3rd_collateral_ratio

    @_3rd_collateral_ratio.setter
    def _3rd_collateral_ratio(self, _3rd_collateral_ratio):
        """Sets the _3rd_collateral_ratio of this InlineResponse200198Rows.


        :param _3rd_collateral_ratio: The _3rd_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _3rd_collateral_ratio is None:
            raise ValueError("Invalid value for `_3rd_collateral_ratio`, must not be `None`")  # noqa: E501

        self.__3rd_collateral_ratio = _3rd_collateral_ratio

    @property
    def _3rd_collateral_range(self):
        """Gets the _3rd_collateral_range of this InlineResponse200198Rows.  # noqa: E501


        :return: The _3rd_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__3rd_collateral_range

    @_3rd_collateral_range.setter
    def _3rd_collateral_range(self, _3rd_collateral_range):
        """Sets the _3rd_collateral_range of this InlineResponse200198Rows.


        :param _3rd_collateral_range: The _3rd_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _3rd_collateral_range is None:
            raise ValueError("Invalid value for `_3rd_collateral_range`, must not be `None`")  # noqa: E501

        self.__3rd_collateral_range = _3rd_collateral_range

    @property
    def _4th_collateral_ratio(self):
        """Gets the _4th_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501


        :return: The _4th_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__4th_collateral_ratio

    @_4th_collateral_ratio.setter
    def _4th_collateral_ratio(self, _4th_collateral_ratio):
        """Sets the _4th_collateral_ratio of this InlineResponse200198Rows.


        :param _4th_collateral_ratio: The _4th_collateral_ratio of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _4th_collateral_ratio is None:
            raise ValueError("Invalid value for `_4th_collateral_ratio`, must not be `None`")  # noqa: E501

        self.__4th_collateral_ratio = _4th_collateral_ratio

    @property
    def _4th_collateral_range(self):
        """Gets the _4th_collateral_range of this InlineResponse200198Rows.  # noqa: E501


        :return: The _4th_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :rtype: str
        """
        return self.__4th_collateral_range

    @_4th_collateral_range.setter
    def _4th_collateral_range(self, _4th_collateral_range):
        """Sets the _4th_collateral_range of this InlineResponse200198Rows.


        :param _4th_collateral_range: The _4th_collateral_range of this InlineResponse200198Rows.  # noqa: E501
        :type: str
        """
        if _4th_collateral_range is None:
            raise ValueError("Invalid value for `_4th_collateral_range`, must not be `None`")  # noqa: E501

        self.__4th_collateral_range = _4th_collateral_range

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
        if issubclass(InlineResponse200198Rows, dict):
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
        if not isinstance(other, InlineResponse200198Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other