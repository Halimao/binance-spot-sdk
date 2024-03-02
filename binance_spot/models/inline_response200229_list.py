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

class InlineResponse200229List(object):
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
        'quote_id': 'str',
        'order_id': 'int',
        'order_status': 'str',
        'from_asset': 'str',
        'from_amount': 'str',
        'to_asset': 'str',
        'to_amount': 'str',
        'ratio': 'str',
        'inverse_ratio': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'quote_id': 'quoteId',
        'order_id': 'orderId',
        'order_status': 'orderStatus',
        'from_asset': 'fromAsset',
        'from_amount': 'fromAmount',
        'to_asset': 'toAsset',
        'to_amount': 'toAmount',
        'ratio': 'ratio',
        'inverse_ratio': 'inverseRatio',
        'create_time': 'createTime'
    }

    def __init__(self, quote_id=None, order_id=None, order_status=None, from_asset=None, from_amount=None, to_asset=None, to_amount=None, ratio=None, inverse_ratio=None, create_time=None):  # noqa: E501
        """InlineResponse200229List - a model defined in Swagger"""  # noqa: E501
        self._quote_id = None
        self._order_id = None
        self._order_status = None
        self._from_asset = None
        self._from_amount = None
        self._to_asset = None
        self._to_amount = None
        self._ratio = None
        self._inverse_ratio = None
        self._create_time = None
        self.discriminator = None
        self.quote_id = quote_id
        self.order_id = order_id
        self.order_status = order_status
        self.from_asset = from_asset
        self.from_amount = from_amount
        self.to_asset = to_asset
        self.to_amount = to_amount
        self.ratio = ratio
        self.inverse_ratio = inverse_ratio
        self.create_time = create_time

    @property
    def quote_id(self):
        """Gets the quote_id of this InlineResponse200229List.  # noqa: E501


        :return: The quote_id of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this InlineResponse200229List.


        :param quote_id: The quote_id of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse200229List.  # noqa: E501


        :return: The order_id of this InlineResponse200229List.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse200229List.


        :param order_id: The order_id of this InlineResponse200229List.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_status(self):
        """Gets the order_status of this InlineResponse200229List.  # noqa: E501


        :return: The order_status of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this InlineResponse200229List.


        :param order_status: The order_status of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if order_status is None:
            raise ValueError("Invalid value for `order_status`, must not be `None`")  # noqa: E501

        self._order_status = order_status

    @property
    def from_asset(self):
        """Gets the from_asset of this InlineResponse200229List.  # noqa: E501


        :return: The from_asset of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._from_asset

    @from_asset.setter
    def from_asset(self, from_asset):
        """Sets the from_asset of this InlineResponse200229List.


        :param from_asset: The from_asset of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if from_asset is None:
            raise ValueError("Invalid value for `from_asset`, must not be `None`")  # noqa: E501

        self._from_asset = from_asset

    @property
    def from_amount(self):
        """Gets the from_amount of this InlineResponse200229List.  # noqa: E501


        :return: The from_amount of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._from_amount

    @from_amount.setter
    def from_amount(self, from_amount):
        """Sets the from_amount of this InlineResponse200229List.


        :param from_amount: The from_amount of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if from_amount is None:
            raise ValueError("Invalid value for `from_amount`, must not be `None`")  # noqa: E501

        self._from_amount = from_amount

    @property
    def to_asset(self):
        """Gets the to_asset of this InlineResponse200229List.  # noqa: E501


        :return: The to_asset of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._to_asset

    @to_asset.setter
    def to_asset(self, to_asset):
        """Sets the to_asset of this InlineResponse200229List.


        :param to_asset: The to_asset of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if to_asset is None:
            raise ValueError("Invalid value for `to_asset`, must not be `None`")  # noqa: E501

        self._to_asset = to_asset

    @property
    def to_amount(self):
        """Gets the to_amount of this InlineResponse200229List.  # noqa: E501


        :return: The to_amount of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._to_amount

    @to_amount.setter
    def to_amount(self, to_amount):
        """Sets the to_amount of this InlineResponse200229List.


        :param to_amount: The to_amount of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if to_amount is None:
            raise ValueError("Invalid value for `to_amount`, must not be `None`")  # noqa: E501

        self._to_amount = to_amount

    @property
    def ratio(self):
        """Gets the ratio of this InlineResponse200229List.  # noqa: E501

        price ratio  # noqa: E501

        :return: The ratio of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this InlineResponse200229List.

        price ratio  # noqa: E501

        :param ratio: The ratio of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if ratio is None:
            raise ValueError("Invalid value for `ratio`, must not be `None`")  # noqa: E501

        self._ratio = ratio

    @property
    def inverse_ratio(self):
        """Gets the inverse_ratio of this InlineResponse200229List.  # noqa: E501

        inverse price  # noqa: E501

        :return: The inverse_ratio of this InlineResponse200229List.  # noqa: E501
        :rtype: str
        """
        return self._inverse_ratio

    @inverse_ratio.setter
    def inverse_ratio(self, inverse_ratio):
        """Sets the inverse_ratio of this InlineResponse200229List.

        inverse price  # noqa: E501

        :param inverse_ratio: The inverse_ratio of this InlineResponse200229List.  # noqa: E501
        :type: str
        """
        if inverse_ratio is None:
            raise ValueError("Invalid value for `inverse_ratio`, must not be `None`")  # noqa: E501

        self._inverse_ratio = inverse_ratio

    @property
    def create_time(self):
        """Gets the create_time of this InlineResponse200229List.  # noqa: E501


        :return: The create_time of this InlineResponse200229List.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InlineResponse200229List.


        :param create_time: The create_time of this InlineResponse200229List.  # noqa: E501
        :type: int
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

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
        if issubclass(InlineResponse200229List, dict):
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
        if not isinstance(other, InlineResponse200229List):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
