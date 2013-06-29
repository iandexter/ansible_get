# -*- coding: utf-8 -*-

"""
Launcher for the web service.
"""

from ansible_api import app

app.run(host = '0.0.0.0', port = 8000, debug = True)
