FROM python:3.11.3-alpine

WORKDIR /usr/src/crawler

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN mkdir -p scraped-data logs
