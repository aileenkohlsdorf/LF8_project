from fastapi import FastAPI
from typing import Union

import videothek
from videothek import db_connect
import requests
import json


app = FastAPI()

@app.get("/")       ##general test whether some connection can be established
def read_root():
    return {"Hello": "World"}

@app.get("/Film/{Film_ID}")
def read_Film(Film_ID: int, q: Union[str, None] = None):
    return {"Film_ID": Film_ID, "q": videothek.db_connect()}