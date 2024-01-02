from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session

from app.models import OglasReadWithPrice
from app.database import engine, create_db_and_tables
import app.crud as crud


def get_session():  # session in a function shared with every route - FastAPI dependency injection
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.on_event("startup")  # deprecated use lifespan events
def on_startup():
    create_db_and_tables()


@app.get("/search/oglas/")
async def read_oglas(*, session: Session = Depends(get_session), url: str) -> OglasReadWithPrice:
    oglas = crud.get_oglas(session=session, url=url)

    if not oglas:
        raise HTTPException(
            status_code=404, detail="Ad with this url not found.")
    return oglas


@app.get("/search/similar/oglasi")
async def read_similar_oglasi(*, session: Session = Depends(get_session), id: int,  regija: str | None = None, vrsta: str | None = None, velikost_min: float | None = None, cena_max: float | None = None):
    query_params: dict = {"id": id, "regija": regija,
                          "vrsta": vrsta, "velikost_min": velikost_min, "cena_max": cena_max}

    similar_oglasi = crud.get_similar_oglasi(
        session=session, query_params=query_params)

    if not similar_oglasi["similar_oglasi"]:
        raise HTTPException(
            status_code=404, detail=f"Similar ads for this ad  not found.")
    return similar_oglasi
