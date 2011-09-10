#!/usr/bin/python

import os
import sys

userdir = os.path.expanduser('~jathan')
project_dir = os.path.join(userdir, 'sandbox/topdouche.com')
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'topdouche.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
