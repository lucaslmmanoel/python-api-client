# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InvitedSignUp(object):
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
        'invitation_token': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'password': 'str',
        'email': 'str'
    }

    attribute_map = {
        'invitation_token': 'invitation_token',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'password': 'password',
        'email': 'email'
    }

    def __init__(self, invitation_token=None, firstname=None, lastname=None, password=None, email=None):  # noqa: E501
        """InvitedSignUp - a model defined in Swagger"""  # noqa: E501

        self._invitation_token = None
        self._firstname = None
        self._lastname = None
        self._password = None
        self._email = None
        self.discriminator = None

        self.invitation_token = invitation_token
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        if email is not None:
            self.email = email

    @property
    def invitation_token(self):
        """Gets the invitation_token of this InvitedSignUp.  # noqa: E501


        :return: The invitation_token of this InvitedSignUp.  # noqa: E501
        :rtype: str
        """
        return self._invitation_token

    @invitation_token.setter
    def invitation_token(self, invitation_token):
        """Sets the invitation_token of this InvitedSignUp.


        :param invitation_token: The invitation_token of this InvitedSignUp.  # noqa: E501
        :type: str
        """
        if invitation_token is None:
            raise ValueError("Invalid value for `invitation_token`, must not be `None`")  # noqa: E501
        if invitation_token is not None and len(invitation_token) < 1:
            raise ValueError("Invalid value for `invitation_token`, length must be greater than or equal to `1`")  # noqa: E501

        self._invitation_token = invitation_token

    @property
    def firstname(self):
        """Gets the firstname of this InvitedSignUp.  # noqa: E501


        :return: The firstname of this InvitedSignUp.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this InvitedSignUp.


        :param firstname: The firstname of this InvitedSignUp.  # noqa: E501
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501
        if firstname is not None and len(firstname) < 1:
            raise ValueError("Invalid value for `firstname`, length must be greater than or equal to `1`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this InvitedSignUp.  # noqa: E501


        :return: The lastname of this InvitedSignUp.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this InvitedSignUp.


        :param lastname: The lastname of this InvitedSignUp.  # noqa: E501
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501
        if lastname is not None and len(lastname) < 1:
            raise ValueError("Invalid value for `lastname`, length must be greater than or equal to `1`")  # noqa: E501

        self._lastname = lastname

    @property
    def password(self):
        """Gets the password of this InvitedSignUp.  # noqa: E501


        :return: The password of this InvitedSignUp.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InvitedSignUp.


        :param password: The password of this InvitedSignUp.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def email(self):
        """Gets the email of this InvitedSignUp.  # noqa: E501


        :return: The email of this InvitedSignUp.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvitedSignUp.


        :param email: The email of this InvitedSignUp.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvitedSignUp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other