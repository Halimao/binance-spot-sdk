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

class InlineResponse200250Details(object):
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
        'target_asset': 'str',
        'average_price_in_usd': 'str',
        'total_invested_in_usd': 'str',
        'current_invested_in_usd': 'str',
        'purchased_amount': 'str',
        'pnl_in_usd': 'str',
        'roi': 'str',
        'percentage': 'str',
        'available_amount': 'str',
        'redeemed_amount': 'str',
        'asset_value_in_usd': 'str'
    }

    attribute_map = {
        'target_asset': 'targetAsset',
        'average_price_in_usd': 'averagePriceInUSD',
        'total_invested_in_usd': 'totalInvestedInUSD',
        'current_invested_in_usd': 'currentInvestedInUSD',
        'purchased_amount': 'purchasedAmount',
        'pnl_in_usd': 'pnlInUSD',
        'roi': 'roi',
        'percentage': 'percentage',
        'available_amount': 'availableAmount',
        'redeemed_amount': 'redeemedAmount',
        'asset_value_in_usd': 'assetValueInUSD'
    }

    def __init__(self, target_asset=None, average_price_in_usd=None, total_invested_in_usd=None, current_invested_in_usd=None, purchased_amount=None, pnl_in_usd=None, roi=None, percentage=None, available_amount=None, redeemed_amount=None, asset_value_in_usd=None):  # noqa: E501
        """InlineResponse200250Details - a model defined in Swagger"""  # noqa: E501
        self._target_asset = None
        self._average_price_in_usd = None
        self._total_invested_in_usd = None
        self._current_invested_in_usd = None
        self._purchased_amount = None
        self._pnl_in_usd = None
        self._roi = None
        self._percentage = None
        self._available_amount = None
        self._redeemed_amount = None
        self._asset_value_in_usd = None
        self.discriminator = None
        self.target_asset = target_asset
        self.average_price_in_usd = average_price_in_usd
        self.total_invested_in_usd = total_invested_in_usd
        self.current_invested_in_usd = current_invested_in_usd
        self.purchased_amount = purchased_amount
        self.pnl_in_usd = pnl_in_usd
        self.roi = roi
        self.percentage = percentage
        self.available_amount = available_amount
        self.redeemed_amount = redeemed_amount
        self.asset_value_in_usd = asset_value_in_usd

    @property
    def target_asset(self):
        """Gets the target_asset of this InlineResponse200250Details.  # noqa: E501


        :return: The target_asset of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._target_asset

    @target_asset.setter
    def target_asset(self, target_asset):
        """Sets the target_asset of this InlineResponse200250Details.


        :param target_asset: The target_asset of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if target_asset is None:
            raise ValueError("Invalid value for `target_asset`, must not be `None`")  # noqa: E501

        self._target_asset = target_asset

    @property
    def average_price_in_usd(self):
        """Gets the average_price_in_usd of this InlineResponse200250Details.  # noqa: E501

        average price of the asset in USD  # noqa: E501

        :return: The average_price_in_usd of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._average_price_in_usd

    @average_price_in_usd.setter
    def average_price_in_usd(self, average_price_in_usd):
        """Sets the average_price_in_usd of this InlineResponse200250Details.

        average price of the asset in USD  # noqa: E501

        :param average_price_in_usd: The average_price_in_usd of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if average_price_in_usd is None:
            raise ValueError("Invalid value for `average_price_in_usd`, must not be `None`")  # noqa: E501

        self._average_price_in_usd = average_price_in_usd

    @property
    def total_invested_in_usd(self):
        """Gets the total_invested_in_usd of this InlineResponse200250Details.  # noqa: E501

        total source asset invested for this target asset in equivilent of USD  # noqa: E501

        :return: The total_invested_in_usd of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._total_invested_in_usd

    @total_invested_in_usd.setter
    def total_invested_in_usd(self, total_invested_in_usd):
        """Sets the total_invested_in_usd of this InlineResponse200250Details.

        total source asset invested for this target asset in equivilent of USD  # noqa: E501

        :param total_invested_in_usd: The total_invested_in_usd of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if total_invested_in_usd is None:
            raise ValueError("Invalid value for `total_invested_in_usd`, must not be `None`")  # noqa: E501

        self._total_invested_in_usd = total_invested_in_usd

    @property
    def current_invested_in_usd(self):
        """Gets the current_invested_in_usd of this InlineResponse200250Details.  # noqa: E501

        current invest  # noqa: E501

        :return: The current_invested_in_usd of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._current_invested_in_usd

    @current_invested_in_usd.setter
    def current_invested_in_usd(self, current_invested_in_usd):
        """Sets the current_invested_in_usd of this InlineResponse200250Details.

        current invest  # noqa: E501

        :param current_invested_in_usd: The current_invested_in_usd of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if current_invested_in_usd is None:
            raise ValueError("Invalid value for `current_invested_in_usd`, must not be `None`")  # noqa: E501

        self._current_invested_in_usd = current_invested_in_usd

    @property
    def purchased_amount(self):
        """Gets the purchased_amount of this InlineResponse200250Details.  # noqa: E501

        purchased amount of target asset  # noqa: E501

        :return: The purchased_amount of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._purchased_amount

    @purchased_amount.setter
    def purchased_amount(self, purchased_amount):
        """Sets the purchased_amount of this InlineResponse200250Details.

        purchased amount of target asset  # noqa: E501

        :param purchased_amount: The purchased_amount of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if purchased_amount is None:
            raise ValueError("Invalid value for `purchased_amount`, must not be `None`")  # noqa: E501

        self._purchased_amount = purchased_amount

    @property
    def pnl_in_usd(self):
        """Gets the pnl_in_usd of this InlineResponse200250Details.  # noqa: E501

        PNL denominated in USD  # noqa: E501

        :return: The pnl_in_usd of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._pnl_in_usd

    @pnl_in_usd.setter
    def pnl_in_usd(self, pnl_in_usd):
        """Sets the pnl_in_usd of this InlineResponse200250Details.

        PNL denominated in USD  # noqa: E501

        :param pnl_in_usd: The pnl_in_usd of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if pnl_in_usd is None:
            raise ValueError("Invalid value for `pnl_in_usd`, must not be `None`")  # noqa: E501

        self._pnl_in_usd = pnl_in_usd

    @property
    def roi(self):
        """Gets the roi of this InlineResponse200250Details.  # noqa: E501

        ROI calculated in decimal  # noqa: E501

        :return: The roi of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._roi

    @roi.setter
    def roi(self, roi):
        """Sets the roi of this InlineResponse200250Details.

        ROI calculated in decimal  # noqa: E501

        :param roi: The roi of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if roi is None:
            raise ValueError("Invalid value for `roi`, must not be `None`")  # noqa: E501

        self._roi = roi

    @property
    def percentage(self):
        """Gets the percentage of this InlineResponse200250Details.  # noqa: E501

        asset allocation in the plan. If it's single plan, then it's 100  # noqa: E501

        :return: The percentage of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this InlineResponse200250Details.

        asset allocation in the plan. If it's single plan, then it's 100  # noqa: E501

        :param percentage: The percentage of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if percentage is None:
            raise ValueError("Invalid value for `percentage`, must not be `None`")  # noqa: E501

        self._percentage = percentage

    @property
    def available_amount(self):
        """Gets the available_amount of this InlineResponse200250Details.  # noqa: E501


        :return: The available_amount of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """Sets the available_amount of this InlineResponse200250Details.


        :param available_amount: The available_amount of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if available_amount is None:
            raise ValueError("Invalid value for `available_amount`, must not be `None`")  # noqa: E501

        self._available_amount = available_amount

    @property
    def redeemed_amount(self):
        """Gets the redeemed_amount of this InlineResponse200250Details.  # noqa: E501


        :return: The redeemed_amount of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._redeemed_amount

    @redeemed_amount.setter
    def redeemed_amount(self, redeemed_amount):
        """Sets the redeemed_amount of this InlineResponse200250Details.


        :param redeemed_amount: The redeemed_amount of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if redeemed_amount is None:
            raise ValueError("Invalid value for `redeemed_amount`, must not be `None`")  # noqa: E501

        self._redeemed_amount = redeemed_amount

    @property
    def asset_value_in_usd(self):
        """Gets the asset_value_in_usd of this InlineResponse200250Details.  # noqa: E501


        :return: The asset_value_in_usd of this InlineResponse200250Details.  # noqa: E501
        :rtype: str
        """
        return self._asset_value_in_usd

    @asset_value_in_usd.setter
    def asset_value_in_usd(self, asset_value_in_usd):
        """Sets the asset_value_in_usd of this InlineResponse200250Details.


        :param asset_value_in_usd: The asset_value_in_usd of this InlineResponse200250Details.  # noqa: E501
        :type: str
        """
        if asset_value_in_usd is None:
            raise ValueError("Invalid value for `asset_value_in_usd`, must not be `None`")  # noqa: E501

        self._asset_value_in_usd = asset_value_in_usd

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
        if issubclass(InlineResponse200250Details, dict):
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
        if not isinstance(other, InlineResponse200250Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other