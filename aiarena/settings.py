"""
Django settings for aiarena project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta
from enum import Enum

from aiarena.core.utils import Elo, EnvironmentType

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't*4r1u49=a!ah1!z8ydsaajr!lv-f(@r07lm)-9fro_9&67xqd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aiarena',
        'USER': 'aiarena',
        'PASSWORD': 'aiarena',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        # todo: having this enabled will open a transaction for every request and therefore slow down the site
        # todo: ideally we will eventually remove this and specify each individual view that needs its own transaction.
        'ATOMIC_REQUESTS': True,
    }
}

# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'avatar',
    'aiarena.core',
    'aiarena.api',
    'private_storage',
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'django_nyt.apps.DjangoNytConfig',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki.apps.WikiConfig',
    'wiki.plugins.attachments.apps.AttachmentsConfig',
    'wiki.plugins.notifications.apps.NotificationsConfig',
    'wiki.plugins.images.apps.ImagesConfig',
    'wiki.plugins.macros.apps.MacrosConfig',
    'wiki.plugins.help.apps.HelpConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aiarena.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'aiarena.core.context_processors.stats',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

REST_FRAMEWORK = {
    # Default to allow access only for admin users
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        # 'django_filters.rest_framework.DjangoFilterBackend',
        # todo: check that opening this generically doesn't leak sensitive info.
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'warning-file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': './logs/django-warning.log',
            'formatter': 'verbose',
        },
        'critical-file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './logs/django-critical.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['warning-file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'aiarena': {
            'handlers': ['warning-file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['critical-file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'aiarena': {
            'handlers': ['critical-file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

WSGI_APPLICATION = 'aiarena.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(APP_DIR, "static"),
]

# public media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Private media storage
# https://github.com/edoburu/django-private-storage
PRIVATE_STORAGE_ROOT = os.path.join(BASE_DIR, "private-media")

# Random scripts such as SQL
SCRIPTS_ROOT = os.path.join(BASE_DIR, "scripts")

# registration
# https://django-registration-redux.readthedocs.io/en/latest/default-backend.html
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
DEFAULT_FROM_EMAIL = 'noreply@localhost'

# Redirect to index page on login/logout
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Custom user model
AUTH_USER_MODEL = "core.User"

# file system permissions of uploaded files
# this needs to be set, otherwise large files can end up with the wrong permissions.
# https://code.djangoproject.com/ticket/28540
FILE_UPLOAD_PERMISSIONS = 0o644

# elo_k for calculating ladder ELO updates
ELO_K = 16

# starting ELO for bots
ELO_START_VALUE = 1600

# Enable a sanity check every time a result is submitted
ENABLE_ELO_SANITY_CHECK = True

# If an arena client requests a match when it has unfinished matches in the queue, reissue it one of the unfinished ones
REISSUE_UNFINISHED_MATCHES = True

# ELO implementation
ELO = Elo(ELO_K)

MAX_USER_BOT_COUNT = 6
MAX_USER_BOT_COUNT_ACTIVE_PER_RACE = 1

# The maximum active rounds allowed at any one time.
# The ladder will stop generating new rounds once this number is reached until previous active rounds are finished off.
MAX_ACTIVE_ROUNDS = 2

# For convenience
BOT_ZIP_MAX_SIZE_MB = 50
# this is the setting that actually dictates the max zip size
BOT_ZIP_MAX_SIZE = 1024 * 1024 * BOT_ZIP_MAX_SIZE_MB

# how long to wait before the website should time out a running match
TIMEOUT_MATCHES_AFTER = timedelta(hours=1)

# This will post results received to another webserver
# if this is None, it is disabled
POST_SUBMITTED_RESULTS_TO_ADDRESS = None

# django-avatar
# https://django-avatar.readthedocs.io/en/latest/
# Cleanup avatar images on deletion
AVATAR_CLEANUP_DELETED = True
# disable the cache until we need it - it causes a user's avatar change to take a while to be reflected
AVATAR_CACHE_ENABLED = False
# pre-generate the most commonly used size
AVATAR_AUTO_GENERATE_SIZES = (150,)
# this fixes PNGs breaking when uploaded
AVATAR_THUMB_FORMAT = 'PNG'

ENVIRONMENT_TYPE = EnvironmentType.DEVELOPMENT

# whether to run matches
LADDER_ENABLED = True

# django wiki
WIKI_ACCOUNT_HANDLING = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = False
SITE_ID = 1

# override any of these settings with an env.py file
try:
    from aiarena.env import *
except ImportError as e:
    if e.name != 'aiarena.env':
        raise
