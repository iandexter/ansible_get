ansible_get
===========

A RESTful API built on [Flask](http://flask.pocoo.org/) to `GET` [Ansible](http://www.ansibleworks.com/) objects.


Prerequisites
-------------

This assumes Ansible is running on the host. Refer to the [Ansible documentation](http://www.ansibleworks.com/docs/) for more details.

Flask can be ran off a [virtual environment](http://www.virtualenv.org/en/latest/). In fact, this is the *recommended* approach. 


Available methods
-----------------

* `/api/version`

  Print API version.

* `/api/methods`

  Print available API methods.

* `/api/hosts`

  List hosts and groups in the inventory.

* `/api/groups`

  List groups in the inventory.

* `/api/listgroups/<host>`

  List groups based on host.

* `/api/listhosts/<group>`

  List hosts based on group.

* `/api/<module>/<pattern>`

  Request allowed module to perform action on host pattern.

* `/api/modules`

  List all allowed modules.
  
* `/api/uptime/<pattern>`

  Get uptime of specified host pattern.

* `/api/is/<status>`

  List servers according to status


Allowed modules
---------------

* `setup`

  Gather useful variables about remote hosts. Returns JSON dict.

* `ping`

  A trivial test module. Returns `pong` on successful contact.
