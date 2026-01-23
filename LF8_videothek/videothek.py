import mariadb
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def db_connect():
    conn = mariadb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host="127.0.0.1",
        port=3306,
        database="videothek"

    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM film")
    for row in cur:
        print(row)

"""
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
"""