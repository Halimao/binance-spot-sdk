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

class InlineResponse200223ReceiverInfoExtend(object):
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
        'institution_name': 'str',
        'card_number': 'str',
        'digital_wallet_id': 'str'
    }

    attribute_map = {
        'institution_name': 'institutionName',
        'card_number': 'cardNumber',
        'digital_wallet_id': 'digitalWalletId'
    }

    def __init__(self, institution_name=None, card_number=None, digital_wallet_id=None):  # noqa: E501
        """InlineResponse200223ReceiverInfoExtend - a model defined in Swagger"""  # noqa: E501
        self._institution_name = None
        self._card_number = None
        self._digital_wallet_id = None
        self.discriminator = None
        self.institution_name = institution_name
        self.card_number = card_number
        self.digital_wallet_id = digital_wallet_id

    @property
    def institution_name(self):
        """Gets the institution_name of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501


        :return: The institution_name of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this InlineResponse200223ReceiverInfoExtend.


        :param institution_name: The institution_name of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :type: str
        """
        if institution_name is None:
            raise ValueError("Invalid value for `institution_name`, must not be `None`")  # noqa: E501

        self._institution_name = institution_name

    @property
    def card_number(self):
        """Gets the card_number of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501


        :return: The card_number of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this InlineResponse200223ReceiverInfoExtend.


        :param card_number: The card_number of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :type: str
        """
        if card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def digital_wallet_id(self):
        """Gets the digital_wallet_id of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501


        :return: The digital_wallet_id of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :rtype: str
        """
        return self._digital_wallet_id

    @digital_wallet_id.setter
    def digital_wallet_id(self, digital_wallet_id):
        """Sets the digital_wallet_id of this InlineResponse200223ReceiverInfoExtend.


        :param digital_wallet_id: The digital_wallet_id of this InlineResponse200223ReceiverInfoExtend.  # noqa: E501
        :type: str
        """
        if digital_wallet_id is None:
            raise ValueError("Invalid value for `digital_wallet_id`, must not be `None`")  # noqa: E501

        self._digital_wallet_id = digital_wallet_id

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
        if issubclass(InlineResponse200223ReceiverInfoExtend, dict):
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
        if not isinstance(other, InlineResponse200223ReceiverInfoExtend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
