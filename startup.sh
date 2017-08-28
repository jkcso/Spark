#!/bin/bash

pip install -r requirements.txt
# To sync the database and start the server
python manage.py collectstatic
#python manage.py migrate
python manage.py runserver
