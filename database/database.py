from sqlmodel import SQLModel, create_engine

CONN_STRING = "mysql+pymysql://root:nsledilnik_db@127.0.0.1:3306/importer_dev?charset=utf8mb4"

# for debugging purposes set echo=True: create_engine(CONN_STRING, echo=True)
engine = create_engine(CONN_STRING)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
