# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

class Employee(object):
    """mapped to roles which have fine grained access rules defined in rbac.model
    """
    def __init__(self, name="Tasdik", bio="uber geek", id=1081310234, salary=10, designation="SDE"):
        self.name = name
        self.bio = bio
        self.id = id
        self.salary = salary
        self.designation = designation
