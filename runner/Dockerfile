FROM python:3.7-alpine

WORKDIR /home/runner

#RUN apk update
RUN apk update && apk add g++  musl-dev python3-dev curl bash make
RUN apk add postgresql-dev
RUN apk add librdkafka-dev

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY runner/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY dependencies/historical_data ./historical_data
RUN pip3 install historical_data

COPY runner app
WORKDIR /home/runner/app

CMD ["python3", "runner.py"]
