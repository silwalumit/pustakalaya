FROM ubuntu

RUN apt-get update
RUN apt-get install -y python
WORKDIR /opt/app
RUN set -xe && apt-get install -y python3-pip
COPY requirements.txt /opt/app
RUN apt-get install -y libpq-dev
RUN pip3 install -r requirements.txt
COPY . /opt/app

ENTRYPOINT FLASK_APP=/opt/app/run.py flask run
