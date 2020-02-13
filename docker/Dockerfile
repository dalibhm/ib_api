FROM python:3.7-stretch

WORKDIR /home

#RUN apk update
RUN apt update
RUN apt install g++ musl-dev python3-dev -y

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

RUN pip3 install --no-cache-dir --upgrade grpcio==1.26.0

CMD []