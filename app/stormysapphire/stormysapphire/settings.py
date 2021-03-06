# -*- encoding: utf-8 -*-
"""
Django settings for stormysapphire project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't^4z)jq3^4#b-2v5yv*%&3tdn0-vvqid-#i9_a(!y&=+&ny#i+'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'accountgroup',
    'menu',
    'participant',
    'participantgroup',
    'reserve'
)

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

ROOT_URLCONF = 'stormysapphire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'stormysapphire/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stormysapphire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'stormy_sapphire',
        'PASSWORD': '',
        'PORT': 3306,
        'USER': 'root'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ja-Jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'var', 'data', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, '..', '..', 'var', 'www'),)

_APPLICATION_LOG_DIR = os.path.join(BASE_DIR, '..', '..', 'var', 'log',
                                    'django')
_LOG_LEVEL = 'DEBUG'
LOGGING = {
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('[' '%(asctime)s ' '%(process)d ' '%(thread)d '
                       '%(levelname)s ' '%(pathname)s:' '%(lineno)s' '] '
                       '%(message)s')
        }
    },
    'handlers': {
        'common': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(_APPLICATION_LOG_DIR, 'common.log'),
            'formatter': 'verbose',
            'level': _LOG_LEVEL
        },
        'console': {'class': 'logging.StreamHandler', 'level': _LOG_LEVEL}
    },
    'loggers': {
        'common': {'handlers': ['common'], 'level': _LOG_LEVEL,
                   'propagate': True},
        'console': {'handlers': ['console'], 'level': _LOG_LEVEL,
                    'propagate': True}
    },
    'version': 1
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/main_menu'

ATOMIC_REQUESTS = True

API_KEY = 'QdcsVGsNiShgbRvHEF5RnTkDq4UhNI5HVfXCMBB7'

GOOGLE_API_KEY = 'xxxx'

HOLIDAYS = {
    '2015-01-01': u'元日',
    '2015-01-12': u'成人の日',
    '2015-02-11': u'建国記念の日',
    '2015-03-21': u'春分の日',
    '2015-04-29': u'昭和の日',
    '2015-05-03': u'憲法記念日',
    '2015-05-04': u'みどりの日',
    '2015-05-05': u'こどもの日',
    '2015-05-06': u'憲法記念日 振替休日',
    '2015-07-20': u'海の日',
    '2015-09-21': u'敬老の日',
    '2015-09-22': u'国民の休日',
    '2015-09-23': u'秋分の日',
    '2015-10-12': u'体育の日',
    '2015-11-03': u'文化の日',
    '2015-11-23': u'勤労感謝の日',
    '2015-12-23': u'天皇誕生日',
    '2016-01-01': u'元日',
    '2016-01-11': u'成人の日',
    '2016-02-11': u'建国記念の日',
    '2016-03-20': u'春分の日',
    '2016-03-21': u'春分の日 振替休日',
    '2016-04-29': u'昭和の日',
    '2016-05-03': u'憲法記念日',
    '2016-05-04': u'みどりの日',
    '2016-05-05': u'こどもの日',
    '2016-07-18': u'海の日',
    '2016-08-11': u'山の日',
    '2016-09-19': u'敬老の日',
    '2016-09-22': u'秋分の日',
    '2016-10-10': u'体育の日',
    '2016-11-03': u'文化の日',
    '2016-11-23': u'勤労感謝の日',
    '2016-12-23': u'天皇誕生日',
    '2017-01-01': u'元日',
    '2017-01-02': u'元日 振替休日',
    '2017-01-09': u'成人の日',
    '2017-02-11': u'建国記念の日',
    '2017-03-20': u'春分の日',
    '2017-04-29': u'昭和の日',
    '2017-05-03': u'憲法記念日',
    '2017-05-04': u'みどりの日',
    '2017-05-05': u'こどもの日',
    '2017-07-17': u'海の日',
    '2017-08-11': u'山の日',
    '2017-09-18': u'敬老の日',
    '2017-09-23': u'秋分の日',
    '2017-10-09': u'体育の日',
    '2017-11-03': u'文化の日',
    '2017-11-23': u'勤労感謝の日',
    '2017-12-23': u'天皇誕生日',
}
