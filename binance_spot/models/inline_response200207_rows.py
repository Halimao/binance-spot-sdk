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

class InlineResponse200207Rows(object):
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
        'loan_coin': 'str',
        'repay_amount': 'str',
        'collateral_coin': 'str',
        'collateral_used': 'str',
        'collateral_return': 'str',
        'repay_type': 'str',
        'repay_status': 'str',
        'repay_time': 'int',
        'order_id': 'int'
    }

    attribute_map = {
        'loan_coin': 'loanCoin',
        'repay_amount': 'repayAmount',
        'collateral_coin': 'collateralCoin',
        'collateral_used': 'collateralUsed',
        'collateral_return': 'collateralReturn',
        'repay_type': 'repayType',
        'repay_status': 'repayStatus',
        'repay_time': 'repayTime',
        'order_id': 'orderId'
    }

    def __init__(self, loan_coin=None, repay_amount=None, collateral_coin=None, collateral_used=None, collateral_return=None, repay_type=None, repay_status=None, repay_time=None, order_id=None):  # noqa: E501
        """InlineResponse200207Rows - a model defined in Swagger"""  # noqa: E501
        self._loan_coin = None
        self._repay_amount = None
        self._collateral_coin = None
        self._collateral_used = None
        self._collateral_return = None
        self._repay_type = None
        self._repay_status = None
        self._repay_time = None
        self._order_id = None
        self.discriminator = None
        self.loan_coin = loan_coin
        self.repay_amount = repay_amount
        self.collateral_coin = collateral_coin
        self.collateral_used = collateral_used
        self.collateral_return = collateral_return
        self.repay_type = repay_type
        self.repay_status = repay_status
        self.repay_time = repay_time
        self.order_id = order_id

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200207Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200207Rows.


        :param loan_coin: The loan_coin of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def repay_amount(self):
        """Gets the repay_amount of this InlineResponse200207Rows.  # noqa: E501


        :return: The repay_amount of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, repay_amount):
        """Sets the repay_amount of this InlineResponse200207Rows.


        :param repay_amount: The repay_amount of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if repay_amount is None:
            raise ValueError("Invalid value for `repay_amount`, must not be `None`")  # noqa: E501

        self._repay_amount = repay_amount

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200207Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200207Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def collateral_used(self):
        """Gets the collateral_used of this InlineResponse200207Rows.  # noqa: E501


        :return: The collateral_used of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_used

    @collateral_used.setter
    def collateral_used(self, collateral_used):
        """Sets the collateral_used of this InlineResponse200207Rows.


        :param collateral_used: The collateral_used of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if collateral_used is None:
            raise ValueError("Invalid value for `collateral_used`, must not be `None`")  # noqa: E501

        self._collateral_used = collateral_used

    @property
    def collateral_return(self):
        """Gets the collateral_return of this InlineResponse200207Rows.  # noqa: E501


        :return: The collateral_return of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_return

    @collateral_return.setter
    def collateral_return(self, collateral_return):
        """Sets the collateral_return of this InlineResponse200207Rows.


        :param collateral_return: The collateral_return of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if collateral_return is None:
            raise ValueError("Invalid value for `collateral_return`, must not be `None`")  # noqa: E501

        self._collateral_return = collateral_return

    @property
    def repay_type(self):
        """Gets the repay_type of this InlineResponse200207Rows.  # noqa: E501


        :return: The repay_type of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._repay_type

    @repay_type.setter
    def repay_type(self, repay_type):
        """Sets the repay_type of this InlineResponse200207Rows.


        :param repay_type: The repay_type of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if repay_type is None:
            raise ValueError("Invalid value for `repay_type`, must not be `None`")  # noqa: E501

        self._repay_type = repay_type

    @property
    def repay_status(self):
        """Gets the repay_status of this InlineResponse200207Rows.  # noqa: E501

        'repayType': '1' // 1 for 'repay with borrowed coin', 2 for 'repay with collateral' 'repayStatus': 'Repaid' // Repaid, Repaying, Failed  # noqa: E501

        :return: The repay_status of this InlineResponse200207Rows.  # noqa: E501
        :rtype: str
        """
        return self._repay_status

    @repay_status.setter
    def repay_status(self, repay_status):
        """Sets the repay_status of this InlineResponse200207Rows.

        'repayType': '1' // 1 for 'repay with borrowed coin', 2 for 'repay with collateral' 'repayStatus': 'Repaid' // Repaid, Repaying, Failed  # noqa: E501

        :param repay_status: The repay_status of this InlineResponse200207Rows.  # noqa: E501
        :type: str
        """
        if repay_status is None:
            raise ValueError("Invalid value for `repay_status`, must not be `None`")  # noqa: E501

        self._repay_status = repay_status

    @property
    def repay_time(self):
        """Gets the repay_time of this InlineResponse200207Rows.  # noqa: E501


        :return: The repay_time of this InlineResponse200207Rows.  # noqa: E501
        :rtype: int
        """
        return self._repay_time

    @repay_time.setter
    def repay_time(self, repay_time):
        """Sets the repay_time of this InlineResponse200207Rows.


        :param repay_time: The repay_time of this InlineResponse200207Rows.  # noqa: E501
        :type: int
        """
        if repay_time is None:
            raise ValueError("Invalid value for `repay_time`, must not be `None`")  # noqa: E501

        self._repay_time = repay_time

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse200207Rows.  # noqa: E501


        :return: The order_id of this InlineResponse200207Rows.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse200207Rows.


        :param order_id: The order_id of this InlineResponse200207Rows.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

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
        if issubclass(InlineResponse200207Rows, dict):
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
        if not isinstance(other, InlineResponse200207Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
