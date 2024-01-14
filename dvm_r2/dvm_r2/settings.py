from pathlib import Path
from dotenv import load_dotenv
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = "django-insecure-w-r!)wn-g1e-c$hmjl37pa4px0jir1s=&@$)*zh773qsgho_mh"


SECRET_KEY = config('SECRET_KEY')
DEBUG= True
ALLOWED_HOSTS = ['*']

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
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': '',
        }
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

environment = config('DJANGO_ENV', 'local')
if(environment=='local'):
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
elif environment=='container':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "dvm_db",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "db",
            "PORT": "5432",
        }
    }
else:
    print("invalid DB config")


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
# STATIC_ROOT = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR,'static/')
print(STATIC_ROOT)

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

CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]