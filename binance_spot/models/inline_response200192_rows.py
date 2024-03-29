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

class InlineResponse200192Rows(object):
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
        'order_id': 'int',
        'loan_coin': 'str',
        'total_debt': 'str',
        'residual_interest': 'str',
        'collateral_account_id': 'str',
        'collateral_coin': 'str',
        'collateral_value': 'str',
        'total_collateral_value_after_haircut': 'str',
        'locked_collateral_value': 'str',
        'current_ltv': 'str',
        'expiration_time': 'int',
        'loan_date': 'str',
        'loan_rate': 'str',
        'loan_term': 'str'
    }

    attribute_map = {
        'order_id': 'orderId',
        'loan_coin': 'loanCoin',
        'total_debt': 'totalDebt',
        'residual_interest': 'residualInterest',
        'collateral_account_id': 'collateralAccountId',
        'collateral_coin': 'collateralCoin',
        'collateral_value': 'collateralValue',
        'total_collateral_value_after_haircut': 'totalCollateralValueAfterHaircut',
        'locked_collateral_value': 'lockedCollateralValue',
        'current_ltv': 'currentLTV',
        'expiration_time': 'expirationTime',
        'loan_date': 'loanDate',
        'loan_rate': 'loanRate',
        'loan_term': 'loanTerm'
    }

    def __init__(self, order_id=None, loan_coin=None, total_debt=None, residual_interest=None, collateral_account_id=None, collateral_coin=None, collateral_value=None, total_collateral_value_after_haircut=None, locked_collateral_value=None, current_ltv=None, expiration_time=None, loan_date=None, loan_rate=None, loan_term=None):  # noqa: E501
        """InlineResponse200192Rows - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._loan_coin = None
        self._total_debt = None
        self._residual_interest = None
        self._collateral_account_id = None
        self._collateral_coin = None
        self._collateral_value = None
        self._total_collateral_value_after_haircut = None
        self._locked_collateral_value = None
        self._current_ltv = None
        self._expiration_time = None
        self._loan_date = None
        self._loan_rate = None
        self._loan_term = None
        self.discriminator = None
        self.order_id = order_id
        self.loan_coin = loan_coin
        self.total_debt = total_debt
        self.residual_interest = residual_interest
        self.collateral_account_id = collateral_account_id
        self.collateral_coin = collateral_coin
        self.collateral_value = collateral_value
        if total_collateral_value_after_haircut is not None:
            self.total_collateral_value_after_haircut = total_collateral_value_after_haircut
        if locked_collateral_value is not None:
            self.locked_collateral_value = locked_collateral_value
        self.current_ltv = current_ltv
        self.expiration_time = expiration_time
        self.loan_date = loan_date
        self.loan_rate = loan_rate
        self.loan_term = loan_term

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse200192Rows.  # noqa: E501


        :return: The order_id of this InlineResponse200192Rows.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse200192Rows.


        :param order_id: The order_id of this InlineResponse200192Rows.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def loan_coin(self):
        """Gets the loan_coin of this InlineResponse200192Rows.  # noqa: E501


        :return: The loan_coin of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_coin

    @loan_coin.setter
    def loan_coin(self, loan_coin):
        """Sets the loan_coin of this InlineResponse200192Rows.


        :param loan_coin: The loan_coin of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if loan_coin is None:
            raise ValueError("Invalid value for `loan_coin`, must not be `None`")  # noqa: E501

        self._loan_coin = loan_coin

    @property
    def total_debt(self):
        """Gets the total_debt of this InlineResponse200192Rows.  # noqa: E501


        :return: The total_debt of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._total_debt

    @total_debt.setter
    def total_debt(self, total_debt):
        """Sets the total_debt of this InlineResponse200192Rows.


        :param total_debt: The total_debt of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if total_debt is None:
            raise ValueError("Invalid value for `total_debt`, must not be `None`")  # noqa: E501

        self._total_debt = total_debt

    @property
    def residual_interest(self):
        """Gets the residual_interest of this InlineResponse200192Rows.  # noqa: E501


        :return: The residual_interest of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._residual_interest

    @residual_interest.setter
    def residual_interest(self, residual_interest):
        """Sets the residual_interest of this InlineResponse200192Rows.


        :param residual_interest: The residual_interest of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if residual_interest is None:
            raise ValueError("Invalid value for `residual_interest`, must not be `None`")  # noqa: E501

        self._residual_interest = residual_interest

    @property
    def collateral_account_id(self):
        """Gets the collateral_account_id of this InlineResponse200192Rows.  # noqa: E501


        :return: The collateral_account_id of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_account_id

    @collateral_account_id.setter
    def collateral_account_id(self, collateral_account_id):
        """Sets the collateral_account_id of this InlineResponse200192Rows.


        :param collateral_account_id: The collateral_account_id of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if collateral_account_id is None:
            raise ValueError("Invalid value for `collateral_account_id`, must not be `None`")  # noqa: E501

        self._collateral_account_id = collateral_account_id

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200192Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200192Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def collateral_value(self):
        """Gets the collateral_value of this InlineResponse200192Rows.  # noqa: E501

        locked collateral value shown in USD value  # noqa: E501

        :return: The collateral_value of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_value

    @collateral_value.setter
    def collateral_value(self, collateral_value):
        """Sets the collateral_value of this InlineResponse200192Rows.

        locked collateral value shown in USD value  # noqa: E501

        :param collateral_value: The collateral_value of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if collateral_value is None:
            raise ValueError("Invalid value for `collateral_value`, must not be `None`")  # noqa: E501

        self._collateral_value = collateral_value

    @property
    def total_collateral_value_after_haircut(self):
        """Gets the total_collateral_value_after_haircut of this InlineResponse200192Rows.  # noqa: E501


        :return: The total_collateral_value_after_haircut of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._total_collateral_value_after_haircut

    @total_collateral_value_after_haircut.setter
    def total_collateral_value_after_haircut(self, total_collateral_value_after_haircut):
        """Sets the total_collateral_value_after_haircut of this InlineResponse200192Rows.


        :param total_collateral_value_after_haircut: The total_collateral_value_after_haircut of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """

        self._total_collateral_value_after_haircut = total_collateral_value_after_haircut

    @property
    def locked_collateral_value(self):
        """Gets the locked_collateral_value of this InlineResponse200192Rows.  # noqa: E501


        :return: The locked_collateral_value of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._locked_collateral_value

    @locked_collateral_value.setter
    def locked_collateral_value(self, locked_collateral_value):
        """Sets the locked_collateral_value of this InlineResponse200192Rows.


        :param locked_collateral_value: The locked_collateral_value of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """

        self._locked_collateral_value = locked_collateral_value

    @property
    def current_ltv(self):
        """Gets the current_ltv of this InlineResponse200192Rows.  # noqa: E501


        :return: The current_ltv of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._current_ltv

    @current_ltv.setter
    def current_ltv(self, current_ltv):
        """Sets the current_ltv of this InlineResponse200192Rows.


        :param current_ltv: The current_ltv of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if current_ltv is None:
            raise ValueError("Invalid value for `current_ltv`, must not be `None`")  # noqa: E501

        self._current_ltv = current_ltv

    @property
    def expiration_time(self):
        """Gets the expiration_time of this InlineResponse200192Rows.  # noqa: E501


        :return: The expiration_time of this InlineResponse200192Rows.  # noqa: E501
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this InlineResponse200192Rows.


        :param expiration_time: The expiration_time of this InlineResponse200192Rows.  # noqa: E501
        :type: int
        """
        if expiration_time is None:
            raise ValueError("Invalid value for `expiration_time`, must not be `None`")  # noqa: E501

        self._expiration_time = expiration_time

    @property
    def loan_date(self):
        """Gets the loan_date of this InlineResponse200192Rows.  # noqa: E501


        :return: The loan_date of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_date

    @loan_date.setter
    def loan_date(self, loan_date):
        """Sets the loan_date of this InlineResponse200192Rows.


        :param loan_date: The loan_date of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if loan_date is None:
            raise ValueError("Invalid value for `loan_date`, must not be `None`")  # noqa: E501

        self._loan_date = loan_date

    @property
    def loan_rate(self):
        """Gets the loan_rate of this InlineResponse200192Rows.  # noqa: E501


        :return: The loan_rate of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_rate

    @loan_rate.setter
    def loan_rate(self, loan_rate):
        """Sets the loan_rate of this InlineResponse200192Rows.


        :param loan_rate: The loan_rate of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if loan_rate is None:
            raise ValueError("Invalid value for `loan_rate`, must not be `None`")  # noqa: E501

        self._loan_rate = loan_rate

    @property
    def loan_term(self):
        """Gets the loan_term of this InlineResponse200192Rows.  # noqa: E501


        :return: The loan_term of this InlineResponse200192Rows.  # noqa: E501
        :rtype: str
        """
        return self._loan_term

    @loan_term.setter
    def loan_term(self, loan_term):
        """Sets the loan_term of this InlineResponse200192Rows.


        :param loan_term: The loan_term of this InlineResponse200192Rows.  # noqa: E501
        :type: str
        """
        if loan_term is None:
            raise ValueError("Invalid value for `loan_term`, must not be `None`")  # noqa: E501

        self._loan_term = loan_term

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
        if issubclass(InlineResponse200192Rows, dict):
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
        if not isinstance(other, InlineResponse200192Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
