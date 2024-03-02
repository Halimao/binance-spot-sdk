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

class InlineResponse200233List(object):
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
        'network': 'str',
        'tx_id': 'str',
        'contract_adrress': 'str',
        'token_id': 'str',
        'timestamp': 'int',
        'fee': 'float',
        'fee_asset': 'str'
    }

    attribute_map = {
        'network': 'network',
        'tx_id': 'txID',
        'contract_adrress': 'contractAdrress',
        'token_id': 'tokenId',
        'timestamp': 'timestamp',
        'fee': 'fee',
        'fee_asset': 'feeAsset'
    }

    def __init__(self, network=None, tx_id=None, contract_adrress=None, token_id=None, timestamp=None, fee=None, fee_asset=None):  # noqa: E501
        """InlineResponse200233List - a model defined in Swagger"""  # noqa: E501
        self._network = None
        self._tx_id = None
        self._contract_adrress = None
        self._token_id = None
        self._timestamp = None
        self._fee = None
        self._fee_asset = None
        self.discriminator = None
        self.network = network
        self.tx_id = tx_id
        self.contract_adrress = contract_adrress
        self.token_id = token_id
        self.timestamp = timestamp
        self.fee = fee
        self.fee_asset = fee_asset

    @property
    def network(self):
        """Gets the network of this InlineResponse200233List.  # noqa: E501


        :return: The network of this InlineResponse200233List.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InlineResponse200233List.


        :param network: The network of this InlineResponse200233List.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def tx_id(self):
        """Gets the tx_id of this InlineResponse200233List.  # noqa: E501


        :return: The tx_id of this InlineResponse200233List.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this InlineResponse200233List.


        :param tx_id: The tx_id of this InlineResponse200233List.  # noqa: E501
        :type: str
        """
        if tx_id is None:
            raise ValueError("Invalid value for `tx_id`, must not be `None`")  # noqa: E501

        self._tx_id = tx_id

    @property
    def contract_adrress(self):
        """Gets the contract_adrress of this InlineResponse200233List.  # noqa: E501


        :return: The contract_adrress of this InlineResponse200233List.  # noqa: E501
        :rtype: str
        """
        return self._contract_adrress

    @contract_adrress.setter
    def contract_adrress(self, contract_adrress):
        """Sets the contract_adrress of this InlineResponse200233List.


        :param contract_adrress: The contract_adrress of this InlineResponse200233List.  # noqa: E501
        :type: str
        """
        if contract_adrress is None:
            raise ValueError("Invalid value for `contract_adrress`, must not be `None`")  # noqa: E501

        self._contract_adrress = contract_adrress

    @property
    def token_id(self):
        """Gets the token_id of this InlineResponse200233List.  # noqa: E501


        :return: The token_id of this InlineResponse200233List.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this InlineResponse200233List.


        :param token_id: The token_id of this InlineResponse200233List.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse200233List.  # noqa: E501


        :return: The timestamp of this InlineResponse200233List.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse200233List.


        :param timestamp: The timestamp of this InlineResponse200233List.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def fee(self):
        """Gets the fee of this InlineResponse200233List.  # noqa: E501


        :return: The fee of this InlineResponse200233List.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this InlineResponse200233List.


        :param fee: The fee of this InlineResponse200233List.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def fee_asset(self):
        """Gets the fee_asset of this InlineResponse200233List.  # noqa: E501


        :return: The fee_asset of this InlineResponse200233List.  # noqa: E501
        :rtype: str
        """
        return self._fee_asset

    @fee_asset.setter
    def fee_asset(self, fee_asset):
        """Sets the fee_asset of this InlineResponse200233List.


        :param fee_asset: The fee_asset of this InlineResponse200233List.  # noqa: E501
        :type: str
        """
        if fee_asset is None:
            raise ValueError("Invalid value for `fee_asset`, must not be `None`")  # noqa: E501

        self._fee_asset = fee_asset

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
        if issubclass(InlineResponse200233List, dict):
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
        if not isinstance(other, InlineResponse200233List):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
