FROM ubuntu:latest
LABEL authors="husandev"

ENTRYPOINT ["top", "-b"]

# Use the official Python image from the DockerHub
FROM python:3.12-slim

# Set the working directory in docker
WORKDIR /gis

# Copy the dependencies file to the working directory
COPY /requirements/ /gis/requirements/

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/local.txt

# Copy the content of the local src directory to the working directory
COPY . .

EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]