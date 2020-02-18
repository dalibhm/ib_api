FROM python:3.7-stretch

WORKDIR /home/app

RUN apt update && apt install  musl-dev python3-dev -y

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY stock_listing/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY dependencies/log_service-1.0.tar.gz .
RUN pip3 install log_service-1.0.tar.gz

COPY stock_listing ./stock_listing
WORKDIR /home/app/stock_listing

CMD ["python3", "stock_listing_server.py"]
