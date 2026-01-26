from annotated_types.test_cases import cases
from fastapi import FastAPI
from typing import Union

from mariadb._mariadb import cursor

import videothek
import requests
import json


app = FastAPI()

@app.get("/")       ##general test whether some connection can be established
def read_root():
    return {"Hello": "World"}

@app.get("/Film")
def read_film(q: Union[str, list, None] = None):
    list = videothek.db_any_connect()
    return {
        q: list
        }

@app.get("/Film/{Film_ID}")
def read_film(Film_ID: int, q: Union[str, list, None] = None):
    list = videothek.db_entry_connect(str(Film_ID))
    return {
        "Film_ID": Film_ID,
        q: list
        }

@app.get("/Film/{Film_ID}/Titel")
def read_film(Film_ID: int, q: Union[str, list, None] = None):
    currentFilm = videothek.db_entry_connect(str(Film_ID))
    return {
        "Film_ID": Film_ID,
        "Titel": currentFilm[0][1]
        }

@app.get("/Film/{Film_ID}/{Attribute}")
def read_film(Film_ID: int, Attribute: str, q: Union[str, list, None] = None):
    currentFilm = videothek.db_any_connect()
    value = Attribute
    valueIndex = 0
    match value:
        case "Titel":
            valueIndex = 1
        case "Erscheinungsjahr":
            valueIndex = 2
        case "Genre":
            valueIndex = 3
        case "Altersfreigabe":
            valueIndex = 4
    return {
        "Film_ID": Film_ID,
        Attribute: currentFilm[int(Film_ID)-1][valueIndex]
        }

"""
@app.get("/Film/{Film_ID}/Genre")
def read_film(Film_ID: int, q: Union[str, list, None] = None):
    list[] = videothek.db_connect(str(Film_ID))
    return {
        "Film_ID": Film_ID,
        q: list[3]
    }
"""
