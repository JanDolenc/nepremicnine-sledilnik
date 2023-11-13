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

    # timestamp value of json file in which the ad first appeared in - was detected
    detected_ts: int

    # timestamp value of (latest) json file in which at least one property of the ad changed
    updated_ts: int

    # timestamp value that represents when the importer script inserted this record into db.
    created_at: int

    # timestamp value that represents when the importer script inserted OR updated this record in db.
    updated_at: int


class OglasCena(SQLModel, table=True):
    __tablename__ = "oglas_cena"

    oglas_id: int = Field(primary_key=True)
    record_ts: int = Field(primary_key=True)
    cena: condecimal(max_digits=14, decimal_places=2)
    created_at: int


# regija labels to regija values in db
regija_mapped: dict = {
    'gorenjska': 'Gorenjska',
    'lj-mesto': 'LJ-mesto',
    'j-primorska': 'J. Primorska',
    'podravska': 'Podravska',
    'lj-okolica': 'LJ-okolica'
}


# vrsta labels to vrsta values in db
vrsta_mapped: dict = {
    's': 'Stanovanje',
    'h': 'Hiša'
}
