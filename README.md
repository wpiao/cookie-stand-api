## Getting started

### Check the app remotely

1. This Django API app is deployed in the AWS.
2. Database is deployed in the Elephantsql.
3. Check the app at `http://18.208.134.116:8000/api/cookie_stand/`

### Check the app in the local machine

**note**: Database is deployed in the Elephantsql. Your local app will be connected to this remote database.

1. Clone down the repo.
2. Download .env file and add it under `cookie_stand_project` folder. Make sure rename the file to `.env`.
3. Run command `docker-compose up --build -d` to start docker container.
4. Run command `docker-compose run web python manage.py makemigrations` and `docker-compose run web python manage.py migrate` to migrate.
5. Run command `docker-compose run web python manage.py createsuperuser` and follow the prompt to create a super user.
6. Run command `docker-compose run web python manage.py collectstatic` to create static files.
7. Check out the app at `http://0.0.0.0:8000/api/cookie_stand/`.
8. Run command `docker-compose down` to shot down the container.
