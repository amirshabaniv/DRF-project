FROM python:3.11.4-alpine

WORKDIR /app


ENV PYTHONDONTWRITEBYECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/PY/BIN:$PATH"


RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
COPY . /app

RUN pip install -r requirements.txt