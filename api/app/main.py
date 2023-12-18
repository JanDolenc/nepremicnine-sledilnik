from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session

from app.models import Oglas, OglasRead, OglasCena
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
async def read_oglas(*, session: Session = Depends(get_session), url: str):
    ad = crud.get_oglas(session=session, url=url)

    if not ad:
        raise HTTPException(
            status_code=404, detail="Ad with this url not found.")
    return ad
