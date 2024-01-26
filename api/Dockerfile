FROM python:3.11.3-alpine

WORKDIR /usr/src/nepremicnine_sledilnik/api

# Install dependencies from Pypi
COPY ./api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install files in db_common_pkg as local package
COPY ./database/db_common_pkg ../database/db_common_pkg

RUN cd ../database/db_common_pkg/ && pip install -e . 

# Copy code and start the server
COPY ./api .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]

# for development | reload on file change
#CMD [ "uvicorn", "app.main:app", "--reload", "--reload-dir", "../.", "--host", "0.0.0.0", "--port", "80" ]
