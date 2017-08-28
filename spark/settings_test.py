from .settings import *

# This file is meant to provide a testing database to be used by the gitlab
# CI runner. The database is provided through a docker image that is linked
# in as a service in the gitlab ci runner yml file.

# To use this file you can either do:
# python manage.py test --settings=spark.spark.settings_test
# OR add the line below to the manage.py file and run the test as usually
# settings = 'spark.spark.settings_test' if 'test' in sys.argv else
# 'spark.spark.settings'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# THe NAME, USER, PASSWORD AND HOST values correspond to values need to
# access the postgres database that is linked in as a service during the test
# face of the CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'group33',
        'PASSWORD': '',
        'HOST': 'postgres',
        'PORT': '5432',
        }
    }

DEBUG = True
