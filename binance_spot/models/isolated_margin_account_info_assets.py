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

class IsolatedMarginAccountInfoAssets(object):
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
        'base_asset': 'IsolatedMarginAccountInfoBaseAsset',
        'quote_asset': 'IsolatedMarginAccountInfoQuoteAsset',
        'symbol': 'str',
        'isolated_created': 'bool',
        'enabled': 'bool',
        'margin_level': 'str',
        'margin_level_status': 'str',
        'margin_ratio': 'str',
        'index_price': 'str',
        'liquidate_price': 'str',
        'liquidate_rate': 'str',
        'trade_enabled': 'bool'
    }

    attribute_map = {
        'base_asset': 'baseAsset',
        'quote_asset': 'quoteAsset',
        'symbol': 'symbol',
        'isolated_created': 'isolatedCreated',
        'enabled': 'enabled',
        'margin_level': 'marginLevel',
        'margin_level_status': 'marginLevelStatus',
        'margin_ratio': 'marginRatio',
        'index_price': 'indexPrice',
        'liquidate_price': 'liquidatePrice',
        'liquidate_rate': 'liquidateRate',
        'trade_enabled': 'tradeEnabled'
    }

    def __init__(self, base_asset=None, quote_asset=None, symbol=None, isolated_created=None, enabled=None, margin_level=None, margin_level_status=None, margin_ratio=None, index_price=None, liquidate_price=None, liquidate_rate=None, trade_enabled=None):  # noqa: E501
        """IsolatedMarginAccountInfoAssets - a model defined in Swagger"""  # noqa: E501
        self._base_asset = None
        self._quote_asset = None
        self._symbol = None
        self._isolated_created = None
        self._enabled = None
        self._margin_level = None
        self._margin_level_status = None
        self._margin_ratio = None
        self._index_price = None
        self._liquidate_price = None
        self._liquidate_rate = None
        self._trade_enabled = None
        self.discriminator = None
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.symbol = symbol
        self.isolated_created = isolated_created
        self.enabled = enabled
        self.margin_level = margin_level
        self.margin_level_status = margin_level_status
        self.margin_ratio = margin_ratio
        self.index_price = index_price
        self.liquidate_price = liquidate_price
        self.liquidate_rate = liquidate_rate
        self.trade_enabled = trade_enabled

    @property
    def base_asset(self):
        """Gets the base_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The base_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: IsolatedMarginAccountInfoBaseAsset
        """
        return self._base_asset

    @base_asset.setter
    def base_asset(self, base_asset):
        """Sets the base_asset of this IsolatedMarginAccountInfoAssets.


        :param base_asset: The base_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: IsolatedMarginAccountInfoBaseAsset
        """
        if base_asset is None:
            raise ValueError("Invalid value for `base_asset`, must not be `None`")  # noqa: E501

        self._base_asset = base_asset

    @property
    def quote_asset(self):
        """Gets the quote_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The quote_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: IsolatedMarginAccountInfoQuoteAsset
        """
        return self._quote_asset

    @quote_asset.setter
    def quote_asset(self, quote_asset):
        """Sets the quote_asset of this IsolatedMarginAccountInfoAssets.


        :param quote_asset: The quote_asset of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: IsolatedMarginAccountInfoQuoteAsset
        """
        if quote_asset is None:
            raise ValueError("Invalid value for `quote_asset`, must not be `None`")  # noqa: E501

        self._quote_asset = quote_asset

    @property
    def symbol(self):
        """Gets the symbol of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The symbol of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this IsolatedMarginAccountInfoAssets.


        :param symbol: The symbol of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def isolated_created(self):
        """Gets the isolated_created of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The isolated_created of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: bool
        """
        return self._isolated_created

    @isolated_created.setter
    def isolated_created(self, isolated_created):
        """Sets the isolated_created of this IsolatedMarginAccountInfoAssets.


        :param isolated_created: The isolated_created of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: bool
        """
        if isolated_created is None:
            raise ValueError("Invalid value for `isolated_created`, must not be `None`")  # noqa: E501

        self._isolated_created = isolated_created

    @property
    def enabled(self):
        """Gets the enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501

        true-enabled, false-disabled  # noqa: E501

        :return: The enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IsolatedMarginAccountInfoAssets.

        true-enabled, false-disabled  # noqa: E501

        :param enabled: The enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def margin_level(self):
        """Gets the margin_level of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The margin_level of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._margin_level

    @margin_level.setter
    def margin_level(self, margin_level):
        """Sets the margin_level of this IsolatedMarginAccountInfoAssets.


        :param margin_level: The margin_level of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if margin_level is None:
            raise ValueError("Invalid value for `margin_level`, must not be `None`")  # noqa: E501

        self._margin_level = margin_level

    @property
    def margin_level_status(self):
        """Gets the margin_level_status of this IsolatedMarginAccountInfoAssets.  # noqa: E501

        \"EXCESSIVE\", \"NORMAL\", \"MARGIN_CALL\", \"PRE_LIQUIDATION\", \"FORCE_LIQUIDATION\"  # noqa: E501

        :return: The margin_level_status of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._margin_level_status

    @margin_level_status.setter
    def margin_level_status(self, margin_level_status):
        """Sets the margin_level_status of this IsolatedMarginAccountInfoAssets.

        \"EXCESSIVE\", \"NORMAL\", \"MARGIN_CALL\", \"PRE_LIQUIDATION\", \"FORCE_LIQUIDATION\"  # noqa: E501

        :param margin_level_status: The margin_level_status of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if margin_level_status is None:
            raise ValueError("Invalid value for `margin_level_status`, must not be `None`")  # noqa: E501

        self._margin_level_status = margin_level_status

    @property
    def margin_ratio(self):
        """Gets the margin_ratio of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The margin_ratio of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._margin_ratio

    @margin_ratio.setter
    def margin_ratio(self, margin_ratio):
        """Sets the margin_ratio of this IsolatedMarginAccountInfoAssets.


        :param margin_ratio: The margin_ratio of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if margin_ratio is None:
            raise ValueError("Invalid value for `margin_ratio`, must not be `None`")  # noqa: E501

        self._margin_ratio = margin_ratio

    @property
    def index_price(self):
        """Gets the index_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The index_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this IsolatedMarginAccountInfoAssets.


        :param index_price: The index_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if index_price is None:
            raise ValueError("Invalid value for `index_price`, must not be `None`")  # noqa: E501

        self._index_price = index_price

    @property
    def liquidate_price(self):
        """Gets the liquidate_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The liquidate_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._liquidate_price

    @liquidate_price.setter
    def liquidate_price(self, liquidate_price):
        """Sets the liquidate_price of this IsolatedMarginAccountInfoAssets.


        :param liquidate_price: The liquidate_price of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if liquidate_price is None:
            raise ValueError("Invalid value for `liquidate_price`, must not be `None`")  # noqa: E501

        self._liquidate_price = liquidate_price

    @property
    def liquidate_rate(self):
        """Gets the liquidate_rate of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The liquidate_rate of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: str
        """
        return self._liquidate_rate

    @liquidate_rate.setter
    def liquidate_rate(self, liquidate_rate):
        """Sets the liquidate_rate of this IsolatedMarginAccountInfoAssets.


        :param liquidate_rate: The liquidate_rate of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: str
        """
        if liquidate_rate is None:
            raise ValueError("Invalid value for `liquidate_rate`, must not be `None`")  # noqa: E501

        self._liquidate_rate = liquidate_rate

    @property
    def trade_enabled(self):
        """Gets the trade_enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501


        :return: The trade_enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :rtype: bool
        """
        return self._trade_enabled

    @trade_enabled.setter
    def trade_enabled(self, trade_enabled):
        """Sets the trade_enabled of this IsolatedMarginAccountInfoAssets.


        :param trade_enabled: The trade_enabled of this IsolatedMarginAccountInfoAssets.  # noqa: E501
        :type: bool
        """
        if trade_enabled is None:
            raise ValueError("Invalid value for `trade_enabled`, must not be `None`")  # noqa: E501

        self._trade_enabled = trade_enabled

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
        if issubclass(IsolatedMarginAccountInfoAssets, dict):
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
        if not isinstance(other, IsolatedMarginAccountInfoAssets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
