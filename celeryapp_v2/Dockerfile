#define image for the base of the container
FROM python:3.12.3-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /celeryapp_v2

# Set the working directory to /celery_app
WORKDIR /celeryapp_v2

# Copy the current directory contents into the container at /celery_app
ADD . /celeryapp_v2/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt 
