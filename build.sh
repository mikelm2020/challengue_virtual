#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

cd agency
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata data.json