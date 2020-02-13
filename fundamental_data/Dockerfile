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

COPY fundamental_data/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY fundamental_data ./fundamental_data
WORKDIR /home/app/fundamental_data

CMD ["python3", "fundamental_server.py"]
