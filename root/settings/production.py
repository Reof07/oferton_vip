from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ofertonvip.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = { 'default': dj_database_url.config() }

django_heroku.settings(locals())