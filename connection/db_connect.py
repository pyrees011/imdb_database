import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database = os.getenv("DB_NAME"),
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = 5432,
)

cur = conn.cursor()

def db_connect():
    return conn, cur

def db_close():
    cur.close()
    conn.close()

