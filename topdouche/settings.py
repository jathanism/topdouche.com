# -*- coding: utf-8 -*-
# Django settings for topdouche project.

import os
import logging
import sys

PROJECT_DIR = os.path.normpath(os.path.dirname(__file__))

# =========================
# Debug
# =========================
DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Flip this if you want the dev versions of servers 
DEV = False
#DEV = True

# Whether the framework should propagate raw exceptions rather than catching
# them. This is useful under some testing siutations and should never be used
# on a live site.
DEBUG_PROPAGATE_EXCEPTIONS = True

# =========================
# Logging
# =========================
logging.basicConfig(
    #format="%(asctime)s [%(levelname)s]: %(lineno)d %(message)s",
    format="*** %(asctime)s [%(levelname)s]: %(message)s",
    level=logging.CRITICAL,
)
LOGGER = logging.getLogger(__name__)
#if DEBUG:
#    LOGGER.setLevel(logging.DEBUG)
LOGGER.setLevel(logging.DEBUG)

# =========================
# Email
# =========================
# A tuple that lists people who get code error notifications. When DEBUG=False
# and a view raises an exception, Django will e-mail these people with the full
# exception information. Each member of the tuple should be a tuple of (Full
# name, e-mail address). 
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Jathan McCollum', 'jathan@gmail.com'),
)

#  A tuple in the same format as ADMINS that specifies who should get broken-link
#  notifications when SEND_BROKEN_LINK_EMAILS=True
MANAGERS = (
    ('Jathan McCollum', 'jathan@gmail.com'),
)

#EMAIL_HOST = 'example.com'

# If sender isn't specified with send_email(), use this instaed
DEFAULT_FROM_EMAIL = 'hoss@topdouche.com'

# =========================
# Database
# =========================
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db/default.db'),
    },
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'topdouche',
        'USER': 'postgres',
        'PASSWORD': 'Password@123',
        #'OPTIONS': {
        #    'autocommit': True
        #},
    }
}

# =========================
# Globals
# =========================
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = ''
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ra-ph^2+ulp=)0ebq5-%g-y0hkoy^)oy!=q&1sw+0w7@&^3d+&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader', # Django 1.3
    'django.template.loaders.app_directories.Loader', # (Django 1.3)
    #'django.template.loaders.eggs.load_template_source',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'topdouche.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
    os.path.join(PROJECT_DIR, 'templates'),
    '/usr/local/lib/python2.6/dist-packages/django/contrib/admin/templates', # For admin
)

# This is to be able to add 'settings' to RequestContext
_context = {}
_local_context = locals()
def settings_context(context):
    for k,v in _local_context.items():
        if k.isupper():
            _context[k] = v

    return {'settings': _context}

# Override the default context processors that add variables to the
# RequestContext sent to templates.
TEMPLATE_CONTEXT_PROCESSORS = (
    # Defaults 
    'django.contrib.auth.context_processors.auth', # Adds 'user', 'perms' (Django 1.3)
    'django.core.context_processors.debug', # Adds 'debug', 'sql_queries'
    'django.core.context_processors.i18n',  # Adds 'LANGUAGES'
    'django.core.context_processors.media', # Adds 'MEDIA_URL'
    # Extra
    'django.core.context_processors.request', # Adds 'request' 
    'topdouche.settings.settings_context', # Custom context, see above
    #'django.core.context_processors.static', # Adds 'STATIC_URL' (New in 1.3)
    #'django.contrib.messages.context_processors.messages', # Adds 'messages' (New in 1.2)
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    ## custom
    'django.contrib.formtools',
    'taggit',
    'api',
)

STATIC_DOC_ROOT = os.path.join(os.getcwd(), 'site_media')


# =========================
# Authentication
# =========================
LOGIN_URL = '/login/'
#LOGIN_URL_EXTERNAL = 'https://whatever/login'
#LOGIN_REDIRECT_URL = '/foo/' # Defaults to '/profile/'
LOGOUT_URL = '/logout/'
#AUTH_PROFILE_MODULE = 'topdouche.UserProfile'

# Sessions
# =========================
# Needed so that the Django session doesn't last longer than the SSO token. We
# might need to make it shorter, but this is a start. Time must be in seconds.
#SESSION_COOKIE_AGE = 86400 # 24 hours, in seconds
#SESSION_COOKIE_AGE = 43200 # 12 hours, in seconds
SESSION_COOKIE_AGE = 60 * 60 # 60 minutes

# NOTE that Django does not automatically cleanup expired sessions. This will
# need to be done manually periodically by way of:
# django-admin.py cleanup --settings='topdouche.settings' --pythonpath='/home/j/jathan/sandbox'

# The domain to use for session cookies. Set this to a string such as
# ".lawrence.com" (note the leading dot!) for cross-domain cookies, or use None
# for a standard domain cookie.
#SESSION_COOKIE_DOMAIN = '.topdouche.com'
