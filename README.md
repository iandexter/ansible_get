ansible_get - Ansible RESTful API
=================================

ansible_get - A RESTful API built on Flask to `GET` Ansible objects.

Host: `0.0.0.0` 

Port: `8000`


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


Allowed modules
---------------

* `setup`

    Gather useful variables about remote hosts. Returns JSON dict.

* `ping`

    A trivial test module. Returns `pong` on successful contact.
