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

class InlineResponse20044UserAssetDribbletDetails(object):
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
        'trans_id': 'int',
        'service_charge_amount': 'str',
        'amount': 'str',
        'operate_time': 'int',
        'transfered_amount': 'str',
        'from_asset': 'str'
    }

    attribute_map = {
        'trans_id': 'transId',
        'service_charge_amount': 'serviceChargeAmount',
        'amount': 'amount',
        'operate_time': 'operateTime',
        'transfered_amount': 'transferedAmount',
        'from_asset': 'fromAsset'
    }

    def __init__(self, trans_id=None, service_charge_amount=None, amount=None, operate_time=None, transfered_amount=None, from_asset=None):  # noqa: E501
        """InlineResponse20044UserAssetDribbletDetails - a model defined in Swagger"""  # noqa: E501
        self._trans_id = None
        self._service_charge_amount = None
        self._amount = None
        self._operate_time = None
        self._transfered_amount = None
        self._from_asset = None
        self.discriminator = None
        self.trans_id = trans_id
        self.service_charge_amount = service_charge_amount
        self.amount = amount
        self.operate_time = operate_time
        self.transfered_amount = transfered_amount
        self.from_asset = from_asset

    @property
    def trans_id(self):
        """Gets the trans_id of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The trans_id of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: int
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this InlineResponse20044UserAssetDribbletDetails.


        :param trans_id: The trans_id of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: int
        """
        if trans_id is None:
            raise ValueError("Invalid value for `trans_id`, must not be `None`")  # noqa: E501

        self._trans_id = trans_id

    @property
    def service_charge_amount(self):
        """Gets the service_charge_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The service_charge_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: str
        """
        return self._service_charge_amount

    @service_charge_amount.setter
    def service_charge_amount(self, service_charge_amount):
        """Sets the service_charge_amount of this InlineResponse20044UserAssetDribbletDetails.


        :param service_charge_amount: The service_charge_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: str
        """
        if service_charge_amount is None:
            raise ValueError("Invalid value for `service_charge_amount`, must not be `None`")  # noqa: E501

        self._service_charge_amount = service_charge_amount

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20044UserAssetDribbletDetails.


        :param amount: The amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def operate_time(self):
        """Gets the operate_time of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The operate_time of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this InlineResponse20044UserAssetDribbletDetails.


        :param operate_time: The operate_time of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: int
        """
        if operate_time is None:
            raise ValueError("Invalid value for `operate_time`, must not be `None`")  # noqa: E501

        self._operate_time = operate_time

    @property
    def transfered_amount(self):
        """Gets the transfered_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The transfered_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: str
        """
        return self._transfered_amount

    @transfered_amount.setter
    def transfered_amount(self, transfered_amount):
        """Sets the transfered_amount of this InlineResponse20044UserAssetDribbletDetails.


        :param transfered_amount: The transfered_amount of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: str
        """
        if transfered_amount is None:
            raise ValueError("Invalid value for `transfered_amount`, must not be `None`")  # noqa: E501

        self._transfered_amount = transfered_amount

    @property
    def from_asset(self):
        """Gets the from_asset of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501


        :return: The from_asset of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :rtype: str
        """
        return self._from_asset

    @from_asset.setter
    def from_asset(self, from_asset):
        """Sets the from_asset of this InlineResponse20044UserAssetDribbletDetails.


        :param from_asset: The from_asset of this InlineResponse20044UserAssetDribbletDetails.  # noqa: E501
        :type: str
        """
        if from_asset is None:
            raise ValueError("Invalid value for `from_asset`, must not be `None`")  # noqa: E501

        self._from_asset = from_asset

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
        if issubclass(InlineResponse20044UserAssetDribbletDetails, dict):
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
        if not isinstance(other, InlineResponse20044UserAssetDribbletDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
