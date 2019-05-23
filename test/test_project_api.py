# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.project_api import ProjectApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_project_user_invitation(self):
        """Test case for cancel_project_user_invitation

        Cancel a pending invitation  # noqa: E501
        """
        pass

    def test_create_classification(self):
        """Test case for create_classification

        Create a classification  # noqa: E501
        """
        pass

    def test_create_document(self):
        """Test case for create_document

        Create a document  # noqa: E501
        """
        pass

    def test_create_folder(self):
        """Test case for create_folder

        Create a folder  # noqa: E501
        """
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a project  # noqa: E501
        """
        pass

    def test_delete_classification(self):
        """Test case for delete_classification

        Delete a classification  # noqa: E501
        """
        pass

    def test_delete_document(self):
        """Test case for delete_document

        Delete the document  # noqa: E501
        """
        pass

    def test_delete_folder(self):
        """Test case for delete_folder

        Delete a folder  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project  # noqa: E501
        """
        pass

    def test_delete_project_user(self):
        """Test case for delete_project_user

        Remove a user from a project  # noqa: E501
        """
        pass

    def test_full_update_classification(self):
        """Test case for full_update_classification

        Update all fields of a classification  # noqa: E501
        """
        pass

    def test_full_update_document(self):
        """Test case for full_update_document

        Update all fields of the document  # noqa: E501
        """
        pass

    def test_full_update_folder(self):
        """Test case for full_update_folder

        Update all fields of a folder  # noqa: E501
        """
        pass

    def test_full_update_project(self):
        """Test case for full_update_project

        Update all fields of a project  # noqa: E501
        """
        pass

    def test_full_update_project_user(self):
        """Test case for full_update_project_user

        Update all fields of a project user  # noqa: E501
        """
        pass

    def test_get_classification(self):
        """Test case for get_classification

        Retrieve a classification  # noqa: E501
        """
        pass

    def test_get_classifications(self):
        """Test case for get_classifications

        Retrieve all classifications  # noqa: E501
        """
        pass

    def test_get_document(self):
        """Test case for get_document

        Retrieve a document  # noqa: E501
        """
        pass

    def test_get_documents(self):
        """Test case for get_documents

        Retrieve all documents  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        Retrieve a folder  # noqa: E501
        """
        pass

    def test_get_folders(self):
        """Test case for get_folders

        Retrieve all folders  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Retrieve a project  # noqa: E501
        """
        pass

    def test_get_project_dms_tree(self):
        """Test case for get_project_dms_tree

        Retrieve the complete DMS tree  # noqa: E501
        """
        pass

    def test_get_project_invitations(self):
        """Test case for get_project_invitations

        Retrieve all pending invitations in the project  # noqa: E501
        """
        pass

    def test_get_project_sub_tree(self):
        """Test case for get_project_sub_tree

        Retrieve the complete projects tree of the cloud  # noqa: E501
        """
        pass

    def test_get_project_tree(self):
        """Test case for get_project_tree

        Retrieve the complete DMS tree  # noqa: E501
        """
        pass

    def test_get_project_user(self):
        """Test case for get_project_user

        Retrieve a user in a project  # noqa: E501
        """
        pass

    def test_get_project_users(self):
        """Test case for get_project_users

        Retrieve all users in a project  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Retrieve all projects  # noqa: E501
        """
        pass

    def test_invite_project_user(self):
        """Test case for invite_project_user

        Invite a project member  # noqa: E501
        """
        pass

    def test_update_classification(self):
        """Test case for update_classification

        Update some fields of a classification  # noqa: E501
        """
        pass

    def test_update_document(self):
        """Test case for update_document

        Update some fields of the document  # noqa: E501
        """
        pass

    def test_update_folder(self):
        """Test case for update_folder

        Update some fields of a folder  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update some fields of a project  # noqa: E501
        """
        pass

    def test_update_project_user(self):
        """Test case for update_project_user

        Update some fields of a project user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
