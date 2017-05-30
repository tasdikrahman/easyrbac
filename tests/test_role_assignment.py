# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

"""Testing assignment of a Role to User
"""

from rbac.model import Role
from rbac.model import User


class TestRoleAssignment:
    def test_role_assignment(self):
        admin_user = User()

