# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bimdata_api_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ask_reset_password_token(self, forgot_password, **kwargs):  # noqa: E501
        """ask_reset_password_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ask_reset_password_token(forgot_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param ForgotPassword forgot_password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ask_reset_password_token_with_http_info(forgot_password, **kwargs)  # noqa: E501
        else:
            (data) = self.ask_reset_password_token_with_http_info(forgot_password, **kwargs)  # noqa: E501
            return data

    def ask_reset_password_token_with_http_info(self, forgot_password, **kwargs):  # noqa: E501
        """ask_reset_password_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ask_reset_password_token_with_http_info(forgot_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param ForgotPassword forgot_password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_password']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ask_reset_password_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'forgot_password' is set
        if ('forgot_password' not in params or
                params['forgot_password'] is None):
            raise ValueError("Missing the required parameter `forgot_password` when calling `ask_reset_password_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_password' in params:
            body_params = params['forgot_password']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/forgot-password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def full_update_notification(self, id, notification, **kwargs):  # noqa: E501
        """full_update_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.full_update_notification(id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param Notification notification: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.full_update_notification_with_http_info(id, notification, **kwargs)  # noqa: E501
        else:
            (data) = self.full_update_notification_with_http_info(id, notification, **kwargs)  # noqa: E501
            return data

    def full_update_notification_with_http_info(self, id, notification, **kwargs):  # noqa: E501
        """full_update_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.full_update_notification_with_http_info(id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param Notification notification: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'notification']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method full_update_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `full_update_notification`")  # noqa: E501
        # verify the required parameter 'notification' is set
        if ('notification' not in params or
                params['notification'] is None):
            raise ValueError("Missing the required parameter `notification` when calling `full_update_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'notification' in params:
            body_params = params['notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/notification/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notification',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notification(self, id, **kwargs):  # noqa: E501
        """get_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_notification(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_notification_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_notification_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_notification_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/notification/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notification',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_self_notifications(self, **kwargs):  # noqa: E501
        """get_self_notifications  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_notifications(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Notification]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_self_notifications_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_self_notifications_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_self_notifications_with_http_info(self, **kwargs):  # noqa: E501
        """get_self_notifications  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_notifications_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Notification]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_self_notifications" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/notification', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Notification]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_self_projects(self, **kwargs):  # noqa: E501
        """get_self_projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_projects(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_self_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_self_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_self_projects_with_http_info(self, **kwargs):  # noqa: E501
        """get_self_projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_projects_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_self_projects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Project]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_self_user(self, **kwargs):  # noqa: E501
        """get_self_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_user(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_self_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_self_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_self_user_with_http_info(self, **kwargs):  # noqa: E501
        """get_self_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_self_user_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_self_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_password(self, reset_password, **kwargs):  # noqa: E501
        """reset_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_password(reset_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param ResetPassword reset_password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_password_with_http_info(reset_password, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_password_with_http_info(reset_password, **kwargs)  # noqa: E501
            return data

    def reset_password_with_http_info(self, reset_password, **kwargs):  # noqa: E501
        """reset_password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_password_with_http_info(reset_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param ResetPassword reset_password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_password']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_password' is set
        if ('reset_password' not in params or
                params['reset_password'] is None):
            raise ValueError("Missing the required parameter `reset_password` when calling `reset_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reset_password' in params:
            body_params = params['reset_password']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/reset-password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sign_up(self, signup_fos_user, **kwargs):  # noqa: E501
        """sign_up  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_up(signup_fos_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignupFosUser signup_fos_user: (required)
        :return: SignupFosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sign_up_with_http_info(signup_fos_user, **kwargs)  # noqa: E501
        else:
            (data) = self.sign_up_with_http_info(signup_fos_user, **kwargs)  # noqa: E501
            return data

    def sign_up_with_http_info(self, signup_fos_user, **kwargs):  # noqa: E501
        """sign_up  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_up_with_http_info(signup_fos_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param SignupFosUser signup_fos_user: (required)
        :return: SignupFosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['signup_fos_user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_up" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'signup_fos_user' is set
        if ('signup_fos_user' not in params or
                params['signup_fos_user'] is None):
            raise ValueError("Missing the required parameter `signup_fos_user` when calling `sign_up`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'signup_fos_user' in params:
            body_params = params['signup_fos_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/signup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignupFosUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sign_up_with_invitation_token(self, invited_sign_up, **kwargs):  # noqa: E501
        """sign_up_with_invitation_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_up_with_invitation_token(invited_sign_up, async=True)
        >>> result = thread.get()

        :param async bool
        :param InvitedSignUp invited_sign_up: (required)
        :return: SignupFosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sign_up_with_invitation_token_with_http_info(invited_sign_up, **kwargs)  # noqa: E501
        else:
            (data) = self.sign_up_with_invitation_token_with_http_info(invited_sign_up, **kwargs)  # noqa: E501
            return data

    def sign_up_with_invitation_token_with_http_info(self, invited_sign_up, **kwargs):  # noqa: E501
        """sign_up_with_invitation_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sign_up_with_invitation_token_with_http_info(invited_sign_up, async=True)
        >>> result = thread.get()

        :param async bool
        :param InvitedSignUp invited_sign_up: (required)
        :return: SignupFosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invited_sign_up']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_up_with_invitation_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invited_sign_up' is set
        if ('invited_sign_up' not in params or
                params['invited_sign_up'] is None):
            raise ValueError("Missing the required parameter `invited_sign_up` when calling `sign_up_with_invitation_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'invited_sign_up' in params:
            body_params = params['invited_sign_up']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/invited-signup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SignupFosUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_notification(self, id, notification, **kwargs):  # noqa: E501
        """update_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_notification(id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param Notification notification: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_notification_with_http_info(id, notification, **kwargs)  # noqa: E501
        else:
            (data) = self.update_notification_with_http_info(id, notification, **kwargs)  # noqa: E501
            return data

    def update_notification_with_http_info(self, id, notification, **kwargs):  # noqa: E501
        """update_notification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_notification_with_http_info(id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: (required)
        :param Notification notification: (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'notification']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_notification`")  # noqa: E501
        # verify the required parameter 'notification' is set
        if ('notification' not in params or
                params['notification'] is None):
            raise ValueError("Missing the required parameter `notification` when calling `update_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'notification' in params:
            body_params = params['notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user/notification/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notification',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_self_user(self, self_fos_user, **kwargs):  # noqa: E501
        """update_self_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_self_user(self_fos_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param SelfFosUser self_fos_user: (required)
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_self_user_with_http_info(self_fos_user, **kwargs)  # noqa: E501
        else:
            (data) = self.update_self_user_with_http_info(self_fos_user, **kwargs)  # noqa: E501
            return data

    def update_self_user_with_http_info(self, self_fos_user, **kwargs):  # noqa: E501
        """update_self_user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_self_user_with_http_info(self_fos_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param SelfFosUser self_fos_user: (required)
        :return: FosUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['self_fos_user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_self_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'self_fos_user' is set
        if ('self_fos_user' not in params or
                params['self_fos_user'] is None):
            raise ValueError("Missing the required parameter `self_fos_user` when calling `update_self_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'self_fos_user' in params:
            body_params = params['self_fos_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/user', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FosUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
