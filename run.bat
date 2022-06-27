if exist env\ (
  env\Script\activate
) else (
  pip install virtualenv
  virtualenv env
  env\Script\activate
  pip install -r requirements.txt
)


python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver