import argparse
import json
from models import RawEvent
import os
import uuid
import db
from time import sleep


#import stomp


def main():
    try:
        engine = db.get_engine()
        conn = engine.connect()
        print(f"Connection to {os.getenv('POSTGRES_DB')} for user {os.getenv('POSTGRES_USER')} created successfully.")
    except Exception as e:
        print("Connection could not be made due to the following error:\n", e)
        return
    conn.close()
    try:
        session = db.create_session(engine)
        session.add(RawEvent(
                msg_type="0003",
            train_id="TEST123",
            payload={"header": {"msg_type": "0003"}, "body": {"train_id": "TEST123", "event_type": "ARRIVAL"}}
        ))
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    main()