from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
uri = 'postgresql://%s:%s@%s:%s/%s' % (USER, PASSWORD, HOST, PORT, os.getenv('POSTGRES_DB'))
engine = create_engine(uri)