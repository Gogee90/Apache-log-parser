FROM python:3.8-slim-bullseye

WORKDIR /home/user/apache_log_parser

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./