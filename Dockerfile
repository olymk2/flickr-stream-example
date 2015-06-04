# VERSION               0.0.1

FROM     ubuntu:15.04
MAINTAINER Oliver Marks "olymk2@gmail.com"

# make sure the package repository is up to date

RUN \
    apt-get update &&   \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common python-software-properties && \
    apt-get install -y python-requests python-cjson python-django wget

ADD . /var/www/
WORKDIR /var/www/

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
