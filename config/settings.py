"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import json
import socket
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = json.loads(os.getenv("DEBUG", "false"))

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1 .localhost [::1]",
).split(" ")

CSRF_TRUSTED_ORIGINS = os.getenv(
    "CSRF_TRUSTED_ORIGINS",
    "http://127.0.0.1 http://localhost",
).split(" ")

CSRF_COOKIE_SECURE = json.loads(os.getenv("CSRF_COOKIE_SECURE", "true"))

SESSION_COOKIE_SECURE = json.loads(os.getenv("SESSION_COOKIE_SECURE", "true"))

CSRF_COOKIE_HTTPONLY = json.loads(os.getenv("CSRF_COOKIE_HTTPONLY", "true"))

SESSION_COOKIE_HTTPONLY = json.loads(os.getenv("SESSION_COOKIE_HTTPONLY", "true"))

SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE", "Lax")

SESSION_ENGINE = os.getenv("SESSION_ENGINE", "django.contrib.sessions.backends.cache")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sorl.thumbnail',
    'bootstrap5',
    'debug_toolbar',


    'art_vostorg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.http.ConditionalGetMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}




CACHE_MIDDLEWARE_SECONDS = json.loads(os.getenv("CACHE_MIDDLEWARE_SECONDS", "0"))

CACHE_MIDDLEWARE_ALIAS = os.getenv("CACHE_MIDDLEWARE_ALIAS", "default")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Setting Email configuration for sending reset email
ENABLED_EMAIL = json.loads(os.getenv("ENABLED_EMAIL", "false"))

if ENABLED_EMAIL:
    EMAIL_USE_TLS = json.loads(os.getenv("EMAIL_USE_TLS", "true"))

    EMAIL_HOST = os.getenv("EMAIL_HOST")

    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

    EMAIL_PORT = json.loads(os.getenv("EMAIL_PORT", "25"))
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Internationalization
LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# Yandex S3 API
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# https://cloud.yandex.com/en/docs/storage/s3/
ENABLED_YANDEX_STORAGE = json.loads(os.getenv("ENABLED_YANDEX_STORAGE", "false"))

if ENABLED_YANDEX_STORAGE:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    AWS_DEFAULT_ACL = "public-read"

    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

    YANDEX_OBJECT_STORAGE_BUCKET_NAME = os.getenv("YANDEX_OBJECT_STORAGE_BUCKET_NAME")

    YANDEX_S3_DOMAIN = os.getenv("YANDEX_S3_DOMAIN")

    AWS_S3_CUSTOM_DOMAIN = f"{YANDEX_OBJECT_STORAGE_BUCKET_NAME}{YANDEX_S3_DOMAIN}"

    # S3 static settings
    STATIC_LOCATION = "static"

    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"

    STATICFILES_STORAGE = "common.custom_storage.StaticYandexCloudStorage"

    # S3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"

    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"

    DEFAULT_FILE_STORAGE = "common.custom_storage.MediaYandexCloudStorage"
else:
    NAME_STATIC_DIR = os.getenv("NAME_STATIC_DIR", "static")

    STATIC_ROOT = BASE_DIR / NAME_STATIC_DIR

    STATIC_URL = f"{NAME_STATIC_DIR}/"

    NAME_MEDIA_DIR = os.getenv("NAME_MEDIA_DIR", "media")

    MEDIA_ROOT = BASE_DIR / NAME_MEDIA_DIR

    MEDIA_URL = f"{NAME_MEDIA_DIR}/"


STATICFILES_DIRS = [
    BASE_DIR / "assets",  # place for favicon.ico
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Setting for django-debug-tool-bar
if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [f"{ip[:-1]}1" for ip in ips] + ["127.0.0.1"]
