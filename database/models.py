from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, SQLModel


class Oglas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    referencna_st: int = Field(unique=True, index=True)
    naslov: str
    url: str = Field(unique=True, index=True)
    posredovanje: str
    agencija: str
    vrsta: str
    tip: Optional[str]
    nadstropje: Optional[str] = None
    velikost: condecimal(max_digits=12, decimal_places=2)
    leto_izgradnje: Optional[int] = None
    zemljisce: Optional[condecimal(
        max_digits=12, decimal_places=2)] = Field(default=None)
    regija: str
    created_at: int
    updated_at: int


class OglasCena(SQLModel, table=True):
    __tablename__ = "oglas_cena"

    oglas_id: int = Field(primary_key=True)
    ts: int = Field(primary_key=True)
    cena: condecimal(max_digits=14, decimal_places=2)
    created_at: int
