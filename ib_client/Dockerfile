FROM python:3.7-stretch

WORKDIR /home/app

RUN apt update && apt install g++  musl-dev python3-dev -y
RUN apt install librdkafka-dev -y


RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY ibclient/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY ./dependencies/ibapi ibapi
RUN pip3 install ibapi

#RUN apt add linux-headers
RUN pip3 install ddtrace

COPY ibclient ./ibclient

WORKDIR /home/app/ibclient

CMD ["python3", "app.py"]
