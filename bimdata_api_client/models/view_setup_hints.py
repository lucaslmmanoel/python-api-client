# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ViewSetupHints(object):
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
        'spaces_visible': 'bool',
        'space_boundaries_visible': 'bool',
        'openings_visible': 'bool'
    }

    attribute_map = {
        'spaces_visible': 'spaces_visible',
        'space_boundaries_visible': 'space_boundaries_visible',
        'openings_visible': 'openings_visible'
    }

    def __init__(self, spaces_visible=None, space_boundaries_visible=None, openings_visible=None):  # noqa: E501
        """ViewSetupHints - a model defined in OpenAPI"""  # noqa: E501

        self._spaces_visible = None
        self._space_boundaries_visible = None
        self._openings_visible = None
        self.discriminator = None

        if spaces_visible is not None:
            self.spaces_visible = spaces_visible
        if space_boundaries_visible is not None:
            self.space_boundaries_visible = space_boundaries_visible
        if openings_visible is not None:
            self.openings_visible = openings_visible

    @property
    def spaces_visible(self):
        """Gets the spaces_visible of this ViewSetupHints.  # noqa: E501


        :return: The spaces_visible of this ViewSetupHints.  # noqa: E501
        :rtype: bool
        """
        return self._spaces_visible

    @spaces_visible.setter
    def spaces_visible(self, spaces_visible):
        """Sets the spaces_visible of this ViewSetupHints.


        :param spaces_visible: The spaces_visible of this ViewSetupHints.  # noqa: E501
        :type: bool
        """

        self._spaces_visible = spaces_visible

    @property
    def space_boundaries_visible(self):
        """Gets the space_boundaries_visible of this ViewSetupHints.  # noqa: E501


        :return: The space_boundaries_visible of this ViewSetupHints.  # noqa: E501
        :rtype: bool
        """
        return self._space_boundaries_visible

    @space_boundaries_visible.setter
    def space_boundaries_visible(self, space_boundaries_visible):
        """Sets the space_boundaries_visible of this ViewSetupHints.


        :param space_boundaries_visible: The space_boundaries_visible of this ViewSetupHints.  # noqa: E501
        :type: bool
        """

        self._space_boundaries_visible = space_boundaries_visible

    @property
    def openings_visible(self):
        """Gets the openings_visible of this ViewSetupHints.  # noqa: E501


        :return: The openings_visible of this ViewSetupHints.  # noqa: E501
        :rtype: bool
        """
        return self._openings_visible

    @openings_visible.setter
    def openings_visible(self, openings_visible):
        """Sets the openings_visible of this ViewSetupHints.


        :param openings_visible: The openings_visible of this ViewSetupHints.  # noqa: E501
        :type: bool
        """

        self._openings_visible = openings_visible

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
        if not isinstance(other, ViewSetupHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
