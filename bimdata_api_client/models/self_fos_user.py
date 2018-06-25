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


class SelfFosUser(object):
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
        'email': 'str',
        'company': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'password': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'clouds': 'list[CloudRole]',
        'projects': 'list[ProjectRole]',
        'last_login': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email': 'email',
        'company': 'company',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'password': 'password',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'clouds': 'clouds',
        'projects': 'projects',
        'last_login': 'last_login'
    }

    def __init__(self, id=None, email=None, company=None, firstname=None, lastname=None, password=None, created_at=None, updated_at=None, clouds=None, projects=None, last_login=None):  # noqa: E501
        """SelfFosUser - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._email = None
        self._company = None
        self._firstname = None
        self._lastname = None
        self._password = None
        self._created_at = None
        self._updated_at = None
        self._clouds = None
        self._projects = None
        self._last_login = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.email = email
        if company is not None:
            self.company = company
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if clouds is not None:
            self.clouds = clouds
        if projects is not None:
            self.projects = projects
        if last_login is not None:
            self.last_login = last_login

    @property
    def id(self):
        """Gets the id of this SelfFosUser.  # noqa: E501


        :return: The id of this SelfFosUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SelfFosUser.


        :param id: The id of this SelfFosUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this SelfFosUser.  # noqa: E501


        :return: The email of this SelfFosUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SelfFosUser.


        :param email: The email of this SelfFosUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 254:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def company(self):
        """Gets the company of this SelfFosUser.  # noqa: E501


        :return: The company of this SelfFosUser.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this SelfFosUser.


        :param company: The company of this SelfFosUser.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def firstname(self):
        """Gets the firstname of this SelfFosUser.  # noqa: E501


        :return: The firstname of this SelfFosUser.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this SelfFosUser.


        :param firstname: The firstname of this SelfFosUser.  # noqa: E501
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501
        if firstname is not None and len(firstname) < 1:
            raise ValueError("Invalid value for `firstname`, length must be greater than or equal to `1`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this SelfFosUser.  # noqa: E501


        :return: The lastname of this SelfFosUser.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this SelfFosUser.


        :param lastname: The lastname of this SelfFosUser.  # noqa: E501
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501
        if lastname is not None and len(lastname) < 1:
            raise ValueError("Invalid value for `lastname`, length must be greater than or equal to `1`")  # noqa: E501

        self._lastname = lastname

    @property
    def password(self):
        """Gets the password of this SelfFosUser.  # noqa: E501


        :return: The password of this SelfFosUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SelfFosUser.


        :param password: The password of this SelfFosUser.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def created_at(self):
        """Gets the created_at of this SelfFosUser.  # noqa: E501


        :return: The created_at of this SelfFosUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SelfFosUser.


        :param created_at: The created_at of this SelfFosUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SelfFosUser.  # noqa: E501


        :return: The updated_at of this SelfFosUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SelfFosUser.


        :param updated_at: The updated_at of this SelfFosUser.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def clouds(self):
        """Gets the clouds of this SelfFosUser.  # noqa: E501


        :return: The clouds of this SelfFosUser.  # noqa: E501
        :rtype: list[CloudRole]
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        """Sets the clouds of this SelfFosUser.


        :param clouds: The clouds of this SelfFosUser.  # noqa: E501
        :type: list[CloudRole]
        """

        self._clouds = clouds

    @property
    def projects(self):
        """Gets the projects of this SelfFosUser.  # noqa: E501


        :return: The projects of this SelfFosUser.  # noqa: E501
        :rtype: list[ProjectRole]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this SelfFosUser.


        :param projects: The projects of this SelfFosUser.  # noqa: E501
        :type: list[ProjectRole]
        """

        self._projects = projects

    @property
    def last_login(self):
        """Gets the last_login of this SelfFosUser.  # noqa: E501


        :return: The last_login of this SelfFosUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this SelfFosUser.


        :param last_login: The last_login of this SelfFosUser.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

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
        if not isinstance(other, SelfFosUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
