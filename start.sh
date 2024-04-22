echo "MAKEMIGRATIONS"
python manage.py makemigrations
echo "MIGRATE"
python manage.py migrate
echo "START GUNICORN"
gunicorn app.wsgi -w 4 -b 0.0.0.0:8000