# config/database.py
import psycopg2
from psycopg2.extras import RealDictCursor

class DB:
  def __init__(self):
    self.connection = psycopg2.connect('postgresql://postgres:ulima@200.11.49.103:5432/quinua')
    self.cursor = self.connection.cursor(cursor_factory = RealDictCursor)