#!/bin/bash
RUN_PORT="8000"

cd /app/
/opt/venv/bin/python manage.py migrate --no-input
export DJANGO_SETTINGS_MODULE=mvp_landing.settings.production
export DJANGO_SUPERUSER_USERNAME="admin"
/opt/venv/bin/python manage.py createsuperuser --no-input --username admin --email admin@cfe.sh || true
/opt/venv/bin/gunicorn  mvp_landing.wsgi:application --bind "0.0.0.0:${RUN_PORT}" --daemon

nginx -g 'daemon off;'