# config/database.py
import psycopg2
connection = psycopg2.connect('postgresql://postgres:ulima@200.11.49.103:5432/quinua')