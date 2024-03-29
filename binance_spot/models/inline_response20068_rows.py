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

class InlineResponse20068Rows(object):
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
        'id': 'int',
        'amount': 'str',
        'asset': 'str',
        'div_time': 'int',
        'en_info': 'str',
        'tran_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'asset': 'asset',
        'div_time': 'divTime',
        'en_info': 'enInfo',
        'tran_id': 'tranId'
    }

    def __init__(self, id=None, amount=None, asset=None, div_time=None, en_info=None, tran_id=None):  # noqa: E501
        """InlineResponse20068Rows - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._asset = None
        self._div_time = None
        self._en_info = None
        self._tran_id = None
        self.discriminator = None
        self.id = id
        self.amount = amount
        self.asset = asset
        self.div_time = div_time
        self.en_info = en_info
        self.tran_id = tran_id

    @property
    def id(self):
        """Gets the id of this InlineResponse20068Rows.  # noqa: E501


        :return: The id of this InlineResponse20068Rows.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20068Rows.


        :param id: The id of this InlineResponse20068Rows.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20068Rows.  # noqa: E501


        :return: The amount of this InlineResponse20068Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20068Rows.


        :param amount: The amount of this InlineResponse20068Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def asset(self):
        """Gets the asset of this InlineResponse20068Rows.  # noqa: E501


        :return: The asset of this InlineResponse20068Rows.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse20068Rows.


        :param asset: The asset of this InlineResponse20068Rows.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def div_time(self):
        """Gets the div_time of this InlineResponse20068Rows.  # noqa: E501


        :return: The div_time of this InlineResponse20068Rows.  # noqa: E501
        :rtype: int
        """
        return self._div_time

    @div_time.setter
    def div_time(self, div_time):
        """Sets the div_time of this InlineResponse20068Rows.


        :param div_time: The div_time of this InlineResponse20068Rows.  # noqa: E501
        :type: int
        """
        if div_time is None:
            raise ValueError("Invalid value for `div_time`, must not be `None`")  # noqa: E501

        self._div_time = div_time

    @property
    def en_info(self):
        """Gets the en_info of this InlineResponse20068Rows.  # noqa: E501


        :return: The en_info of this InlineResponse20068Rows.  # noqa: E501
        :rtype: str
        """
        return self._en_info

    @en_info.setter
    def en_info(self, en_info):
        """Sets the en_info of this InlineResponse20068Rows.


        :param en_info: The en_info of this InlineResponse20068Rows.  # noqa: E501
        :type: str
        """
        if en_info is None:
            raise ValueError("Invalid value for `en_info`, must not be `None`")  # noqa: E501

        self._en_info = en_info

    @property
    def tran_id(self):
        """Gets the tran_id of this InlineResponse20068Rows.  # noqa: E501


        :return: The tran_id of this InlineResponse20068Rows.  # noqa: E501
        :rtype: int
        """
        return self._tran_id

    @tran_id.setter
    def tran_id(self, tran_id):
        """Sets the tran_id of this InlineResponse20068Rows.


        :param tran_id: The tran_id of this InlineResponse20068Rows.  # noqa: E501
        :type: int
        """
        if tran_id is None:
            raise ValueError("Invalid value for `tran_id`, must not be `None`")  # noqa: E501

        self._tran_id = tran_id

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
        if issubclass(InlineResponse20068Rows, dict):
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
        if not isinstance(other, InlineResponse20068Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
