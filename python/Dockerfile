FROM python:3.8

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY rola /app/rola
COPY setup.py /app/setup.py
COPY tests/ /app/tests/

