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

class Sapiv1lendingautoinvestrebalancehistoryTransactionDetails(object):
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
        'transaction_date_time': 'int',
        'rebalance_direction': 'str',
        'rebalance_amount': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'transaction_date_time': 'transactionDateTime',
        'rebalance_direction': 'rebalanceDirection',
        'rebalance_amount': 'rebalanceAmount'
    }

    def __init__(self, asset=None, transaction_date_time=None, rebalance_direction=None, rebalance_amount=None):  # noqa: E501
        """Sapiv1lendingautoinvestrebalancehistoryTransactionDetails - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._transaction_date_time = None
        self._rebalance_direction = None
        self._rebalance_amount = None
        self.discriminator = None
        self.asset = asset
        self.transaction_date_time = transaction_date_time
        self.rebalance_direction = rebalance_direction
        self.rebalance_amount = rebalance_amount

    @property
    def asset(self):
        """Gets the asset of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501


        :return: The asset of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.


        :param asset: The asset of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def transaction_date_time(self):
        """Gets the transaction_date_time of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501


        :return: The transaction_date_time of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :rtype: int
        """
        return self._transaction_date_time

    @transaction_date_time.setter
    def transaction_date_time(self, transaction_date_time):
        """Sets the transaction_date_time of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.


        :param transaction_date_time: The transaction_date_time of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :type: int
        """
        if transaction_date_time is None:
            raise ValueError("Invalid value for `transaction_date_time`, must not be `None`")  # noqa: E501

        self._transaction_date_time = transaction_date_time

    @property
    def rebalance_direction(self):
        """Gets the rebalance_direction of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501


        :return: The rebalance_direction of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :rtype: str
        """
        return self._rebalance_direction

    @rebalance_direction.setter
    def rebalance_direction(self, rebalance_direction):
        """Sets the rebalance_direction of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.


        :param rebalance_direction: The rebalance_direction of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :type: str
        """
        if rebalance_direction is None:
            raise ValueError("Invalid value for `rebalance_direction`, must not be `None`")  # noqa: E501

        self._rebalance_direction = rebalance_direction

    @property
    def rebalance_amount(self):
        """Gets the rebalance_amount of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501


        :return: The rebalance_amount of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :rtype: str
        """
        return self._rebalance_amount

    @rebalance_amount.setter
    def rebalance_amount(self, rebalance_amount):
        """Sets the rebalance_amount of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.


        :param rebalance_amount: The rebalance_amount of this Sapiv1lendingautoinvestrebalancehistoryTransactionDetails.  # noqa: E501
        :type: str
        """
        if rebalance_amount is None:
            raise ValueError("Invalid value for `rebalance_amount`, must not be `None`")  # noqa: E501

        self._rebalance_amount = rebalance_amount

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
        if issubclass(Sapiv1lendingautoinvestrebalancehistoryTransactionDetails, dict):
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
        if not isinstance(other, Sapiv1lendingautoinvestrebalancehistoryTransactionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
