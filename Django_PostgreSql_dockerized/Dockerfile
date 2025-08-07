#defining the base of the container
FROM python:3.12.3-slim

#this ensures that python output is straight to terminal without buffering
ENV PYTHONUNBUFFERED 1

#root directory for the container
RUN mkdir /django_postgres

# set working directory to /ourDefinedDirectory
WORKDIR /django_postgres

# now copy all django project files to the root dir
COPY . /django_postgres/

# install all library/dependencies using RUN
RUN pip install -r requirements.txt
