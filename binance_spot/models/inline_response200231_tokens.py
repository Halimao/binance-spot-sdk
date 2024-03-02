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

class InlineResponse200231Tokens(object):
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
        'token_id': 'str',
        'contract_address': 'str'
    }

    attribute_map = {
        'network': 'network',
        'token_id': 'tokenId',
        'contract_address': 'contractAddress'
    }

    def __init__(self, network=None, token_id=None, contract_address=None):  # noqa: E501
        """InlineResponse200231Tokens - a model defined in Swagger"""  # noqa: E501
        self._network = None
        self._token_id = None
        self._contract_address = None
        self.discriminator = None
        self.network = network
        self.token_id = token_id
        self.contract_address = contract_address

    @property
    def network(self):
        """Gets the network of this InlineResponse200231Tokens.  # noqa: E501


        :return: The network of this InlineResponse200231Tokens.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InlineResponse200231Tokens.


        :param network: The network of this InlineResponse200231Tokens.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def token_id(self):
        """Gets the token_id of this InlineResponse200231Tokens.  # noqa: E501


        :return: The token_id of this InlineResponse200231Tokens.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this InlineResponse200231Tokens.


        :param token_id: The token_id of this InlineResponse200231Tokens.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def contract_address(self):
        """Gets the contract_address of this InlineResponse200231Tokens.  # noqa: E501


        :return: The contract_address of this InlineResponse200231Tokens.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this InlineResponse200231Tokens.


        :param contract_address: The contract_address of this InlineResponse200231Tokens.  # noqa: E501
        :type: str
        """
        if contract_address is None:
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

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
        if issubclass(InlineResponse200231Tokens, dict):
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
        if not isinstance(other, InlineResponse200231Tokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
