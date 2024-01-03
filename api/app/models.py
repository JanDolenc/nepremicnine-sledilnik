from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, SQLModel


# Oglas models


class OglasBase(SQLModel):
    referencna_st: int = Field(unique=True, index=True)
    naslov: str
    vrsta: str
    tip: Optional[str]
    velikost: condecimal(max_digits=12, decimal_places=2)
    leto_izgradnje: Optional[int] = None
    nadstropje: Optional[str] = None


class OglasBasic(OglasBase):
    url: str = Field(unique=True, index=True)
    regija: str
    agencija: str
    posredovanje: str
    zemljisce: Optional[condecimal(
        max_digits=12, decimal_places=2)] = Field(default=None)
    regija: str

    # timestamp value of json file in which the ad first appeared in - was detected
    detected_ts: int

    # timestamp value of (latest) json file in which at least one property of the ad changed
    updated_ts: int


class Oglas(OglasBasic, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # timestamp value that represents when the importer script inserted this record into db.
    created_at: int

    # timestamp value that represents when the importer script inserted OR updated this record in db.
    updated_at: int


class OglasRead(OglasBasic):
    id: int


# OglasCena models


class OglasCenaBase(SQLModel):
    record_ts: int = Field(primary_key=True)
    cena: condecimal(max_digits=14, decimal_places=2)


class OglasCena(OglasCenaBase, table=True):
    __tablename__ = "oglas_cena"

    oglas_id: int = Field(primary_key=True, foreign_key="oglas.id")
    created_at: int


class OglasCenaRead(OglasCenaBase):
    pass


# Mixed models
class OglasReadWithPrice(OglasRead):
    price_data: list[OglasCenaRead]


class SimilarOglasReadWithPrice(OglasBase):
    cena: condecimal(max_digits=14, decimal_places=2)


class SimilarOglasiRead(SQLModel):
    similar_oglasi: list[SimilarOglasReadWithPrice]
