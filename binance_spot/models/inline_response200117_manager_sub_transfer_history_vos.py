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

class InlineResponse200117ManagerSubTransferHistoryVos(object):
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
        'from_email': 'str',
        'from_account_type': 'str',
        'to_email': 'str',
        'to_account_type': 'str',
        'asset': 'str',
        'amount': 'str',
        'scheduled_data': 'int',
        'create_time': 'int',
        'status': 'str',
        'tran_id': 'int'
    }

    attribute_map = {
        'from_email': 'fromEmail',
        'from_account_type': 'fromAccountType',
        'to_email': 'toEmail',
        'to_account_type': 'toAccountType',
        'asset': 'asset',
        'amount': 'amount',
        'scheduled_data': 'scheduledData',
        'create_time': 'createTime',
        'status': 'status',
        'tran_id': 'tranId'
    }

    def __init__(self, from_email=None, from_account_type=None, to_email=None, to_account_type=None, asset=None, amount=None, scheduled_data=None, create_time=None, status=None, tran_id=None):  # noqa: E501
        """InlineResponse200117ManagerSubTransferHistoryVos - a model defined in Swagger"""  # noqa: E501
        self._from_email = None
        self._from_account_type = None
        self._to_email = None
        self._to_account_type = None
        self._asset = None
        self._amount = None
        self._scheduled_data = None
        self._create_time = None
        self._status = None
        self._tran_id = None
        self.discriminator = None
        self.from_email = from_email
        self.from_account_type = from_account_type
        self.to_email = to_email
        self.to_account_type = to_account_type
        self.asset = asset
        self.amount = amount
        self.scheduled_data = scheduled_data
        self.create_time = create_time
        self.status = status
        self.tran_id = tran_id

    @property
    def from_email(self):
        """Gets the from_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The from_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param from_email: The from_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if from_email is None:
            raise ValueError("Invalid value for `from_email`, must not be `None`")  # noqa: E501

        self._from_email = from_email

    @property
    def from_account_type(self):
        """Gets the from_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The from_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._from_account_type

    @from_account_type.setter
    def from_account_type(self, from_account_type):
        """Sets the from_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param from_account_type: The from_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if from_account_type is None:
            raise ValueError("Invalid value for `from_account_type`, must not be `None`")  # noqa: E501

        self._from_account_type = from_account_type

    @property
    def to_email(self):
        """Gets the to_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The to_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._to_email

    @to_email.setter
    def to_email(self, to_email):
        """Sets the to_email of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param to_email: The to_email of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if to_email is None:
            raise ValueError("Invalid value for `to_email`, must not be `None`")  # noqa: E501

        self._to_email = to_email

    @property
    def to_account_type(self):
        """Gets the to_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The to_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._to_account_type

    @to_account_type.setter
    def to_account_type(self, to_account_type):
        """Sets the to_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param to_account_type: The to_account_type of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if to_account_type is None:
            raise ValueError("Invalid value for `to_account_type`, must not be `None`")  # noqa: E501

        self._to_account_type = to_account_type

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The asset of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param asset: The asset of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The amount of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param amount: The amount of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def scheduled_data(self):
        """Gets the scheduled_data of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The scheduled_data of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_data

    @scheduled_data.setter
    def scheduled_data(self, scheduled_data):
        """Sets the scheduled_data of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param scheduled_data: The scheduled_data of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: int
        """
        if scheduled_data is None:
            raise ValueError("Invalid value for `scheduled_data`, must not be `None`")  # noqa: E501

        self._scheduled_data = scheduled_data

    @property
    def create_time(self):
        """Gets the create_time of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The create_time of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param create_time: The create_time of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: int
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The status of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param status: The status of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tran_id(self):
        """Gets the tran_id of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501


        :return: The tran_id of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
        :rtype: int
        """
        return self._tran_id

    @tran_id.setter
    def tran_id(self, tran_id):
        """Sets the tran_id of this InlineResponse200117ManagerSubTransferHistoryVos.


        :param tran_id: The tran_id of this InlineResponse200117ManagerSubTransferHistoryVos.  # noqa: E501
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
        if issubclass(InlineResponse200117ManagerSubTransferHistoryVos, dict):
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
        if not isinstance(other, InlineResponse200117ManagerSubTransferHistoryVos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
