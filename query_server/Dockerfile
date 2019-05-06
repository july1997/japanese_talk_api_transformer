FROM python:3.6-slim-jessie

RUN apt-get update && apt install -y git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
VOLUME /Users/makoto/work/problem
VOLUME /Users/makoto/work/dataset

RUN pip install pandas

EXPOSE 5000
