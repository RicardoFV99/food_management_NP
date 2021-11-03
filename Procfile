release: python manage.py makemigrations food_management_app
release: python manage.py migrate

web: gunicorn wsgi:food_management --log-file -