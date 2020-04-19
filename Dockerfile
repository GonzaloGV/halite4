FROM python:3.8-slim-buster
WORKDIR /usr/src/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt