# ----------------------------------------------------------------------------
# Copyright (c) 2018-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .shared import (
    BASE_DIR,
    PROJ_DIR,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    WSGI_APPLICATION,
    DATABASES,
    AUTH_PASSWORD_VALIDATORS,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    STATIC_URL,
    STATICFILES_DIRS,
    STATIC_ROOT,
    env,
    APPEND_SLASH,
    LOGOUT_REDIRECT_URL,
    list_of_tuples,
    AUTH_USER_MODEL,
    LOGIN_URL,
    CELERY_RESULT_BACKEND,
    CELERY_RESULT_EXPIRES,
    CELERY_RESULT_SERIALIZER,
    CELERY_TASK_SERIALIZER,
    CELERY_ACCEPT_CONTENT,
    CELERY_TASK_ROUTES,
    TASK_TIMES,
    CELERY_BEAT_SCHEDULE,
    GITHUB_TOKEN,
    INTEGRATION_REPO,
    BASE_CONDA_PATH,
    GATE_TESTED,
    GATE_STAGED,
    GATE_PASSED,
)

__all__ = [
    'BASE_DIR',
    'PROJ_DIR',
    'SECRET_KEY',
    'DEBUG',
    'ALLOWED_HOSTS',
    'INSTALLED_APPS',
    'MIDDLEWARE',
    'ROOT_URLCONF',
    'WSGI_APPLICATION',
    'DATABASES',
    'AUTH_PASSWORD_VALIDATORS',
    'LANGUAGE_CODE',
    'TIME_ZONE',
    'USE_I18N',
    'USE_L10N',
    'USE_TZ',
    'STATIC_URL',
    'STATICFILES_DIRS',
    'STATIC_ROOT',
    'APPEND_SLASH',
    'LOGOUT_REDIRECT_URL',
    'AUTH_USER_MODEL',
    'LOGIN_URL',
    'RABBITMQ_URL',
    'CELERY_BROKER_URL',
    'CELERY_RESULT_BACKEND',
    'CELERY_RESULT_EXPIRES',
    'CELERY_RESULT_SERIALIZER',
    'CELERY_TASK_SERIALIZER',
    'CELERY_ACCEPT_CONTENT',
    'CELERY_TASK_ROUTES',
    'TASK_TIMES',
    'CELERY_BEAT_SCHEDULE',
    'GITHUB_TOKEN',
    'INTEGRATION_REPO',
    'BASE_CONDA_PATH',
    'GATE_TESTED',
    'GATE_STAGED',
    'GATE_PASSED',
]

DEBUG = False
DATABASES['default'] = env.db('DATABASE_URL')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME')
AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT')
ADMINS = env('ADMINS', cast=list_of_tuples)
DEFAULT_FROM_EMAIL = 'no-reply@library.qiime2.org'
SERVER_EMAIL = 'no-reply@library.qiime2.org'
EMAIL_HOST = 'library.qiime2.org'
EMAIL_SUBJECT_PREFIX = '[library.qiime2.org] '
DISCOURSE_SSO_PROVIDER = 'forum.qiime2.org'
DISCOURSE_SSO_SECRET = env('DISCOURSE_SSO_SECRET')
GOOGLE_ANALYTICS_PROPERTY_ID = env('GOOGLE_ANALYTICS_PROPERTY_ID')
TEMPLATES[0]['OPTIONS']['context_processors'].append('library.utils.context_processors.google_analytics')
RABBITMQ_URL = env('RABBITMQ_URL')
# We want to use the rmq url set by dokku
CELERY_BROKER_URL = env('RABBITMQ_URL')
INTEGRATION_REPO['owner'] = 'qiime2'
INTEGRATION_REPO['token'] = env('INTEGRATION_REPO_TOKEN')
