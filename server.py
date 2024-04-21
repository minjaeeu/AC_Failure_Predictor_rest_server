from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from configurations.base import Base
from fastapi import FastAPI
from configurations.pydantic_models.post import AC_Info_Post
from fastapi.responses import JSONResponse
import db


# creating session from ac_info.db sqlite db file.
engine = create_engine(
    "sqlite:///ac_info.db", echo=True
)  # this will create a new "ac_info.db" file if one is not found in the root path, if the file is found it will use it instead.
Base.metadata.create_all(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()  # session object, used to manipulate/query the db


app = FastAPI()  # our fastAPI application/listener


# FastAPI routes
@app.get("/ac_info/get/all_entries")
def get_all_entries() -> JSONResponse:
    """Returns all entries in the DB.

    Returns:
        JSONResponse: list of all DB entries
    """
    query_result = session.query(db.AC_Info).all()
    return query_result


@app.get("/ac_info/get/latest_entry")
def get_latest_entry() -> JSONResponse:
    """Returns the last entry in the DB.

    Returns:
        JSONResponse: DB's last entry.
    """
    db_len = session.query(db.AC_Info).count()
    last_entry = session.query(db.AC_Info)[db_len - 1]
    return last_entry


@app.get("/ac_info/get/first_entry")
def get_latest_entry() -> JSONResponse:
    """Returns the first entry in the DB.

    Returns:
        JSONResponse: DB's first entry.
    """
    first_entry = session.query(db.AC_Info)[0]
    return first_entry


@app.post("/ac_info/post/new_entry")
def post_new_entry(payload: AC_Info_Post) -> JSONResponse:
    """Creates a new entry in the DB.

    Args:
        payload (AC_Info_Post): payload containing ac_info captured

    Returns:
        JSONResponse: success message or error message containing logs from SQLAlchemy
    """
    new_entry = db.AC_Info(
        datetime=payload.datetime,
        humidity=payload.humidity,
        temperature=payload.temperature,
        wattage=payload.wattage,
    )
    try:
        session.add(new_entry)
        session.commit()
    except IntegrityError as err:
        session.rollback()
        return (
            f"Could not validate payload, please see the below SQLAlchemy error log: ",
            {err},
        )
    return f"entry succesfully inserted"
