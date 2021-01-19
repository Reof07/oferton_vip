import json
import os

from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = True


ALLOWED_HOSTS = []

with open(os.path.join('secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('POSTGRESQL_NAME'),
        'USER': get_secret('POSTGRESQL_USER'),
        'PASSWORD': get_secret('POSTGRESQL_PASS'),
        'HOST': get_secret('POSTGRESQL_HOST'), 
        'PORT': get_secret('POSTGRESQL_PORT'),
    }
}