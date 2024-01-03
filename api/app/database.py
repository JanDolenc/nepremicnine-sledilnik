from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv()

database_user: str = getenv('DATABASE_USER')
database_password: str = getenv('DATABASE_PASSWORD')
database_host: str = getenv('DATABASE_HOST')
database_port: str = getenv('DATABASE_PORT')
database_name: str = getenv('DATABASE_NAME')

CONN_STRING = f"mysql+pymysql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}?charset=utf8mb4"

# for debugging purposes set echo=True: create_engine(CONN_STRING, echo=True)

# this is in sqlmodel fastapi tutorial. Only sqlite thing?
# connect_args = {"check_same_thread": False}
# engine = create_engine(CONN_STRING, echo=True, connect_args=connect_args)
engine = create_engine(CONN_STRING, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
