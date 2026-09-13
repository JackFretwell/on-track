import os
from models import RawEvent
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

def create_raw_event(session, type, id, pl):
    session.add(RawEvent(
        msg_type=type,
        train_id=id,
        payload=pl
    ))
