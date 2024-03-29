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

class SubAccountUSDTFuturesDetails(object):
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
        'future_account_resp': 'SubAccountUSDTFuturesDetailsFutureAccountResp'
    }

    attribute_map = {
        'future_account_resp': 'futureAccountResp'
    }

    def __init__(self, future_account_resp=None):  # noqa: E501
        """SubAccountUSDTFuturesDetails - a model defined in Swagger"""  # noqa: E501
        self._future_account_resp = None
        self.discriminator = None
        self.future_account_resp = future_account_resp

    @property
    def future_account_resp(self):
        """Gets the future_account_resp of this SubAccountUSDTFuturesDetails.  # noqa: E501


        :return: The future_account_resp of this SubAccountUSDTFuturesDetails.  # noqa: E501
        :rtype: SubAccountUSDTFuturesDetailsFutureAccountResp
        """
        return self._future_account_resp

    @future_account_resp.setter
    def future_account_resp(self, future_account_resp):
        """Sets the future_account_resp of this SubAccountUSDTFuturesDetails.


        :param future_account_resp: The future_account_resp of this SubAccountUSDTFuturesDetails.  # noqa: E501
        :type: SubAccountUSDTFuturesDetailsFutureAccountResp
        """
        if future_account_resp is None:
            raise ValueError("Invalid value for `future_account_resp`, must not be `None`")  # noqa: E501

        self._future_account_resp = future_account_resp

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
        if issubclass(SubAccountUSDTFuturesDetails, dict):
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
        if not isinstance(other, SubAccountUSDTFuturesDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
