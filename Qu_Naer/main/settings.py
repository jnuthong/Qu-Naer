"""
Django settings for Qu_Naer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm8=0qg2)8gx3b!nl-z)c)828m+g@j@591#msb-y51+b7)*!dmp'

# ACCESS KEY
ACCESS_KEY = 'df^has83$47kj!gha31jk_dg46f%aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
CSRF_COOKIE_DOMAIN = '127.0.0.1'

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_extensions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # our apps
    'mapi',
    'apps.profile',
    'apps.user',
    'apps.user_third',
    # 'utils',
    # 'apps.comment',
    # 'apps.message',
    # 'apps.post',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

AUTH_USER_MODEL = 'apps.profile.UserProfile'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#################### Database setting ####################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "devdb",
        'HOST': "localhost",
        'PORT': "5432",
        'USER': "postgres",
        'PASSWORD': "postgres",
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

AUTH_USER_MODEL = 'user.SUser'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# CSRF_COOKIE_SECURE = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#################### Caches settings ####################
import redis_cache
import redis

REDIS_CACHE_POOL = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 1,
    'desc': 'default pool for django'
}

REDIS_USER_POOL = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 2,
    'desc': 'default pool for user'
}

# REDIS_CACHE_POOL = redis.ConnectionPool(host=REDIS_CACHE_POOL['host'],
#                                        port=REDIS_CACHE_POOL['port'],
#                                        db=REDIS_CACHE_POOL['db'])
#
# REDIS_USER_POOL = redis.ConnectionPool(host=REDIS_USER_POOL['host'],
#                                        port=REDIS_USER_POOL['port'],
#                                        db=REDIS_USER_POOL['db'])

default_cache_location = '%s:%d:%s' % (REDIS_CACHE_POOL['host'], REDIS_CACHE_POOL['port'],REDIS_CACHE_POOL['db'])
user_cache_location = '%s:%d:%s' % (REDIS_USER_POOL['host'], REDIS_USER_POOL['port'],REDIS_USER_POOL['db'])

CACHES = {
            'default': {
                'BACKEND': 'redis_cache.cache.RedisCache',
                'LOCATION': default_cache_location,
                'TIMEOUT': 60 * 10,
            },
            'user_info_cache': {
                'BACKEND': 'redis_cache.cache.RedisCache',
                'LOCATION': user_cache_location,
                'TIMEOUT': 60 * 60 * 24 * 10,
            },
}

# ===========
# = Session =
# ===========
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

SESSION_ENGINE = 'redis_sessions.session'
SITE_ID = 1