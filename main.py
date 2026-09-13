import argparse
import json
import sys
from models import RawEvent
import os
import stomp
import db
from time import sleep
from dotenv import load_dotenv

class Listener(stomp.ConnectionListener):
    def on_message(self, frame):
        print('received a message "%s"' % frame.body)

def main():
    load_dotenv()
    conn = stomp.Connection([('publicdatafeeds.networkrail.co.uk', 61618)], keepalive=True, heartbeats=(5000,5000))
    conn.set_listener('', Listener())
    while True:
        try:
            conn.connect(os.getenv('NR_USER'), os.getenv('NR_PASSWORD'), wait=True)
            conn.subscribe(destination='/topic/TD_ALL_SIG_AREA', id=1, ack='auto')
            while conn.is_connected():
                sleep(1)
        except Exception as e:
            print("Connection lost, retrying:", e)
            sleep(5)


    try:
        engine = db.get_engine()
        testConn = engine.connect()
        print(f"Connection to {os.getenv('POSTGRES_DB')} for user {os.getenv('POSTGRES_USER')} created successfully.")
    except Exception as e:
        print("Connection could not be made due to the following error:\n", e)
        return
    testConn.close()
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