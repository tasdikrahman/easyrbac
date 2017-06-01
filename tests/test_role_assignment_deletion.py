# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

"""Testing assignment and deletion of a Role to User
"""

from easyrbac import Role, User


default_role = Role('default')
admin_role = Role('admin')

default_user = User(roles=[default_role])
admin_user = User(roles=[admin_role, default_role])


class TestRoleAssignmentDeletion:

    def test_role_assignment(self):
        """Creates the roles which need to be assigned to users
        """
        assert [role.get_name() for role in default_user.get_roles()] == ['default']
        assert [role.get_name() for role in admin_user.get_roles()].sort() == ['admin', 'default'].sort()

    def test_delete_role_from_user(self):
        """Tests the function to delete a role from a user
        """
        anonymous_user = User(roles=[default_role, admin_role])
        anonymous_user.remove_role('admin')
        assert 'admin' not in [role.get_name() for role in anonymous_user.get_roles()]

    def test_delete_user(self):
        """Tests successful deletion of user
        """
        unwanted_user = User(roles=[default_role])
        del unwanted_user
        assert 'unwanted_user' not in dir()
