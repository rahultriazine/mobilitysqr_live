"""
Django settings for family project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime
import pyodbc
from importlib import import_module
WEB_ENV = os.environ.get('WEB_ENV',"local")

try:
    setts = import_module('settings.%s'% WEB_ENV)
    globals().update(setts.__dict__)
except ImportError:
    pass

# =============== ENV Redirection=================

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start deveent settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=n1)7@ws=@^f&_xbq!q(v15aj29gd4ex+dv49f)ou80&0q6x%q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.1.230']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',  # https://django-extensions.readthedocs.io/en/latest/
    'mobility_apps.employee',
    # 'rest_framework.authtoken',
    'mobility_apps.master',
    'mobility_apps.travel',
    'mobility_apps.visa',
    'mobility_apps.letter',
    # 'mobility_apps.base',
    'mobility_apps.superadmin',
    # 'mobility_apps.reports',
    'rest_framework',
	'corsheaders',
     # 'rest-auth',
    'api',
    # 'oauth2_provider',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#CORS_ORIGIN_ALLOW_ALL = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend']



ROOT_URLCONF = 'settings.urls'


# PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'media/templates')],
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

WSGI_APPLICATION = 'settings.wsgi.application'

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.ext.rest_framework.OAuth2Authentication',
#     )
# }
REST_FRAMEWORK = {

'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    'pagination.CustomPagination',
),

}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
	'UNICODE_JSON': False,
}

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }

# staging_database
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'mob_test',
        'HOST': 'mobilitysqrdev.database.windows.net',
	    'PORT': '1433',
        'USER': 'mobilitysqr_admin',
        'PASSWORD': 'mob!@sqr1123573121',
        'OPTIONS': {
             'host_is_server': True,
             'driver':'ODBC Driver 17 for SQL Server',
        }
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'mobilitysqrpreprod',
#         'HOST': 'mobilitysqrdev.database.windows.net',
# 	'PORT': '1433',
#         'USER': 'mobilitysqr_admin',
#         'PASSWORD': 'mob!@sqr1123573121',
#         'OPTIONS': {
# 		 'host_is_server': True,'driver':'ODBC Driver 17 for SQL Server',
#         }
#     }
# }

CORS_ORIGIN_ALLOW_ALL = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JWT_AUTH = {
    # how long the original token is valid for
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),

    # allow refreshing of tokens
    'JWT_ALLOW_REFRESH': True,

    # this is the maximum time AFTER the token was issued that
    # it can be refreshed.  exprired tokens can't be refreshed.
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#AUTH_USER_MODEL = 'api.User'
AUTH_USER_MODEL = 'api.User'

TIME_ZONE =  'Asia/Kolkata'


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vikasy@triazinesoft.com'
EMAIL_HOST_PASSWORD = '9455@LOVE'
EMAIL_FROM ='vikasy@triazinesoft.com'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DATA_UPLOAD_MAX_NUMBER_FIELDS = 102400

from settings.settings_log import *