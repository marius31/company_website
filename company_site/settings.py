import os
from django.conf.global_settings import *
import socket

this = os.path.realpath(__file__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(this))

#development environment settings
if socket.gethostname() == 'eu-VirtualBox':
    DEBUG = TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    INSTALLED_APPS += (
    'debug_toolbar',
    )
    MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'company_site/sitestatic')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'company_site/static/'),
    )
    STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'company_site/media/')
    MEDIA_URL = '/media/'
    ADMIN_MEDIA_PREFIX = '/static/admin/'

#live envinronment settings
else:
    DEBUG = TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['46.101.188.181']

ADMINS = (
    ('Admin', 'marius.gheorghe22@yahoo.com'),
)
MANAGERS = ADMINS
#SERVER_EMAIL = 'amenajariprofi@gmail.com'
#Marius - creeaza un cont de gmail special pentru site-ul asta

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'company_site.urls'

WSGI_APPLICATION = 'company_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'company_site/templates/'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*qf*wyyb*=5ctb+6ak9rccjmh2gcr)o7g0&qsogx&4#*1fo+22'

################################################################################
### Emailing
################################################################################
from . import extra_data
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = extra_data.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = extra_data.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
