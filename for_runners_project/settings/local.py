# flake8: noqa: E405

"""
    Django settings for local development


"""

import sys as __sys

from for_runners_project.settings.base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Serve static/media files for local development:
SERVE_FILES = True


# Disable caches:
CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}

# Required for the debug toolbar to be displayed:
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost')

ALLOWED_HOSTS = INTERNAL_IPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_PATH / 'Django-ForRunners-database.sqlite3'),
        # https://docs.djangoproject.com/en/dev/ref/databases/#database-is-locked-errors
        'timeout': 30,
    }
}
print(f'Use Database: {DATABASES["default"]["NAME"]!r}', file=__sys.stderr)

# _____________________________________________________________________________

# Download map via geotiler in for_runners.gpx_tools.gpxpy2map.generate_map
MAP_DOWNLOAD = True

# Auto login for dev. server:
MIDDLEWARE = MIDDLEWARE.copy()
MIDDLEWARE += ['django_tools.middlewares.local_auto_login.AlwaysLoggedInAsSuperUserMiddleware']

# _____________________________________________________________________________
# Django-Debug-Toolbar

INSTALLED_APPS = INSTALLED_APPS.copy()
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

DEBUG_TOOLBAR_PATCH_SETTINGS = True
from debug_toolbar.settings import CONFIG_DEFAULTS as DEBUG_TOOLBAR_CONFIG  # noqa


# Disable some more panels that will slow down the page:
DEBUG_TOOLBAR_CONFIG['DISABLE_PANELS'].add('debug_toolbar.panels.sql.SQLPanel')
DEBUG_TOOLBAR_CONFIG['DISABLE_PANELS'].add('debug_toolbar.panels.cache.CachePanel')

# don't load jquery from ajax.googleapis.com, just use django's version:
DEBUG_TOOLBAR_CONFIG['JQUERY_URL'] = STATIC_URL + 'admin/js/vendor/jquery/jquery.min.js'

DEBUG_TOOLBAR_CONFIG['SHOW_TEMPLATE_CONTEXT'] = True
DEBUG_TOOLBAR_CONFIG['SHOW_COLLAPSED'] = True  # Show toolbar collapsed by default.
DEBUG_TOOLBAR_CONFIG['SHOW_TOOLBAR_CALLBACK'] = 'for_runners_project.middlewares.djdt_show'
