# -*- coding: utf-8 -*-

"""
ansible_get - A RESTful API built on Flask to get Ansible objects.
"""

from setuptools import setup

setup(
    name = 'Ansible RESTful API',
    version = '0.5',
    description = 'Web service for getting Ansible objects',
    long_description = __doc__,
    author = 'Ian Dexter D. Marquez',
    author_email = 'iandexter+tech@gmail.com'
    packages = ['ansible_get'],
    include_package_data = True,
    zip_safe = False,
    install_requires = ['Flask']
)
