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

class InlineResponse20042(object):
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
        'symbol': 'str',
        'tier': 'int',
        'effective_multiple': 'str',
        'initial_risk_ratio': 'str',
        'liquidation_risk_ratio': 'str',
        'base_asset_max_borrowable': 'str',
        'quote_asset_max_borrowable': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'tier': 'tier',
        'effective_multiple': 'effectiveMultiple',
        'initial_risk_ratio': 'initialRiskRatio',
        'liquidation_risk_ratio': 'liquidationRiskRatio',
        'base_asset_max_borrowable': 'baseAssetMaxBorrowable',
        'quote_asset_max_borrowable': 'quoteAssetMaxBorrowable'
    }

    def __init__(self, symbol=None, tier=None, effective_multiple=None, initial_risk_ratio=None, liquidation_risk_ratio=None, base_asset_max_borrowable=None, quote_asset_max_borrowable=None):  # noqa: E501
        """InlineResponse20042 - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._tier = None
        self._effective_multiple = None
        self._initial_risk_ratio = None
        self._liquidation_risk_ratio = None
        self._base_asset_max_borrowable = None
        self._quote_asset_max_borrowable = None
        self.discriminator = None
        if symbol is not None:
            self.symbol = symbol
        if tier is not None:
            self.tier = tier
        if effective_multiple is not None:
            self.effective_multiple = effective_multiple
        if initial_risk_ratio is not None:
            self.initial_risk_ratio = initial_risk_ratio
        if liquidation_risk_ratio is not None:
            self.liquidation_risk_ratio = liquidation_risk_ratio
        if base_asset_max_borrowable is not None:
            self.base_asset_max_borrowable = base_asset_max_borrowable
        if quote_asset_max_borrowable is not None:
            self.quote_asset_max_borrowable = quote_asset_max_borrowable

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse20042.  # noqa: E501


        :return: The symbol of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse20042.


        :param symbol: The symbol of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def tier(self):
        """Gets the tier of this InlineResponse20042.  # noqa: E501


        :return: The tier of this InlineResponse20042.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this InlineResponse20042.


        :param tier: The tier of this InlineResponse20042.  # noqa: E501
        :type: int
        """

        self._tier = tier

    @property
    def effective_multiple(self):
        """Gets the effective_multiple of this InlineResponse20042.  # noqa: E501


        :return: The effective_multiple of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._effective_multiple

    @effective_multiple.setter
    def effective_multiple(self, effective_multiple):
        """Sets the effective_multiple of this InlineResponse20042.


        :param effective_multiple: The effective_multiple of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._effective_multiple = effective_multiple

    @property
    def initial_risk_ratio(self):
        """Gets the initial_risk_ratio of this InlineResponse20042.  # noqa: E501


        :return: The initial_risk_ratio of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._initial_risk_ratio

    @initial_risk_ratio.setter
    def initial_risk_ratio(self, initial_risk_ratio):
        """Sets the initial_risk_ratio of this InlineResponse20042.


        :param initial_risk_ratio: The initial_risk_ratio of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._initial_risk_ratio = initial_risk_ratio

    @property
    def liquidation_risk_ratio(self):
        """Gets the liquidation_risk_ratio of this InlineResponse20042.  # noqa: E501


        :return: The liquidation_risk_ratio of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._liquidation_risk_ratio

    @liquidation_risk_ratio.setter
    def liquidation_risk_ratio(self, liquidation_risk_ratio):
        """Sets the liquidation_risk_ratio of this InlineResponse20042.


        :param liquidation_risk_ratio: The liquidation_risk_ratio of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._liquidation_risk_ratio = liquidation_risk_ratio

    @property
    def base_asset_max_borrowable(self):
        """Gets the base_asset_max_borrowable of this InlineResponse20042.  # noqa: E501


        :return: The base_asset_max_borrowable of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._base_asset_max_borrowable

    @base_asset_max_borrowable.setter
    def base_asset_max_borrowable(self, base_asset_max_borrowable):
        """Sets the base_asset_max_borrowable of this InlineResponse20042.


        :param base_asset_max_borrowable: The base_asset_max_borrowable of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._base_asset_max_borrowable = base_asset_max_borrowable

    @property
    def quote_asset_max_borrowable(self):
        """Gets the quote_asset_max_borrowable of this InlineResponse20042.  # noqa: E501


        :return: The quote_asset_max_borrowable of this InlineResponse20042.  # noqa: E501
        :rtype: str
        """
        return self._quote_asset_max_borrowable

    @quote_asset_max_borrowable.setter
    def quote_asset_max_borrowable(self, quote_asset_max_borrowable):
        """Sets the quote_asset_max_borrowable of this InlineResponse20042.


        :param quote_asset_max_borrowable: The quote_asset_max_borrowable of this InlineResponse20042.  # noqa: E501
        :type: str
        """

        self._quote_asset_max_borrowable = quote_asset_max_borrowable

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
        if issubclass(InlineResponse20042, dict):
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
        if not isinstance(other, InlineResponse20042):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
