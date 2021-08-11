import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary
import mimetypes
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)xbm6n6whd#-+mi9j4%n-l-n9jj*74ws#mz9v8w5%nthmw#i91'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'omega_beats.common',
    'omega_beats.beats',
    'omega_beats.omega_beats_auth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'omega_beats.urls'

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

WSGI_APPLICATION = 'omega_beats.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'beats_db',
        'USER': 'postgres',
        'PASSWORD': 'passpost',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.omega_beats_auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.omega_beats_auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.omega_beats_auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.omega_beats_auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (BASE_DIR / 'static/styles/'),
    (BASE_DIR / 'static/scripts/'),
    (BASE_DIR / 'static/notes/'),
    (BASE_DIR / 'static/images/'),
    (BASE_DIR / 'static/gifs/'),
    (BASE_DIR / 'static/favicons/'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'omega_beats_auth.OmegaBeatsUser'

LOGIN_URL = reverse_lazy('login user')

cloudinary.config(
    cloud_name='omega-beats',
    api_key='171293578469246',
    api_secret='-i91rvUefrehQjKXZc3nABetTOg',
    secure=True
)

mimetypes.add_type("text/css", ".css", True)
