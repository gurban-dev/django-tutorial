from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# In production means ready to be made public.
DEBUG = True

'''
"localhost" is a domain name for accessing local network
services, while "127.0. 0.1" and "::1" are loopback IP
addresses for IPv4 and IPv6, respectively, used for
device communication. The transition to IPv6, offering a
larger address space, is crucial for modern networking.'''
ALLOWED_HOSTS = [
	# 127.0.0.1 is the IP address.
	'127.0.0.1',

	'localhost',
	# '*' will match anything.
	# '*'
]

INSTALLED_APPS = [
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'playground',
	'debug_toolbar',
	'store',
	'tags',
	'rest_framework',
	'quickstart',
	'snippets',
	'polls.apps.PollsConfig'
]

# The global settings for a REST framework API are kept in
# a single configuration dictionary named REST_FRAMEWORK.
REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	],

	# Pagination dictates how many objects
	# per page are returned.
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10
}

MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.common.BrokenLinkEmailsMiddleware'
]

INTERNAL_IPS = [
  "127.0.0.1",
]

ROOT_URLCONF = 'storefront.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			# Added so that Django could find the "templates"
			# directory located in the project's root directory.
			BASE_DIR.joinpath('templates')
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			]
		}
	}
]

WSGI_APPLICATION = 'storefront.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

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
	}
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-GB'

# United Kingdom: en-GB
# Egyptian Arabic: ar-GE
# Azeri: az-Latn
# Russian: ru-RU
# Georgian: ka

TIME_ZONE = 'Asia/Tbilisi'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'static_root'

STATIC_URL = 'static/'

# For static files used across the entire project,
# it's common to create a project-level static
# folder instead.
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

# For receiving emails about 404 HTTP status codes.
MANAGERS = [("gurbanoglu", "dennisgurban44@gmail.com")]

# For receiving emails regarding 500 HTTP status codes.
ADMINS = [
  ("gurbanoglu", "dennisgurban44@gmail.com")
]

LOGGING = {
	# The dictConfig format version.
	"version": 1,

	# Retain the default loggers.
	"disable_existing_loggers": False,
	"handlers": {
		"mail_admins": {
			"level": "ERROR",
			"class": "django.utils.log.AdminEmailHandler",
			"include_html": True,
		}
	}
}