web: gunicorn python_todo_list.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate