#!/bin/sh

python manage.py makemigrations 
python manage.py migrate 
python manage.py create_initial_trains 
python manage.py populate_myapp_station
# python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate 
gunicorn -c gunicorn_conf.py dvm_r2.wsgi:application --bind 0.0.0.0:8000
