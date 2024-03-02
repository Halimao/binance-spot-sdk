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

class InlineResponse200250(object):
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
        'index_id': 'int',
        'total_invested_in_usd': 'str',
        'current_invested_in_usd': 'str',
        'pnl_in_usd': 'str',
        'roi': 'str',
        'asset_allocation': 'list[InlineResponse200250AssetAllocation]',
        'details': 'list[InlineResponse200250Details]'
    }

    attribute_map = {
        'index_id': 'indexId',
        'total_invested_in_usd': 'totalInvestedInUSD',
        'current_invested_in_usd': 'currentInvestedInUSD',
        'pnl_in_usd': 'pnlInUSD',
        'roi': 'roi',
        'asset_allocation': 'assetAllocation',
        'details': 'details'
    }

    def __init__(self, index_id=None, total_invested_in_usd=None, current_invested_in_usd=None, pnl_in_usd=None, roi=None, asset_allocation=None, details=None):  # noqa: E501
        """InlineResponse200250 - a model defined in Swagger"""  # noqa: E501
        self._index_id = None
        self._total_invested_in_usd = None
        self._current_invested_in_usd = None
        self._pnl_in_usd = None
        self._roi = None
        self._asset_allocation = None
        self._details = None
        self.discriminator = None
        self.index_id = index_id
        self.total_invested_in_usd = total_invested_in_usd
        self.current_invested_in_usd = current_invested_in_usd
        self.pnl_in_usd = pnl_in_usd
        self.roi = roi
        self.asset_allocation = asset_allocation
        self.details = details

    @property
    def index_id(self):
        """Gets the index_id of this InlineResponse200250.  # noqa: E501


        :return: The index_id of this InlineResponse200250.  # noqa: E501
        :rtype: int
        """
        return self._index_id

    @index_id.setter
    def index_id(self, index_id):
        """Sets the index_id of this InlineResponse200250.


        :param index_id: The index_id of this InlineResponse200250.  # noqa: E501
        :type: int
        """
        if index_id is None:
            raise ValueError("Invalid value for `index_id`, must not be `None`")  # noqa: E501

        self._index_id = index_id

    @property
    def total_invested_in_usd(self):
        """Gets the total_invested_in_usd of this InlineResponse200250.  # noqa: E501


        :return: The total_invested_in_usd of this InlineResponse200250.  # noqa: E501
        :rtype: str
        """
        return self._total_invested_in_usd

    @total_invested_in_usd.setter
    def total_invested_in_usd(self, total_invested_in_usd):
        """Sets the total_invested_in_usd of this InlineResponse200250.


        :param total_invested_in_usd: The total_invested_in_usd of this InlineResponse200250.  # noqa: E501
        :type: str
        """
        if total_invested_in_usd is None:
            raise ValueError("Invalid value for `total_invested_in_usd`, must not be `None`")  # noqa: E501

        self._total_invested_in_usd = total_invested_in_usd

    @property
    def current_invested_in_usd(self):
        """Gets the current_invested_in_usd of this InlineResponse200250.  # noqa: E501

        current invest  # noqa: E501

        :return: The current_invested_in_usd of this InlineResponse200250.  # noqa: E501
        :rtype: str
        """
        return self._current_invested_in_usd

    @current_invested_in_usd.setter
    def current_invested_in_usd(self, current_invested_in_usd):
        """Sets the current_invested_in_usd of this InlineResponse200250.

        current invest  # noqa: E501

        :param current_invested_in_usd: The current_invested_in_usd of this InlineResponse200250.  # noqa: E501
        :type: str
        """
        if current_invested_in_usd is None:
            raise ValueError("Invalid value for `current_invested_in_usd`, must not be `None`")  # noqa: E501

        self._current_invested_in_usd = current_invested_in_usd

    @property
    def pnl_in_usd(self):
        """Gets the pnl_in_usd of this InlineResponse200250.  # noqa: E501

        PNL of the plan in USD based on current amount  # noqa: E501

        :return: The pnl_in_usd of this InlineResponse200250.  # noqa: E501
        :rtype: str
        """
        return self._pnl_in_usd

    @pnl_in_usd.setter
    def pnl_in_usd(self, pnl_in_usd):
        """Sets the pnl_in_usd of this InlineResponse200250.

        PNL of the plan in USD based on current amount  # noqa: E501

        :param pnl_in_usd: The pnl_in_usd of this InlineResponse200250.  # noqa: E501
        :type: str
        """
        if pnl_in_usd is None:
            raise ValueError("Invalid value for `pnl_in_usd`, must not be `None`")  # noqa: E501

        self._pnl_in_usd = pnl_in_usd

    @property
    def roi(self):
        """Gets the roi of this InlineResponse200250.  # noqa: E501

        ROI of the plan based on current amount  # noqa: E501

        :return: The roi of this InlineResponse200250.  # noqa: E501
        :rtype: str
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this InlineResponse200250.

        ROI of the plan based on current amount  # noqa: E501

        :param roi: The roi of this InlineResponse200250.  # noqa: E501
        :type: str
        """
        if roi is None:
            raise ValueError("Invalid value for `roi`, must not be `None`")  # noqa: E501

        self._roi = roi

    @property
    def asset_allocation(self):
        """Gets the asset_allocation of this InlineResponse200250.  # noqa: E501


        :return: The asset_allocation of this InlineResponse200250.  # noqa: E501
        :rtype: list[InlineResponse200250AssetAllocation]
        """
        return self._asset_allocation

    @asset_allocation.setter
    def asset_allocation(self, asset_allocation):
        """Sets the asset_allocation of this InlineResponse200250.


        :param asset_allocation: The asset_allocation of this InlineResponse200250.  # noqa: E501
        :type: list[InlineResponse200250AssetAllocation]
        """
        if asset_allocation is None:
            raise ValueError("Invalid value for `asset_allocation`, must not be `None`")  # noqa: E501

        self._asset_allocation = asset_allocation

    @property
    def details(self):
        """Gets the details of this InlineResponse200250.  # noqa: E501


        :return: The details of this InlineResponse200250.  # noqa: E501
        :rtype: list[InlineResponse200250Details]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this InlineResponse200250.


        :param details: The details of this InlineResponse200250.  # noqa: E501
        :type: list[InlineResponse200250Details]
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

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
        if issubclass(InlineResponse200250, dict):
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
        if not isinstance(other, InlineResponse200250):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
