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

class InlineResponse20020Rows(object):
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
        'isolated_symbol': 'str',
        'amount': 'str',
        'asset': 'str',
        'interest': 'str',
        'principal': 'str',
        'status': 'str',
        'timestamp': 'int',
        'tx_id': 'int'
    }

    attribute_map = {
        'isolated_symbol': 'isolatedSymbol',
        'amount': 'amount',
        'asset': 'asset',
        'interest': 'interest',
        'principal': 'principal',
        'status': 'status',
        'timestamp': 'timestamp',
        'tx_id': 'txId'
    }

    def __init__(self, isolated_symbol=None, amount=None, asset=None, interest=None, principal=None, status=None, timestamp=None, tx_id=None):  # noqa: E501
        """InlineResponse20020Rows - a model defined in Swagger"""  # noqa: E501
        self._isolated_symbol = None
        self._amount = None
        self._asset = None
        self._interest = None
        self._principal = None
        self._status = None
        self._timestamp = None
        self._tx_id = None
        self.discriminator = None
        self.isolated_symbol = isolated_symbol
        self.amount = amount
        self.asset = asset
        self.interest = interest
        self.principal = principal
        self.status = status
        self.timestamp = timestamp
        self.tx_id = tx_id

    @property
    def isolated_symbol(self):
        """Gets the isolated_symbol of this InlineResponse20020Rows.  # noqa: E501

        Isolated symbol, will not be returned for crossed margin  # noqa: E501

        :return: The isolated_symbol of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._isolated_symbol

    @isolated_symbol.setter
    def isolated_symbol(self, isolated_symbol):
        """Sets the isolated_symbol of this InlineResponse20020Rows.

        Isolated symbol, will not be returned for crossed margin  # noqa: E501

        :param isolated_symbol: The isolated_symbol of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if isolated_symbol is None:
            raise ValueError("Invalid value for `isolated_symbol`, must not be `None`")  # noqa: E501

        self._isolated_symbol = isolated_symbol

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20020Rows.  # noqa: E501

        Total amount repaid  # noqa: E501

        :return: The amount of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20020Rows.

        Total amount repaid  # noqa: E501

        :param amount: The amount of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20020Rows.  # noqa: E501


        :return: The asset of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20020Rows.


        :param asset: The asset of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def interest(self):
        """Gets the interest of this InlineResponse20020Rows.  # noqa: E501

        Interest repaid  # noqa: E501

        :return: The interest of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this InlineResponse20020Rows.

        Interest repaid  # noqa: E501

        :param interest: The interest of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def principal(self):
        """Gets the principal of this InlineResponse20020Rows.  # noqa: E501

        Principal repaid  # noqa: E501

        :return: The principal of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this InlineResponse20020Rows.

        Principal repaid  # noqa: E501

        :param principal: The principal of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def status(self):
        """Gets the status of this InlineResponse20020Rows.  # noqa: E501

        One of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account)  # noqa: E501

        :return: The status of this InlineResponse20020Rows.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20020Rows.

        One of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account)  # noqa: E501

        :param status: The status of this InlineResponse20020Rows.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse20020Rows.  # noqa: E501


        :return: The timestamp of this InlineResponse20020Rows.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse20020Rows.


        :param timestamp: The timestamp of this InlineResponse20020Rows.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def tx_id(self):
        """Gets the tx_id of this InlineResponse20020Rows.  # noqa: E501


        :return: The tx_id of this InlineResponse20020Rows.  # noqa: E501
        :rtype: int
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this InlineResponse20020Rows.


        :param tx_id: The tx_id of this InlineResponse20020Rows.  # noqa: E501
        :type: int
        """
        if tx_id is None:
            raise ValueError("Invalid value for `tx_id`, must not be `None`")  # noqa: E501

        self._tx_id = tx_id

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
        if issubclass(InlineResponse20020Rows, dict):
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
        if not isinstance(other, InlineResponse20020Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other