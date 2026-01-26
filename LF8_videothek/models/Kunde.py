from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Kunde(BaseModel):

    Kunde_ID: int
    Vorname: str
    Nachname: str
    Geburtstag: date
    Straße_Nr: str
    PLZ: str
    City: str