import os
from .settings import *  # noqa: F403
from .settings import BASE_DIR

SECRET_KEY = os.getenv['SECRET']
# ALLOWED_HOSTs=[os.getenv['WEBSITE_HOSTNAME']]
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS=['https://'+ os.getenv['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '',
#         'HOST': '',
#         'USER': '',
#         'PASSWORD': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv['AZURE_MYSQL_NAME'],
        'HOST': os.getenv['AZURE_MYSQL_HOST'],
        'USER': os.getenv['AZURE_MYSQL_USER'],
        'PASSWORD': os.getenv['AZURE_MYSQL_PASSWORD'],
    }
}
