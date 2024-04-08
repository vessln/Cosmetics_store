import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


SECRET_KEY = 'django-insecure--*_w@i9p3l79j+8f&eu0q^kwv51u(-p@(i3$p)@r^0^%7x*9_h'


# DEBUG = os.environ.get("DEBUG", "1") == "1"
# DEBUG = False
DEBUG = True
ALLOWED_HOSTS = []

# ALLOWED_HOSTS = ["bestbeauty.azurewebsites.net", "localhost"]
# CSRF_TRUSTED_ORIGINS = [f'https://{host}' for host in ALLOWED_HOSTS]

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise.runserver_nostatic',

    'cosmetics_store.common',
    'cosmetics_store.accounts',
    'cosmetics_store.blog',
    'cosmetics_store.products',
    'cosmetics_store.orders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cosmetics_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'cosmetics_store.wsgi.application'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
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
    },
]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = ()


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles/"
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_ROOT = BASE_DIR / 'static'


MEDIA_ROOT = BASE_DIR / "mediafiles"

MEDIA_URL = "/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.StoreUserModel"


LOGIN_REDIRECT_URL = "home page"

