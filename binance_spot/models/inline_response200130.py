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

class InlineResponse200130(object):
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
        'can_transfer': 'bool',
        'create_timestamp': 'int',
        'duration': 'int',
        'end_time': 'int',
        'interest': 'str',
        'interest_rate': 'str',
        'lot': 'int',
        'position_id': 'int',
        'principal': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'purchase_time': 'int',
        'redeem_date': 'date',
        'start_time': 'int',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'can_transfer': 'canTransfer',
        'create_timestamp': 'createTimestamp',
        'duration': 'duration',
        'end_time': 'endTime',
        'interest': 'interest',
        'interest_rate': 'interestRate',
        'lot': 'lot',
        'position_id': 'positionId',
        'principal': 'principal',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'purchase_time': 'purchaseTime',
        'redeem_date': 'redeemDate',
        'start_time': 'startTime',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, asset=None, can_transfer=None, create_timestamp=None, duration=None, end_time=None, interest=None, interest_rate=None, lot=None, position_id=None, principal=None, project_id=None, project_name=None, purchase_time=None, redeem_date=None, start_time=None, status=None, type=None):  # noqa: E501
        """InlineResponse200130 - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._can_transfer = None
        self._create_timestamp = None
        self._duration = None
        self._end_time = None
        self._interest = None
        self._interest_rate = None
        self._lot = None
        self._position_id = None
        self._principal = None
        self._project_id = None
        self._project_name = None
        self._purchase_time = None
        self._redeem_date = None
        self._start_time = None
        self._status = None
        self._type = None
        self.discriminator = None
        self.asset = asset
        self.can_transfer = can_transfer
        self.create_timestamp = create_timestamp
        self.duration = duration
        self.end_time = end_time
        self.interest = interest
        self.interest_rate = interest_rate
        self.lot = lot
        self.position_id = position_id
        self.principal = principal
        self.project_id = project_id
        self.project_name = project_name
        self.purchase_time = purchase_time
        self.redeem_date = redeem_date
        self.start_time = start_time
        self.status = status
        self.type = type

    @property
    def asset(self):
        """Gets the asset of this InlineResponse200130.  # noqa: E501


        :return: The asset of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InlineResponse200130.


        :param asset: The asset of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def can_transfer(self):
        """Gets the can_transfer of this InlineResponse200130.  # noqa: E501


        :return: The can_transfer of this InlineResponse200130.  # noqa: E501
        :rtype: bool
        """
        return self._can_transfer

    @can_transfer.setter
    def can_transfer(self, can_transfer):
        """Sets the can_transfer of this InlineResponse200130.


        :param can_transfer: The can_transfer of this InlineResponse200130.  # noqa: E501
        :type: bool
        """
        if can_transfer is None:
            raise ValueError("Invalid value for `can_transfer`, must not be `None`")  # noqa: E501

        self._can_transfer = can_transfer

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this InlineResponse200130.  # noqa: E501


        :return: The create_timestamp of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this InlineResponse200130.


        :param create_timestamp: The create_timestamp of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if create_timestamp is None:
            raise ValueError("Invalid value for `create_timestamp`, must not be `None`")  # noqa: E501

        self._create_timestamp = create_timestamp

    @property
    def duration(self):
        """Gets the duration of this InlineResponse200130.  # noqa: E501


        :return: The duration of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse200130.


        :param duration: The duration of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this InlineResponse200130.  # noqa: E501


        :return: The end_time of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InlineResponse200130.


        :param end_time: The end_time of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def interest(self):
        """Gets the interest of this InlineResponse200130.  # noqa: E501


        :return: The interest of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this InlineResponse200130.


        :param interest: The interest of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def interest_rate(self):
        """Gets the interest_rate of this InlineResponse200130.  # noqa: E501


        :return: The interest_rate of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this InlineResponse200130.


        :param interest_rate: The interest_rate of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if interest_rate is None:
            raise ValueError("Invalid value for `interest_rate`, must not be `None`")  # noqa: E501

        self._interest_rate = interest_rate

    @property
    def lot(self):
        """Gets the lot of this InlineResponse200130.  # noqa: E501


        :return: The lot of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._lot

    @lot.setter
    def lot(self, lot):
        """Sets the lot of this InlineResponse200130.


        :param lot: The lot of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if lot is None:
            raise ValueError("Invalid value for `lot`, must not be `None`")  # noqa: E501

        self._lot = lot

    @property
    def position_id(self):
        """Gets the position_id of this InlineResponse200130.  # noqa: E501


        :return: The position_id of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this InlineResponse200130.


        :param position_id: The position_id of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if position_id is None:
            raise ValueError("Invalid value for `position_id`, must not be `None`")  # noqa: E501

        self._position_id = position_id

    @property
    def principal(self):
        """Gets the principal of this InlineResponse200130.  # noqa: E501


        :return: The principal of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this InlineResponse200130.


        :param principal: The principal of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def project_id(self):
        """Gets the project_id of this InlineResponse200130.  # noqa: E501


        :return: The project_id of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this InlineResponse200130.


        :param project_id: The project_id of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this InlineResponse200130.  # noqa: E501


        :return: The project_name of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InlineResponse200130.


        :param project_name: The project_name of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

    @property
    def purchase_time(self):
        """Gets the purchase_time of this InlineResponse200130.  # noqa: E501


        :return: The purchase_time of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._purchase_time

    @purchase_time.setter
    def purchase_time(self, purchase_time):
        """Sets the purchase_time of this InlineResponse200130.


        :param purchase_time: The purchase_time of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if purchase_time is None:
            raise ValueError("Invalid value for `purchase_time`, must not be `None`")  # noqa: E501

        self._purchase_time = purchase_time

    @property
    def redeem_date(self):
        """Gets the redeem_date of this InlineResponse200130.  # noqa: E501


        :return: The redeem_date of this InlineResponse200130.  # noqa: E501
        :rtype: date
        """
        return self._redeem_date

    @redeem_date.setter
    def redeem_date(self, redeem_date):
        """Sets the redeem_date of this InlineResponse200130.


        :param redeem_date: The redeem_date of this InlineResponse200130.  # noqa: E501
        :type: date
        """
        if redeem_date is None:
            raise ValueError("Invalid value for `redeem_date`, must not be `None`")  # noqa: E501

        self._redeem_date = redeem_date

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse200130.  # noqa: E501


        :return: The start_time of this InlineResponse200130.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse200130.


        :param start_time: The start_time of this InlineResponse200130.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this InlineResponse200130.  # noqa: E501


        :return: The status of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200130.


        :param status: The status of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this InlineResponse200130.  # noqa: E501


        :return: The type of this InlineResponse200130.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200130.


        :param type: The type of this InlineResponse200130.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(InlineResponse200130, dict):
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
        if not isinstance(other, InlineResponse200130):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
