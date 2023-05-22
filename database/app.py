
from sqlmodel import Session, select

from .models import Nepremicnina, Oglas
from .database import create_db_and_tables, engine


def create_nepremicnina():
    with Session(engine) as session:
        nepremicnina_za_vnos = Nepremicnina(
            vrsta="Stanovanje", tip="2-sobno", nadstropje="1", velikost=59.6, leto_izgradnje=1900, lokacija_id=1)
        session.add(nepremicnina_za_vnos)
        session.commit()

        oglas_za_vnos = Oglas(
            referencna_st=6545780, naslov="LJ. MOSTE, BLIŽINA TRŽNICE", url="vnos-z-sqlmodel-tutorial-connect-rows-join", posredovanje="Prodaja", nepremicnina_id=nepremicnina_za_vnos.id, agencija_id=1
        )

        # this line above: nepremicnina_id=nepremicnina_za_vnos.id works because it triggers a refresh

        session.add(oglas_za_vnos)
        session.commit()

        session.refresh(oglas_za_vnos)

        print("Created oglas:", oglas_za_vnos)


def select_oglase():
    with Session(engine) as session:
        statement = select(Oglas, Nepremicnina).where(
            Oglas.nepremicnina_id == Nepremicnina.id)
        results = session.exec(statement)
        for oglas, nepremicnina in results:
            print("Oglas:", oglas, "Nepremicnina:", nepremicnina)


def select_oglase_join():
    with Session(engine) as session:
        statement = select(Oglas, Nepremicnina).join(Nepremicnina)
        results = session.exec(statement)
        for oglas, nepremicnina in results:
            print("Oglas:", oglas, "Nepremicnina:", nepremicnina)


def main():
    # create_db_and_tables()
    # create_nepremicnina()
    # select_oglase()
    select_oglase_join()


if __name__ == "__main__":
    main()
