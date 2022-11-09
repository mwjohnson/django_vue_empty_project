FROM python:3.10-slim-bullseye

RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install nano -y

RUN apt-get install gettext gettext-base -y
RUN apt-get -y install python-celery-common

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . ./