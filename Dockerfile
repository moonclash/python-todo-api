FROM python:3.11.1

WORKDIR /todo-api

COPY ./src/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./src/ .