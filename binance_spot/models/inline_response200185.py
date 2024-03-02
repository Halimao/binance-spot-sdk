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

class InlineResponse200185(object):
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
        'pool_id': 'int',
        'pool_nmae': 'str',
        'update_time': 'int',
        'liquidity': 'Sapiv1bswappoolConfigureLiquidity',
        'asset_configure': 'Sapiv1bswappoolConfigureAssetConfigure'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'pool_nmae': 'poolNmae',
        'update_time': 'updateTime',
        'liquidity': 'liquidity',
        'asset_configure': 'assetConfigure'
    }

    def __init__(self, pool_id=None, pool_nmae=None, update_time=None, liquidity=None, asset_configure=None):  # noqa: E501
        """InlineResponse200185 - a model defined in Swagger"""  # noqa: E501
        self._pool_id = None
        self._pool_nmae = None
        self._update_time = None
        self._liquidity = None
        self._asset_configure = None
        self.discriminator = None
        self.pool_id = pool_id
        self.pool_nmae = pool_nmae
        self.update_time = update_time
        self.liquidity = liquidity
        self.asset_configure = asset_configure

    @property
    def pool_id(self):
        """Gets the pool_id of this InlineResponse200185.  # noqa: E501


        :return: The pool_id of this InlineResponse200185.  # noqa: E501
        :rtype: int
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this InlineResponse200185.


        :param pool_id: The pool_id of this InlineResponse200185.  # noqa: E501
        :type: int
        """
        if pool_id is None:
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def pool_nmae(self):
        """Gets the pool_nmae of this InlineResponse200185.  # noqa: E501


        :return: The pool_nmae of this InlineResponse200185.  # noqa: E501
        :rtype: str
        """
        return self._pool_nmae

    @pool_nmae.setter
    def pool_nmae(self, pool_nmae):
        """Sets the pool_nmae of this InlineResponse200185.


        :param pool_nmae: The pool_nmae of this InlineResponse200185.  # noqa: E501
        :type: str
        """
        if pool_nmae is None:
            raise ValueError("Invalid value for `pool_nmae`, must not be `None`")  # noqa: E501

        self._pool_nmae = pool_nmae

    @property
    def update_time(self):
        """Gets the update_time of this InlineResponse200185.  # noqa: E501


        :return: The update_time of this InlineResponse200185.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this InlineResponse200185.


        :param update_time: The update_time of this InlineResponse200185.  # noqa: E501
        :type: int
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def liquidity(self):
        """Gets the liquidity of this InlineResponse200185.  # noqa: E501


        :return: The liquidity of this InlineResponse200185.  # noqa: E501
        :rtype: Sapiv1bswappoolConfigureLiquidity
        """
        return self._liquidity

    @liquidity.setter
    def liquidity(self, liquidity):
        """Sets the liquidity of this InlineResponse200185.


        :param liquidity: The liquidity of this InlineResponse200185.  # noqa: E501
        :type: Sapiv1bswappoolConfigureLiquidity
        """
        if liquidity is None:
            raise ValueError("Invalid value for `liquidity`, must not be `None`")  # noqa: E501

        self._liquidity = liquidity

    @property
    def asset_configure(self):
        """Gets the asset_configure of this InlineResponse200185.  # noqa: E501


        :return: The asset_configure of this InlineResponse200185.  # noqa: E501
        :rtype: Sapiv1bswappoolConfigureAssetConfigure
        """
        return self._asset_configure

    @asset_configure.setter
    def asset_configure(self, asset_configure):
        """Sets the asset_configure of this InlineResponse200185.


        :param asset_configure: The asset_configure of this InlineResponse200185.  # noqa: E501
        :type: Sapiv1bswappoolConfigureAssetConfigure
        """
        if asset_configure is None:
            raise ValueError("Invalid value for `asset_configure`, must not be `None`")  # noqa: E501

        self._asset_configure = asset_configure

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
        if issubclass(InlineResponse200185, dict):
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
        if not isinstance(other, InlineResponse200185):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other