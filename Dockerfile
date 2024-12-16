# This app was built with Python 3.10.10
FROM python:3.10.10
LABEL authors="Matt Popelka"

# Setting working directory
WORKDIR /babydataproject

# Copying current directory components into /babydataproject
COPY . /babydataproject/

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Open port 8000 for Django
EXPOSE 8000

# Defining environment variable for production environment
ENV PYTHONUNBUFFERED 1

# Make sure all necessary migrations are applied
#RUN python manage.py migrate
CMD ["sh", "-c", "python manage.py migrate &&  waitress-serve --listen=*:8000 BabyDataProject.wsgi.application"]
## Collect static files for production (if using static files)
#RUN python manage.py collectstatic --noinput

# Start the app using waitress
#CMD ["waitress-serve", "--listen=*:8000", "BabyDataProject.wsgi:application"]
## Run migrations and start the dev server
##CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
#
