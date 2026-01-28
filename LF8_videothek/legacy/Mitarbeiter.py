from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Mitarbeiter(BaseModel):

    Mitarbeiter_ID: int
    Vorname: str
    Nachname: str