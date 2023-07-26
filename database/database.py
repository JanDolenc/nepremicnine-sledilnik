from sqlmodel import SQLModel, create_engine

CONN_STRING = "mysql+pymysql://root:nsledilnik_db@127.0.0.1:3306/importer"

engine = create_engine(CONN_STRING, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
