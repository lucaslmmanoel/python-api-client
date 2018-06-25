# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Coloring(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'str',
        'components': 'list[Component]'
    }

    attribute_map = {
        'color': 'color',
        'components': 'components'
    }

    def __init__(self, color=None, components=None):  # noqa: E501
        """Coloring - a model defined in OpenAPI"""  # noqa: E501

        self._color = None
        self._components = None
        self.discriminator = None

        self.color = color
        self.components = components

    @property
    def color(self):
        """Gets the color of this Coloring.  # noqa: E501


        :return: The color of this Coloring.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Coloring.


        :param color: The color of this Coloring.  # noqa: E501
        :type: str
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501
        if color is not None and len(color) > 255:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `255`")  # noqa: E501
        if color is not None and len(color) < 1:
            raise ValueError("Invalid value for `color`, length must be greater than or equal to `1`")  # noqa: E501

        self._color = color

    @property
    def components(self):
        """Gets the components of this Coloring.  # noqa: E501


        :return: The components of this Coloring.  # noqa: E501
        :rtype: list[Component]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Coloring.


        :param components: The components of this Coloring.  # noqa: E501
        :type: list[Component]
        """
        if components is None:
            raise ValueError("Invalid value for `components`, must not be `None`")  # noqa: E501

        self._components = components

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Coloring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
