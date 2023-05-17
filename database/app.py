from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, SQLModel, create_engine


class Agencija(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    naziv: Optional[str] = Field(default=None, unique=True)


class Lokacija(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    regija: str = Field(unique=True)


class Nepremicnina(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vrsta: str
    tip: Optional[str]
    nadstropje: Optional[str] = None
    velikost: condecimal(max_digits=10, decimal_places=2)
    leto_izgradnje: Optional[int]
    zemljisce: Optional[condecimal(
        max_digits=10, decimal_places=2)] = Field(default=0)
    lokacija_id: Optional[int] = Field(default=None, foreign_key="lokacija.id")


class Oglas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    referencna_st: int = Field(unique=True, index=True)
    naslov: Optional[str]
    url: str = Field(unique=True, index=True)
    posredovanje: str
    nepremicnina_id: int = Field(foreign_key="nepremicnina.id")
    agencija_id: int = Field(foreign_key="agencija.id")


class OglasCena(SQLModel, table=True):
    __tablename__ = "oglas_cena"

    oglas_id: int = Field(primary_key=True)
    ts: int = Field(primary_key=True)
    cena: condecimal(max_digits=13, decimal_places=2)


CONN_STRING = "mysql+pymysql://root:nsledilnik_db@127.0.0.1:3306/sqlmodelwithfk"

engine = create_engine(CONN_STRING, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
