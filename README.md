Base functionality for online shop creation on Django with Bootstrap4 on russian language. 

Clone project:
> git clone https://github.com/SviatlanaYermalinskaya/djangoSV.git

Start virtual environment:
> python3 -m venv venv
> 
> source venv/bin/activate 

or start venv for Windows:
> python -m venv venv
> 
> venv\Scripts\activate.bat

Change directory:
> cd first_shop

Install:
> pip install -r requirements.txt

Create .env file with values for the next settings.py variables:

    SECRET_KEY
    DEBUG
    SQL_ENGINE
    POSTGRES_NAME
    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_HOST
    POSTGRES_PORT

Make migrations:
> python manage.py makemigrations
> 
> python manage.py migrate

Create superuser:
> python manage.py createsuperuser

Run project:
> python manage.py runserver

SOME USEFUL CHANGES:

* Default sqlite3 database instead of postgres in settings.py:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'firs_shop.data'),
            }
        }

* Add all allowed hosts or you domain in settings.py for hosting setup

  >ALLOWED_HOSTS = ['*']

  or
  
    >ALLOWED_HOSTS = ['Pheia.pythonanywhere.com']

* Change DEBUG = False to prevent all errors info 
* For hosting setup make directories 'media' and 'static' 
in django project directory '/svDjango/first_shop/' and update 
settings.py with:

   >STATIC_URL = 'static/'
   >
   >STATIC_ROOT = os.path.join(BASE_DIR, 'static')
   >
   >MEDIA_URL = '/media/'
   >
   >MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

  then collect static via command:

  > python manage.py collectstatic
