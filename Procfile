release: python manage.py makemigrations food_management_app
release: python manage.py migrate

web: gunicorn food_management.wsgi --log-file -