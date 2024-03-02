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

class InlineResponse20060(object):
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
        'amount': 'str',
        'coin': 'str',
        'network': 'str',
        'status': 'int',
        'address': 'str',
        'address_tag': 'str',
        'tx_id': 'str',
        'insert_time': 'int',
        'transfer_type': 'int',
        'unlock_confirm': 'str',
        'confirm_times': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'coin': 'coin',
        'network': 'network',
        'status': 'status',
        'address': 'address',
        'address_tag': 'addressTag',
        'tx_id': 'txId',
        'insert_time': 'insertTime',
        'transfer_type': 'transferType',
        'unlock_confirm': 'unlockConfirm',
        'confirm_times': 'confirmTimes'
    }

    def __init__(self, amount=None, coin=None, network=None, status=None, address=None, address_tag=None, tx_id=None, insert_time=None, transfer_type=None, unlock_confirm=None, confirm_times=None):  # noqa: E501
        """InlineResponse20060 - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._coin = None
        self._network = None
        self._status = None
        self._address = None
        self._address_tag = None
        self._tx_id = None
        self._insert_time = None
        self._transfer_type = None
        self._unlock_confirm = None
        self._confirm_times = None
        self.discriminator = None
        self.amount = amount
        self.coin = coin
        self.network = network
        self.status = status
        self.address = address
        self.address_tag = address_tag
        self.tx_id = tx_id
        self.insert_time = insert_time
        self.transfer_type = transfer_type
        self.unlock_confirm = unlock_confirm
        self.confirm_times = confirm_times

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20060.  # noqa: E501


        :return: The amount of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20060.


        :param amount: The amount of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def coin(self):
        """Gets the coin of this InlineResponse20060.  # noqa: E501


        :return: The coin of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this InlineResponse20060.


        :param coin: The coin of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if coin is None:
            raise ValueError("Invalid value for `coin`, must not be `None`")  # noqa: E501

        self._coin = coin

    @property
    def network(self):
        """Gets the network of this InlineResponse20060.  # noqa: E501


        :return: The network of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InlineResponse20060.


        :param network: The network of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def status(self):
        """Gets the status of this InlineResponse20060.  # noqa: E501


        :return: The status of this InlineResponse20060.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20060.


        :param status: The status of this InlineResponse20060.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def address(self):
        """Gets the address of this InlineResponse20060.  # noqa: E501


        :return: The address of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse20060.


        :param address: The address of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address_tag(self):
        """Gets the address_tag of this InlineResponse20060.  # noqa: E501


        :return: The address_tag of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._address_tag

    @address_tag.setter
    def address_tag(self, address_tag):
        """Sets the address_tag of this InlineResponse20060.


        :param address_tag: The address_tag of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if address_tag is None:
            raise ValueError("Invalid value for `address_tag`, must not be `None`")  # noqa: E501

        self._address_tag = address_tag

    @property
    def tx_id(self):
        """Gets the tx_id of this InlineResponse20060.  # noqa: E501


        :return: The tx_id of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this InlineResponse20060.


        :param tx_id: The tx_id of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if tx_id is None:
            raise ValueError("Invalid value for `tx_id`, must not be `None`")  # noqa: E501

        self._tx_id = tx_id

    @property
    def insert_time(self):
        """Gets the insert_time of this InlineResponse20060.  # noqa: E501


        :return: The insert_time of this InlineResponse20060.  # noqa: E501
        :rtype: int
        """
        return self._insert_time

    @insert_time.setter
    def insert_time(self, insert_time):
        """Sets the insert_time of this InlineResponse20060.


        :param insert_time: The insert_time of this InlineResponse20060.  # noqa: E501
        :type: int
        """
        if insert_time is None:
            raise ValueError("Invalid value for `insert_time`, must not be `None`")  # noqa: E501

        self._insert_time = insert_time

    @property
    def transfer_type(self):
        """Gets the transfer_type of this InlineResponse20060.  # noqa: E501


        :return: The transfer_type of this InlineResponse20060.  # noqa: E501
        :rtype: int
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        """Sets the transfer_type of this InlineResponse20060.


        :param transfer_type: The transfer_type of this InlineResponse20060.  # noqa: E501
        :type: int
        """
        if transfer_type is None:
            raise ValueError("Invalid value for `transfer_type`, must not be `None`")  # noqa: E501

        self._transfer_type = transfer_type

    @property
    def unlock_confirm(self):
        """Gets the unlock_confirm of this InlineResponse20060.  # noqa: E501

        confirm times for unlocking  # noqa: E501

        :return: The unlock_confirm of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._unlock_confirm

    @unlock_confirm.setter
    def unlock_confirm(self, unlock_confirm):
        """Sets the unlock_confirm of this InlineResponse20060.

        confirm times for unlocking  # noqa: E501

        :param unlock_confirm: The unlock_confirm of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if unlock_confirm is None:
            raise ValueError("Invalid value for `unlock_confirm`, must not be `None`")  # noqa: E501

        self._unlock_confirm = unlock_confirm

    @property
    def confirm_times(self):
        """Gets the confirm_times of this InlineResponse20060.  # noqa: E501


        :return: The confirm_times of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._confirm_times

    @confirm_times.setter
    def confirm_times(self, confirm_times):
        """Sets the confirm_times of this InlineResponse20060.


        :param confirm_times: The confirm_times of this InlineResponse20060.  # noqa: E501
        :type: str
        """
        if confirm_times is None:
            raise ValueError("Invalid value for `confirm_times`, must not be `None`")  # noqa: E501

        self._confirm_times = confirm_times

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
        if issubclass(InlineResponse20060, dict):
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
        if not isinstance(other, InlineResponse20060):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other