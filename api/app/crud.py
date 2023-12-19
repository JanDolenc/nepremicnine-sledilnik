from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from app.models import Oglas, OglasCena


def parse_referencna_st_from_url(url): return int(
    url.split("_")[-1].split("/")[0])


def select_oglas(session: Session, referecna_st):
    return session.exec(select(Oglas).where(
        Oglas.referencna_st == referecna_st)).first()


def select_oglas_price_data(session: Session, oglas_id: int):
    return session.exec(select(OglasCena.record_ts, OglasCena.cena).where(
        OglasCena.oglas_id == oglas_id)).all()


def get_oglas(session: Session, url: str):
    referecna_st: int = parse_referencna_st_from_url(url)

    oglas = select_oglas(session=session, referecna_st=referecna_st)

    if oglas:
        oglas_price_data = select_oglas_price_data(
            session=session, oglas_id=oglas.id)

        oglas_dict = jsonable_encoder(oglas)

        oglas_dict['price_data'] = oglas_price_data

        return oglas_dict
