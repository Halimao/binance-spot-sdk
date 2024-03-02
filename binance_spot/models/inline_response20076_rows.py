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

class InlineResponse20076Rows(object):
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
        'tran_id': 'int',
        'type': 'int',
        'time': 'int',
        'deducted_asset': 'str',
        'deducted_amount': 'str',
        'target_asset': 'str',
        'target_amount': 'str',
        'status': 'str',
        'account_type': 'str'
    }

    attribute_map = {
        'tran_id': 'tranId',
        'type': 'type',
        'time': 'time',
        'deducted_asset': 'deductedAsset',
        'deducted_amount': 'deductedAmount',
        'target_asset': 'targetAsset',
        'target_amount': 'targetAmount',
        'status': 'status',
        'account_type': 'accountType'
    }

    def __init__(self, tran_id=None, type=None, time=None, deducted_asset=None, deducted_amount=None, target_asset=None, target_amount=None, status=None, account_type=None):  # noqa: E501
        """InlineResponse20076Rows - a model defined in Swagger"""  # noqa: E501
        self._tran_id = None
        self._type = None
        self._time = None
        self._deducted_asset = None
        self._deducted_amount = None
        self._target_asset = None
        self._target_amount = None
        self._status = None
        self._account_type = None
        self.discriminator = None
        self.tran_id = tran_id
        self.type = type
        self.time = time
        self.deducted_asset = deducted_asset
        self.deducted_amount = deducted_amount
        self.target_asset = target_asset
        self.target_amount = target_amount
        self.status = status
        self.account_type = account_type

    @property
    def tran_id(self):
        """Gets the tran_id of this InlineResponse20076Rows.  # noqa: E501


        :return: The tran_id of this InlineResponse20076Rows.  # noqa: E501
        :rtype: int
        """
        return self._tran_id

    @tran_id.setter
    def tran_id(self, tran_id):
        """Sets the tran_id of this InlineResponse20076Rows.


        :param tran_id: The tran_id of this InlineResponse20076Rows.  # noqa: E501
        :type: int
        """
        if tran_id is None:
            raise ValueError("Invalid value for `tran_id`, must not be `None`")  # noqa: E501

        self._tran_id = tran_id

    @property
    def type(self):
        """Gets the type of this InlineResponse20076Rows.  # noqa: E501


        :return: The type of this InlineResponse20076Rows.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20076Rows.


        :param type: The type of this InlineResponse20076Rows.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def time(self):
        """Gets the time of this InlineResponse20076Rows.  # noqa: E501


        :return: The time of this InlineResponse20076Rows.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20076Rows.


        :param time: The time of this InlineResponse20076Rows.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def deducted_asset(self):
        """Gets the deducted_asset of this InlineResponse20076Rows.  # noqa: E501


        :return: The deducted_asset of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._deducted_asset

    @deducted_asset.setter
    def deducted_asset(self, deducted_asset):
        """Sets the deducted_asset of this InlineResponse20076Rows.


        :param deducted_asset: The deducted_asset of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if deducted_asset is None:
            raise ValueError("Invalid value for `deducted_asset`, must not be `None`")  # noqa: E501

        self._deducted_asset = deducted_asset

    @property
    def deducted_amount(self):
        """Gets the deducted_amount of this InlineResponse20076Rows.  # noqa: E501


        :return: The deducted_amount of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._deducted_amount

    @deducted_amount.setter
    def deducted_amount(self, deducted_amount):
        """Sets the deducted_amount of this InlineResponse20076Rows.


        :param deducted_amount: The deducted_amount of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if deducted_amount is None:
            raise ValueError("Invalid value for `deducted_amount`, must not be `None`")  # noqa: E501

        self._deducted_amount = deducted_amount

    @property
    def target_asset(self):
        """Gets the target_asset of this InlineResponse20076Rows.  # noqa: E501


        :return: The target_asset of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._target_asset

    @target_asset.setter
    def target_asset(self, target_asset):
        """Sets the target_asset of this InlineResponse20076Rows.


        :param target_asset: The target_asset of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if target_asset is None:
            raise ValueError("Invalid value for `target_asset`, must not be `None`")  # noqa: E501

        self._target_asset = target_asset

    @property
    def target_amount(self):
        """Gets the target_amount of this InlineResponse20076Rows.  # noqa: E501


        :return: The target_amount of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._target_amount

    @target_amount.setter
    def target_amount(self, target_amount):
        """Sets the target_amount of this InlineResponse20076Rows.


        :param target_amount: The target_amount of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if target_amount is None:
            raise ValueError("Invalid value for `target_amount`, must not be `None`")  # noqa: E501

        self._target_amount = target_amount

    @property
    def status(self):
        """Gets the status of this InlineResponse20076Rows.  # noqa: E501


        :return: The status of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20076Rows.


        :param status: The status of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def account_type(self):
        """Gets the account_type of this InlineResponse20076Rows.  # noqa: E501


        :return: The account_type of this InlineResponse20076Rows.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this InlineResponse20076Rows.


        :param account_type: The account_type of this InlineResponse20076Rows.  # noqa: E501
        :type: str
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

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
        if issubclass(InlineResponse20076Rows, dict):
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
        if not isinstance(other, InlineResponse20076Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
