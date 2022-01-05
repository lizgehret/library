# ----------------------------------------------------------------------------
# Copyright (c) 2018-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pathlib

from .shared import (
    BASE_DIR,
    PROJ_DIR,
    SECRET_KEY,
    DEBUG,
    ALLOWED_HOSTS,
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
    APPEND_SLASH,
    LOGIN_URL,
    LOGOUT_REDIRECT_URL,
    EMAIL_BACKEND,
    ADMINS,
    AUTH_USER_MODEL,
    RABBITMQ_URL,
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    CELERY_RESULT_SERIALIZER,
    CELERY_TASK_SERIALIZER,
    CELERY_ACCEPT_CONTENT,
    CELERY_TASK_ROUTES,
    GITHUB_TOKEN,
    INTEGRATION_REPO,
    GATE_TESTED,
    GATE_STAGED,
    GATE_PASSED,

    generate_beat_schedule,
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
    'TEMPLATES',
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
    'INTERNAL_IPS',
    'LOGIN_URL',
    'LOGOUT_REDIRECT_URL',
    'EMAIL_BACKEND',
    'ADMINS',
    'AUTH_USER_MODEL',
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
    'BASE_CONDA_PATH',
    'INTEGRATION_REPO',
    'GATE_TESTED',
    'GATE_STAGED',
    'GATE_PASSED',
]

MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware'
])
INTERNAL_IPS = ['127.0.0.1', 'localhost']
INSTALLED_APPS = ['whitenoise.runserver_nostatic', *INSTALLED_APPS, 'debug_toolbar']
CELERY_RESULT_EXPIRES = 60 * 10
# For development purposes it's a lot nicer to have short cycle times (30 sec)
TASK_TIMES = {
    '03_MIN': 30,
    '05_MIN': 30,
    '10_MIN': 30,
    '90_MIN': 30,
    '02_HR': 30,
    '4A_CRON': 30,
    'HRLY_CRON': 30,
}
CELERY_BEAT_SCHEDULE = generate_beat_schedule(TASK_TIMES)
BASE_CONDA_PATH = pathlib.Path('data/qiime2')
