import argparse
import json
import os
from time import sleep
from sqlalchemy import create_engine
from dotenv import load_dotenv


#import stomp

def get_connection():
    load_dotenv()
    engine = create_engine(os.getenv('DATABASE_URL'))
    return engine

def main():
    try:
        engine = get_connection()
        print(f"Connection to {os.getenv('POSTGRES_DB')} for user {os.getenv('POSTGRES_USER')} created successfully.")
    except Exception as e:
        print("Connection could not be made due to the following error:\n", e)


if __name__ == "__main__":
    main()