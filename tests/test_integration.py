# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

from rbac.model import Role
from rbac.model import User

from resource import Employee


class IntegrationTest:

    resource_employee = Employee()

    def test_with_admin(self):
        """checking resource access with the employee himself in context
        """
        pass