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

class BswapAddLiquidityPreviewSingle(object):
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
        'quote_asset': 'str',
        'quote_amt': 'int',
        'price': 'float',
        'share': 'float',
        'slippage': 'float',
        'fee': 'float'
    }

    attribute_map = {
        'quote_asset': 'quoteAsset',
        'quote_amt': 'quoteAmt',
        'price': 'price',
        'share': 'share',
        'slippage': 'slippage',
        'fee': 'fee'
    }

    def __init__(self, quote_asset=None, quote_amt=None, price=None, share=None, slippage=None, fee=None):  # noqa: E501
        """BswapAddLiquidityPreviewSingle - a model defined in Swagger"""  # noqa: E501
        self._quote_asset = None
        self._quote_amt = None
        self._price = None
        self._share = None
        self._slippage = None
        self._fee = None
        self.discriminator = None
        self.quote_asset = quote_asset
        self.quote_amt = quote_amt
        self.price = price
        self.share = share
        self.slippage = slippage
        self.fee = fee

    @property
    def quote_asset(self):
        """Gets the quote_asset of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The quote_asset of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: str
        """
        return self._quote_asset

    @quote_asset.setter
    def quote_asset(self, quote_asset):
        """Sets the quote_asset of this BswapAddLiquidityPreviewSingle.


        :param quote_asset: The quote_asset of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: str
        """
        if quote_asset is None:
            raise ValueError("Invalid value for `quote_asset`, must not be `None`")  # noqa: E501

        self._quote_asset = quote_asset

    @property
    def quote_amt(self):
        """Gets the quote_amt of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The quote_amt of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: int
        """
        return self._quote_amt

    @quote_amt.setter
    def quote_amt(self, quote_amt):
        """Sets the quote_amt of this BswapAddLiquidityPreviewSingle.


        :param quote_amt: The quote_amt of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: int
        """
        if quote_amt is None:
            raise ValueError("Invalid value for `quote_amt`, must not be `None`")  # noqa: E501

        self._quote_amt = quote_amt

    @property
    def price(self):
        """Gets the price of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The price of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BswapAddLiquidityPreviewSingle.


        :param price: The price of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def share(self):
        """Gets the share of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The share of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: float
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this BswapAddLiquidityPreviewSingle.


        :param share: The share of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: float
        """
        if share is None:
            raise ValueError("Invalid value for `share`, must not be `None`")  # noqa: E501

        self._share = share

    @property
    def slippage(self):
        """Gets the slippage of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The slippage of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: float
        """
        return self._slippage

    @slippage.setter
    def slippage(self, slippage):
        """Sets the slippage of this BswapAddLiquidityPreviewSingle.


        :param slippage: The slippage of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: float
        """
        if slippage is None:
            raise ValueError("Invalid value for `slippage`, must not be `None`")  # noqa: E501

        self._slippage = slippage

    @property
    def fee(self):
        """Gets the fee of this BswapAddLiquidityPreviewSingle.  # noqa: E501


        :return: The fee of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this BswapAddLiquidityPreviewSingle.


        :param fee: The fee of this BswapAddLiquidityPreviewSingle.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

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
        if issubclass(BswapAddLiquidityPreviewSingle, dict):
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
        if not isinstance(other, BswapAddLiquidityPreviewSingle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other