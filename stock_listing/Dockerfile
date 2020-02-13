FROM python:3.7-stretch

WORKDIR /home/app

#RUN apt update
RUN apt update && apt install g++ musl-dev python3-dev -y
#RUN apt install postgresql-dev -y
#RUN apt update && apt add g++ linux-headers make

#RUN apt update

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY stock_listing/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade logbook
COPY stock_listing ./stock_listing
WORKDIR /home/app/stock_listing

CMD ["python3", "stock_listing_server.py"]
