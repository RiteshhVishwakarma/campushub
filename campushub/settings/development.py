"""
Development settings for campushub project.
"""
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_&ns+68tj__r@m#kl71-8ola$ww-za2bykbs++^%k7=f2-id!j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
