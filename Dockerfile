# make a base image that has the requirements and use it for building the app and api images
FROM python:3.10
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt