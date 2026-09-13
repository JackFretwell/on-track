import argparse
import json
import sys
from models import RawEvent
from util import trust
import os
import stomp
import db
from time import sleep
from dotenv import load_dotenv

class Listener(stomp.ConnectionListener):
    def __init__(self, engine):
        self.engine = engine

    def on_message(self, frame):
        headers, message_raw = frame.headers, frame.body
        parsed_body = json.loads(message_raw)
        
        if "TRAIN_MVT_" in headers["destination"]:
            try:
                session = db.create_session(self.engine)
                for msg in parsed_body:
                    train_id, msg_type = trust.extract_trust_fields(msg)
                    if train_id != "" and msg_type != "":
                        db.create_raw_event(session, msg_type, train_id, msg)
                    else:    
                        continue
                    
                session.commit()
            finally:
                session.close()
        else:
            print("Unknown destination: ", headers["destination"])

def main():
    load_dotenv()
    
    try:
        engine = db.get_engine()
        testConn = engine.connect()
        print(f"Connection to {os.getenv('POSTGRES_DB')} for user {os.getenv('POSTGRES_USER')} created successfully.")
    except Exception as e:
        print("Connection could not be made due to the following error:\n", e)
        return
    testConn.close()

    conn = stomp.Connection([('publicdatafeeds.networkrail.co.uk', 61618)], keepalive=True, heartbeats=(5000,5000))
    conn.set_listener('', Listener(engine))
    while True:
        try:
            conn.connect(os.getenv('NR_USER'), os.getenv('NR_PASSWORD'), wait=True)
            conn.subscribe(destination='/topic/TD_ALL_SIG_AREA', id=1, ack='auto')
            conn.subscribe(destination='/topic/TRAIN_MVT_ALL_TOC', id=2, ack='auto')
            while conn.is_connected():
                sleep(1)
        except Exception as e:
            print("Connection lost, retrying:", e)
            sleep(5)

if __name__ == "__main__":
    main()