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

class InlineResponse200223Data(object):
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
        'order_type': 'str',
        'transaction_id': 'str',
        'transaction_time': 'int',
        'amount': 'str',
        'currency': 'str',
        'wallet_type': 'int',
        'wallet_types': 'list[int]',
        'funds_detail': 'list[InlineResponse200223FundsDetail]',
        'payer_info': 'InlineResponse200223PayerInfo',
        'receiver_info': 'InlineResponse200223ReceiverInfo'
    }

    attribute_map = {
        'order_type': 'orderType',
        'transaction_id': 'transactionId',
        'transaction_time': 'transactionTime',
        'amount': 'amount',
        'currency': 'currency',
        'wallet_type': 'walletType',
        'wallet_types': 'walletTypes',
        'funds_detail': 'fundsDetail',
        'payer_info': 'payerInfo',
        'receiver_info': 'receiverInfo'
    }

    def __init__(self, order_type=None, transaction_id=None, transaction_time=None, amount=None, currency=None, wallet_type=None, wallet_types=None, funds_detail=None, payer_info=None, receiver_info=None):  # noqa: E501
        """InlineResponse200223Data - a model defined in Swagger"""  # noqa: E501
        self._order_type = None
        self._transaction_id = None
        self._transaction_time = None
        self._amount = None
        self._currency = None
        self._wallet_type = None
        self._wallet_types = None
        self._funds_detail = None
        self._payer_info = None
        self._receiver_info = None
        self.discriminator = None
        self.order_type = order_type
        self.transaction_id = transaction_id
        self.transaction_time = transaction_time
        self.amount = amount
        self.currency = currency
        self.wallet_type = wallet_type
        self.wallet_types = wallet_types
        self.funds_detail = funds_detail
        self.payer_info = payer_info
        self.receiver_info = receiver_info

    @property
    def order_type(self):
        """Gets the order_type of this InlineResponse200223Data.  # noqa: E501

        Enum：PAY(C2B Merchant Acquiring Payment), PAY_REFUND(C2B Merchant Acquiring Payment,refund), C2C(C2C Transfer Payment),CRYPTO_BOX(Crypto box), CRYPTO_BOX_RF(Crypto Box, refund), C2C_HOLDING(Transfer to new Binance user), C2C_HOLDING_RF(Transfer to new Binance user,refund), PAYOUT(B2C Disbursement Payment)  # noqa: E501

        :return: The order_type of this InlineResponse200223Data.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this InlineResponse200223Data.

        Enum：PAY(C2B Merchant Acquiring Payment), PAY_REFUND(C2B Merchant Acquiring Payment,refund), C2C(C2C Transfer Payment),CRYPTO_BOX(Crypto box), CRYPTO_BOX_RF(Crypto Box, refund), C2C_HOLDING(Transfer to new Binance user), C2C_HOLDING_RF(Transfer to new Binance user,refund), PAYOUT(B2C Disbursement Payment)  # noqa: E501

        :param order_type: The order_type of this InlineResponse200223Data.  # noqa: E501
        :type: str
        """
        if order_type is None:
            raise ValueError("Invalid value for `order_type`, must not be `None`")  # noqa: E501

        self._order_type = order_type

    @property
    def transaction_id(self):
        """Gets the transaction_id of this InlineResponse200223Data.  # noqa: E501


        :return: The transaction_id of this InlineResponse200223Data.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this InlineResponse200223Data.


        :param transaction_id: The transaction_id of this InlineResponse200223Data.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this InlineResponse200223Data.  # noqa: E501


        :return: The transaction_time of this InlineResponse200223Data.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this InlineResponse200223Data.


        :param transaction_time: The transaction_time of this InlineResponse200223Data.  # noqa: E501
        :type: int
        """
        if transaction_time is None:
            raise ValueError("Invalid value for `transaction_time`, must not be `None`")  # noqa: E501

        self._transaction_time = transaction_time

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200223Data.  # noqa: E501

        order amount(up to 8 decimal places), positive is income, negative is expenditure  # noqa: E501

        :return: The amount of this InlineResponse200223Data.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200223Data.

        order amount(up to 8 decimal places), positive is income, negative is expenditure  # noqa: E501

        :param amount: The amount of this InlineResponse200223Data.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InlineResponse200223Data.  # noqa: E501


        :return: The currency of this InlineResponse200223Data.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse200223Data.


        :param currency: The currency of this InlineResponse200223Data.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def wallet_type(self):
        """Gets the wallet_type of this InlineResponse200223Data.  # noqa: E501


        :return: The wallet_type of this InlineResponse200223Data.  # noqa: E501
        :rtype: int
        """
        return self._wallet_type

    @wallet_type.setter
    def wallet_type(self, wallet_type):
        """Sets the wallet_type of this InlineResponse200223Data.


        :param wallet_type: The wallet_type of this InlineResponse200223Data.  # noqa: E501
        :type: int
        """
        if wallet_type is None:
            raise ValueError("Invalid value for `wallet_type`, must not be `None`")  # noqa: E501

        self._wallet_type = wallet_type

    @property
    def wallet_types(self):
        """Gets the wallet_types of this InlineResponse200223Data.  # noqa: E501


        :return: The wallet_types of this InlineResponse200223Data.  # noqa: E501
        :rtype: list[int]
        """
        return self._wallet_types

    @wallet_types.setter
    def wallet_types(self, wallet_types):
        """Sets the wallet_types of this InlineResponse200223Data.


        :param wallet_types: The wallet_types of this InlineResponse200223Data.  # noqa: E501
        :type: list[int]
        """
        if wallet_types is None:
            raise ValueError("Invalid value for `wallet_types`, must not be `None`")  # noqa: E501

        self._wallet_types = wallet_types

    @property
    def funds_detail(self):
        """Gets the funds_detail of this InlineResponse200223Data.  # noqa: E501


        :return: The funds_detail of this InlineResponse200223Data.  # noqa: E501
        :rtype: list[InlineResponse200223FundsDetail]
        """
        return self._funds_detail

    @funds_detail.setter
    def funds_detail(self, funds_detail):
        """Sets the funds_detail of this InlineResponse200223Data.


        :param funds_detail: The funds_detail of this InlineResponse200223Data.  # noqa: E501
        :type: list[InlineResponse200223FundsDetail]
        """
        if funds_detail is None:
            raise ValueError("Invalid value for `funds_detail`, must not be `None`")  # noqa: E501

        self._funds_detail = funds_detail

    @property
    def payer_info(self):
        """Gets the payer_info of this InlineResponse200223Data.  # noqa: E501


        :return: The payer_info of this InlineResponse200223Data.  # noqa: E501
        :rtype: InlineResponse200223PayerInfo
        """
        return self._payer_info

    @payer_info.setter
    def payer_info(self, payer_info):
        """Sets the payer_info of this InlineResponse200223Data.


        :param payer_info: The payer_info of this InlineResponse200223Data.  # noqa: E501
        :type: InlineResponse200223PayerInfo
        """
        if payer_info is None:
            raise ValueError("Invalid value for `payer_info`, must not be `None`")  # noqa: E501

        self._payer_info = payer_info

    @property
    def receiver_info(self):
        """Gets the receiver_info of this InlineResponse200223Data.  # noqa: E501


        :return: The receiver_info of this InlineResponse200223Data.  # noqa: E501
        :rtype: InlineResponse200223ReceiverInfo
        """
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, receiver_info):
        """Sets the receiver_info of this InlineResponse200223Data.


        :param receiver_info: The receiver_info of this InlineResponse200223Data.  # noqa: E501
        :type: InlineResponse200223ReceiverInfo
        """
        if receiver_info is None:
            raise ValueError("Invalid value for `receiver_info`, must not be `None`")  # noqa: E501

        self._receiver_info = receiver_info

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
        if issubclass(InlineResponse200223Data, dict):
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
        if not isinstance(other, InlineResponse200223Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
