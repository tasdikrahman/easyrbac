# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus


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
        """
        self.roles.extend(role)

    def get_roles(self):
        """Returns a generator object for the roles held by the User
        """
        for role in self.roles.copy():
            yield role

    def remove_role(self, role_name):
        """Remove a role assigned to a User
        
        :param role_name: name of the role which needs to be removed 
        """
        for role in self.get_roles():
            if role.get_name() == role_name:
                self.roles.remove(role)

    def __repr__(self):
        return '<User %s>' % self.roles
