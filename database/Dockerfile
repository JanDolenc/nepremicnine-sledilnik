FROM python:3.11.3-alpine

WORKDIR /usr/src/importer

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "importer.py" ]
    