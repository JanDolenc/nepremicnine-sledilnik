FROM python:3.11.3-alpine

WORKDIR /usr/src/importer

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comment out cmd command when building testing image importer-manual
CMD [ "python", "importer.py" ]
