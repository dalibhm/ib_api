FROM python:3.6-alpine

WORKDIR /home/flask_api

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app app
COPY migrations migrations
COPY app.py config.py ./

EXPOSE 5000
CMD ["python", "./app.py", "runserver"]
