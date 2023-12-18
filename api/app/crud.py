from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from app.models import Oglas, OglasCena


def parse_referencna_st_from_url(url): return int(
    url.split("_")[-1].split("/")[0])


def select_oglas(session: Session, referecna_st):
    statement = select(Oglas).where(
        Oglas.referencna_st == referecna_st)
    result = session.exec(statement).first()

    return result


def select_oglas_price_data(session: Session, oglas_id: int):
    statement = select(OglasCena.record_ts, OglasCena.cena).where(
        OglasCena.oglas_id == oglas_id)
    result = session.exec(statement).all()

    return result


def get_oglas(session: Session, url: str):
    referecna_st: int = parse_referencna_st_from_url(url)

    oglas = select_oglas(session=session, referecna_st=referecna_st)

    oglas_price_data = select_oglas_price_data(
        session=session, oglas_id=oglas.id)

    oglas_dict = jsonable_encoder(oglas)

    oglas_dict['price_data'] = oglas_price_data

    return oglas_dict
