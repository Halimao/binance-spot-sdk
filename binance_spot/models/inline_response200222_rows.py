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

class InlineResponse200222Rows(object):
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
        'collateral_coin': 'str',
        'initial_ltv': 'str',
        'margin_call_ltv': 'str',
        'liquidation_ltv': 'str',
        'max_limit': 'str'
    }

    attribute_map = {
        'collateral_coin': 'collateralCoin',
        'initial_ltv': 'initialLTV',
        'margin_call_ltv': 'marginCallLTV',
        'liquidation_ltv': 'liquidationLTV',
        'max_limit': 'maxLimit'
    }

    def __init__(self, collateral_coin=None, initial_ltv=None, margin_call_ltv=None, liquidation_ltv=None, max_limit=None):  # noqa: E501
        """InlineResponse200222Rows - a model defined in Swagger"""  # noqa: E501
        self._collateral_coin = None
        self._initial_ltv = None
        self._margin_call_ltv = None
        self._liquidation_ltv = None
        self._max_limit = None
        self.discriminator = None
        self.collateral_coin = collateral_coin
        self.initial_ltv = initial_ltv
        self.margin_call_ltv = margin_call_ltv
        self.liquidation_ltv = liquidation_ltv
        self.max_limit = max_limit

    @property
    def collateral_coin(self):
        """Gets the collateral_coin of this InlineResponse200222Rows.  # noqa: E501


        :return: The collateral_coin of this InlineResponse200222Rows.  # noqa: E501
        :rtype: str
        """
        return self._collateral_coin

    @collateral_coin.setter
    def collateral_coin(self, collateral_coin):
        """Sets the collateral_coin of this InlineResponse200222Rows.


        :param collateral_coin: The collateral_coin of this InlineResponse200222Rows.  # noqa: E501
        :type: str
        """
        if collateral_coin is None:
            raise ValueError("Invalid value for `collateral_coin`, must not be `None`")  # noqa: E501

        self._collateral_coin = collateral_coin

    @property
    def initial_ltv(self):
        """Gets the initial_ltv of this InlineResponse200222Rows.  # noqa: E501


        :return: The initial_ltv of this InlineResponse200222Rows.  # noqa: E501
        :rtype: str
        """
        return self._initial_ltv

    @initial_ltv.setter
    def initial_ltv(self, initial_ltv):
        """Sets the initial_ltv of this InlineResponse200222Rows.


        :param initial_ltv: The initial_ltv of this InlineResponse200222Rows.  # noqa: E501
        :type: str
        """
        if initial_ltv is None:
            raise ValueError("Invalid value for `initial_ltv`, must not be `None`")  # noqa: E501

        self._initial_ltv = initial_ltv

    @property
    def margin_call_ltv(self):
        """Gets the margin_call_ltv of this InlineResponse200222Rows.  # noqa: E501


        :return: The margin_call_ltv of this InlineResponse200222Rows.  # noqa: E501
        :rtype: str
        """
        return self._margin_call_ltv

    @margin_call_ltv.setter
    def margin_call_ltv(self, margin_call_ltv):
        """Sets the margin_call_ltv of this InlineResponse200222Rows.


        :param margin_call_ltv: The margin_call_ltv of this InlineResponse200222Rows.  # noqa: E501
        :type: str
        """
        if margin_call_ltv is None:
            raise ValueError("Invalid value for `margin_call_ltv`, must not be `None`")  # noqa: E501

        self._margin_call_ltv = margin_call_ltv

    @property
    def liquidation_ltv(self):
        """Gets the liquidation_ltv of this InlineResponse200222Rows.  # noqa: E501


        :return: The liquidation_ltv of this InlineResponse200222Rows.  # noqa: E501
        :rtype: str
        """
        return self._liquidation_ltv

    @liquidation_ltv.setter
    def liquidation_ltv(self, liquidation_ltv):
        """Sets the liquidation_ltv of this InlineResponse200222Rows.


        :param liquidation_ltv: The liquidation_ltv of this InlineResponse200222Rows.  # noqa: E501
        :type: str
        """
        if liquidation_ltv is None:
            raise ValueError("Invalid value for `liquidation_ltv`, must not be `None`")  # noqa: E501

        self._liquidation_ltv = liquidation_ltv

    @property
    def max_limit(self):
        """Gets the max_limit of this InlineResponse200222Rows.  # noqa: E501


        :return: The max_limit of this InlineResponse200222Rows.  # noqa: E501
        :rtype: str
        """
        return self._max_limit

    @max_limit.setter
    def max_limit(self, max_limit):
        """Sets the max_limit of this InlineResponse200222Rows.


        :param max_limit: The max_limit of this InlineResponse200222Rows.  # noqa: E501
        :type: str
        """
        if max_limit is None:
            raise ValueError("Invalid value for `max_limit`, must not be `None`")  # noqa: E501

        self._max_limit = max_limit

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
        if issubclass(InlineResponse200222Rows, dict):
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
        if not isinstance(other, InlineResponse200222Rows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
