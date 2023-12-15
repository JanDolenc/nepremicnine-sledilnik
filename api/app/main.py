from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from app.models import Oglas
from app.database import engine


def get_session():  # session in a function shared with every route - FastAPI dependency injection
    with Session(engine) as session:
        yield session


app = FastAPI()

# deprecated use lifespan events
# @app.on_event("startup")
# def on_startup():
#    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello Mom!"}


# "response model" and "-> Oglas" do the same thing (next endpoint). This example is without dependency injection
@app.get("/ad/", response_model=Oglas)
async def read_ad():
    with Session(engine) as session:
        st_ref = 6667291
        ad = session.exec(select(Oglas).where(
            Oglas.referencna_st == st_ref)).first()
        return ad


# FastAPI dependency injection system is used to get the session. One session per request. We also handle the error if the ad is not found -> is None
@app.get("/ad/2/")
async def read_ad(session: Session = Depends(get_session)) -> Oglas:
    st_ref = 6666455
    ad = session.exec(select(Oglas).where(
        Oglas.referencna_st == st_ref)).first()
    if not ad:
        raise HTTPException(
            status_code=404, detail="Ad with this ref_st not found")
    return ad
