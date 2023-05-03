FROM python:3.11-slim

RUN apt update
RUN apt -y upgrade
RUN pip install --upgrade pip

RUN mkdir -p /home/python/app
WORKDIR /home/python/app

COPY req.txt ./
RUN pip install -r req.txt
