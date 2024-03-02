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

class InlineResponse200127Data(object):
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
        'order_no': 'str',
        'source_amount': 'str',
        'fiat_currency': 'str',
        'obtain_amount': 'str',
        'crypto_currency': 'str',
        'total_fee': 'str',
        'price': 'str',
        'status': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'order_no': 'orderNo',
        'source_amount': 'sourceAmount',
        'fiat_currency': 'fiatCurrency',
        'obtain_amount': 'obtainAmount',
        'crypto_currency': 'cryptoCurrency',
        'total_fee': 'totalFee',
        'price': 'price',
        'status': 'status',
        'create_time': 'createTime',
        'update_time': 'updateTime'
    }

    def __init__(self, order_no=None, source_amount=None, fiat_currency=None, obtain_amount=None, crypto_currency=None, total_fee=None, price=None, status=None, create_time=None, update_time=None):  # noqa: E501
        """InlineResponse200127Data - a model defined in Swagger"""  # noqa: E501
        self._order_no = None
        self._source_amount = None
        self._fiat_currency = None
        self._obtain_amount = None
        self._crypto_currency = None
        self._total_fee = None
        self._price = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None
        self.order_no = order_no
        self.source_amount = source_amount
        self.fiat_currency = fiat_currency
        self.obtain_amount = obtain_amount
        self.crypto_currency = crypto_currency
        self.total_fee = total_fee
        self.price = price
        self.status = status
        self.create_time = create_time
        self.update_time = update_time

    @property
    def order_no(self):
        """Gets the order_no of this InlineResponse200127Data.  # noqa: E501


        :return: The order_no of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this InlineResponse200127Data.


        :param order_no: The order_no of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if order_no is None:
            raise ValueError("Invalid value for `order_no`, must not be `None`")  # noqa: E501

        self._order_no = order_no

    @property
    def source_amount(self):
        """Gets the source_amount of this InlineResponse200127Data.  # noqa: E501

        Fiat trade amount  # noqa: E501

        :return: The source_amount of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._source_amount

    @source_amount.setter
    def source_amount(self, source_amount):
        """Sets the source_amount of this InlineResponse200127Data.

        Fiat trade amount  # noqa: E501

        :param source_amount: The source_amount of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if source_amount is None:
            raise ValueError("Invalid value for `source_amount`, must not be `None`")  # noqa: E501

        self._source_amount = source_amount

    @property
    def fiat_currency(self):
        """Gets the fiat_currency of this InlineResponse200127Data.  # noqa: E501

        Fiat token  # noqa: E501

        :return: The fiat_currency of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._fiat_currency

    @fiat_currency.setter
    def fiat_currency(self, fiat_currency):
        """Sets the fiat_currency of this InlineResponse200127Data.

        Fiat token  # noqa: E501

        :param fiat_currency: The fiat_currency of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if fiat_currency is None:
            raise ValueError("Invalid value for `fiat_currency`, must not be `None`")  # noqa: E501

        self._fiat_currency = fiat_currency

    @property
    def obtain_amount(self):
        """Gets the obtain_amount of this InlineResponse200127Data.  # noqa: E501

        Crypto trade amount  # noqa: E501

        :return: The obtain_amount of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._obtain_amount

    @obtain_amount.setter
    def obtain_amount(self, obtain_amount):
        """Sets the obtain_amount of this InlineResponse200127Data.

        Crypto trade amount  # noqa: E501

        :param obtain_amount: The obtain_amount of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if obtain_amount is None:
            raise ValueError("Invalid value for `obtain_amount`, must not be `None`")  # noqa: E501

        self._obtain_amount = obtain_amount

    @property
    def crypto_currency(self):
        """Gets the crypto_currency of this InlineResponse200127Data.  # noqa: E501

        Crypto token  # noqa: E501

        :return: The crypto_currency of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._crypto_currency

    @crypto_currency.setter
    def crypto_currency(self, crypto_currency):
        """Sets the crypto_currency of this InlineResponse200127Data.

        Crypto token  # noqa: E501

        :param crypto_currency: The crypto_currency of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if crypto_currency is None:
            raise ValueError("Invalid value for `crypto_currency`, must not be `None`")  # noqa: E501

        self._crypto_currency = crypto_currency

    @property
    def total_fee(self):
        """Gets the total_fee of this InlineResponse200127Data.  # noqa: E501

        Trade fee  # noqa: E501

        :return: The total_fee of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this InlineResponse200127Data.

        Trade fee  # noqa: E501

        :param total_fee: The total_fee of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if total_fee is None:
            raise ValueError("Invalid value for `total_fee`, must not be `None`")  # noqa: E501

        self._total_fee = total_fee

    @property
    def price(self):
        """Gets the price of this InlineResponse200127Data.  # noqa: E501


        :return: The price of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InlineResponse200127Data.


        :param price: The price of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def status(self):
        """Gets the status of this InlineResponse200127Data.  # noqa: E501

        Processing, Completed, Failed, Refunded  # noqa: E501

        :return: The status of this InlineResponse200127Data.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200127Data.

        Processing, Completed, Failed, Refunded  # noqa: E501

        :param status: The status of this InlineResponse200127Data.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this InlineResponse200127Data.  # noqa: E501


        :return: The create_time of this InlineResponse200127Data.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InlineResponse200127Data.


        :param create_time: The create_time of this InlineResponse200127Data.  # noqa: E501
        :type: int
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this InlineResponse200127Data.  # noqa: E501


        :return: The update_time of this InlineResponse200127Data.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this InlineResponse200127Data.


        :param update_time: The update_time of this InlineResponse200127Data.  # noqa: E501
        :type: int
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

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
        if issubclass(InlineResponse200127Data, dict):
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
        if not isinstance(other, InlineResponse200127Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
