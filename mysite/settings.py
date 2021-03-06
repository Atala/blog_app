# Django settings for mysite project.

import os

import django.conf.global_settings as DEFAULT_SETTINGS



DEBUG = False 

TEMPLATE_DEBUG = DEBUG



ADMINS = (

    # ('Your Name', 'your_email@example.com'),

)



MANAGERS = ADMINS







# Hosts/domain names that are valid for this site; required if DEBUG is False

# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowedhosts

ALLOWED_HOSTS = []



# Local time zone for this installation. Choices can be found here:

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name

# although not all choices may be available on all operating systems.

# In a Windows environment this must be set to your system time zone.

TIME_ZONE = 'Europe/Paris'



# Language code for this installation. All choices can be found here:

# http://www.i18nguy.com/unicode/languageidentifiers.html

LANGUAGE_CODE = 'frFR'



SITE_ID = 1



# If you set this to False, Django will make some optimizations so as not

# to load the internationalization machinery.

USE_I18N = True



# If you set this to False, Django will not format dates, numbers and

# calendars according to the current locale.

USE_L10N = True



# If you set this to False, Django will not use timezoneaware datetimes.

USE_TZ = True



# Absolute filesystem path to the directory that will hold useruploaded files.

# Example: "/var/www/example.com/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')



# URL that handles the media served from MEDIA_ROOT. Make sure to use a

# trailing slash.

# Examples: "http://example.com/media/", "http://media.example.com/"

MEDIA_URL = '/media/'





STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATIC_URL = '/static/'







#STATICFILES_DIRS = (

#    os.path.join(BASE_DIR, 'static'),

#)



# Additional locations of static files

STATICFILES_DIRS = (

    # Put strings here, like "/home/html/static" or "C:/www/django/static".

    # Always use forward slashes, even on Windows.

    # Don't forget to use absolute paths, not relative paths.

  

)



# List of finder classes that know how to find static files in

# various locations.

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

#    'django.contrib.staticfiles.finders.DefaultStorageFinder',

)



# Make this unique, and don't share it with anybody.

SECRET_KEY = 'wp9seq8a#!nk2fe$oqc8=k%&=rmtu(ow$8wh^ph#v9hni8u_m'



# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',

    'django.template.loaders.app_directories.Loader',

#     'django.template.loaders.eggs.Loader',

)



MIDDLEWARE_CLASSES = (

    'django.middleware.common.CommonMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    

    # Uncomment the next line for simple clickjacking protection:

    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

)



ROOT_URLCONF = 'mysite.urls'



# Python dotted path to the WSGI application used by Django's runserver.

WSGI_APPLICATION = 'mysite.wsgi.application'



TEMPLATE_DIRS = (

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".

    # Always use forward slashes, even on Windows.

    # Don't forget to use absolute paths, not relative paths.

)



INSTALLED_APPS = (

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.sites',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:

     'django.contrib.admin',

    # Uncomment the next line to enable admin documentation:

     'django.contrib.admindocs',

     'storages',
    
    'django_mandrill',

     'blog',

)



# A sample logging configuration. The only tangible logging

# performed by this configuration is to send an email to

# the site admins on every HTTP 500 error when DEBUG=False.

# See http://docs.djangoproject.com/en/dev/topics/logging for

# more details on how to customize your logging configuration.

LOGGING = {

    'version': 1,

    'disable_existing_loggers': False,

    'filters': {

        'require_debug_false': {

            '()': 'django.utils.log.RequireDebugFalse'

        }

    },

    'handlers': {

        'mail_admins': {

            'level': 'ERROR',

            'filters': ['require_debug_false'],

            'class': 'django.utils.log.AdminEmailHandler'

        }

    },

    'loggers': {

        'django.request': {

            'handlers': ['mail_admins'],

            'level': 'ERROR',

            'propagate': True,

        },

    }

}





# Honor the 'XForwardedProto' header for request.is_secure()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Allow all host headers

ALLOWED_HOSTS = ['*']



if not DEBUG:

    # Parse database configuration from $DATABASE_URL

    import dj_database_url

    DATABASES = {

  'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))

    }



    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = 'AKIAJL2R2RLYIXDZP2MQ'

    AWS_SECRET_ACCESS_KEY = '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'

    AWS_STORAGE_BUCKET_NAME = 'djangoblogpictures'

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/static/'

    STATIC_URL = '/static/'



    #ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    MEDIA_ROOT = ''

    MEDIA_URL = ''



else:

    DATABASES = {

       'default': {

      'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.

     'NAME': '/home/guillope/Documents/Code/Django/mysite.db',                      # Or path to database file if using sqlite3.

      # The following settings are not used with sqlite3:

      'USER': '',

      'PASSWORD': '',

      'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.

     'PORT': '',                      # Set to empty string for default.

  },

    }





TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + ("blog.pass_date.get_base_content",

             "django.core.context_processors.request",

             "django.contrib.auth.context_processors.auth")


if not DEBUG :
    EMAIL_HOST = 'smtp.mandrillapp.com'
    EMAIL_BACKEND = 'django_mandrill.mail.backends.mandrillbackend.EmailBackend'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'alois.guillope@gmail.com'
    MANDRILL_API_KEY = '1iYNensLNHVrivrRo2ZMtA' 

else:
    EMAIL_HOST = 'localhost'
