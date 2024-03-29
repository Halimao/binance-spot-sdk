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

class AggTrade(object):
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
        'a': 'int',
        'p': 'str',
        'q': 'str',
        'f': 'int',
        'l': 'int',
        't': 'bool',
        'm': 'bool',
        'm': 'bool'
    }

    attribute_map = {
        'a': 'a',
        'p': 'p',
        'q': 'q',
        'f': 'f',
        'l': 'l',
        't': 'T',
        'm': 'm',
        'm': 'M'
    }

    def __init__(self, a=None, p=None, q=None, f=None, l=None, t=None, m=None, m=None):  # noqa: E501
        """AggTrade - a model defined in Swagger"""  # noqa: E501
        self._a = None
        self._p = None
        self._q = None
        self._f = None
        self._l = None
        self._t = None
        self._m = None
        self._m = None
        self.discriminator = None
        self.a = a
        self.p = p
        self.q = q
        self.f = f
        self.l = l
        self.t = t
        self.m = m
        self.m = m

    @property
    def a(self):
        """Gets the a of this AggTrade.  # noqa: E501

        Aggregate tradeId  # noqa: E501

        :return: The a of this AggTrade.  # noqa: E501
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this AggTrade.

        Aggregate tradeId  # noqa: E501

        :param a: The a of this AggTrade.  # noqa: E501
        :type: int
        """
        if a is None:
            raise ValueError("Invalid value for `a`, must not be `None`")  # noqa: E501

        self._a = a

    @property
    def p(self):
        """Gets the p of this AggTrade.  # noqa: E501

        Price  # noqa: E501

        :return: The p of this AggTrade.  # noqa: E501
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this AggTrade.

        Price  # noqa: E501

        :param p: The p of this AggTrade.  # noqa: E501
        :type: str
        """
        if p is None:
            raise ValueError("Invalid value for `p`, must not be `None`")  # noqa: E501

        self._p = p

    @property
    def q(self):
        """Gets the q of this AggTrade.  # noqa: E501

        Quantity  # noqa: E501

        :return: The q of this AggTrade.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this AggTrade.

        Quantity  # noqa: E501

        :param q: The q of this AggTrade.  # noqa: E501
        :type: str
        """
        if q is None:
            raise ValueError("Invalid value for `q`, must not be `None`")  # noqa: E501

        self._q = q

    @property
    def f(self):
        """Gets the f of this AggTrade.  # noqa: E501

        First tradeId  # noqa: E501

        :return: The f of this AggTrade.  # noqa: E501
        :rtype: int
        """
        return self._f

    @f.setter
    def f(self, f):
        """Sets the f of this AggTrade.

        First tradeId  # noqa: E501

        :param f: The f of this AggTrade.  # noqa: E501
        :type: int
        """
        if f is None:
            raise ValueError("Invalid value for `f`, must not be `None`")  # noqa: E501

        self._f = f

    @property
    def l(self):
        """Gets the l of this AggTrade.  # noqa: E501

        Last tradeId  # noqa: E501

        :return: The l of this AggTrade.  # noqa: E501
        :rtype: int
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this AggTrade.

        Last tradeId  # noqa: E501

        :param l: The l of this AggTrade.  # noqa: E501
        :type: int
        """
        if l is None:
            raise ValueError("Invalid value for `l`, must not be `None`")  # noqa: E501

        self._l = l

    @property
    def t(self):
        """Gets the t of this AggTrade.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The t of this AggTrade.  # noqa: E501
        :rtype: bool
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this AggTrade.

        Timestamp  # noqa: E501

        :param t: The t of this AggTrade.  # noqa: E501
        :type: bool
        """
        if t is None:
            raise ValueError("Invalid value for `t`, must not be `None`")  # noqa: E501

        self._t = t

    @property
    def m(self):
        """Gets the m of this AggTrade.  # noqa: E501

        Was the buyer the maker?  # noqa: E501

        :return: The m of this AggTrade.  # noqa: E501
        :rtype: bool
        """
        return self._m

    @m.setter
    def m(self, m):
        """Sets the m of this AggTrade.

        Was the buyer the maker?  # noqa: E501

        :param m: The m of this AggTrade.  # noqa: E501
        :type: bool
        """
        if m is None:
            raise ValueError("Invalid value for `m`, must not be `None`")  # noqa: E501

        self._m = m

    @property
    def m(self):
        """Gets the m of this AggTrade.  # noqa: E501

        Was the trade the best price match?  # noqa: E501

        :return: The m of this AggTrade.  # noqa: E501
        :rtype: bool
        """
        return self._m

    @m.setter
    def m(self, m):
        """Sets the m of this AggTrade.

        Was the trade the best price match?  # noqa: E501

        :param m: The m of this AggTrade.  # noqa: E501
        :type: bool
        """
        if m is None:
            raise ValueError("Invalid value for `m`, must not be `None`")  # noqa: E501

        self._m = m

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
        if issubclass(AggTrade, dict):
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
        if not isinstance(other, AggTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
