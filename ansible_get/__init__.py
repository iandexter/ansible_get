# -*- coding: utf-8 -*-

"""
Initiator for the web service.
"""

from flask import Flask

app = Flask(__name__)

import ansible_api.routes
