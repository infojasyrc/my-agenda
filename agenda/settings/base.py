"""
Generated by 'django-admin startproject' using Django 1.8.5.
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#d=g&cy%!2sn6fa^a$@zi+a=4*k&fnojdc1de-g^ondg5#98_5'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']

# Database empty default
DATABASES = {
    'default': {}
}

# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    'apps.companies',
    'apps.skills',
    'apps.projects',
    'apps.contacts',
    'apps.levels',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'agenda.urls'

WSGI_APPLICATION = 'agenda.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    PROJECT_DIR.child('assets'),
)

#Media files
MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'
