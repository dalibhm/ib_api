FROM python:3.7-stretch

WORKDIR /home/app

RUN apt update && apt install g++  musl-dev python3-dev -y
#RUN apt install postgresql-dev

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY historical_data/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY historical_data ./historical_data
WORKDIR /home/app/historical_data

CMD ["python3", "historical_data_server.py"]
