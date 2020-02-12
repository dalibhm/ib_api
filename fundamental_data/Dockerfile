FROM python:3.7-alpine

WORKDIR /home/app

#RUN apk update
RUN apk update && apk add g++  musl-dev python3-dev
RUN apk add postgresql-dev
#RUN apk update && apk add g++ linux-headers make

#RUN apk update

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY fundamental_data/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY fundamental_data ./fundamental_data
WORKDIR /home/app/fundamental_data

CMD ["python3", "fundamental_server.py"]
