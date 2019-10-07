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


class Cloud(object):
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
        'id': 'int',
        'name': 'str',
        'features': 'list[Feature]',
        'creator': 'User',
        'is_default': 'bool',
        'created_at': 'datetime',
        'image': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'features': 'features',
        'creator': 'creator',
        'is_default': 'is_default',
        'created_at': 'created_at',
        'image': 'image',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, features=None, creator=None, is_default=None, created_at=None, image=None, updated_at=None):  # noqa: E501
        """Cloud - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._features = None
        self._creator = None
        self._is_default = None
        self._created_at = None
        self._image = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if features is not None:
            self.features = features
        if creator is not None:
            self.creator = creator
        if is_default is not None:
            self.is_default = is_default
        if created_at is not None:
            self.created_at = created_at
        self.image = image
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Cloud.  # noqa: E501


        :return: The id of this Cloud.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cloud.


        :param id: The id of this Cloud.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Cloud.  # noqa: E501

        Name of the cloud  # noqa: E501

        :return: The name of this Cloud.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cloud.

        Name of the cloud  # noqa: E501

        :param name: The name of this Cloud.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def features(self):
        """Gets the features of this Cloud.  # noqa: E501


        :return: The features of this Cloud.  # noqa: E501
        :rtype: list[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Cloud.


        :param features: The features of this Cloud.  # noqa: E501
        :type: list[Feature]
        """

        self._features = features

    @property
    def creator(self):
        """Gets the creator of this Cloud.  # noqa: E501


        :return: The creator of this Cloud.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Cloud.


        :param creator: The creator of this Cloud.  # noqa: E501
        :type: User
        """

        self._creator = creator

    @property
    def is_default(self):
        """Gets the is_default of this Cloud.  # noqa: E501


        :return: The is_default of this Cloud.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this Cloud.


        :param is_default: The is_default of this Cloud.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def created_at(self):
        """Gets the created_at of this Cloud.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this Cloud.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Cloud.

        Creation date  # noqa: E501

        :param created_at: The created_at of this Cloud.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def image(self):
        """Gets the image of this Cloud.  # noqa: E501


        :return: The image of this Cloud.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Cloud.


        :param image: The image of this Cloud.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def updated_at(self):
        """Gets the updated_at of this Cloud.  # noqa: E501

        Date of the last update  # noqa: E501

        :return: The updated_at of this Cloud.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Cloud.

        Date of the last update  # noqa: E501

        :param updated_at: The updated_at of this Cloud.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Cloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
