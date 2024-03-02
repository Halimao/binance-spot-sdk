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

class InlineResponse200223ReceiverInfo(object):
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
        'name': 'str',
        'type': 'str',
        'email': 'str',
        'binance_id': 'str',
        'account_id': 'str',
        'country_code': 'str',
        'phone_number': 'str',
        'mobile_code': 'str',
        'extend': 'list[InlineResponse200223ReceiverInfoExtend]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'email': 'email',
        'binance_id': 'binanceId',
        'account_id': 'accountId',
        'country_code': 'countryCode',
        'phone_number': 'phoneNumber',
        'mobile_code': 'mobileCode',
        'extend': 'extend'
    }

    def __init__(self, name=None, type=None, email=None, binance_id=None, account_id=None, country_code=None, phone_number=None, mobile_code=None, extend=None):  # noqa: E501
        """InlineResponse200223ReceiverInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._email = None
        self._binance_id = None
        self._account_id = None
        self._country_code = None
        self._phone_number = None
        self._mobile_code = None
        self._extend = None
        self.discriminator = None
        self.name = name
        self.type = type
        self.email = email
        self.binance_id = binance_id
        self.account_id = account_id
        self.country_code = country_code
        self.phone_number = phone_number
        self.mobile_code = mobile_code
        if extend is not None:
            self.extend = extend

    @property
    def name(self):
        """Gets the name of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The name of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200223ReceiverInfo.


        :param name: The name of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The type of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200223ReceiverInfo.


        :param type: The type of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def email(self):
        """Gets the email of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The email of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse200223ReceiverInfo.


        :param email: The email of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def binance_id(self):
        """Gets the binance_id of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The binance_id of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._binance_id

    @binance_id.setter
    def binance_id(self, binance_id):
        """Sets the binance_id of this InlineResponse200223ReceiverInfo.


        :param binance_id: The binance_id of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if binance_id is None:
            raise ValueError("Invalid value for `binance_id`, must not be `None`")  # noqa: E501

        self._binance_id = binance_id

    @property
    def account_id(self):
        """Gets the account_id of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The account_id of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InlineResponse200223ReceiverInfo.


        :param account_id: The account_id of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def country_code(self):
        """Gets the country_code of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The country_code of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this InlineResponse200223ReceiverInfo.


        :param country_code: The country_code of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The phone_number of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse200223ReceiverInfo.


        :param phone_number: The phone_number of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def mobile_code(self):
        """Gets the mobile_code of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The mobile_code of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: str
        """
        return self._mobile_code

    @mobile_code.setter
    def mobile_code(self, mobile_code):
        """Sets the mobile_code of this InlineResponse200223ReceiverInfo.


        :param mobile_code: The mobile_code of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: str
        """
        if mobile_code is None:
            raise ValueError("Invalid value for `mobile_code`, must not be `None`")  # noqa: E501

        self._mobile_code = mobile_code

    @property
    def extend(self):
        """Gets the extend of this InlineResponse200223ReceiverInfo.  # noqa: E501


        :return: The extend of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :rtype: list[InlineResponse200223ReceiverInfoExtend]
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this InlineResponse200223ReceiverInfo.


        :param extend: The extend of this InlineResponse200223ReceiverInfo.  # noqa: E501
        :type: list[InlineResponse200223ReceiverInfoExtend]
        """

        self._extend = extend

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
        if issubclass(InlineResponse200223ReceiverInfo, dict):
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
        if not isinstance(other, InlineResponse200223ReceiverInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
