from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Ausleihe(BaseModel):

    Ausleihe_ID: int
    Ausleihdatum: date
    Rückgabedatum: date
    Kunde_ID: int
    Film_ID: int
    Mitarbeiter_ID: int
