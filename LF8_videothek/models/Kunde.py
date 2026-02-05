from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Kunde(BaseModel):

    __Kunde_ID__: int
    __Vorname__: str
    __Nachname__: str
    __Geburtstag__: date
    __Straße_Nr__: str
    __PLZ__: str
    __City__: str