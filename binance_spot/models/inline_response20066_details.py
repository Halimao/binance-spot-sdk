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

class InlineResponse20066Details(object):
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
        'asset_full_name': 'str',
        'amount_free': 'str',
        'to_btc': 'str',
        'to_bnb': 'str',
        'to_bnb_off_exchange': 'str',
        'exchange': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'asset_full_name': 'assetFullName',
        'amount_free': 'amountFree',
        'to_btc': 'toBTC',
        'to_bnb': 'toBNB',
        'to_bnb_off_exchange': 'toBNBOffExchange',
        'exchange': 'exchange'
    }

    def __init__(self, asset=None, asset_full_name=None, amount_free=None, to_btc=None, to_bnb=None, to_bnb_off_exchange=None, exchange=None):  # noqa: E501
        """InlineResponse20066Details - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._asset_full_name = None
        self._amount_free = None
        self._to_btc = None
        self._to_bnb = None
        self._to_bnb_off_exchange = None
        self._exchange = None
        self.discriminator = None
        self.asset = asset
        self.asset_full_name = asset_full_name
        self.amount_free = amount_free
        self.to_btc = to_btc
        self.to_bnb = to_bnb
        self.to_bnb_off_exchange = to_bnb_off_exchange
        self.exchange = exchange

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20066Details.  # noqa: E501


        :return: The asset of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20066Details.


        :param asset: The asset of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def asset_full_name(self):
        """Gets the asset_full_name of this InlineResponse20066Details.  # noqa: E501


        :return: The asset_full_name of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._asset_full_name

    @asset_full_name.setter
    def asset_full_name(self, asset_full_name):
        """Sets the asset_full_name of this InlineResponse20066Details.


        :param asset_full_name: The asset_full_name of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if asset_full_name is None:
            raise ValueError("Invalid value for `asset_full_name`, must not be `None`")  # noqa: E501

        self._asset_full_name = asset_full_name

    @property
    def amount_free(self):
        """Gets the amount_free of this InlineResponse20066Details.  # noqa: E501

        Convertible amount  # noqa: E501

        :return: The amount_free of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._amount_free

    @amount_free.setter
    def amount_free(self, amount_free):
        """Sets the amount_free of this InlineResponse20066Details.

        Convertible amount  # noqa: E501

        :param amount_free: The amount_free of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if amount_free is None:
            raise ValueError("Invalid value for `amount_free`, must not be `None`")  # noqa: E501

        self._amount_free = amount_free

    @property
    def to_btc(self):
        """Gets the to_btc of this InlineResponse20066Details.  # noqa: E501

        BTC amount  # noqa: E501

        :return: The to_btc of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._to_btc

    @to_btc.setter
    def to_btc(self, to_btc):
        """Sets the to_btc of this InlineResponse20066Details.

        BTC amount  # noqa: E501

        :param to_btc: The to_btc of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if to_btc is None:
            raise ValueError("Invalid value for `to_btc`, must not be `None`")  # noqa: E501

        self._to_btc = to_btc

    @property
    def to_bnb(self):
        """Gets the to_bnb of this InlineResponse20066Details.  # noqa: E501

        BNB amount(Not deducted commission fee  # noqa: E501

        :return: The to_bnb of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._to_bnb

    @to_bnb.setter
    def to_bnb(self, to_bnb):
        """Sets the to_bnb of this InlineResponse20066Details.

        BNB amount(Not deducted commission fee  # noqa: E501

        :param to_bnb: The to_bnb of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if to_bnb is None:
            raise ValueError("Invalid value for `to_bnb`, must not be `None`")  # noqa: E501

        self._to_bnb = to_bnb

    @property
    def to_bnb_off_exchange(self):
        """Gets the to_bnb_off_exchange of this InlineResponse20066Details.  # noqa: E501

        BNB amount(Deducted commission fee  # noqa: E501

        :return: The to_bnb_off_exchange of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._to_bnb_off_exchange

    @to_bnb_off_exchange.setter
    def to_bnb_off_exchange(self, to_bnb_off_exchange):
        """Sets the to_bnb_off_exchange of this InlineResponse20066Details.

        BNB amount(Deducted commission fee  # noqa: E501

        :param to_bnb_off_exchange: The to_bnb_off_exchange of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if to_bnb_off_exchange is None:
            raise ValueError("Invalid value for `to_bnb_off_exchange`, must not be `None`")  # noqa: E501

        self._to_bnb_off_exchange = to_bnb_off_exchange

    @property
    def exchange(self):
        """Gets the exchange of this InlineResponse20066Details.  # noqa: E501

        Commission fee  # noqa: E501

        :return: The exchange of this InlineResponse20066Details.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this InlineResponse20066Details.

        Commission fee  # noqa: E501

        :param exchange: The exchange of this InlineResponse20066Details.  # noqa: E501
        :type: str
        """
        if exchange is None:
            raise ValueError("Invalid value for `exchange`, must not be `None`")  # noqa: E501

        self._exchange = exchange

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
        if issubclass(InlineResponse20066Details, dict):
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
        if not isinstance(other, InlineResponse20066Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
