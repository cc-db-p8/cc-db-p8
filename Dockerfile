FROM ubuntu:14.04
RUN apt-get update && apt-get -y install sqlite3 python python-setuptools
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN easy_install pip
RUN pip install -r requirements.txt