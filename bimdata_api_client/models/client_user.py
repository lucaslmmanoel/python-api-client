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


class ClientUser(object):
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
        'client_id': 'str',
        'provider': 'int'
    }

    attribute_map = {
        'client_id': 'client_id',
        'provider': 'provider'
    }

    def __init__(self, client_id=None, provider=None):  # noqa: E501
        """ClientUser - a model defined in OpenAPI"""  # noqa: E501

        self._client_id = None
        self._provider = None
        self.discriminator = None

        self.client_id = client_id
        self.provider = provider

    @property
    def client_id(self):
        """Gets the client_id of this ClientUser.  # noqa: E501


        :return: The client_id of this ClientUser.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ClientUser.


        :param client_id: The client_id of this ClientUser.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501
        if client_id is not None and len(client_id) > 64:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `64`")  # noqa: E501
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def provider(self):
        """Gets the provider of this ClientUser.  # noqa: E501


        :return: The provider of this ClientUser.  # noqa: E501
        :rtype: int
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ClientUser.


        :param provider: The provider of this ClientUser.  # noqa: E501
        :type: int
        """

        self._provider = provider

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
        if not isinstance(other, ClientUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other