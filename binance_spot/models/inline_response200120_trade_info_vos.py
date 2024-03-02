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

class InlineResponse200120TradeInfoVos(object):
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
        'user_id': 'int',
        'btc': 'float',
        'btc_futures': 'float',
        'btc_margin': 'float',
        'busd': 'float',
        'busd_futures': 'float',
        'busd_margin': 'float',
        '_date': 'int'
    }

    attribute_map = {
        'user_id': 'userId',
        'btc': 'btc',
        'btc_futures': 'btcFutures',
        'btc_margin': 'btcMargin',
        'busd': 'busd',
        'busd_futures': 'busdFutures',
        'busd_margin': 'busdMargin',
        '_date': 'date'
    }

    def __init__(self, user_id=None, btc=None, btc_futures=None, btc_margin=None, busd=None, busd_futures=None, busd_margin=None, _date=None):  # noqa: E501
        """InlineResponse200120TradeInfoVos - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._btc = None
        self._btc_futures = None
        self._btc_margin = None
        self._busd = None
        self._busd_futures = None
        self._busd_margin = None
        self.__date = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if btc is not None:
            self.btc = btc
        if btc_futures is not None:
            self.btc_futures = btc_futures
        if btc_margin is not None:
            self.btc_margin = btc_margin
        if busd is not None:
            self.busd = busd
        if busd_futures is not None:
            self.busd_futures = busd_futures
        if busd_margin is not None:
            self.busd_margin = busd_margin
        if _date is not None:
            self._date = _date

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The user_id of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponse200120TradeInfoVos.


        :param user_id: The user_id of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def btc(self):
        """Gets the btc of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The btc of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._btc

    @btc.setter
    def btc(self, btc):
        """Sets the btc of this InlineResponse200120TradeInfoVos.


        :param btc: The btc of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._btc = btc

    @property
    def btc_futures(self):
        """Gets the btc_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The btc_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._btc_futures

    @btc_futures.setter
    def btc_futures(self, btc_futures):
        """Sets the btc_futures of this InlineResponse200120TradeInfoVos.


        :param btc_futures: The btc_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._btc_futures = btc_futures

    @property
    def btc_margin(self):
        """Gets the btc_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The btc_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._btc_margin

    @btc_margin.setter
    def btc_margin(self, btc_margin):
        """Sets the btc_margin of this InlineResponse200120TradeInfoVos.


        :param btc_margin: The btc_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._btc_margin = btc_margin

    @property
    def busd(self):
        """Gets the busd of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The busd of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._busd

    @busd.setter
    def busd(self, busd):
        """Sets the busd of this InlineResponse200120TradeInfoVos.


        :param busd: The busd of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._busd = busd

    @property
    def busd_futures(self):
        """Gets the busd_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The busd_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._busd_futures

    @busd_futures.setter
    def busd_futures(self, busd_futures):
        """Sets the busd_futures of this InlineResponse200120TradeInfoVos.


        :param busd_futures: The busd_futures of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._busd_futures = busd_futures

    @property
    def busd_margin(self):
        """Gets the busd_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The busd_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: float
        """
        return self._busd_margin

    @busd_margin.setter
    def busd_margin(self, busd_margin):
        """Sets the busd_margin of this InlineResponse200120TradeInfoVos.


        :param busd_margin: The busd_margin of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: float
        """

        self._busd_margin = busd_margin

    @property
    def _date(self):
        """Gets the _date of this InlineResponse200120TradeInfoVos.  # noqa: E501


        :return: The _date of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :rtype: int
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this InlineResponse200120TradeInfoVos.


        :param _date: The _date of this InlineResponse200120TradeInfoVos.  # noqa: E501
        :type: int
        """

        self.__date = _date

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
        if issubclass(InlineResponse200120TradeInfoVos, dict):
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
        if not isinstance(other, InlineResponse200120TradeInfoVos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
