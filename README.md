# mentor.lol

A web application to pair people who want mentoring, with people who want to be mentored.

## Getting Started

1. Clone the repository
2. `pip install virtualenv`
3. `virtualenv create venv`
4. `pip install -r requirements.txt --allow-all-external`
3. `./manage.py migrate`
4. `./manage.py createsuperuser`
5. `./manage.py runserver`

The frontend will be at http://localhost:8000/ and the admin backend at http://localhost:8000/admin

## When Coming Back

1. `virtualenv activate venv`
2. `pip install -r requirements.txt --allow-all-external`
3. `./manage.py migrate`
4. `./manage.py runserver`
