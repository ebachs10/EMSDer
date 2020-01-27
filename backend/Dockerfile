# Pull base image

FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /

# Copies the requirements.txt to the container
COPY requirements.txt .


# Install requirements
RUN pip install -r requirements.txt


# Copy project
COPY . /code/