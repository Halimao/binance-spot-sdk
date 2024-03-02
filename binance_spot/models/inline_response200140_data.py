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

class InlineResponse200140Data(object):
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
        'worker_datas': 'list[InlineResponse200140DataWorkerDatas]',
        'total_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'worker_datas': 'workerDatas',
        'total_num': 'totalNum',
        'page_size': 'pageSize'
    }

    def __init__(self, worker_datas=None, total_num=None, page_size=None):  # noqa: E501
        """InlineResponse200140Data - a model defined in Swagger"""  # noqa: E501
        self._worker_datas = None
        self._total_num = None
        self._page_size = None
        self.discriminator = None
        self.worker_datas = worker_datas
        self.total_num = total_num
        self.page_size = page_size

    @property
    def worker_datas(self):
        """Gets the worker_datas of this InlineResponse200140Data.  # noqa: E501


        :return: The worker_datas of this InlineResponse200140Data.  # noqa: E501
        :rtype: list[InlineResponse200140DataWorkerDatas]
        """
        return self._worker_datas

    @worker_datas.setter
    def worker_datas(self, worker_datas):
        """Sets the worker_datas of this InlineResponse200140Data.


        :param worker_datas: The worker_datas of this InlineResponse200140Data.  # noqa: E501
        :type: list[InlineResponse200140DataWorkerDatas]
        """
        if worker_datas is None:
            raise ValueError("Invalid value for `worker_datas`, must not be `None`")  # noqa: E501

        self._worker_datas = worker_datas

    @property
    def total_num(self):
        """Gets the total_num of this InlineResponse200140Data.  # noqa: E501


        :return: The total_num of this InlineResponse200140Data.  # noqa: E501
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this InlineResponse200140Data.


        :param total_num: The total_num of this InlineResponse200140Data.  # noqa: E501
        :type: int
        """
        if total_num is None:
            raise ValueError("Invalid value for `total_num`, must not be `None`")  # noqa: E501

        self._total_num = total_num

    @property
    def page_size(self):
        """Gets the page_size of this InlineResponse200140Data.  # noqa: E501


        :return: The page_size of this InlineResponse200140Data.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineResponse200140Data.


        :param page_size: The page_size of this InlineResponse200140Data.  # noqa: E501
        :type: int
        """
        if page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

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
        if issubclass(InlineResponse200140Data, dict):
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
        if not isinstance(other, InlineResponse200140Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
