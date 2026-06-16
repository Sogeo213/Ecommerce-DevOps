#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate

# ប្រើប្រាស់ export PYTHONPATH មុនពេលរត់ Server
export PYTHONPATH=$PYTHONPATH:.
exec python manage.py runserver 0.0.0.0:8000