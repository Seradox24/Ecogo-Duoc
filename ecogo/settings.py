"""
Django settings for ecogo project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from django.utils.html import format_html


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-08*br$bv^h5p1)ug01l27s1c)51@wv$qub&1fd-5h8*b%v-)=y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','http://ecogo.brazilsouth.cloudapp.azure.com','ecogo.cloud','http://ecogo.cloud','https://ecogo.cloud']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'alumno',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
ROOT_URLCONF = 'ecogo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ecogo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Ecogo",
        "USER": "fl0user",
        "PASSWORD": "j1olWNaG4LEq",
        "HOST": "ep-fragrant-recipe-85739519.us-east-2.aws.neon.fl0.io",
        "PORT": "5432",
    }
}

'''

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "admin_ecogo",
        "PASSWORD": "pass_ecogo2023",
        "HOST": "ecogo-db.postgres.database.azure.com",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

#STATIC_URL = 'static/'



STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'resetprizus@gmail.com'
EMAIL_HOST_PASSWORD = 'nkqzgcoubezwtpqd'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Eco-Go Administracion",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Backend Eco-Go",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Backend Eco-go",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "",
    "site_logo_classes": "",
    
    "copyright": "Desarrollado por <a href='https://www.admin.cl/' target='_blank'>Eco-Go</a>",
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
    "user_avatar": None,

    
}