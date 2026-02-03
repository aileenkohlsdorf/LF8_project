import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mariadb.connect(
        user="remoteuser",                   ## os.getenv("DB_USER"),
        password="Passwort",               ## os.getenv("DB_PASSWORD"),
        host="192.168.88.141",                   ## "127.0.0.1",
        port=3306,
        database="videothek"
    )