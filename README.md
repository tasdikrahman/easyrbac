# easyrbac

[![Build Status](https://travis-ci.org/prodicus/easyrbac.svg?branch=master)](https://travis-ci.org/prodicus/rbac)

Role based Access Control implementation using the standard library

I wrote a little piece [on medium about it](https://medium.com/@tasdikrahman/implementing-role-based-access-control-a2bbcb4dfdb0) if you are interested on reading.

**NOTE**: _Still under heavy development._

## Installation

```bash
$ mkvirtualenv rbac
$ workon rbac
(rbac)$ pip install easyrbac
```

## Demo

### Role creation and assignment of role to a User

```python
from easyrbac import Role, User


default_role = Role('default')
admin_role = Role('admin')

default_user = User(roles=[default_role])
admin_user = User(roles=[admin_role, default_role])
```

### User resource access permissions allocation

```python
from easyrbac import AccessControlList, User, Role

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

## Tests

`easyrbac` uses `py.test` for running the tests, running which is as simple as doing a

```bash
$ py.test
```

## TODO

- [ ] Adding hierarchical roles, which represent parent<->child relations
- [ ] Adding this on top of Bottle/Flask
- [x] Make it `pip` installable

## Issues

You can submit the issues on the issue tracker [here](https://github.com/prodicus/rbac/issues)

## Literature material

- [http://profsandhu.com/articles/advcom/adv_comp_rbac.pdf](http://profsandhu.com/articles/advcom/adv_comp_rbac.pdf)
- [http://www.comp.nus.edu.sg/~tankl/cs5322/readings/rbac1.pdf](http://www.comp.nus.edu.sg/~tankl/cs5322/readings/rbac1.pdf)
- [https://symas.com/ansi-rbac-intro/](https://symas.com/ansi-rbac-intro/)
- [https://pythonhosted.org/Flask-Principal/](https://pythonhosted.org/Flask-Principal/)
- [https://iamfortress.net/2014/11/24/using-role-for-access-control-is-not-rbac/](https://iamfortress.net/2014/11/24/using-role-for-access-control-is-not-rbac/)
- [http://cloudify.co/2016/04/15/simple-secure-role-based-access-control-rest-api-rbac-server-devops-cloud-orchestration.html](http://cloudify.co/2016/04/15/simple-secure-role-based-access-control-rest-api-rbac-server-devops-cloud-orchestration.html)

## RBAC in simple terms

<p align="center">
  <img src="http://tasdikrahman.me/content/images/2017/06/rbac_model.jpg" alt="rbac"/>
</p>

# Links

- [medium blog post](https://medium.com/@tasdikrahman/implementing-role-based-access-control-a2bbcb4dfdb0)

## LICENSE

GPLv3

## Donation 


If you have found my little bits of software being of any use to you, do consider helping me pay my internet bills :)

| £ (GBP) | <a href="https://transferwise.com/pay/d804d854-6862-4127-afdd-4687d64cbd28" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| € Euros | <a href="https://transferwise.com/pay/64c586e3-ec99-4be8-af0b-59241f7b9b79" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
| ₹ (INR)  | <a href="https://www.instamojo.com/@tasdikrahman" target="_blank"><img src="https://www.instamojo.com/blog/wp-content/uploads/2017/01/instamojo-91.png" alt="Donate via instamojo" title="Donate via instamojo" /></a> | 
