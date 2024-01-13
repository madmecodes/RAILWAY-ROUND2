from pathlib import Path
from dotenv import load_dotenv
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-w-r!)wn-g1e-c$hmjl37pa4px0jir1s=&@$)*zh773qsgho_mh"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True
# ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "tailwind",
    'import_export',
    "myapp.apps.MyappConfig",
    "booking.apps.BookingConfig",
    "theme",
    "users.apps.UsersConfig",
    "django_browser_reload",
    'adminlte3',
    'adminlte3_theme',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    'corsheaders',
]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
]

SOCIALACCOUNT_PROVIDERS = {
    "google":{
        "SCOPE":[
            "profile",
            "email"
        ],
        "AUTH_PARAMS" : {"access_type" : "online"},
        # 'APP': {
        #     'client_id': config('GOOGLE_CLIENT_ID'),
        #     'secret': config('GOOGLE_CLIENT_SECRET'),
        #     'key': '',
        # }
    }
}

TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "dvm_r2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dvm_r2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

load_dotenv()

# if config("DOCKERIZED", default=False, cast=bool):
#     # Running inside Docker container
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql_psycopg2",
#             "NAME": config("DB_NAME"),
#             "USER": config("DB_USER"),
#             "PASSWORD": config("DB_PASSWORD"),
#             "HOST": config("DB_HOST"),
#             "PORT": config("DB_PORT"),
#         }
#     }
# else:
    # Running locally
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql_psycopg2",
    #         "NAME": config("DB_NAME_LOCAL"),
    #         "USER": config("DB_USER_LOCAL"),
    #         "PASSWORD": config("DB_PASSWORD_LOCAL"),
    #         "HOST": config("DB_HOST_LOCAL"),
    #         "PORT": config("DB_PORT_LOCAL"),
    #     }
    # }

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("DB_NAME_LOCAL"),
            "USER": config("DB_USER_LOCAL"),
            "PASSWORD": config("DB_PASSWORD_LOCAL"),
            "HOST": config("DB_HOST_LOCAL"),
            "PORT": config("DB_PORT_LOCAL"),
        }
    }
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "myapp/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "profile"

LOGOUT_REDIRECT_URL = "myapp-home"
LOGIN_URL = "login"

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

SITE_ID=2
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)
SOCIALACCOUNT_LOGIN_ON_GET=True # stackOverflow said not a secure approach, but i'm fed up of that intermediate confirmation
