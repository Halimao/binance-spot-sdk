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

class InlineResponse20091Rows(object):
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
        'client_tran_id': 'str',
        'transfer_type': 'str',
        'asset': 'str',
        'amount': 'str',
        'time': 'int'
    }

    attribute_map = {
        'client_tran_id': 'clientTranId',
        'transfer_type': 'transferType',
        'asset': 'asset',
        'amount': 'amount',
        'time': 'time'
    }

    def __init__(self, client_tran_id=None, transfer_type=None, asset=None, amount=None, time=None):  # noqa: E501
        """InlineResponse20091Rows - a model defined in Swagger"""  # noqa: E501
        self._client_tran_id = None
        self._transfer_type = None
        self._asset = None
        self._amount = None
        self._time = None
        self.discriminator = None
        self.client_tran_id = client_tran_id
        self.transfer_type = transfer_type
        self.asset = asset
        self.amount = amount
        self.time = time

    @property
    def client_tran_id(self):
        """Gets the client_tran_id of this InlineResponse20091Rows.  # noqa: E501


        :return: The client_tran_id of this InlineResponse20091Rows.  # noqa: E501
        :rtype: str
        """
        return self._client_tran_id

    @client_tran_id.setter
    def client_tran_id(self, client_tran_id):
        """Sets the client_tran_id of this InlineResponse20091Rows.


        :param client_tran_id: The client_tran_id of this InlineResponse20091Rows.  # noqa: E501
        :type: str
        """
        if client_tran_id is None:
            raise ValueError("Invalid value for `client_tran_id`, must not be `None`")  # noqa: E501

        self._client_tran_id = client_tran_id

    @property
    def transfer_type(self):
        """Gets the transfer_type of this InlineResponse20091Rows.  # noqa: E501


        :return: The transfer_type of this InlineResponse20091Rows.  # noqa: E501
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        """Sets the transfer_type of this InlineResponse20091Rows.


        :param transfer_type: The transfer_type of this InlineResponse20091Rows.  # noqa: E501
        :type: str
        """
        if transfer_type is None:
            raise ValueError("Invalid value for `transfer_type`, must not be `None`")  # noqa: E501

        self._transfer_type = transfer_type

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20091Rows.  # noqa: E501


        :return: The asset of this InlineResponse20091Rows.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20091Rows.


        :param asset: The asset of this InlineResponse20091Rows.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20091Rows.  # noqa: E501


        :return: The amount of this InlineResponse20091Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20091Rows.


        :param amount: The amount of this InlineResponse20091Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def time(self):
        """Gets the time of this InlineResponse20091Rows.  # noqa: E501


        :return: The time of this InlineResponse20091Rows.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20091Rows.


        :param time: The time of this InlineResponse20091Rows.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(InlineResponse20091Rows, dict):
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
        if not isinstance(other, InlineResponse20091Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
