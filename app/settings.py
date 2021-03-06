import os
from viewer.settings_common import *

DEBUG_LOGGING = True

ALLOWED_HOSTS.append('127.0.0.1')
ALLOWED_HOSTS.append('localhost')
##
ALLOWED_HOSTS.append('web.viewer-spin.sandbox.stable.spin.nersc.org')
ALLOWED_HOSTS.append('web.viewer-spin.dev-cattle.stable.spin.nersc.org')
ALLOWED_HOSTS.append('spin.legacysurvey.org')
ALLOWED_HOSTS.append('spin-dev.legacysurvey.org')
ALLOWED_HOSTS.append('dev.legacysurvey.org')
ALLOWED_HOSTS.append('a.dev.legacysurvey.org')
ALLOWED_HOSTS.append('b.dev.legacysurvey.org')
ALLOWED_HOSTS.append('c.dev.legacysurvey.org')
ALLOWED_HOSTS.append('d.dev.legacysurvey.org')

STATIC_TILE_URL_B = 'http://{s}.imagine.legacysurvey.org/static/tiles/{id}/{ver}/{z}/{x}/{y}.jpg'
SUBDOMAINS_B = ['a','b','c','d']

#DATABASE_ROUTERS = ['cat.models.Router']

HOSTNAME = 'localhost'

ROOT_URL = ''
SUBDOMAINS = []

STATIC_URL = '/static/'
STATIC_ROOT = None

TILE_URL = 'http://{s}.%s%s/{id}/{ver}/{z}/{x}/{y}.jpg' % ('legacysurvey.org', '/viewer-dev')
CAT_URL = '/{id}/{ver}/{z}/{x}/{y}.cat.json'
STATIC_TILE_URL = 'http://{s}.legacysurvey.org/viewer-dev/static/tiles/{id}/{ver}/{z}/{x}/{y}.jpg'

