FROM python:3.11.3-alpine

WORKDIR /usr/src/nepremicnine_sledilnik/database/importer

# Install dependencies from Pypi
COPY importer/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install files in db_common_pkg as local package
COPY ./db_common_pkg ../db_common_pkg

RUN cd ../db_common_pkg/ && pip install -e . 

# Copy code and start the importer script
COPY ./importer/ ./

# Comment out cmd command when building testing image importer-manual
CMD [ "python", "importer.py" ]
