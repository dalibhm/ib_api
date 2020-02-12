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

COPY stock_listing/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade logbook
COPY stock_listing ./stock_listing
WORKDIR /home/app/stock_listing

CMD ["python3", "stock_listing_server.py"]
