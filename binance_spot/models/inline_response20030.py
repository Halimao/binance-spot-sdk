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

class InlineResponse20030(object):
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
        'order_list_id': 'int',
        'contingency_type': 'str',
        'list_status_type': 'str',
        'list_order_status': 'str',
        'list_client_order_id': 'str',
        'transaction_time': 'int',
        'symbol': 'str',
        'margin_buy_borrow_amount': 'str',
        'margin_buy_borrow_asset': 'str',
        'is_isolated': 'bool',
        'orders': 'list[OcoOrderOrders]',
        'order_reports': 'list[InlineResponse20030OrderReports]'
    }

    attribute_map = {
        'order_list_id': 'orderListId',
        'contingency_type': 'contingencyType',
        'list_status_type': 'listStatusType',
        'list_order_status': 'listOrderStatus',
        'list_client_order_id': 'listClientOrderId',
        'transaction_time': 'transactionTime',
        'symbol': 'symbol',
        'margin_buy_borrow_amount': 'marginBuyBorrowAmount',
        'margin_buy_borrow_asset': 'marginBuyBorrowAsset',
        'is_isolated': 'isIsolated',
        'orders': 'orders',
        'order_reports': 'orderReports'
    }

    def __init__(self, order_list_id=None, contingency_type=None, list_status_type=None, list_order_status=None, list_client_order_id=None, transaction_time=None, symbol=None, margin_buy_borrow_amount=None, margin_buy_borrow_asset=None, is_isolated=None, orders=None, order_reports=None):  # noqa: E501
        """InlineResponse20030 - a model defined in Swagger"""  # noqa: E501
        self._order_list_id = None
        self._contingency_type = None
        self._list_status_type = None
        self._list_order_status = None
        self._list_client_order_id = None
        self._transaction_time = None
        self._symbol = None
        self._margin_buy_borrow_amount = None
        self._margin_buy_borrow_asset = None
        self._is_isolated = None
        self._orders = None
        self._order_reports = None
        self.discriminator = None
        self.order_list_id = order_list_id
        self.contingency_type = contingency_type
        self.list_status_type = list_status_type
        self.list_order_status = list_order_status
        self.list_client_order_id = list_client_order_id
        self.transaction_time = transaction_time
        self.symbol = symbol
        self.margin_buy_borrow_amount = margin_buy_borrow_amount
        self.margin_buy_borrow_asset = margin_buy_borrow_asset
        self.is_isolated = is_isolated
        self.orders = orders
        self.order_reports = order_reports

    @property
    def order_list_id(self):
        """Gets the order_list_id of this InlineResponse20030.  # noqa: E501


        :return: The order_list_id of this InlineResponse20030.  # noqa: E501
        :rtype: int
        """
        return self._order_list_id

    @order_list_id.setter
    def order_list_id(self, order_list_id):
        """Sets the order_list_id of this InlineResponse20030.


        :param order_list_id: The order_list_id of this InlineResponse20030.  # noqa: E501
        :type: int
        """
        if order_list_id is None:
            raise ValueError("Invalid value for `order_list_id`, must not be `None`")  # noqa: E501

        self._order_list_id = order_list_id

    @property
    def contingency_type(self):
        """Gets the contingency_type of this InlineResponse20030.  # noqa: E501


        :return: The contingency_type of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._contingency_type

    @contingency_type.setter
    def contingency_type(self, contingency_type):
        """Sets the contingency_type of this InlineResponse20030.


        :param contingency_type: The contingency_type of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if contingency_type is None:
            raise ValueError("Invalid value for `contingency_type`, must not be `None`")  # noqa: E501

        self._contingency_type = contingency_type

    @property
    def list_status_type(self):
        """Gets the list_status_type of this InlineResponse20030.  # noqa: E501


        :return: The list_status_type of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._list_status_type

    @list_status_type.setter
    def list_status_type(self, list_status_type):
        """Sets the list_status_type of this InlineResponse20030.


        :param list_status_type: The list_status_type of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if list_status_type is None:
            raise ValueError("Invalid value for `list_status_type`, must not be `None`")  # noqa: E501

        self._list_status_type = list_status_type

    @property
    def list_order_status(self):
        """Gets the list_order_status of this InlineResponse20030.  # noqa: E501


        :return: The list_order_status of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._list_order_status

    @list_order_status.setter
    def list_order_status(self, list_order_status):
        """Sets the list_order_status of this InlineResponse20030.


        :param list_order_status: The list_order_status of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if list_order_status is None:
            raise ValueError("Invalid value for `list_order_status`, must not be `None`")  # noqa: E501

        self._list_order_status = list_order_status

    @property
    def list_client_order_id(self):
        """Gets the list_client_order_id of this InlineResponse20030.  # noqa: E501


        :return: The list_client_order_id of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._list_client_order_id

    @list_client_order_id.setter
    def list_client_order_id(self, list_client_order_id):
        """Sets the list_client_order_id of this InlineResponse20030.


        :param list_client_order_id: The list_client_order_id of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if list_client_order_id is None:
            raise ValueError("Invalid value for `list_client_order_id`, must not be `None`")  # noqa: E501

        self._list_client_order_id = list_client_order_id

    @property
    def transaction_time(self):
        """Gets the transaction_time of this InlineResponse20030.  # noqa: E501


        :return: The transaction_time of this InlineResponse20030.  # noqa: E501
        :rtype: int
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this InlineResponse20030.


        :param transaction_time: The transaction_time of this InlineResponse20030.  # noqa: E501
        :type: int
        """
        if transaction_time is None:
            raise ValueError("Invalid value for `transaction_time`, must not be `None`")  # noqa: E501

        self._transaction_time = transaction_time

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse20030.  # noqa: E501


        :return: The symbol of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse20030.


        :param symbol: The symbol of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def margin_buy_borrow_amount(self):
        """Gets the margin_buy_borrow_amount of this InlineResponse20030.  # noqa: E501

        will not return if no margin trade happens  # noqa: E501

        :return: The margin_buy_borrow_amount of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._margin_buy_borrow_amount

    @margin_buy_borrow_amount.setter
    def margin_buy_borrow_amount(self, margin_buy_borrow_amount):
        """Sets the margin_buy_borrow_amount of this InlineResponse20030.

        will not return if no margin trade happens  # noqa: E501

        :param margin_buy_borrow_amount: The margin_buy_borrow_amount of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if margin_buy_borrow_amount is None:
            raise ValueError("Invalid value for `margin_buy_borrow_amount`, must not be `None`")  # noqa: E501

        self._margin_buy_borrow_amount = margin_buy_borrow_amount

    @property
    def margin_buy_borrow_asset(self):
        """Gets the margin_buy_borrow_asset of this InlineResponse20030.  # noqa: E501

        will not return if no margin trade happens  # noqa: E501

        :return: The margin_buy_borrow_asset of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._margin_buy_borrow_asset

    @margin_buy_borrow_asset.setter
    def margin_buy_borrow_asset(self, margin_buy_borrow_asset):
        """Sets the margin_buy_borrow_asset of this InlineResponse20030.

        will not return if no margin trade happens  # noqa: E501

        :param margin_buy_borrow_asset: The margin_buy_borrow_asset of this InlineResponse20030.  # noqa: E501
        :type: str
        """
        if margin_buy_borrow_asset is None:
            raise ValueError("Invalid value for `margin_buy_borrow_asset`, must not be `None`")  # noqa: E501

        self._margin_buy_borrow_asset = margin_buy_borrow_asset

    @property
    def is_isolated(self):
        """Gets the is_isolated of this InlineResponse20030.  # noqa: E501


        :return: The is_isolated of this InlineResponse20030.  # noqa: E501
        :rtype: bool
        """
        return self._is_isolated

    @is_isolated.setter
    def is_isolated(self, is_isolated):
        """Sets the is_isolated of this InlineResponse20030.


        :param is_isolated: The is_isolated of this InlineResponse20030.  # noqa: E501
        :type: bool
        """
        if is_isolated is None:
            raise ValueError("Invalid value for `is_isolated`, must not be `None`")  # noqa: E501

        self._is_isolated = is_isolated

    @property
    def orders(self):
        """Gets the orders of this InlineResponse20030.  # noqa: E501


        :return: The orders of this InlineResponse20030.  # noqa: E501
        :rtype: list[OcoOrderOrders]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this InlineResponse20030.


        :param orders: The orders of this InlineResponse20030.  # noqa: E501
        :type: list[OcoOrderOrders]
        """
        if orders is None:
            raise ValueError("Invalid value for `orders`, must not be `None`")  # noqa: E501

        self._orders = orders

    @property
    def order_reports(self):
        """Gets the order_reports of this InlineResponse20030.  # noqa: E501


        :return: The order_reports of this InlineResponse20030.  # noqa: E501
        :rtype: list[InlineResponse20030OrderReports]
        """
        return self._order_reports

    @order_reports.setter
    def order_reports(self, order_reports):
        """Sets the order_reports of this InlineResponse20030.


        :param order_reports: The order_reports of this InlineResponse20030.  # noqa: E501
        :type: list[InlineResponse20030OrderReports]
        """
        if order_reports is None:
            raise ValueError("Invalid value for `order_reports`, must not be `None`")  # noqa: E501

        self._order_reports = order_reports

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
        if issubclass(InlineResponse20030, dict):
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
        if not isinstance(other, InlineResponse20030):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
