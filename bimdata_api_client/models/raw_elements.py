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


class RawElements(object):
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
        'units': 'list[RawUnit]',
        'definitions': 'list[RawDefinition]',
        'property_sets': 'list[RawPropertySet]',
        'classifications': 'list[Classification]',
        'elements': 'list[RawElement]'
    }

    attribute_map = {
        'units': 'units',
        'definitions': 'definitions',
        'property_sets': 'property_sets',
        'classifications': 'classifications',
        'elements': 'elements'
    }

    def __init__(self, units=None, definitions=None, property_sets=None, classifications=None, elements=None):  # noqa: E501
        """RawElements - a model defined in OpenAPI"""  # noqa: E501

        self._units = None
        self._definitions = None
        self._property_sets = None
        self._classifications = None
        self._elements = None
        self.discriminator = None

        if units is not None:
            self.units = units
        if definitions is not None:
            self.definitions = definitions
        if property_sets is not None:
            self.property_sets = property_sets
        if classifications is not None:
            self.classifications = classifications
        self.elements = elements

    @property
    def units(self):
        """Gets the units of this RawElements.  # noqa: E501


        :return: The units of this RawElements.  # noqa: E501
        :rtype: list[RawUnit]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this RawElements.


        :param units: The units of this RawElements.  # noqa: E501
        :type: list[RawUnit]
        """

        self._units = units

    @property
    def definitions(self):
        """Gets the definitions of this RawElements.  # noqa: E501


        :return: The definitions of this RawElements.  # noqa: E501
        :rtype: list[RawDefinition]
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """Sets the definitions of this RawElements.


        :param definitions: The definitions of this RawElements.  # noqa: E501
        :type: list[RawDefinition]
        """

        self._definitions = definitions

    @property
    def property_sets(self):
        """Gets the property_sets of this RawElements.  # noqa: E501


        :return: The property_sets of this RawElements.  # noqa: E501
        :rtype: list[RawPropertySet]
        """
        return self._property_sets

    @property_sets.setter
    def property_sets(self, property_sets):
        """Sets the property_sets of this RawElements.


        :param property_sets: The property_sets of this RawElements.  # noqa: E501
        :type: list[RawPropertySet]
        """

        self._property_sets = property_sets

    @property
    def classifications(self):
        """Gets the classifications of this RawElements.  # noqa: E501


        :return: The classifications of this RawElements.  # noqa: E501
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this RawElements.


        :param classifications: The classifications of this RawElements.  # noqa: E501
        :type: list[Classification]
        """

        self._classifications = classifications

    @property
    def elements(self):
        """Gets the elements of this RawElements.  # noqa: E501


        :return: The elements of this RawElements.  # noqa: E501
        :rtype: list[RawElement]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this RawElements.


        :param elements: The elements of this RawElements.  # noqa: E501
        :type: list[RawElement]
        """
        if elements is None:
            raise ValueError("Invalid value for `elements`, must not be `None`")  # noqa: E501

        self._elements = elements

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
        if not isinstance(other, RawElements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other