# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

from .acl import AccessControlList


class RBAC(object):
    """Defines the RBAC policies for the resources"""

    def __init__(self):
        self.acl = AccessControlList()
        self._before_acl = {
            'read': [],
            'write': [],
            'delete': []
        }

    def has_permission(self, method, endpoint, user=None):
        pass

