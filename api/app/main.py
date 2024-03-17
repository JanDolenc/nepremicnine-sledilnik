from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from db_common.models import OglasReadWithPrice, SimilarOglasiRead
from db_common.database import engine, create_db_and_tables
from app import crud


def get_session():  # session in a function shared with every route - FastAPI dependency injection
    with Session(engine) as session:
        yield session


app = FastAPI()

# origins = [
#    "http://localhost",
#    "http://localhost:80",
# ]
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
async def read_similar_oglasi(*, session: Session = Depends(get_session), id: int,  regija: str | None = None, vrsta: str | None = None, velikost_min: float | None = None, cena_max: float | None = None) -> SimilarOglasiRead:
    query_params: dict = {"id": id, "regija": regija,
                          "vrsta": vrsta, "velikost_min": velikost_min, "cena_max": cena_max}

    similar_oglasi = crud.get_similar_oglasi(
        session=session, query_params=query_params)

    if not similar_oglasi["similar_oglasi"]:
        raise HTTPException(
            status_code=404, detail=f"Similar ads for this ad  not found.")
    return similar_oglasi


@app.get("/analytics/median")
async def read_median(*, session: Session = Depends(get_session)):
    median = crud.get_median(session=session)

    if not median:
        raise HTTPException(
            status_code=404, detail="Something went wrong.")
    return median
