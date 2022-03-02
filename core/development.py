from .base import *

import socket

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y$@!yer6rqez&@^*c5w+gu+kry-o0rf&@7g63ozls-7=epg9=u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': "ilm",
        'HOST': "postgres",
        'PORT': "5432",
        'USER': "postgres",
        'PASSWORD': "postgres"
    }
}

# Internal IPs for Debug Toolbar (Docker)
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

# Authentication
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
CORS_ORIGIN_ALLOW_ALL = True
