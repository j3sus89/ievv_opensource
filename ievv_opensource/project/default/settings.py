"""
Django settings for ievv_opensource project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from os.path import join
from os.path import dirname
import os


REPOROOT_DIR = dirname(dirname(dirname(dirname(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%a+ly@5m4g6fl2yhc2(i#cfz+x&_$uyh9o8%z6srhk)-)yzm('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'crispy_forms',
    'ievv_opensource.ievv_tagframework',
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(REPOROOT_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

DATETIME_INPUT_FORMATS = (
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
)

LANGUAGE_CODE = 'nb'
LOCALE_PATHS = (
    join(REPOROOT_DIR, 'locale'),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Setup static files to be served at /static/.
STATIC_URL = '/static/'

# Use bootstrap3 template pack to django-crispy-forms.
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Setup user uploads directory
MEDIA_ROOT = join(REPOROOT_DIR, 'media')
MEDIA_URL = '/media/'


# Thumbnails (sorl-thumbnail)
# See: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html
#THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'
#THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.cached_db_kvstore.KVStore'
#THUMBNAIL_PREFIX = 'sorlcache/'
#THUMBNAIL_DEBUG = False

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]

