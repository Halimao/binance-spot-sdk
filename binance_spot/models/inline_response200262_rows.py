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

class InlineResponse200262Rows(object):
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
        'position_id': 'str',
        'project_id': 'str',
        'asset': 'str',
        'amount': 'str',
        'purchase_time': 'str',
        'duration': 'str',
        'accrual_days': 'str',
        'reward_asset': 'str',
        'apy': 'str',
        'is_renewable': 'bool',
        'is_auto_renew': 'bool',
        'redeem_date': 'str'
    }

    attribute_map = {
        'position_id': 'positionId',
        'project_id': 'projectId',
        'asset': 'asset',
        'amount': 'amount',
        'purchase_time': 'purchaseTime',
        'duration': 'duration',
        'accrual_days': 'accrualDays',
        'reward_asset': 'rewardAsset',
        'apy': 'APY',
        'is_renewable': 'isRenewable',
        'is_auto_renew': 'isAutoRenew',
        'redeem_date': 'redeemDate'
    }

    def __init__(self, position_id=None, project_id=None, asset=None, amount=None, purchase_time=None, duration=None, accrual_days=None, reward_asset=None, apy=None, is_renewable=None, is_auto_renew=None, redeem_date=None):  # noqa: E501
        """InlineResponse200262Rows - a model defined in Swagger"""  # noqa: E501
        self._position_id = None
        self._project_id = None
        self._asset = None
        self._amount = None
        self._purchase_time = None
        self._duration = None
        self._accrual_days = None
        self._reward_asset = None
        self._apy = None
        self._is_renewable = None
        self._is_auto_renew = None
        self._redeem_date = None
        self.discriminator = None
        self.position_id = position_id
        self.project_id = project_id
        self.asset = asset
        self.amount = amount
        self.purchase_time = purchase_time
        self.duration = duration
        self.accrual_days = accrual_days
        self.reward_asset = reward_asset
        self.apy = apy
        self.is_renewable = is_renewable
        self.is_auto_renew = is_auto_renew
        self.redeem_date = redeem_date

    @property
    def position_id(self):
        """Gets the position_id of this InlineResponse200262Rows.  # noqa: E501


        :return: The position_id of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this InlineResponse200262Rows.


        :param position_id: The position_id of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if position_id is None:
            raise ValueError("Invalid value for `position_id`, must not be `None`")  # noqa: E501

        self._position_id = position_id

    @property
    def project_id(self):
        """Gets the project_id of this InlineResponse200262Rows.  # noqa: E501


        :return: The project_id of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this InlineResponse200262Rows.


        :param project_id: The project_id of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200262Rows.  # noqa: E501


        :return: The asset of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200262Rows.


        :param asset: The asset of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def amount(self):
        """Gets the amount of this InlineResponse200262Rows.  # noqa: E501


        :return: The amount of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse200262Rows.


        :param amount: The amount of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def purchase_time(self):
        """Gets the purchase_time of this InlineResponse200262Rows.  # noqa: E501


        :return: The purchase_time of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._purchase_time

    @purchase_time.setter
    def purchase_time(self, purchase_time):
        """Sets the purchase_time of this InlineResponse200262Rows.


        :param purchase_time: The purchase_time of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if purchase_time is None:
            raise ValueError("Invalid value for `purchase_time`, must not be `None`")  # noqa: E501

        self._purchase_time = purchase_time

    @property
    def duration(self):
        """Gets the duration of this InlineResponse200262Rows.  # noqa: E501


        :return: The duration of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse200262Rows.


        :param duration: The duration of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def accrual_days(self):
        """Gets the accrual_days of this InlineResponse200262Rows.  # noqa: E501


        :return: The accrual_days of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._accrual_days

    @accrual_days.setter
    def accrual_days(self, accrual_days):
        """Sets the accrual_days of this InlineResponse200262Rows.


        :param accrual_days: The accrual_days of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if accrual_days is None:
            raise ValueError("Invalid value for `accrual_days`, must not be `None`")  # noqa: E501

        self._accrual_days = accrual_days

    @property
    def reward_asset(self):
        """Gets the reward_asset of this InlineResponse200262Rows.  # noqa: E501


        :return: The reward_asset of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._reward_asset

    @reward_asset.setter
    def reward_asset(self, reward_asset):
        """Sets the reward_asset of this InlineResponse200262Rows.


        :param reward_asset: The reward_asset of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if reward_asset is None:
            raise ValueError("Invalid value for `reward_asset`, must not be `None`")  # noqa: E501

        self._reward_asset = reward_asset

    @property
    def apy(self):
        """Gets the apy of this InlineResponse200262Rows.  # noqa: E501


        :return: The apy of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._apy

    @apy.setter
    def apy(self, apy):
        """Sets the apy of this InlineResponse200262Rows.


        :param apy: The apy of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if apy is None:
            raise ValueError("Invalid value for `apy`, must not be `None`")  # noqa: E501

        self._apy = apy

    @property
    def is_renewable(self):
        """Gets the is_renewable of this InlineResponse200262Rows.  # noqa: E501


        :return: The is_renewable of this InlineResponse200262Rows.  # noqa: E501
        :rtype: bool
        """
        return self._is_renewable

    @is_renewable.setter
    def is_renewable(self, is_renewable):
        """Sets the is_renewable of this InlineResponse200262Rows.


        :param is_renewable: The is_renewable of this InlineResponse200262Rows.  # noqa: E501
        :type: bool
        """
        if is_renewable is None:
            raise ValueError("Invalid value for `is_renewable`, must not be `None`")  # noqa: E501

        self._is_renewable = is_renewable

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this InlineResponse200262Rows.  # noqa: E501


        :return: The is_auto_renew of this InlineResponse200262Rows.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this InlineResponse200262Rows.


        :param is_auto_renew: The is_auto_renew of this InlineResponse200262Rows.  # noqa: E501
        :type: bool
        """
        if is_auto_renew is None:
            raise ValueError("Invalid value for `is_auto_renew`, must not be `None`")  # noqa: E501

        self._is_auto_renew = is_auto_renew

    @property
    def redeem_date(self):
        """Gets the redeem_date of this InlineResponse200262Rows.  # noqa: E501


        :return: The redeem_date of this InlineResponse200262Rows.  # noqa: E501
        :rtype: str
        """
        return self._redeem_date

    @redeem_date.setter
    def redeem_date(self, redeem_date):
        """Sets the redeem_date of this InlineResponse200262Rows.


        :param redeem_date: The redeem_date of this InlineResponse200262Rows.  # noqa: E501
        :type: str
        """
        if redeem_date is None:
            raise ValueError("Invalid value for `redeem_date`, must not be `None`")  # noqa: E501

        self._redeem_date = redeem_date

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
        if issubclass(InlineResponse200262Rows, dict):
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
        if not isinstance(other, InlineResponse200262Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other