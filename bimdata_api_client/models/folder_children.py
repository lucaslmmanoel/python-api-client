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


class FolderChildren(object):
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
        'parent_id': 'int',
        'created_by': 'User',
        'creator': 'User',
        'type': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'file_name': 'str',
        'description': 'str',
        'size': 'int',
        'ifc_id': 'int',
        'file': 'str',
        'children': 'list[dict(str, str)]'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'created_by': 'created_by',
        'creator': 'creator',
        'type': 'type',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'file_name': 'file_name',
        'description': 'description',
        'size': 'size',
        'ifc_id': 'ifc_id',
        'file': 'file',
        'children': 'children'
    }

    def __init__(self, id=None, parent_id=None, created_by=None, creator=None, type=None, name=None, created_at=None, updated_at=None, file_name=None, description=None, size=None, ifc_id=None, file=None, children=None):  # noqa: E501
        """FolderChildren - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._parent_id = None
        self._created_by = None
        self._creator = None
        self._type = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._file_name = None
        self._description = None
        self._size = None
        self._ifc_id = None
        self._file = None
        self._children = None
        self.discriminator = None

        self.id = id
        self.parent_id = parent_id
        self.created_by = created_by
        self.creator = creator
        if type is not None:
            self.type = type
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        if file_name is not None:
            self.file_name = file_name
        if description is not None:
            self.description = description
        if size is not None:
            self.size = size
        if ifc_id is not None:
            self.ifc_id = ifc_id
        if file is not None:
            self.file = file
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this FolderChildren.  # noqa: E501


        :return: The id of this FolderChildren.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderChildren.


        :param id: The id of this FolderChildren.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this FolderChildren.  # noqa: E501


        :return: The parent_id of this FolderChildren.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this FolderChildren.


        :param parent_id: The parent_id of this FolderChildren.  # noqa: E501
        :type: int
        """
        if parent_id is None:
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def created_by(self):
        """Gets the created_by of this FolderChildren.  # noqa: E501


        :return: The created_by of this FolderChildren.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FolderChildren.


        :param created_by: The created_by of this FolderChildren.  # noqa: E501
        :type: User
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def creator(self):
        """Gets the creator of this FolderChildren.  # noqa: E501


        :return: The creator of this FolderChildren.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FolderChildren.


        :param creator: The creator of this FolderChildren.  # noqa: E501
        :type: User
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def type(self):
        """Gets the type of this FolderChildren.  # noqa: E501

        Values can be 'Folder', 'Document' or 'Ifc'. It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :return: The type of this FolderChildren.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FolderChildren.

        Values can be 'Folder', 'Document' or 'Ifc'. It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :param type: The type of this FolderChildren.  # noqa: E501
        :type: str
        """
        allowed_values = ["Folder", "Document", "Ifc"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this FolderChildren.  # noqa: E501


        :return: The name of this FolderChildren.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderChildren.


        :param name: The name of this FolderChildren.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this FolderChildren.  # noqa: E501


        :return: The created_at of this FolderChildren.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FolderChildren.


        :param created_at: The created_at of this FolderChildren.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FolderChildren.  # noqa: E501


        :return: The updated_at of this FolderChildren.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FolderChildren.


        :param updated_at: The updated_at of this FolderChildren.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def file_name(self):
        """Gets the file_name of this FolderChildren.  # noqa: E501


        :return: The file_name of this FolderChildren.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FolderChildren.


        :param file_name: The file_name of this FolderChildren.  # noqa: E501
        :type: str
        """
        if file_name is not None and len(file_name) < 1:
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._file_name = file_name

    @property
    def description(self):
        """Gets the description of this FolderChildren.  # noqa: E501


        :return: The description of this FolderChildren.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FolderChildren.


        :param description: The description of this FolderChildren.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def size(self):
        """Gets the size of this FolderChildren.  # noqa: E501


        :return: The size of this FolderChildren.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FolderChildren.


        :param size: The size of this FolderChildren.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def ifc_id(self):
        """Gets the ifc_id of this FolderChildren.  # noqa: E501


        :return: The ifc_id of this FolderChildren.  # noqa: E501
        :rtype: int
        """
        return self._ifc_id

    @ifc_id.setter
    def ifc_id(self, ifc_id):
        """Sets the ifc_id of this FolderChildren.


        :param ifc_id: The ifc_id of this FolderChildren.  # noqa: E501
        :type: int
        """

        self._ifc_id = ifc_id

    @property
    def file(self):
        """Gets the file of this FolderChildren.  # noqa: E501


        :return: The file of this FolderChildren.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FolderChildren.


        :param file: The file of this FolderChildren.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def children(self):
        """Gets the children of this FolderChildren.  # noqa: E501


        :return: The children of this FolderChildren.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this FolderChildren.


        :param children: The children of this FolderChildren.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._children = children

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
        if not isinstance(other, FolderChildren):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
