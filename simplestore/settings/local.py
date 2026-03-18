from .base import *

DEBUG = True

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# No arquivo simplestore/settings/local.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'simplestore',      # Deve ser igual ao POSTGRES_DB do docker-compose
        'USER': 'postgres',         # Deve ser igual ao POSTGRES_USER do docker-compose
        'PASSWORD': 'postgres',     # Deve ser igual ao POSTGRES_PASSWORD do docker-compose
        'HOST': 'db',               # Nome do serviço no docker-compose
        'PORT': '5432',
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1'
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
