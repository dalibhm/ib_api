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

COPY contract_service/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./contract_service ./contract_service
WORKDIR /home/app/contract_service

CMD ["python3", "contract_server.py"]
