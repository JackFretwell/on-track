import os
from models import RawEvent, Location
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from dotenv import load_dotenv


def get_url():
    url = os.getenv('DATABASE_URL')
    return url.replace("postgresql+asyncpg://", "postgresql+psycopg2://")

def get_engine():
    load_dotenv()
    return create_engine(get_url())

def create_session(engine):
    return Session(engine)

def create_raw_event(session, msg_type, train_id, payload):
    session.add(RawEvent(
        msg_type=msg_type,
        train_id=train_id,
        payload=payload
    ))

def create_location(session, stanox, uic, three_alpha, tiploc, nlc, nlc_description):
    session.add(Location(
        stanox=stanox,
        uic=uic,
        three_alpha=three_alpha,
        tiploc=tiploc,
        nlc=nlc,
        nlc_description=nlc_description
    ))