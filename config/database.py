# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:ulima@200.11.49.103:5432/quinua')
session_db = sessionmaker()
session_db.configure(bind=engine)

import psycopg2
connection = psycopg2.connect('postgresql://postgres:ulima@200.11.49.103:5432/quinua')