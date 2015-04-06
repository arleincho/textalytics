"""
Django settings for analitycs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from django.utils.translation import ugettext_lazy as _

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "5un?VT|fmX(_UU1UYZY}la1Hu5ztp5!y3nqe_Thain<ahH0Ieg9Eew@ophia1Hshi4)s'6aAXRkL8z2$h+1j=-d6#y0k2jyfog3baw+^iebah5eger$uraechohyoh3see9shaizu2fhu7bo7she_Th"
NEVERCACHE_KEY = "?%=UC?.L/UIb'O7Ksul8v3)Mo9WS;[4Bino.6ZJ1tl?cnTxej|xZ'VD@Zm|->qY'<i2FV\q6/sz.GmZ:V'69E^,#);X#&f#P)b)da43BW=)hen<ahH0Ieg9Eew@ophimae7aeph4ait"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'ecci.arley.co'
]
INTERNAL_IPS = ("127.0.0.1",)


# Application definition

INSTALLED_APPS = (
    # 'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'highcharts',
    'import_export',
    'djcelery',
    'lecciones',
    'tasks',
    'dashboard',
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

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.tz",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# STATICFILES_DIRS = (
#     STATIC_ROOT,
#     os.path.join(PROJECT_ROOT, "static"),
# )

# print os.path.join(PROJECT_ROOT, "static")


GRAPPELLI_ADMIN_TITLE = 'TextAlytics'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

PROJECT_NAME = DB_USER = DB_NAME = "textalytics"
DB_PASS = ":)J#lv:taaNX)zW7cY{wj(4~]@r+cka[kDk-.>CZ^Jj!z\9zt37!Hl"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': 'localhost'
    }
}


import djcelery
djcelery.setup_loader()


BROKER_URL = 'amqp://guest:guest@localhost:5672'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "celery",
    "taskmeta_collection": "textalytics" # Collection name to use for task output
}

CELERY_IMPORTS = ("tasks.tasks")

# The default Django db scheduler
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


DEFAULT_CHARSET = 'utf-8'

TIME_ZONE = "America/Bogota"
CELERY_TIMEZONE = 'America/Bogota'
CELERY_ENABLE_UTC = True

LANGUAGE_CODE = "es"

# Supported languages
LANGUAGES = (
    ('es', _('Spanish')),
)


TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

# STATIC_URL = '/static/'



LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'conf', 'locale'),
)


FABRIC = {
    "SSH_USER": "admin", # SSH username for host deploying to
    "SSH_PORT": 65372,
    "SSH_KEY_PATH": '/Users/arley/Dropbox/proyectos/skosh-data/skosh.pem',
    "HOSTS": ALLOWED_HOSTS[:1], # List of hosts to deploy to (eg, first host)
    "HOSTS": ALLOWED_HOSTS[:1], # List of domains to deploy to (eg, first host)
    "DOMAINS": ALLOWED_HOSTS, # Domains for public site
    "REPO_URL": "https://github.com/arleincho/textalytics.git", # Project's repo URL
    "VIRTUALENV_HOME":  "/var/textalytics", # Absolute remote path for virtualenvs
    "PROJECT_NAME": PROJECT_NAME, # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt", # Project's pip requirements
    "GUNICORN_PORT": 8070, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "DB_PASS": DB_PASS, # Live database password
    "ADMIN_PASS": "lzv0p6t6wcbh&s=h", # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}