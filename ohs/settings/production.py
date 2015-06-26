from .base import *

import os
# Disable debug mode


DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET')

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PASSWORD': os.environ.get('DB_ENV_POSTGRES_PASSWORD', os.environ.get('POSTGRES_PASSWORD')),
        'PORT': 5432,
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}


# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'ohs',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }


STATIC_URL = '/'
MEDIA_URL = '/media/'

import logging

LOGGING = {
    'version': 1,
    'root': {'level': 'DEBUG' if DEBUG else 'INFO'},
}


try:
    from .local import *
except ImportError:
    pass
