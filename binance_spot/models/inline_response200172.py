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

class InlineResponse200172(object):
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
        'token_name': 'str',
        'description': 'str',
        'underlying': 'str',
        'token_issued': 'str',
        'basket': 'str',
        'current_baskets': 'list[Sapiv1blvttokenInfoCurrentBaskets]',
        'nav': 'str',
        'real_leverage': 'str',
        'funding_rate': 'str',
        'daily_management_fee': 'str',
        'purchase_fee_pct': 'str',
        'daily_purchase_limit': 'str',
        'redeem_fee_pct': 'str',
        'daily_redeem_limit': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'token_name': 'tokenName',
        'description': 'description',
        'underlying': 'underlying',
        'token_issued': 'tokenIssued',
        'basket': 'basket',
        'current_baskets': 'currentBaskets',
        'nav': 'nav',
        'real_leverage': 'realLeverage',
        'funding_rate': 'fundingRate',
        'daily_management_fee': 'dailyManagementFee',
        'purchase_fee_pct': 'purchaseFeePct',
        'daily_purchase_limit': 'dailyPurchaseLimit',
        'redeem_fee_pct': 'redeemFeePct',
        'daily_redeem_limit': 'dailyRedeemLimit',
        'timestamp': 'timestamp'
    }

    def __init__(self, token_name=None, description=None, underlying=None, token_issued=None, basket=None, current_baskets=None, nav=None, real_leverage=None, funding_rate=None, daily_management_fee=None, purchase_fee_pct=None, daily_purchase_limit=None, redeem_fee_pct=None, daily_redeem_limit=None, timestamp=None):  # noqa: E501
        """InlineResponse200172 - a model defined in Swagger"""  # noqa: E501
        self._token_name = None
        self._description = None
        self._underlying = None
        self._token_issued = None
        self._basket = None
        self._current_baskets = None
        self._nav = None
        self._real_leverage = None
        self._funding_rate = None
        self._daily_management_fee = None
        self._purchase_fee_pct = None
        self._daily_purchase_limit = None
        self._redeem_fee_pct = None
        self._daily_redeem_limit = None
        self._timestamp = None
        self.discriminator = None
        self.token_name = token_name
        self.description = description
        self.underlying = underlying
        self.token_issued = token_issued
        self.basket = basket
        self.current_baskets = current_baskets
        self.nav = nav
        self.real_leverage = real_leverage
        self.funding_rate = funding_rate
        self.daily_management_fee = daily_management_fee
        self.purchase_fee_pct = purchase_fee_pct
        self.daily_purchase_limit = daily_purchase_limit
        self.redeem_fee_pct = redeem_fee_pct
        self.daily_redeem_limit = daily_redeem_limit
        self.timestamp = timestamp

    @property
    def token_name(self):
        """Gets the token_name of this InlineResponse200172.  # noqa: E501


        :return: The token_name of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this InlineResponse200172.


        :param token_name: The token_name of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if token_name is None:
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def description(self):
        """Gets the description of this InlineResponse200172.  # noqa: E501


        :return: The description of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse200172.


        :param description: The description of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def underlying(self):
        """Gets the underlying of this InlineResponse200172.  # noqa: E501


        :return: The underlying of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._underlying

    @underlying.setter
    def underlying(self, underlying):
        """Sets the underlying of this InlineResponse200172.


        :param underlying: The underlying of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if underlying is None:
            raise ValueError("Invalid value for `underlying`, must not be `None`")  # noqa: E501

        self._underlying = underlying

    @property
    def token_issued(self):
        """Gets the token_issued of this InlineResponse200172.  # noqa: E501


        :return: The token_issued of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._token_issued

    @token_issued.setter
    def token_issued(self, token_issued):
        """Sets the token_issued of this InlineResponse200172.


        :param token_issued: The token_issued of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if token_issued is None:
            raise ValueError("Invalid value for `token_issued`, must not be `None`")  # noqa: E501

        self._token_issued = token_issued

    @property
    def basket(self):
        """Gets the basket of this InlineResponse200172.  # noqa: E501


        :return: The basket of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._basket

    @basket.setter
    def basket(self, basket):
        """Sets the basket of this InlineResponse200172.


        :param basket: The basket of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if basket is None:
            raise ValueError("Invalid value for `basket`, must not be `None`")  # noqa: E501

        self._basket = basket

    @property
    def current_baskets(self):
        """Gets the current_baskets of this InlineResponse200172.  # noqa: E501


        :return: The current_baskets of this InlineResponse200172.  # noqa: E501
        :rtype: list[Sapiv1blvttokenInfoCurrentBaskets]
        """
        return self._current_baskets

    @current_baskets.setter
    def current_baskets(self, current_baskets):
        """Sets the current_baskets of this InlineResponse200172.


        :param current_baskets: The current_baskets of this InlineResponse200172.  # noqa: E501
        :type: list[Sapiv1blvttokenInfoCurrentBaskets]
        """
        if current_baskets is None:
            raise ValueError("Invalid value for `current_baskets`, must not be `None`")  # noqa: E501

        self._current_baskets = current_baskets

    @property
    def nav(self):
        """Gets the nav of this InlineResponse200172.  # noqa: E501


        :return: The nav of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._nav

    @nav.setter
    def nav(self, nav):
        """Sets the nav of this InlineResponse200172.


        :param nav: The nav of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if nav is None:
            raise ValueError("Invalid value for `nav`, must not be `None`")  # noqa: E501

        self._nav = nav

    @property
    def real_leverage(self):
        """Gets the real_leverage of this InlineResponse200172.  # noqa: E501


        :return: The real_leverage of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._real_leverage

    @real_leverage.setter
    def real_leverage(self, real_leverage):
        """Sets the real_leverage of this InlineResponse200172.


        :param real_leverage: The real_leverage of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if real_leverage is None:
            raise ValueError("Invalid value for `real_leverage`, must not be `None`")  # noqa: E501

        self._real_leverage = real_leverage

    @property
    def funding_rate(self):
        """Gets the funding_rate of this InlineResponse200172.  # noqa: E501


        :return: The funding_rate of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._funding_rate

    @funding_rate.setter
    def funding_rate(self, funding_rate):
        """Sets the funding_rate of this InlineResponse200172.


        :param funding_rate: The funding_rate of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if funding_rate is None:
            raise ValueError("Invalid value for `funding_rate`, must not be `None`")  # noqa: E501

        self._funding_rate = funding_rate

    @property
    def daily_management_fee(self):
        """Gets the daily_management_fee of this InlineResponse200172.  # noqa: E501


        :return: The daily_management_fee of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._daily_management_fee

    @daily_management_fee.setter
    def daily_management_fee(self, daily_management_fee):
        """Sets the daily_management_fee of this InlineResponse200172.


        :param daily_management_fee: The daily_management_fee of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if daily_management_fee is None:
            raise ValueError("Invalid value for `daily_management_fee`, must not be `None`")  # noqa: E501

        self._daily_management_fee = daily_management_fee

    @property
    def purchase_fee_pct(self):
        """Gets the purchase_fee_pct of this InlineResponse200172.  # noqa: E501


        :return: The purchase_fee_pct of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._purchase_fee_pct

    @purchase_fee_pct.setter
    def purchase_fee_pct(self, purchase_fee_pct):
        """Sets the purchase_fee_pct of this InlineResponse200172.


        :param purchase_fee_pct: The purchase_fee_pct of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if purchase_fee_pct is None:
            raise ValueError("Invalid value for `purchase_fee_pct`, must not be `None`")  # noqa: E501

        self._purchase_fee_pct = purchase_fee_pct

    @property
    def daily_purchase_limit(self):
        """Gets the daily_purchase_limit of this InlineResponse200172.  # noqa: E501


        :return: The daily_purchase_limit of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._daily_purchase_limit

    @daily_purchase_limit.setter
    def daily_purchase_limit(self, daily_purchase_limit):
        """Sets the daily_purchase_limit of this InlineResponse200172.


        :param daily_purchase_limit: The daily_purchase_limit of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if daily_purchase_limit is None:
            raise ValueError("Invalid value for `daily_purchase_limit`, must not be `None`")  # noqa: E501

        self._daily_purchase_limit = daily_purchase_limit

    @property
    def redeem_fee_pct(self):
        """Gets the redeem_fee_pct of this InlineResponse200172.  # noqa: E501


        :return: The redeem_fee_pct of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._redeem_fee_pct

    @redeem_fee_pct.setter
    def redeem_fee_pct(self, redeem_fee_pct):
        """Sets the redeem_fee_pct of this InlineResponse200172.


        :param redeem_fee_pct: The redeem_fee_pct of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if redeem_fee_pct is None:
            raise ValueError("Invalid value for `redeem_fee_pct`, must not be `None`")  # noqa: E501

        self._redeem_fee_pct = redeem_fee_pct

    @property
    def daily_redeem_limit(self):
        """Gets the daily_redeem_limit of this InlineResponse200172.  # noqa: E501


        :return: The daily_redeem_limit of this InlineResponse200172.  # noqa: E501
        :rtype: str
        """
        return self._daily_redeem_limit

    @daily_redeem_limit.setter
    def daily_redeem_limit(self, daily_redeem_limit):
        """Sets the daily_redeem_limit of this InlineResponse200172.


        :param daily_redeem_limit: The daily_redeem_limit of this InlineResponse200172.  # noqa: E501
        :type: str
        """
        if daily_redeem_limit is None:
            raise ValueError("Invalid value for `daily_redeem_limit`, must not be `None`")  # noqa: E501

        self._daily_redeem_limit = daily_redeem_limit

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse200172.  # noqa: E501


        :return: The timestamp of this InlineResponse200172.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse200172.


        :param timestamp: The timestamp of this InlineResponse200172.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(InlineResponse200172, dict):
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
        if not isinstance(other, InlineResponse200172):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other