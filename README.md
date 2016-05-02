Heroku Django Deploy
Created a simple app that shortens urls. This simple app will be deployed in heroku.  


Dependencies:
 - python 2.7
 - pip version >= 1.3
 - django >= 1.8

Assumptions:
 - You have finished building your own django app.
 - Have installed heroku toolbelt and has existing account.

From Scratch:
 - mkdir <your project path> && cd <your project path>
 - git init
 - touch .gitignore Procfile requirements.txt
 - virtualenv venv
 - source venv/bin/activate
 - django-admin startproject [project name] .

Before Deploying Heroku:
 - Must have the following:
    Inside your Procfile:
        web: gunicorn [project name].wsgi --log-file -

    Inside your requirements.txt:
        gunicorn==19.4.5
        psycopg2==2.6.1
        whitenoise==2.0.6
        dj-database-url==0.4.0

    Inside your settings.py:
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)

        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        ALLOWED_HOSTS = ['*']
        DEBUG = False

Deploying to Heroku:
 - heroku login (input username, password)
 - heroku create
 - git push heroku master
 - heroku run python manage.py migrate
 - heroku open
 - heroku ps:scale web=1 
