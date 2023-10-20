from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, Relationship, SQLModel


""" class Agencija(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    naziv: Optional[str] = Field(default=None, unique=True)

    oglasi: list["Oglas"] = Relationship(back_populates="agencija") """


""" class Lokacija(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    regija: str = Field(unique=True)

    nepremicnine: list["Nepremicnina"] = Relationship(
        back_populates="lokacija") """


class Oglas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    referencna_st: int = Field(unique=True, index=True)
    naslov: Optional[str]
    url: str = Field(unique=True, index=True)
    posredovanje: str
    agencija: str
    vrsta: str
    tip: Optional[str]
    nadstropje: Optional[str] = None
    velikost: condecimal(max_digits=12, decimal_places=2)
    leto_izgradnje: Optional[int]
    zemljisce: Optional[condecimal(
        max_digits=12, decimal_places=2)] = Field(default=None)
    regija: str
    ts_insert: Optional[int]

    # oglasi: list["Oglas"] = Relationship(back_populates="nepremicnina")


# class Oglas(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    referencna_st: int = Field(unique=True, index=True)
#    naslov: Optional[str]
#    url: str = Field(unique=True, index=True)
#    posredovanje: str
#    nepremicnina_id: int = Field(foreign_key="nepremicnina.id")
#    agencija_id: int = Field(foreign_key="agencija.id")
#
#    nepremicnina: Nepremicnina = Relationship(back_populates="oglasi")
#    agencija: Agencija = Relationship(back_populates="oglasi")


class OglasCena(SQLModel, table=True):
    __tablename__ = "oglas_cena"

    oglas_id: int = Field(primary_key=True)
    ts: int = Field(primary_key=True)
    cena: condecimal(max_digits=14, decimal_places=2)
    ts_insert: Optional[int]
