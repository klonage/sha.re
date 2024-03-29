"""
Django settings for sha_re project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'usk$)k9nd3(tl)n2_q5j-@%fox0h@yli_342@=a)cwjg^-%-*x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_auth', # social media sign in (facebook, twitter, google+)
    'sha_auth',
    'sha_main',
    'sha_events',
    'sha_user',
    'django_messages',
    'notification',
    'friends'
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
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'messages_module/templates')
]

ROOT_URLCONF = 'sha_re.urls'

WSGI_APPLICATION = 'sha_re.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sha-re-db',
        'USER': 'sha-re',
        'PASSWORD': 'sha-re-test',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

FACEBOOK_APP_ID = '340796046081649'
FACEBOOK_API_SECRET = '3d69aa3188940fef081e1b9ecfe552b5'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


GOOGLE_OAUTH2_CLIENT_ID = '257711607634-d81sdppmlafpl1abk41o6gvo22c4c6qm.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'EIpp2jy9eFa-noZboU9BHikP'

TWITTER_CONSUMER_KEY = 'gHuRCE1CoksfdjJJltOmzRHPb'
TWITTER_CONSUMER_SECRET = 'jIhO17jJ4j7zr8EnTS7VArKYFjG2q7inrEtBPkIM0UE0pnYQIh'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025