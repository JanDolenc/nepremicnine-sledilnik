FROM python:3.11.3-alpine

WORKDIR /usr/src/api

COPY ./api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/app ./database/database.py ./database/models.py ./app/

#CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]

# for development | reload on file change
CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80" ]
