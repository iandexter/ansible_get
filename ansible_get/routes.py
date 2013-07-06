# -*- coding: utf-8 -*-

"""
Routes for the Ansible RESTful API.
"""

from ansible_api import app
from flask import jsonify, request
from ansible import runner, inventory

__appname__ = 'ansible_get - Ansible RESTful API'
__version__ = '0.5'

allowed_modules = ['setup', 'ping']

# Helpers

def respond_with(body = {}, status = 200):
    """Format API response"""
    response = jsonify(body)
    response.headers['X-Title'] =  "%s v%s" % (__appname__, __version__)
    response.status_code = status
    return response

def no_result():
    return respond_with({ 'result': [] }, 200)

def get_servers(status = None):
    """List all servers based on status"""
    results = runner.Runner(module_name='ping', module_args='',
                            pattern='all', forks=10).run()
    return results[status].items()


# Routes

@app.errorhandler(404)
def not_found(error = None):
    message = { 'status': 404, 'Message': "Not Found: %s" % (request.path) }
    return respond_with(message, 404)

@app.route('/api/version', methods = ['GET'])
def list_version():
    """Print API version"""
    return respond_with({ 'version': __version__ }, 200)

@app.route('/api/methods', methods = ['GET'])
def list_methods():
    """Print available API methods"""
    api_methods = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods = rule.methods.difference(['OPTIONS', 'HEAD'])
            helper_text = "%s (%s)" % (app.view_functions[rule.endpoint].__doc__,
                                      " ".join(methods))
            api_methods[rule.rule] = helper_text
    return respond_with(api_methods, 200)

@app.route('/api/modules', methods = ['GET'])
def list_modules():
    """List all allowed modules"""
    return respond_with({ 'allowed_modules': allowed_modules }, 200)

@app.route('/api/<module>/<pattern>', methods = ['GET'])
def get_response(module = None, pattern = None):
    """Request allowed module to perform action on host pattern"""
    if module not in allowed_modules:
        msg = "Module %s is not allowed or is not a valid module" \
		      % ((request.path).split('/')[2])
        message = { 'status': 405, 'Message': msg }
        return respond_with(message, 405)
    else:
        conn = runner.Runner(pattern = pattern, timeout = 30)
        conn.module_name = module
        result = conn.run()
        return respond_with(result, 200)

@app.route('/api/hosts', methods = ['GET'])
def list_hosts():
    """List hosts and groups in the inventory"""
    this_inv = inventory.Inventory()
    return respond_with(this_inv.groups_list(), 200)

@app.route('/api/groups', methods = ['GET'])
def list_groups():
    """List groups in the inventory"""
    this_inv = inventory.Inventory()
    return respond_with({ 'groups': this_inv.list_groups() }, 200)

@app.route('/api/listhosts/<group>', methods = ['GET'])
def get_hosts(group = 'all'):
    """List hosts based on group"""
    this_inv = inventory.Inventory()
    hosts = this_inv.list_hosts(group)
    if not hosts:
        return no_result()
    else:
        return respond_with({ group: hosts }, 200)

@app.route('/api/listgroups/<host>', methods = ['GET'])
def get_groups(host = None):
    """List groups based on host"""
    this_inv = inventory.Inventory()
    groups = this_inv.groups_for_host(host)
    grouplist = []
    if not groups:
        return no_result()
    else:
        for g in groups:
            grouplist.append(g.name)
            grouplist.sort()
        return respond_with({ host: grouplist }, 200)

@app.route('/api/uptime/<pattern>', methods = ['GET'])
def get_uptime(pattern = None):
    """Get uptime of specified host pattern"""
    conn = runner.Runner(pattern = pattern, forks=10)
    conn.module_name = 'command'
    conn.module_args = '/usr/bin/uptime'
    result = conn.run()
    return respond_with(result, 200)

@app.route('/api/is/<status>', methods = ['GET'])
def get_server_status(status = None):
    """List servers according to status"""
    if status == 'up':
        server_status = 'contacted'
    elif status == 'down':
        server_status = 'dark'
    else:
        return no_result()
    results = get_servers(server_status)
    return respond_with({ status: results }, 200)
