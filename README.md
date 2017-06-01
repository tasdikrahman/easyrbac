# rbac

Role based Access Control

**NOTE**: _Still under heavy development._

## Demo

### Role creation and assignment of role to a User

```python
from rbac import Role, User


default_role = Role('default')
admin_role = Role('admin')

default_user = User(roles=[default_role])
admin_user = User(roles=[admin_role, default_role])
```

### User resource access permissions allocation

```python
from rbac import AccessControlList, User, Role

everyone_role = Role('everyone')
admin_role = Role('admin')

everyone_user = User(roles=[everyone_role])
admin_user = User(roles=[admin_role, everyone_role])


acl = AccessControlList()

acl.resource_read_rule(everyone_role, 'GET', '/api/v1/employee/1/info')
acl.resource_delete_rule(admin_role, 'DELETE', '/api/v1/employee/1/')

# checking READ operation on resource for user `everyone_user`
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_read_allowed(user_role, 'GET', '/api/v1/employee/1/info') == True

# checking WRITE operation on resource for user `everyone_user`
# Since you have not defined the rule for the particular, it will disallow any such operation by default.
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_write_allowed(user_role, 'WRITE', '/api/v1/employee/1/info') == False

# checking WRITE operation on resource for user `admin_user`
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    if user_role == 'admin': # as a user can have more than one role assigned to them
        assert acl.is_delete_allowed(user_role, 'DELETE', '/api/v1/employee/1/') == True
    else:
        assert acl.is_delete_allowed(user_role, 'DELETE', '/api/v1/employee/1/') == False
```


## TODO

- [ ] Adding hierarchical roles, which represent parent<->child relations
- [ ] Adding this on top of Bottle/Flask
- [ ] Make it `pip` installable

## Issues

You can submit the issues on the issue tracker [here](https://github.com/prodicus/rbac/)

## Literature material

- [http://profsandhu.com/articles/advcom/adv_comp_rbac.pdf](http://profsandhu.com/articles/advcom/adv_comp_rbac.pdf)
- [http://www.comp.nus.edu.sg/~tankl/cs5322/readings/rbac1.pdf](http://www.comp.nus.edu.sg/~tankl/cs5322/readings/rbac1.pdf)
- [https://symas.com/ansi-rbac-intro/](https://symas.com/ansi-rbac-intro/)
- [https://pythonhosted.org/Flask-Principal/](https://pythonhosted.org/Flask-Principal/)
- [https://iamfortress.net/2014/11/24/using-role-for-access-control-is-not-rbac/](https://iamfortress.net/2014/11/24/using-role-for-access-control-is-not-rbac/)
- [http://cloudify.co/2016/04/15/simple-secure-role-based-access-control-rest-api-rbac-server-devops-cloud-orchestration.html](http://cloudify.co/2016/04/15/simple-secure-role-based-access-control-rest-api-rbac-server-devops-cloud-orchestration.html)

## LICENSE

GPLv3
