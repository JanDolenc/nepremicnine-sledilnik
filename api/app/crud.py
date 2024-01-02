from datetime import datetime, timedelta
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select, func

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


def get_similar_oglasi(session: Session, query_params: dict):

    optional_conditions: list = []
    if query_params["regija"] is not None:
        optional_conditions.append(Oglas.regija == query_params["regija"])

    if query_params["vrsta"] is not None:
        optional_conditions.append(Oglas.vrsta == query_params["vrsta"])

    if query_params["velikost_min"] is not None:
        optional_conditions.append(Oglas.velikost >=
                                   query_params["velikost_min"])

    if query_params["cena_max"] is not None:
        optional_conditions.append(OglasCena.cena <= query_params["cena_max"])

    statement = (
        select(
            Oglas.referencna_st,
            Oglas.naslov,
            Oglas.vrsta,
            Oglas.tip,
            Oglas.nadstropje,
            Oglas.leto_izgradnje,
            Oglas.velikost,
            OglasCena.cena,
        )
        .join(OglasCena)
        .where(
            *optional_conditions,
            Oglas.id != query_params["id"],
            # expensive ads have price listed per m2 and appear in results as the cheapest option. Exlude them from results
            OglasCena.cena >= 10000,
            OglasCena.record_ts >= (
                datetime.now() - timedelta(days=70)).timestamp(),
            OglasCena.record_ts == (
                select(func.max(OglasCena.record_ts))
                .where(Oglas.id == OglasCena.oglas_id)
                    .scalar_subquery()
                    .correlate(Oglas)
            )
        )
        .order_by(OglasCena.cena)
        .limit(40)
    )

    results = session.exec(statement).all()

    similar_oglasi = {
        "similar_oglasi": results
    }

    print()
    print("results count ---", len(results))

    return similar_oglasi
