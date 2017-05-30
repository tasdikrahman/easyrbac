# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

"""
    Role Based Access Control:

    Implementing a role based auth system. System should be able to assign a role to user and remove a user from the role.

    Entities are USER, ACTION TYPE, RESOURCE, ROLE

    ACTION TYPE defines the access level(Ex: READ, WRITE, DELETE)

    Access to resources for users are controlled strictly by the role.One user can have multiple roles. 
    Given a user, action type and resource system should be able to tell whether user has access or not.

"""


class Role(object):
    """roles which are associated to permissions to access resources
    
    :param name: the name of the role
    """
    # TODO: Adding hierarchical roles, which represent parent<->child relations

    roles = {}

    def __init__(self, name=None):
        """Initializes the a role with the permissions associated with it.

        """
        self.name = name
        Role.roles[name] = self

    def get_name(self):
        """returns the name of the role
        """
        return self.name

    def __repr__(self):
        return '<Role %s>' % self.name



class User(object):
    """A role gets assigned to a user
    """

    def __init__(self, roles=[]):
        """Initialises the roles assigned to the user when created or updated later

        :param roles: <list> object which holds the roles assigned to the user
        """
        self.roles = set(roles)

    def add_role(self, role):
        """Adds the role to this user
        
        :param role: the role to be assigned to the user
        :return: 
        """
        self.roles.extend(role)


    def remove_role(self, role):
        """
        
        :param role: 
        :return: 
        """
        pass

    def __repr__(self):
        return '<User %s>' % self.name

