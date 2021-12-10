from bfr.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bfr',
        'USER': 'postgres',
        'PASSWORD': '123456qQ',
        'HOST': 'localhost',
        'PORT': '5432'
    },
}