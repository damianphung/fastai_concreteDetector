#FROM python:3.8-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY model ./model/
COPY *.py ./
COPY templates ./templates/

RUN mkdir -p resources/tmp
