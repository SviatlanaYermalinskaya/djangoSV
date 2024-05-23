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