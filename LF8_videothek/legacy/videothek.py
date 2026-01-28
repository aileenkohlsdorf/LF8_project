import mariadb
import sys
import os
from dotenv import load_dotenv

load_dotenv()

conn = mariadb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host="127.0.0.1",
    port=3306,
    database="videothek"
)

def db_any_connect():
    cur = conn.cursor()
    list = []
    cur.execute("SELECT * FROM film")
    for row in cur:
        list += [row]
    return list


def db_entry_connect(Film_ID):
    cur = conn.cursor()
    list = []
    cur.execute("SELECT * FROM film WHERE film_id = %s", (Film_ID,))
    for row in cur:
        list += [row]
    return list

"""
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
"""